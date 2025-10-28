from fastapi import HTTPException
from fastapi_versioning import version
from pscompose.form_schemas import ADDRESS_SCHEMA, ADDRESS_UI_SCHEMA
from pscompose.utils import generate_router, enrich_schema
from pscompose.settings import DataTypes
from pscompose.backends.postgres import backend
from fastapi.responses import JSONResponse

# Setup CRUD endpoints
router = generate_router("address")


# Custom sanitize function to transform the data for the backend
def sanitize_data(data):
    print("inside sanitize data ", data)
    json_data = data["json"]

    # Cleaning up the data since empty strings are not allowed for these fields
    for field in ["lead-bind-address", "pscheduler-address"]:
        if field in json_data and json_data[field] == "":
            json_data[field] = None

    ref_set = data["ref_set"]
    if json_data.get("contexts") is not None:
        for context in json_data.get("contexts", []):
            ref_set.append(context)

    data["ref_set"] = ref_set
    data["json"] = json_data
    return data


router.sanitize = sanitize_data


# Custom endpoints
@router.get("/api/address/new/form", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    try:
        context_rows = backend.get_results(datatype=DataTypes.CONTEXT)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch addresses: {str(e)}")

    enriched_schema = enrich_schema(base_schema=ADDRESS_SCHEMA, updates={"contexts": context_rows})

    payload = {"ui_schema": ADDRESS_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/api/address/{item_id}/form",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.ADDRESS, item_id=item_id)
        response_json = response.json
        response_json = {
            k: v for k, v in response_json.items() if v is not None
        }  # Need to remove null fields

        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Address with id: {item_id} not found")

    try:
        context_rows = backend.get_results(datatype=DataTypes.CONTEXT)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch addresses: {str(e)}")

    enriched_schema = enrich_schema(base_schema=ADDRESS_SCHEMA, updates={"contexts": context_rows})

    payload = {
        "ui_schema": ADDRESS_UI_SCHEMA,
        "json_schema": enriched_schema,
        "form_data": response_json,
    }

    return JSONResponse(content=payload)
