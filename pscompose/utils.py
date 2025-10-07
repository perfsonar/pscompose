from copy import deepcopy
from typing import Dict, List
from fastapi_versioning import version
from fastapi.responses import Response
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, HTTPException
from pscompose.backends.postgres import backend
from pscompose.schemas import DataTableBase, DataTableUpdate


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
        print("Create item data:", data)
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

            return {"message": f"{datatype} created successfully", "id": response.id}
        except IntegrityError as e:
            # backend.session.rollback()  # Roll back transaction in case of failure
            print("Integrity error:", str(e))
            raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
        except Exception as e:
            # backend.session.rollback()
            print("Error creating datatype:", str(e))
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
        print("Update item ID:", item_id)
        print("Update item data:", updated_data)
        existing_result = backend.get_datatype(datatype=datatype, item_id=item_id)
        if not existing_result:
            raise HTTPException(
                status_code=404, detail=f"{datatype.capitalize()} with ID {item_id} not found"
            )

        # TODO: In this, how will ref_set be updated?
        response = backend.update_datatype(
            existing_result=existing_result, updated_data=updated_data
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
            raise HTTPException(
                status_code=404, detail=f"{datatype.capitalize()} with ID {item_id} not found"
            )

        response = backend.delete_datatype(existing_item)
        print("Delete response:", response)
        # Return success response with redirect
        # TODO: This isn't working
        return Response(
            status_code=200,
            headers={"HX-Redirect": "http://localhost:5001"},  # Redirect after success
        )

    # Endpoint for retrieving a specific item by ID
    @router.get(
        f"/api/{datatype}/{{item_id}}", summary=f"Retrieve a specific {datatype} record by its ID"
    )
    def get_item(item_id: str):
        try:
            response = backend.get_datatype(datatype=datatype, item_id=item_id)
        except HTTPException:
            raise HTTPException(
                status_code=404, detail=f"{datatype.capitalize()} with id: {item_id} not found"
            )
        return response

    # Endpoint for retrieving a specific item's json
    @router.get(
        f"/api/{datatype}/{{item_id}}/json",
        summary=f"Retrieve the JSON of a specific {datatype} record",
    )
    def get_item_json(item_id: str):
        try:
            response = backend.get_datatype(datatype=datatype, item_id=item_id)
            response_json = response.json
        except HTTPException:
            raise HTTPException(
                status_code=404, detail=f"{datatype.capitalize()} with id: {item_id} not found"
            )
        return response_json

    return router


# Helper function to ensure unique items while preserving order
def _unique_keep_order(seq):
    """Return a new list with duplicate items removed while preserving order."""
    seen, out = set(), []
    for item in seq:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


# Helper function to enrich the group schema with address IDs and labels
def enrich_group_schema(base_schema: Dict, properties: List[str], rows: List) -> (Dict, Dict):
    """
    Returns a copy of the group JSON-schema and UI-schema where each
    property contains
        - items.oneOf -> dictionary containing unique IDs and label
    """
    ids: List[str] = []
    labels: List[str] = []

    for row in rows:
        ids.append(str(row.id))
        labels.append(str(row.name))

    ids = _unique_keep_order(ids)

    # Update JSON Schema
    schema_copy = deepcopy(base_schema)
    for branch in schema_copy.get("allOf", []):
        then_part = branch.get("then")
        if not then_part:
            continue

        props = then_part.get("properties", {})
        if not any(k in props for k in properties):
            continue

        # inject the enum of IDs into the JSON‑schema
        for prop in properties:
            if prop not in props:
                continue
            addr_items = props[prop]["items"]
            for id in ids:
                res = {"const": id, "title": labels[ids.index(id)]}
                addr_items["oneOf"].append(res)

    return schema_copy
