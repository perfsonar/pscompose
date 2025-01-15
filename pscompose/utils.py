from fastapi import APIRouter, HTTPException, Security
from fastapi_versioning import version

from pscompose.backends.postgres import backend
from pscompose.settings import DataTypes
from pscompose.models import User, DataTable
from pscompose.auth import auth_check
from pscompose.backends.postgres import backend
from pscompose.settings import DataTypes, TOKEN_SCOPES
from pscompose.form_schemas import HOST_SCHEMA, HOST_UI_SCHEMA
from pscompose.schemas import DataTableBase

from sqlalchemy.exc import IntegrityError

def generate_router(datatype: str, user: User):
    """
    Generates a FastAPI router with list and item-specific endpoints for a given datatype.
    
    :param datatype: The name of the datatype (e.g., "template", "host").
    :return: A FastAPI router.
    """

    router = APIRouter(tags=[f"{datatype}"])

    # Endpoint for retrieving all records of a given datatype (e.g., GET /templates)
    # List endpoint (e.g., GET /templates)
    @router.get(f"/{datatype}s/", summary=f"List all {datatype}s")
    @version(1)
    def list_items():
        rows = backend.get_results(type=datatype)
        if not rows:
            raise HTTPException(status_code=404, detail=f"No {datatype}s found")
        return rows

    # router.post(f"/{datatype}/", summary=f"Create a new {datatype}")(
    #     create_item_endpoint(datatype, item_handler, "create")
    # )

    # Endpoint for CREATING a new record
    # Create endpoint (e.g., POST /template)
    @router.post(f"/{datatype}", summary=f"Create a new {datatype}")
    @version(1)
    def create_item(
        data: DataTableBase,
        user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        try:
            response = backend.create_datatype(
                ref_set=data.ref_set,
                type=datatype,
                json=data.json,
                name=data.name,
                created_by=user.name,
                # created_at = ""
                last_edited_by=user.name,
                # last_edited_at = ""
            )
            return {
                "message": f"{datatype} created successfully", 
                "id": response.id
            }
        except IntegrityError as e:
            backend.session.rollback()  # Roll back transaction in case of failure
            raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
        except Exception as e:
            backend.session.rollback()

    # Endpoint for UPDATING an existing record
    # Update endpoint (e.g., PUT /template)
    @router.put(f"/{datatype}/{{item_id}}/", summary=f"Update a {datatype}")
    @version(1)
    def update_item(
        item_id: str,
        updated_data: DataTableBase,
        user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        existing_item = backend.get_datatype(type=datatype, id=item_id)
        if not existing_item:
            raise HTTPException(status_code=404, detail=f"{datatype.capitalize()} with ID {item_id} not found")

        response = backend.update_datatype(
            res=existing_item,
            ref_set=updated_data.ref_set,
            json=updated_data.json,
            name=updated_data.name,
            last_edited_by=user.name
            # last_edited_at=""
        )
        return response

    # Endpoint for DELETING an existing record
    @router.delete(f"/{datatype}/{{item_id}}/", summary=f"Delete a {datatype}")
    @version(1)
    def delete_item(
        item_id: str,
        user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        existing_item = backend.get_datatype(type=datatype, id=item_id)
        if not existing_item:
            raise HTTPException(status_code=404, detail=f"{datatype.capitalize()} with ID {item_id} not found")

        response = backend.delete_datatype(existing_item)
        return response

    # Endpoint for retrieving JSON of a specific item by ID
    @router.get(f"/{datatype}/{{item_id}}/json", summary=f"Get the corresponding {datatype} JSON")
    def get_item_json(item_id: str):
        try:
            response = backend.get_datatype_json(type=datatype, id=item_id)
        except HTTPException as e:
            raise HTTPException(status_code=404, detail=f"{datatype.capitalize()} with id: {item_id} not found")
        return response

    # Endpoint for retrieving the URL of a specific item by ID
    @router.get(f"/{datatype}/{{item_id}}/json", summary=f"Get the corresponding {datatype} JSON")
    def get_item_url(item_id: str):
        try:
            response = backend.get_datatype_json(type=datatype, id=item_id)
        except HTTPException as e:
            raise HTTPException(status_code=404, detail=f"{datatype.capitalize()} with id: {item_id} not found")
        return response

    return router