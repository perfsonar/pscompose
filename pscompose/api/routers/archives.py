import requests

from copy import deepcopy
from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router
from pscompose.backends.postgres import backend
from pscompose.form_schemas import ARCHIVE_SCHEMA, ARCHIVE_UI_SCHEMA

# Setup CRUD endpoints
router = generate_router("archive")


# Custom endpoints
# TODO: This will need a parameter to specify which type of archive it is
# and then enrich the form based on that?
@router.get("/archive/new/form/", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    # TODO: This is just a placeholder
    url = "https://chic-ps-lat.es.net/pscheduler/archivers"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Failed to fetch external data: {str(e)}")

    # Extract just the archive names (last part of each URL)
    archives = [el.split("/")[-1] for el in data]
    one_of = [{"const": name, "title": name.upper()} for name in archives]

    # Clone and enrich the schema dynamically
    enriched_schema = deepcopy(ARCHIVE_SCHEMA)
    enriched_schema["properties"]["archiver"]["oneOf"] = one_of

    payload = {"ui_schema": ARCHIVE_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/archive/{item_id}/form/",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.ARCHIVE, item_id=item_id)
        response_json = response.json
        response_json = {
            k: v for k, v in response_json.items() if v is not None
        }  # Need to remove null fields

        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Address with id: {item_id} not found")

    payload = {
        "ui_schema": ARCHIVE_UI_SCHEMA,
        "json_schema": ARCHIVE_SCHEMA,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)


@router.get("/api/archive/new/{archiver}/form", summary="Return schema for the relevant archiver")
@version(1)
def retrieve_form(archiver: str):
    print("Retrieving form for archiver type:", archiver)  # archiver will be http
    if archiver != "http":
        return JSONResponse(content={})

    http_schema = {
        "schema": 1,
        "name": "http",
        "description": "Send a raw JSON result to a HTTP server",
        "version": "1.0",
        "maintainer": {
            "name": "perfSONAR Development Team",
            "email": "perfsonar-developer@internet2.edu",
            "href": "http://www.perfsonar.net",
        },
        "spec": {
            "jsonschema": {
                "versions": {
                    1: {
                        "type": "object",
                        "properties": {
                            "schema": {"title": "Schema Version", "type": "integer", "enum": [1]},
                            "_url": {
                                "title": "URL",
                                "type": "string",
                                "format": "uri",
                            },
                            "op": {
                                "title": "Operation",
                                "type": "string",
                                "enum": [
                                    "put",
                                    "post",
                                ],
                            },
                            "bind": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 255,
                                "pattern": r"^[A-Za-z0-9_][A-Za-z0-9\-]{0,62}(\.[A-Za-z0-9][A-Za-z0-9\-]{1,62})*\.?$",  # noqa: E501
                            },
                            # "retry-policy": {
                            #     "type": "array",
                            #     "items": {
                            #         "$ref": "#/pScheduler/RetryPolicyEntry"
                            #     }
                            # }
                        },
                        "required": ["_url"],
                        "additionalProperties": False,
                    },
                    2: {
                        "type": "object",
                        "properties": {
                            "schema": {"title": "Schema Version", "type": "integer", "enum": [2]},
                            "_url": {
                                "title": "URL",
                                "type": "string",
                                "format": "uri",
                            },
                            "op": {
                                "title": "Operation",
                                "type": "string",
                                "enum": [
                                    "put",
                                    "post",
                                ],
                            },
                            "_headers": {
                                "title": "Headers",
                                "type": "object",
                            },
                            # Not complete
                            "bind": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 255,
                                "pattern": r"^[A-Za-z0-9_][A-Za-z0-9\-]{0,62}(\.[A-Za-z0-9][A-Za-z0-9\-]{1,62})*\.?$",  # noqa: E501
                            },
                            # "retry-policy": {
                            #     "type": "array",
                            #     "items": {
                            #         "$ref": "#/pScheduler/RetryPolicyEntry"
                            #     }
                            # }
                        },
                        "required": ["schema", "_url"],
                        "additionalProperties": False,
                    },
                    3: {
                        "type": "object",
                        "properties": {
                            "schema": {"title": "Schema Version", "type": "integer", "enum": [3]},
                            "_url": {
                                "title": "URL",
                                "type": "string",
                                "format": "uri",
                            },
                            "op": {
                                "title": "Operation",
                                "type": "string",
                                "enum": [
                                    "put",
                                    "post",
                                ],
                            },
                            "verify-ssl": {"title": "Verify SSL Certificate", "type": "boolean"},
                            "_headers": {
                                "type": "object",
                            },
                            # Not complete
                            "bind": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 255,
                                "pattern": r"^[A-Za-z0-9_][A-Za-z0-9\-]{0,62}(\.[A-Za-z0-9][A-Za-z0-9\-]{1,62})*\.?$",  # noqa: E501
                            },
                            # "retry-policy": {
                            #     "type": "array",
                            #     "items": {
                            #         "$ref": "#/pScheduler/RetryPolicyEntry"
                            #     }
                            # }
                        },
                        "required": ["schema", "_url"],
                        "additionalProperties": False,
                    },
                    4: {
                        "type": "object",
                        "properties": {
                            "schema": {"title": "Schema Version", "type": "integer", "enum": [4]},
                            "_url": {
                                "title": "URL",
                                "type": "string",
                                "format": "uri",
                            },
                            "op": {
                                "title": "Operation",
                                "type": "string",
                                "enum": [
                                    "put",
                                    "post",
                                ],
                            },
                            "verify-ssl": {"title": "Verify SSL Certificate", "type": "boolean"},
                            "_headers": {
                                "title": "Headers",
                                "type": "object",
                            },
                            "timeout": {
                                "title": "Timeout",
                                "type": "string",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            # Not complete
                            "bind": {
                                "title": "Bind Address",
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 255,
                                "pattern": r"^[A-Za-z0-9_][A-Za-z0-9\-]{0,62}(\.[A-Za-z0-9][A-Za-z0-9\-]{1,62})*\.?$",  # noqa: E501
                            },
                            # "retry-policy": {
                            #     "type": "array",
                            #     "items": {
                            #         "$ref": "#/pScheduler/RetryPolicyEntry"
                            #     }
                            # }
                        },
                        "required": ["schema", "_url"],
                        "additionalProperties": False,
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
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/_url",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/op",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/bind",
                                "customComponent": "input-text",
                            },
                            # {
                            #     "type": "Control",
                            #     "scope": "#/properties/retry-policy",
                            #     "customComponent": "input-text",
                            # },
                        ],
                    },
                    2: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/_url",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/op",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/_headers",
                                "customComponent": "input-text-area",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/bind",
                                "customComponent": "input-text",
                            },
                            # {
                            #     "type": "Control",
                            #     "scope": "#/properties/retry-policy",
                            #     "customComponent": "input-text",
                            # },
                        ],
                    },
                    3: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/_url",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/op",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/verify-ssl",
                                "customComponent": "input-checkbox",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/_headers",
                                "customComponent": "input-text-area",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/bind",
                                "customComponent": "input-text",
                            },
                            # {
                            #     "type": "Control",
                            #     "scope": "#/properties/retry-policy",
                            #     "customComponent": "input-text",
                            # },
                        ],
                    },
                    4: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/_url",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/op",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/_headers",
                                "customComponent": "input-text-area",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/verify-ssl",
                                "customComponent": "input-checkbox",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/timeout",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/bind",
                                "customComponent": "input-text",
                            },
                            # {
                            #     "type": "Control",
                            #     "scope": "#/properties/retry-policy",
                            #     "customComponent": "input-text",
                            # },
                        ],
                    },
                },
            },
            "versions": [None, "1", "2", "3", "4"],
        },
    }
    return JSONResponse(content=http_schema)
