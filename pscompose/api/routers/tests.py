import requests
from copy import deepcopy
from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router
from pscompose.backends.postgres import backend
from pscompose.form_schemas import TEST_SCHEMA, TEST_UI_SCHEMA

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


@router.get("/api/test/new/form", summary="Return the form to be rendered")
@version(1)
def get_form():
    # Clone and enrich the schema dynamically
    tests = fetch_pscheduler_test_list()
    enriched_schema = deepcopy(TEST_SCHEMA)
    enriched_schema["properties"]["type"]["oneOf"] = [
        {"const": name, "title": name.upper()} for name in tests
    ]

    # Remove "spec" from TEST_UI_SCHEMA for the new form
    enriched_schema["properties"].pop("spec", None)

    enriched_ui_schema = deepcopy(TEST_UI_SCHEMA)
    enriched_ui_schema["elements"] = [
        elem for elem in enriched_ui_schema["elements"] if elem.get("scope") != "#/properties/spec"
    ]

    payload = {"ui_schema": enriched_ui_schema, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get("/api/test/new/{testType}/form", summary="Return schema for the relevant test type")
@version(1)
def retrieve_form(testType: str):
    print("Retrieving form for test type:", testType)  # testType will be idle
    if testType != "idle":
        return JSONResponse(content={})

    idle_schema = {
        "schema": 1,
        "name": "idle",
        "description": "Consume time in the background",
        "version": "1.0",
        "maintainer": {
            "name": "perfSONAR Development Team",
            "email": "perfsonar-developer@internet2.edu",
            "href": "http://www.perfsonar.net",
        },
        "scheduling-class": "background",
        "spec": {
            "jsonschema": {
                "versions": {
                    1: {
                        "additionalProperties": False,
                        "properties": {
                            "duration": {
                                "title": "Duration",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "type": "string",
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "host-node": {
                                "pattern": r"(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\](:[0-9]+)?$)",  # noqa: E501
                                "type": "string",
                                "title": "Host Node",
                            },
                            "parting-comment": {
                                "type": "string",
                                "title": "Parting Comment",
                            },
                            "schema": {
                                "enum": [1],
                                "type": "integer",
                                "title": "Schema Version",
                            },
                            "starting-comment": {
                                "type": "string",
                                "title": "Starting Comment",
                            },
                        },
                        "required": ["duration"],
                        "type": "object",
                    },
                    2: {
                        "additionalProperties": False,
                        "properties": {
                            "duration": {
                                "title": "Duration",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "type": "string",
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "parting-comment": {
                                "type": "string",
                                "title": "Parting Comment",
                            },
                            "schema": {
                                "enum": [2],
                                "type": "integer",
                                "title": "Schema",
                            },
                            "starting-comment": {
                                "type": "string",
                                "title": "Starting Comment",
                            },
                        },
                        "required": ["duration", "schema"],
                        "type": "object",
                    },
                },
            },
            "uischema": {
                "versions": {
                    1: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/duration",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/host-node",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/starting-comment",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/parting-comment",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                        ],
                    },
                    2: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/duration",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/starting-comment",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/parting-comment",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                        ],
                    },
                },
            },
            "versions": [None, "1", "2"],
        },
    }
    return JSONResponse(content=idle_schema)


@router.get(
    "/api/test/{item_id}/form",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.TEST, item_id=item_id)
        response_json = response.json
        response_json = {
            k: v for k, v in response_json.items() if v is not None
        }  # Need to remove null fields

        response_json["name"] = response.name  # Adding "name" since it's not present in the json
        response_json["favorited"] = response.favorited
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Test with id: {item_id} not found")

    # Clone and enrich the schema dynamically
    tests = fetch_pscheduler_test_list()
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
