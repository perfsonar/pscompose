import json
import requests

from copy import deepcopy
from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router
from pscompose.backends.postgres import backend
from pscompose.form_schemas import ARCHIVE_SCHEMA, ARCHIVE_UI_SCHEMA, http_schema

# Setup CRUD endpoints
router = generate_router("archive")


def sanitize_data(data):
    """
    Nest archive version-specific fields under 'data' object.

    Top-level fields: archiver, schema, label, ttl, transform, _meta
    Nested under 'data': All other version-specific fields
    """
    json_data = data["json"]

    # Fields that should remain at top level
    top_level_fields = {"archiver", "schema", "label", "ttl", "transform", "_meta"}

    # Extract version-specific fields into data object
    data_obj = {k: v for k, v in json_data.items() if k not in top_level_fields}

    # Build output with top-level fields
    output = {}

    for field in ["archiver", "schema", "label", "ttl", "transform", "_meta"]:
        if field in json_data:
            output[field] = json_data[field]

    # Add nested data object if it has any fields
    if data_obj:
        output["data"] = data_obj

    data["json"] = output

    print("Sanitized archive data:", data)
    return data


router.sanitize = sanitize_data


# Custom endpoints
@router.get("/archive/new/form/", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    # TODO: This is just a placeholder
    url = "https://chic-ps-lat.es.net/pscheduler/archivers"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # data = response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Failed to fetch external data: {str(e)}")

    # Extract just the archive names (last part of each URL)
    archives = ["http"]
    # archives = [el.split("/")[-1] for el in data]
    one_of = [{"const": name, "title": name.upper()} for name in archives]

    # Clone and enrich the schema dynamically
    enriched_schema = deepcopy(ARCHIVE_SCHEMA)
    enriched_schema["properties"]["type"]["oneOf"] = one_of

    payload = {"ui_schema": ARCHIVE_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/archive/{item_id}/form/",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str, edit: bool = False):
    try:
        response = backend.get_datatype(datatype=DataTypes.ARCHIVE, item_id=item_id)
        response_json = response.json
        response_json = {
            k: v for k, v in response_json.items() if v is not None
        }  # Need to remove null fields

        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Archive with id: {item_id} not found")

    # Map "archiver" from DB to "type" for frontend consistency
    if "archiver" in response_json:
        response_json["type"] = response_json.pop("archiver")

    # Flatten the nested data structure if present
    if "data" in response_json and isinstance(response_json["data"], dict):
        data_fields = response_json.pop("data")
        response_json.update(data_fields)

    print("Existing archive form data:", response_json)
    print("Edit mode:", edit)

    # Get the archive type and schema version from the existing data
    archive_type = response_json.get("type")
    schema_version = response_json.get("schema")

    if not archive_type or schema_version is None:
        # Fallback to generic schema
        archives = ["http"]
        enriched_schema = deepcopy(ARCHIVE_SCHEMA)
        enriched_schema["properties"]["type"]["oneOf"] = [
            {"const": name, "title": name.upper()} for name in archives
        ]

        payload = {
            "ui_schema": ARCHIVE_UI_SCHEMA,
            "json_schema": enriched_schema,
            "form_data": response_json,
        }
        return JSONResponse(content=payload)

    # Get the full archive schema by calling retrieve_form
    archive_schema_response = retrieve_form(archive_type)
    full_archive_schema = json.loads(archive_schema_response.body.decode("utf-8"))

    # Build specific version schema (works for both readonly and edit mode)
    print(
        "Available versions in schema:",
        list(full_archive_schema["spec"]["jsonschema"]["versions"].keys()),
    )
    print("Looking for version:", schema_version, "type:", type(schema_version))

    schema_version_key = str(schema_version)
    version_jsonschema = full_archive_schema["spec"]["jsonschema"]["versions"].get(
        schema_version_key
    )
    version_uischema = full_archive_schema["spec"]["uischema"]["versions"].get(schema_version_key)

    if not version_jsonschema or not version_uischema:
        raise HTTPException(
            status_code=400,
            detail=f"Version {schema_version} not found for archive type {archive_type}",
        )

    # Build enriched schema
    archives = ["http"]
    base_schema = deepcopy(ARCHIVE_SCHEMA)
    base_schema["properties"]["type"]["oneOf"] = [
        {"const": name, "title": name.upper()} for name in archives
    ]

    # Merge version-specific properties
    base_schema["properties"].update(version_jsonschema["properties"])

    if "required" in version_jsonschema:
        base_schema["required"] = list(
            set(base_schema.get("required", []) + version_jsonschema["required"])
        )

    # Build enriched UI schema
    base_ui_schema = deepcopy(ARCHIVE_UI_SCHEMA)

    for element in base_ui_schema["elements"]:
        if element.get("type") == "Group" and "rule" in element:
            element["rule"]["condition"]["schema"]["const"] = archive_type
            element["elements"] = version_uischema["elements"]
            break

    print("Returning readonly schema for type:", archive_type, "version:", schema_version)

    payload = {
        "ui_schema": base_ui_schema,
        "json_schema": base_schema,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)


@router.get("/archive/new/{archiver}/form/", summary="Return schema for the relevant archiver")
@version(1)
def retrieve_form(archiver: str):
    print("Retrieving form for archiver type:", archiver)  # archiver will be http
    if archiver != "http":
        return JSONResponse(content={})

    return JSONResponse(content=http_schema)
