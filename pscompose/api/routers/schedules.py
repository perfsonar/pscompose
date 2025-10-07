from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router
from pscompose.backends.postgres import backend
from pscompose.form_schemas import SCHEDULE_SCHEMA, SCHEDULE_UI_SCHEMA

# Setup CRUD endpoints
router = generate_router("schedule")


# Custom endpoints
@router.get("/api/schedule/new/form", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    print("get new form schedule")
    payload = {"ui_schema": SCHEDULE_UI_SCHEMA, "json_schema": SCHEDULE_SCHEMA, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/api/schedule/{item_id}/form",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.SCHEDULE, item_id=item_id)
        response_json = response.json
        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Address with id: {item_id} not found")

    payload = {
        "ui_schema": SCHEDULE_UI_SCHEMA,
        "json_schema": SCHEDULE_SCHEMA,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)
