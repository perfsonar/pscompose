from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.backends.postgres import backend
from pscompose.form_schemas import GROUP_SCHEMA, GROUP_UI_SCHEMA
from pscompose.utils import generate_router, enrich_group_schema

# Setup CRUD endpoints
router = generate_router("group")


# Custom endpoints
@router.get("/api/group/new/form", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    try:
        address_rows = backend.get_results(datatype=DataTypes.ADDRESS)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch addresses: {str(e)}")

    enriched_schema = enrich_group_schema(
        base_schema=GROUP_SCHEMA,
        properties=["addresses", "a-addresses", "b-addresses", "excludes"],
        rows=address_rows,
    )

    payload = {"ui_schema": GROUP_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/api/group/{item_id}/form",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.GROUP, item_id=item_id)
        response_json = response.json
        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Address with id: {item_id} not found")

    try:
        address_rows = backend.get_results(datatype=DataTypes.ADDRESS)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch addresses: {str(e)}")

    enriched_schema = enrich_group_schema(
        base_schema=GROUP_SCHEMA,
        properties=["addresses", "a-addresses", "b-addresses", "excludes"],
        rows=address_rows,
    )

    payload = {
        "ui_schema": GROUP_UI_SCHEMA,
        "json_schema": enriched_schema,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)
