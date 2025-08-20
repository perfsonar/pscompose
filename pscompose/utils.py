from fastapi import APIRouter, HTTPException, Security, Request, Form, Body
from fastapi_versioning import version
from fastapi.responses import HTMLResponse, Response

from pscompose.backends.postgres import backend
from pscompose.settings import DataTypes
from pscompose.models import User, DataTable
from pscompose.auth import auth_check
from pscompose.backends.postgres import backend
from pscompose.settings import DataTypes, TOKEN_SCOPES, PARENT_CHILD_RELATIONSHIP
from pscompose.schemas import DataTableBase, DataTableUpdate

from sqlalchemy.exc import IntegrityError

def generate_router(datatype: str):
    """
    Generates a FastAPI router with list and item-specific endpoints for a given datatype.
    
    :param datatype: The name of the datatype (e.g., "template", "host").
    :return: A FastAPI router.
    """

    router = APIRouter(tags=[f"{datatype}"])

    # Endpoint for retrieving all records of a given datatype (e.g., GET /template)
    # List endpoint (e.g., GET /api/template)
    @router.get(f"/api/{datatype}", summary=f"List all {datatype}s")
    @version(1)
    def list_items():
        rows = backend.get_results(datatype=datatype)
        return rows

    # Endpoint for CREATING a new record
    # Create endpoint (e.g., POST /api/template)
    @router.post(f"/api/{datatype}", summary=f"Create a new {datatype}")
    @version(1)
    def create_item(
        data: DataTableBase,
        # user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        try:
            response = backend.create_datatype(
                ref_set=data.ref_set,
                datatype=datatype,
                json=data.json_data.dict(by_alias=True),
                name=data.name,
                created_by=data.created_by,
                # created_by=user.name,
                last_edited_by=data.last_edited_by,
                # last_edited_by=user.name,
            )

            # TODO: See comment below?
            # Do we need to update on each of the child objects when a new type is created?
    
            return {
                "message": f"{datatype} created successfully", 
                "id": response["id"]
            }
        except IntegrityError as e:
            # backend.session.rollback()  # Roll back transaction in case of failure
            raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
        except Exception as e:
            # backend.session.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    # Endpoint for UPDATING an existing record
    # Update endpoint (e.g., PUT /api/template/uuid-slug)
    @router.put(f"/api/{datatype}/{{item_id}}", summary=f"Update a {datatype}")
    @version(1)
    def update_item(
        item_id: str,
        updated_data: DataTableUpdate,
        # user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        existing_result = backend.get_datatype(datatype=datatype, item_id=item_id)
        if not existing_result:
            raise HTTPException(status_code=404, detail=f"{datatype.capitalize()} with ID {item_id} not found")

        # TODO: In this, how will ref_set be updated?
        response = backend.update_datatype(
            existing_result=existing_result,
            updated_data=updated_data
        )
        print("update response:", response)
        return response

    # Endpoint for DELETING an existing record
    # Delete endpoint (e.g., DELETE /template)
    @router.delete(f"/api/{datatype}/{{item_id}}", summary=f"Delete a {datatype}")
    @version(1)
    def delete_item(
        item_id: str,
        # user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        print("Deleting item with ID:", item_id)
        existing_item = backend.get_datatype(datatype=datatype, item_id=item_id)
        if not existing_item:
            raise HTTPException(status_code=404, detail=f"{datatype.capitalize()} with ID {item_id} not found")

        response = backend.delete_datatype(existing_item)
        print("Delete response:", response)
        # Return success response with redirect
        # TODO: This isn't working
        return Response(
            status_code=200,
            headers={"HX-Redirect": "http://localhost:5001"}  # Redirect after success
        )

    # Endpoint for retrieving a specific item by ID
    @router.get(f"/api/{datatype}/{{item_id}}", summary=f"Retrieve a specific {datatype} record by its ID")
    def get_item(item_id: str):
        try:
            response = backend.get_datatype(datatype=datatype, item_id=item_id)
        except HTTPException as e:
            raise HTTPException(status_code=404, detail=f"{datatype.capitalize()} with id: {item_id} not found")
        return response

    # Endpoint for retrieving a specific item's json
    @router.get(f"/api/{datatype}/{{item_id}}/json", summary=f"Retrieve the JSON of a specific {datatype} record")
    def get_item_json(item_id: str):
        try:
            response = backend.get_datatype(datatype=datatype, item_id=item_id)
            response_json = response.json
        except HTTPException as e:
            raise HTTPException(status_code=404, detail=f"{datatype.capitalize()} with id: {item_id} not found")
        return response_json

    return router