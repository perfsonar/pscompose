import json
import requests

from pathlib import Path
from collections import defaultdict
from types import SimpleNamespace
from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router, enrich_schema
from pscompose.backends.postgres import backend
from pscompose.form_schemas.task_schemas import TASK_SCHEMA, TASK_UI_SCHEMA

PSCHEDULER_BASE_URL = "http://127.0.0.1:21044/pscheduler"
try:
    _raw = requests.get(f"{PSCHEDULER_BASE_URL}/tools?expanded", timeout=5).json()
except Exception:
    _raw = json.load((Path(__file__).parents[2] / "form_schemas" / "tools.json").open())
TOOL_SCHEMAS = {item["name"]: item for item in _raw}

# Setup CRUD endpoints
router = generate_router("task")

# Cache for test-to-tools mapping
_test_tools_cache = None


def sanitize_data(data):
    json_data = data["json"]

    ref_set = data["ref_set"]
    for key in ("group", "test", "schedule"):
        if json_data.get(key) is not None:
            value = json_data.get(key)
            if value not in ref_set:
                ref_set.append(json_data.get(key))

    if json_data.get("archives") is not None:
        for archive in json_data.get("archives"):
            if archive is not None and archive not in ref_set:
                ref_set.append(archive)

    data["ref_set"] = ref_set

    return data


router.sanitize = sanitize_data


def build_test_tools_mapping():
    """
    Build a mapping of test types to available tools.
    Returns: dict mapping test_type -> list of tool names
    """
    global _test_tools_cache

    if _test_tools_cache is not None:
        return _test_tools_cache

    # --- Local (static) implementation ---
    test_to_tools = defaultdict(list)
    for tool_data in TOOL_SCHEMAS.values():
        tool_name = tool_data.get("name")
        for test_type in tool_data.get("tests", []):
            test_to_tools[test_type].append(tool_name)

    # TODO: pScheduler API implementation (swap in when ready)
    # try:
    #     tools_url = f"{PSCHEDULER_BASE_URL}/tools"
    #     response = requests.get(tools_url, timeout=10)
    #     response.raise_for_status()
    #     tool_urls = response.json()
    #     for tool_url in tool_urls:
    #         try:
    #             tool_response = requests.get(tool_url, timeout=10)
    #             tool_response.raise_for_status()
    #             tool_data = tool_response.json()
    #             tool_name = tool_data.get("name")
    #             for test_type in tool_data.get("tests", []):
    #                 test_to_tools[test_type].append(tool_name)
    #         except Exception as e:
    #             print(f"Error fetching {tool_url}: {e}")
    #             continue
    # except Exception as e:
    #     raise HTTPException(status_code=503, detail=f"Failed to fetch tools from pScheduler")

    result = {test_type: sorted(tools) for test_type, tools in sorted(test_to_tools.items())}
    _test_tools_cache = result
    return result


@router.get("/task/tools/{test_type}/", summary="Get available tools for a specific test type")
@version(1)
def get_tools_for_test(test_type: str):
    """
    Returns a list of available tools for the specified test type.
    Example: /task/tools/idle/ returns ["sleep", "sleepbgm", "snooze"]
    """
    mapping = build_test_tools_mapping()
    tools = mapping.get(test_type, [])
    print("test type: ", test_type)
    print("tools: ", tools)
    if not tools:
        raise HTTPException(status_code=404, detail=f"No tools found for test type: {test_type}")

    tools_with_labels = [
        {"name": name, "label": TOOL_SCHEMAS.get(name, {}).get("label", name)} for name in tools
    ]
    return JSONResponse(content={"test_type": test_type, "tools": tools_with_labels})


@router.get("/task/new/form/", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    try:
        groups = backend.get_results(datatype=DataTypes.GROUP)
        tests = backend.get_results(datatype=DataTypes.TEST)
        schedules = backend.get_results(datatype=DataTypes.SCHEDULE)
        archives = backend.get_results(datatype=DataTypes.ARCHIVE)
        tools = []  # Start with empty tools - will be populated after test selection
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

    enriched_schema = enrich_schema(
        base_schema=TASK_SCHEMA,
        updates={
            "group": groups,
            "test": tests,
            "schedule": schedules,
            "archives": archives,
            "tools": tools,
        },
    )

    payload = {"ui_schema": TASK_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/task/{item_id}/form/",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str, edit: bool = False):
    try:
        response = backend.get_datatype(datatype=DataTypes.TASK, item_id=item_id)
        response_json = response.json
        response_json = {
            k: v for k, v in response_json.items() if v is not None
        }  # Need to remove null fields

        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Task with id: {item_id} not found")

    try:
        groups = backend.get_results(datatype=DataTypes.GROUP)
        tests = backend.get_results(datatype=DataTypes.TEST)
        schedules = backend.get_results(datatype=DataTypes.SCHEDULE)
        archives = backend.get_results(datatype=DataTypes.ARCHIVE)

        # Populate tools based on mode
        tools = []
        if edit:
            # Edit mode: Fetch all available tools for the test type from pScheduler
            test_id = response_json.get("test")
            if test_id:
                try:
                    test_obj = backend.get_datatype(datatype=DataTypes.TEST, item_id=test_id)
                    test_type = test_obj.json.get("type")
                    if test_type:
                        mapping = build_test_tools_mapping()
                        available_tools = mapping.get(test_type, [])
                        tools = [
                            SimpleNamespace(
                                id=name, name=TOOL_SCHEMAS.get(name, {}).get("label", name)
                            )
                            for name in available_tools
                        ]
                except Exception as e:
                    print(f"Error fetching tools for test: {e}")
        else:
            # Readonly mode: Only create options for selected tools (no pScheduler API call needed)
            selected_tools = response_json.get("tools", [])
            if selected_tools:
                tools = [
                    SimpleNamespace(id=name, name=TOOL_SCHEMAS.get(name, {}).get("label", name))
                    for name in selected_tools
                ]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

    enriched_schema = enrich_schema(
        base_schema=TASK_SCHEMA,
        updates={
            "group": groups,
            "test": tests,
            "schedule": schedules,
            "archives": archives,
            "tools": tools,
        },
    )

    payload = {
        "ui_schema": TASK_UI_SCHEMA,
        "json_schema": enriched_schema,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)
