from copy import deepcopy
from typing import Dict, List, Optional
from fastapi import Body
from fastapi_versioning import version
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, HTTPException, Security, Header
from pscompose.backends.postgres import backend
from pscompose.schemas import DataTableBase, DataTableUpdate
from pscompose.logger import logger
from pydantic import ValidationError

from pscompose.auth import auth_check
from pscompose.settings import TOKEN_SCOPES
from pscompose.auth.basic import backend as backend_user
from pscompose.models import User

def generate_router(datatype: str):
    """
    Generates a FastAPI router with list and item-specific endpoints for a given datatype.

    :param datatype: The name of the datatype (e.g., "template", "host").
    :return: A FastAPI router.
    """

    router = APIRouter(tags=[f"{datatype}"])

    def sanitize_input(data):
        return data

    router.sanitize = sanitize_input

    # Endpoint for retrieving all records of a given datatype (e.g., GET /template/)
    # List endpoint (e.g., GET /template/)
    @router.get(f"/{datatype}/", summary=f"List all {datatype}s")
    @version(1)
    def list_items():
        rows = backend.get_results(datatype=datatype)
        return rows

    # List endpoints with favorites sorted first
    @router.get(f"/{datatype}/favorites/{{username}}/", summary=f"List all {datatype}s with user's favorites sorted first")
    @version(1)
    def list_items(
        username: str,
        user: User = Security(auth_check, scopes=[TOKEN_SCOPES["read"]]),
    ):
        try:
            db_user = backend_user.query(username=username)[0]
        except Exception:
            raise HTTPException(status_code=422)

        rows = backend.get_results(datatype=datatype)
        
        favorite_ids = set(getattr(db_user, "favorites", [])) 
        favorites_first = sorted(rows, key=lambda item: 0 if item.id in favorite_ids else 1)

        return favorites_first

    # Endpoint for CREATING a new record
    # Create endpoint (e.g., POST /template/)
    @router.post(f"/{datatype}/", summary=f"Create a new {datatype}")
    @version(1)
    def create_item(
        data=Body(...),
        # user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
        isImport: Optional[bool] = Header(default=None, alias="X-Import"),
        conflictResolve: Optional[str] = Header(default=None, alias="X-Conflict"),
        orphanBool: Optional[bool] = Header(default=None, alias="X-Orphan")
    ):
        try:
            response = _create_item(data, isImport, conflictResolve, orphanBool)
            result = {"message": f"{datatype} created successfully", "id": response.id}
            if hasattr(response, 'orphans') and response.orphans:
                result["orphans"] = response.orphans
            return result
        except Exception as e:
            logger.error(f"Unhandled error in create_item {datatype}: {str(e)}", exc_info=True)
            raise HTTPException(status_code=500, detail="Internal server error")
        
    
    def _create_item(
            data, 
            isImport: Optional[bool] = False, 
            conflictResolve: Optional[str] = 'keep_both',
            orphanBool: Optional[bool] = False):
        """
        Internal create_item 
        """
        # TODO: Check if datatype with name already exists -> error (or do this in frontend?)
                
        if isImport:
            try: 
                return router.create_import_template(data, conflictResolve, orphanBool)
                return result
            except Exception as e:
                logger.debug("Error creating datatype:", str(e))
                raise HTTPException(status_code=500, detail=str(e))
        sanitized_data = router.sanitize(data)

        # Convert sanitized dict into a proper DataTableBase object
        try:
            data = DataTableBase(**sanitized_data)
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=str(e))
        
        # TODO: Fix the created_by and last_edited_by
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
            return response
        except IntegrityError as e:
            # backend.session.rollback()  # Roll back transaction in case of failure
            logger.debug("Integrity error:", str(e))
            raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
        except Exception as e:
            # backend.session.rollback()
            print("Error creating datatype:", str(e))
            raise HTTPException(status_code=500, detail=str(e))

    router._create_item = _create_item

    # Endpoint for UPDATING an existing record
    # Update endpoint (e.g., PUT /template/uuid-slug/)
    @router.put(f"/{datatype}/{{item_id}}/", summary=f"Update a {datatype}")
    @version(1)
    def update_item(
        item_id: str,
        updated_data=Body(...),
        # user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        return _update_item(item_id, updated_data)
    
    def _update_item(item_id, updated_data):
        """
        Internal update_item
        """
        sanitized_data = router.sanitize(updated_data)

        try:
            updated_data = DataTableUpdate(**sanitized_data)
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=str(e))

        existing_result = backend.get_datatype(datatype=datatype, item_id=item_id)
        if not existing_result:
            raise HTTPException(
                status_code=404, detail=f"{datatype.capitalize()} with ID {item_id} not found"
            )

        response = backend.update_datatype(
            existing_result=existing_result, updated_data=updated_data
        )
        return response
    
    router._update_item = _update_item


    # Endpoint for DELETING an existing record
    # Delete endpoint (e.g., DELETE /template/)
    @router.delete(f"/{datatype}/{{item_id}}/", summary=f"Delete a {datatype}")
    @version(1)
    def delete_item(
        item_id: str,
        # user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        logger.debug("Deleting item with ID:", item_id)

        # Find all ref_set references to this item_id and remove them
        # Also, update the JSON
        cleanup_response = backend.remove_references(item_id)  # noqa: F841

        existing_item = backend.get_datatype(datatype=datatype, item_id=item_id)
        if not existing_item:
            raise HTTPException(
                status_code=404, detail=f"{datatype.capitalize()} with ID {item_id} not found"
            )

        response = backend.delete_datatype(existing_item)
        logger.debug("Delete response:", response)
        return response

    # Endpoint for retrieving a specific item by ID
    @router.get(
        f"/{datatype}/{{item_id}}/", summary=f"Retrieve a specific {datatype} record by its ID"
    )
    def get_item(item_id: str):
        try:
            response = backend.get_datatype(datatype=datatype, item_id=item_id)
        except HTTPException:
            raise HTTPException(
                status_code=404, detail=f"{datatype.capitalize()} with id: {item_id} not found"
            )
        return response

    # Endpoint for retrieving list of records which reference a particular item
    @router.get(
        f"/{datatype}/{{item_id}}/find/",
        summary="Retrieve the records which reference a particular record",
    )
    def find_records(item_id: str):        
        try:
            response = backend.find_records(target_id=item_id)
        except HTTPException:
            raise HTTPException(status_code=404, detail="Error in finding records")
        return response

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


def enrich_schema(base_schema: Dict, updates: Dict[str, List]) -> Dict:
    """
    Enrich a JSON schema by injecting 'oneOf' options for multiple properties at once.

    Args:
        base_schema: JSON schema to enrich.
        updates: Mapping of property name -> rows list
                 (e.g., {"group": groups, "addresses": address_rows})

    Returns:
        Updated copy of the schema.
    """
    schema_copy = deepcopy(base_schema)

    def inject_items(props: Dict, prop_name: str, rows: List):
        """Inject oneOf entries for a single property."""
        if prop_name not in props:
            return

        prop_def = props[prop_name]

        # Determine where the 'oneOf' list lives
        if prop_def.get("type") == "array":
            items = prop_def.get("items")
            if not items or "oneOf" not in items:
                return
            oneof_target = items["oneOf"]
        else:
            if "oneOf" not in prop_def:
                prop_def["oneOf"] = []
            oneof_target = prop_def["oneOf"]

        # Clear existing options
        oneof_target.clear()

        # Handle empty rows
        if not rows:
            oneof_target.append({"const": "", "title": "No options available"})
            return

        # Prepare unique IDs and labels
        ids = _unique_keep_order([str(row.id) for row in rows])
        labels = [str(row.name) for row in rows if str(row.id) in ids]

        for id_, label in zip(ids, labels):
            oneof_target.append({"const": id_, "title": label})

    # Update top-level properties
    if "properties" in schema_copy:
        for prop_name, rows in updates.items():
            inject_items(schema_copy["properties"], prop_name, rows)

    # Update nested allOf → then → properties
    for branch in schema_copy.get("allOf", []):
        then_part = branch.get("then")
        if not then_part:
            continue
        props = then_part.get("properties", {})
        for prop_name, rows in updates.items():
            inject_items(props, prop_name, rows)

    return schema_copy
