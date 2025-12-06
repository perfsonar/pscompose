import requests
import json
from copy import deepcopy
from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router
from pscompose.backends.postgres import backend
from pscompose.form_schemas import (
    TEST_SCHEMA,
    TEST_UI_SCHEMA,
    idle_schema,
    throughput_schema,
    latency_schema,
)

# Setup CRUD endpoints
router = generate_router("test")


# Custom sanitize function to transform the data for the backend
def sanitize_data(data):
    json_data = data["json"]
    spec = {k: v for k, v in json_data.items() if k not in ("type", "_meta")}

    output = {"type": json_data["type"], "spec": spec}

    if "_meta" in json_data:
        output["_meta"] = json_data["_meta"]

    data["json"] = output

    print("Sanitized data:", data)
    return data


router.sanitize = sanitize_data


# Custom endpoints
# @router.get("/test/{testType}/new/form", summary="Return the form to be rendered")
# @version(1)
# def get_form():
#     # Talk to pScheduler API
#     pass

# @router.post(
#   "/test/{testType}/{testId}/form/validate",
#   summary="Validate the form data once user submits the form"
# )
# @version(1)
# def validate_form(testType: str, testId: str):
#     # Talk to pScheduler API
#     # pScheduler API will look at the form data and then append a version number as well
#     pass

# @router.get("/test/{testId}/change")
# @version(1)
# def get_updated_entries(testId: str):
#     results = backend.find_records(target_id=testId)
#     return results


def fetch_pscheduler_test_list() -> list[str]:
    """Fetch available test types from the pScheduler API"""
    url = "https://chic-ps-lat.es.net/pscheduler/tests"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [el.split("/")[-1] for el in data]
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Failed to fetch external data: {str(e)}",
        )


@router.get("/test/new/form/", summary="Return the form to be rendered")
@version(1)
def get_form():
    # Clone and enrich the schema dynamically
    # tests = fetch_pscheduler_test_list()
    tests = ["idle", "latency", "throughput"]
    enriched_schema = deepcopy(TEST_SCHEMA)
    enriched_schema["properties"]["type"]["oneOf"] = [
        {"const": name, "title": name.upper()} for name in tests
    ]

    # Remove "spec" from TEST_UI_SCHEMA for the new form
    # enriched_schema["properties"].pop("spec", None)

    enriched_ui_schema = deepcopy(TEST_UI_SCHEMA)
    enriched_ui_schema["elements"] = [
        elem for elem in enriched_ui_schema["elements"] if elem.get("scope") != "#/properties/spec"
    ]

    payload = {"ui_schema": enriched_ui_schema, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get("/test/new/{testType}/form/", summary="Return schema for the relevant test type")
@version(1)
def retrieve_form(testType: str):
    print("Retrieving form for test type:", testType)

    if testType == "idle":
        return JSONResponse(content=idle_schema)
    elif testType == "throughput":
        return JSONResponse(content=throughput_schema)
    elif testType == "latency":
        return JSONResponse(content=latency_schema)
    else:
        return JSONResponse(content={})


@router.get(
    "/test/{item_id}/form/",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str, edit: bool = False):
    try:
        response = backend.get_datatype(datatype=DataTypes.TEST, item_id=item_id)
        response_json = response.json
        response_json = {
            k: v for k, v in response_json.items() if v is not None
        }  # Need to remove null fields

        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Test with id: {item_id} not found")

    # Flatten the nested spec structure back to form format
    if "spec" in response_json and isinstance(response_json["spec"], dict):
        # Extract spec fields into the main object
        spec_data = response_json.pop("spec")
        response_json.update(spec_data)

    print("Existing form data:", response_json)
    print("Edit mode:", edit)

    # Get the test type and schema version from the existing data
    test_type = response_json.get("type")
    schema_version = response_json.get("schema")  # This is the numeric version (1, 2, 6, 7, etc.)

    if not test_type or schema_version is None:
        # Fallback to generic schema if no type or schema version specified
        tests = ["idle", "latency", "throughput"]
        # tests = fetch_pscheduler_test_list()
        enriched_schema = deepcopy(TEST_SCHEMA)
        enriched_schema["properties"]["type"]["oneOf"] = [
            {"const": name, "title": name.upper()} for name in tests
        ]

        payload = {
            "ui_schema": TEST_UI_SCHEMA,
            "json_schema": enriched_schema,
            "form_data": response_json,
        }
        return JSONResponse(content=payload)

    # Get the full test schema by calling retrieve_form
    test_schema_response = retrieve_form(test_type)
    # The response is a JSONResponse, so we need to decode it properly
    full_test_schema = json.loads(test_schema_response.body.decode("utf-8"))

    # # If in edit mode, return the full schema and let frontend handle version logic
    # if edit:
    #     print("Edit mode - returning full schema for frontend to handle versions")
    #     # Add the version field to form data so frontend knows which version to load
    #     response_json["version"] = str(schema_version)

    #     payload = {
    #         "ui_schema": full_test_schema["ui_schema"],
    #         "json_schema": full_test_schema["json_schema"],
    #         "form_data": response_json,
    #         "spec": full_test_schema["spec"],  # Include full spec with all versions
    #     }
    #     return JSONResponse(content=payload)

    # Readonly mode - build specific version schema
    print(
        "Available versions in schema:",
        list(full_test_schema["spec"]["jsonschema"]["versions"].keys()),
    )
    print("Looking for version:", schema_version, "type:", type(schema_version))

    # Extract the specific version's jsonschema and uischema
    # JSON keys are always strings, so convert schema_version to string
    schema_version_key = str(schema_version)

    version_jsonschema = full_test_schema["spec"]["jsonschema"]["versions"].get(schema_version_key)
    version_uischema = full_test_schema["spec"]["uischema"]["versions"].get(schema_version_key)

    if not version_jsonschema or not version_uischema:
        raise HTTPException(
            status_code=400, detail=f"Version {schema_version} not found for test type {test_type}"
        )

    # Build the enriched schema by merging base schema with version-specific schema
    tests = ["idle", "latency", "throughput"]
    # tests = fetch_pscheduler_test_list()
    base_schema = deepcopy(TEST_SCHEMA)
    base_schema["properties"]["type"]["oneOf"] = [
        {"const": name, "title": name.upper()} for name in tests
    ]

    # Merge version-specific properties into base schema
    base_schema["properties"].update(version_jsonschema["properties"])

    # Merge required fields
    if "required" in version_jsonschema:
        base_schema["required"] = list(
            set(base_schema.get("required", []) + version_jsonschema["required"])
        )

    # Build the enriched UI schema
    base_ui_schema = deepcopy(TEST_UI_SCHEMA)

    # Find the Group element in the layout and update it
    for element in base_ui_schema["elements"]:
        if element.get("type") == "Group" and "rule" in element:
            # Set the condition to match the current test type
            element["rule"]["condition"]["schema"]["const"] = test_type
            # Replace the group's elements with the version-specific UI elements
            element["elements"] = version_uischema["elements"]
            break

    print("Returning readonly schema for type:", test_type, "version:", schema_version)
    print("json_schema:", base_schema)
    print("ui_schema:", base_ui_schema)
    print("form_data:", response_json)

    payload = {
        "ui_schema": base_ui_schema,
        "json_schema": base_schema,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)
