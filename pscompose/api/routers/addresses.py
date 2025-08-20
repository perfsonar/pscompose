from fastapi import HTTPException, Request
from fastapi_versioning import version
from pscompose.form_schemas import ADDRESS_SCHEMA, ADDRESS_UI_SCHEMA
from pscompose.utils import generate_router
from pscompose.settings import DataTypes
from pscompose.backends.postgres import backend
from fastapi.responses import JSONResponse, HTMLResponse

# Setup CRUD endpoints
# - GET /api/address
# - POST /api/address
# - PUT /api/address/uuid-slug
# - DELETE /api/address/uuid-slug
# - GET /api/address/uuid-slug
# - GET /api/address/uuid-slug/json
router = generate_router("address")

# Custom endpoints
@router.get("/api/address/new/form", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    payload = {
        "ui_schema": ADDRESS_UI_SCHEMA,
        "json_schema": ADDRESS_SCHEMA,
        "form_data": {}
    }
    return JSONResponse(content=payload)

@router.get(f"/api/address/{{item_id}}/form", summary="Get the JSON Data and form data identified by the uuid-slug")
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.ADDRESS, item_id=item_id)
        response_json = response.json
        response_json['name'] = response.name # Adding "name" since it's not present in the json
    except HTTPException as e:
        raise HTTPException(status_code=404, detail=f"Address with id: {item_id} not found")
    payload = {
        "ui_schema": ADDRESS_UI_SCHEMA,
        "json_schema": ADDRESS_SCHEMA,
        "form_data": response_json
    }
    return JSONResponse(content=payload)

# TODO: Test this
# @router.get("/api/address/{addressId}/change")
# @version(1)
# def get_updated_entries(addressId: str):
#     '''
#     Get the entire list of things that will need to be updated when some information about a given host is changed.
#     This will include host groups that reference this host, along with perhaps tests, tasks, templates and others
#     '''
#     results = backend.find_records(target_id=addressId)
#     return results