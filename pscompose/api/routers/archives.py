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
@router.get("/api/archive/new/form", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    payload = {"ui_schema": ARCHIVE_UI_SCHEMA, "json_schema": ARCHIVE_SCHEMA, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/api/archive/{item_id}/form",
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
