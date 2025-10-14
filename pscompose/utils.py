from copy import deepcopy
from typing import Dict, List
from fastapi import Body
from fastapi_versioning import version
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, HTTPException
from pscompose.backends.postgres import backend
from pscompose.schemas import DataTableBase, DataTableUpdate
from pydantic import ValidationError


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
        data=Body(...),
        # user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        print("CREATE Unsanitized data:", data)
        sanitized_data = router.sanitize(data)
        print("CREATE Sanitized data:", sanitized_data)
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

            # TODO: Do we need to update on each of the child objects when a new type is created?
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
        updated_data=Body(...),
        # user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        sanitized_data = router.sanitize(updated_data)

        # Convert sanitized dict into a proper DataTableUpdate object
        try:
            updated_data = DataTableUpdate(**sanitized_data)
        except ValidationError as e:
            raise HTTPException(status_code=422, detail=str(e))

        existing_result = backend.get_datatype(datatype=datatype, item_id=item_id)
        if not existing_result:
            raise HTTPException(
                status_code=404, detail=f"{datatype.capitalize()} with ID {item_id} not found"
            )

        # TODO: In this, how will ref_set be updated?
        response = backend.update_datatype(
            existing_result=existing_result, updated_data=updated_data
        )
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
        print("response from delete:", response)
        return response

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
