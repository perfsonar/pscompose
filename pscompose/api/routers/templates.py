from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router, enrich_schema
from pscompose.backends.postgres import backend
from pscompose.form_schemas import TEMPLATE_SCHEMA, TEMPLATE_UI_SCHEMA

# Setup CRUD endpoints
router = generate_router("template")


# Custom endpoints
@router.get("/api/template/new/form", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    try:
        tasks = backend.get_results(datatype=DataTypes.TASK)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

    enriched_schema = enrich_schema(
        base_schema=TEMPLATE_SCHEMA,
        properties=["tasks"],
        rows=tasks,
    )

    payload = {"ui_schema": TEMPLATE_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/api/template/{item_id}/form",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.TEMPLATE, item_id=item_id)
        response_json = response.json
        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Address with id: {item_id} not found")

    payload = {
        "ui_schema": TEMPLATE_UI_SCHEMA,
        "json_schema": TEMPLATE_SCHEMA,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)
