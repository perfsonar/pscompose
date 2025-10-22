from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router, enrich_schema
from pscompose.backends.postgres import backend
from pscompose.form_schemas import TASK_SCHEMA, TASK_UI_SCHEMA

# Setup CRUD endpoints
router = generate_router("task")


# Custom endpoints
@router.get("/api/task/new/form", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    try:
        groups = backend.get_results(datatype=DataTypes.GROUP)
        tests = backend.get_results(datatype=DataTypes.TEST)
        schedules = backend.get_results(datatype=DataTypes.SCHEDULE)
        archives = backend.get_results(datatype=DataTypes.ARCHIVE)
        tools = backend.get_results(datatype="tool")  # TODO: Get this from pScheduler
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

    enriched_schema = enrich_schema(
        base_schema=TASK_SCHEMA,
        updates={
            "group": groups,
            "test": tests,
            "schedule": schedules,
            "archives": archives,
            "tools": tools,
        },
    )

    print("enriched_schema:", enriched_schema)

    payload = {"ui_schema": TASK_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/api/task/{item_id}/form",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.TASK, item_id=item_id)
        response_json = response.json
        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Task with id: {item_id} not found")

    try:
        groups = backend.get_results(datatype=DataTypes.GROUP)
        tests = backend.get_results(datatype=DataTypes.TEST)
        schedules = backend.get_results(datatype=DataTypes.SCHEDULE)
        archives = backend.get_results(datatype=DataTypes.ARCHIVE)
        tools = backend.get_results(datatype="tool")  # TODO: Get this from pScheduler
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

    enriched_schema = enrich_schema(
        base_schema=TASK_SCHEMA,
        updates={
            "group": groups,
            "test": tests,
            "schedule": schedules,
            "archives": archives,
            "tools": tools,
        },
    )

    payload = {
        "ui_schema": TASK_UI_SCHEMA,
        "json_schema": enriched_schema,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)
