import json
import requests

from copy import deepcopy
from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router
from pscompose.backends.postgres import backend
from pscompose.form_schemas.context_schemas import (
    CONTEXT_SCHEMA,
    CONTEXT_UI_SCHEMA,
    CONTEXT_SCHEMAS,
)

# Setup CRUD endpoints
router = generate_router("context")

PSCHEDULER_BASE_URL = "https://chic-ps-lat.es.net/pscheduler"


def sanitize_data(data):
    """
    Nest context version-specific fields (including schema) under 'data' object.

    Top-level fields: context, _meta
    Nested under 'data': schema + all other version-specific fields
    """
    json_data = data["json"]

    # Rename type -> context for pSConfig storage
    if "type" in json_data:
        json_data["context"] = json_data.pop("type")

    # Fields that should remain at top level
    top_level_fields = {"context", "_meta"}

    # Everything else (including schema) goes into data
    data_obj = {k: v for k, v in json_data.items() if k not in top_level_fields}

    output = {"context": json_data["context"]}

    if "_meta" in json_data:
        output["_meta"] = json_data["_meta"]

    # data is required by ContextSpecification; use empty dict for types with no fields
    output["data"] = data_obj if data_obj else {}

    data["json"] = output
    return data


router.sanitize = sanitize_data


def fetch_pscheduler_context_list() -> list[str]:
    url = f"{PSCHEDULER_BASE_URL}/contexts"
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


# Custom endpoints
@router.get("/context/new/form/", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    """TODO: Fetch available contexts from the pScheduler API"""
    # contexts = fetch_pscheduler_context_list()
    contexts = [
        name
        for name, schema in CONTEXT_SCHEMAS.items()
        if schema.get("json-forms-compatible", False)
    ]
    one_of = [{"const": name, "title": name.upper()} for name in contexts]

    enriched_schema = deepcopy(CONTEXT_SCHEMA)
    enriched_schema["properties"]["type"]["oneOf"] = one_of

    payload = {"ui_schema": CONTEXT_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/context/{item_id}/form/",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.CONTEXT, item_id=item_id)
        response_json = response.json
        response_json = {
            k: v for k, v in response_json.items() if v is not None
        }  # Need to remove null fields

        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Context with id: {item_id} not found")

    # Map "context" from DB to "type" for frontend consistency
    if "context" in response_json:
        response_json["type"] = response_json.pop("context")

    # Flatten the nested data structure if present
    if "data" in response_json and isinstance(response_json["data"], dict):
        data_fields = response_json.pop("data")
        response_json.update(data_fields)

    # Get the context type and schema version from the existing data
    context_type = response_json.get("type")
    schema_version = response_json.get("schema")

    if not context_type or schema_version is None:
        # Fallback to generic schema
        contexts = [n for n, s in CONTEXT_SCHEMAS.items() if s.get("json-forms-compatible", False)]
        enriched_schema = deepcopy(CONTEXT_SCHEMA)
        enriched_schema["properties"]["type"]["oneOf"] = [
            {"const": name, "title": name.upper()} for name in contexts
        ]

        payload = {
            "ui_schema": CONTEXT_UI_SCHEMA,
            "json_schema": enriched_schema,
            "form_data": response_json,
        }
        return JSONResponse(content=payload)

    # Get the full context schema by calling retrieve_form
    context_schema_response = retrieve_form(context_type)
    full_context_schema = json.loads(context_schema_response.body.decode("utf-8"))

    # Build specific version schema
    versions_json = full_context_schema["spec"]["jsonschema"]["versions"]
    versions_ui = full_context_schema["spec"]["uischema"]["versions"]

    schema_version_key = int(schema_version)
    version_jsonschema = (
        versions_json[schema_version_key] if schema_version_key < len(versions_json) else None
    )
    version_uischema = (
        versions_ui[schema_version_key] if schema_version_key < len(versions_ui) else None
    )

    if not version_jsonschema or not version_uischema:
        raise HTTPException(
            status_code=400,
            detail=f"Version {schema_version} not found for context type {context_type}",
        )

    # Build enriched schema
    contexts = [n for n, s in CONTEXT_SCHEMAS.items() if s.get("json-forms-compatible", False)]
    base_schema = deepcopy(CONTEXT_SCHEMA)
    base_schema["properties"]["type"]["oneOf"] = [
        {"const": name, "title": name.upper()} for name in contexts
    ]

    # Merge version-specific properties
    base_schema["properties"].update(version_jsonschema["properties"])

    if "required" in version_jsonschema:
        base_schema["required"] = list(
            set(base_schema.get("required", []) + version_jsonschema["required"])
        )

    # Build enriched UI schema
    base_ui_schema = deepcopy(CONTEXT_UI_SCHEMA)

    for element in base_ui_schema["elements"]:
        if element.get("type") == "Group" and "rule" in element:
            element["rule"]["condition"]["schema"]["const"] = context_type
            element["elements"] = version_uischema["elements"]
            break

    payload = {
        "ui_schema": base_ui_schema,
        "json_schema": base_schema,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)


@router.get(
    "/context/new/{context_type}/form/",
    summary="Return schema for the relevant context type",
)
@version(1)
def retrieve_form(context_type: str):
    schema = CONTEXT_SCHEMAS.get(context_type)
    return JSONResponse(content=schema if schema else {})
