import requests

from copy import deepcopy
from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router
from pscompose.backends.postgres import backend
from pscompose.form_schemas import CONTEXT_SCHEMA, CONTEXT_UI_SCHEMA

# Setup CRUD endpoints
router = generate_router("context")


# Custom endpoints
@router.get("/api/context/new/form", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    # TODO: This is just a placeholder
    url = "https://chic-ps-lat.es.net/pscheduler/contexts"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Failed to fetch external data: {str(e)}")

    # Extract just the archive names (last part of each URL)
    contexts = [el.split("/")[-1] for el in data]
    one_of = [{"const": name, "title": name.upper()} for name in contexts]

    # Clone and enrich the schema dynamically
    enriched_schema = deepcopy(CONTEXT_SCHEMA)
    enriched_schema["properties"]["context"]["oneOf"] = one_of

    payload = {"ui_schema": CONTEXT_UI_SCHEMA, "json_schema": CONTEXT_SCHEMA, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/api/context/{item_id}/form",
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
        response_json["favorited"] = response.favorited
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Address with id: {item_id} not found")

    payload = {
        "ui_schema": CONTEXT_UI_SCHEMA,
        "json_schema": CONTEXT_SCHEMA,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)
