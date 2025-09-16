from fastapi import HTTPException
from fastapi_versioning import version
from pscompose.form_schemas import GROUP_SCHEMA, GROUP_UI_SCHEMA
from pscompose.utils import generate_router
from pscompose.settings import DataTypes
from pscompose.backends.postgres import backend
from fastapi.responses import JSONResponse
from copy import deepcopy
from typing import Dict, List

# Setup CRUD endpoints
# - GET /api/group
# - POST /api/group
# - PUT /api/group/uuid-slug
# - DELETE /api/group/uuid-slug
# - GET /api/group/uuid-slug
# - GET /api/group/uuid-slug/json
router = generate_router("group")


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
def enrich_group_schema(
    base_schema: Dict, properties: List[str], address_rows: List
) -> (Dict, Dict):
    """
    Returns a copy of the group JSON-schema and UI-schema where the
    addresses property contains
        - items.oneOf -> dictionary containing unique IDs and label
    """
    ids: List[str] = []
    labels: List[str] = []

    for row in address_rows:
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


# Custom endpoints
# TODO: Do these need trailing slashes?
@router.get("/api/group/new/form", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    try:
        address_rows = backend.get_results(datatype=DataTypes.ADDRESS)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch addresses: {str(e)}")

    enriched_schema = enrich_group_schema(
        base_schema=GROUP_SCHEMA,
        properties=["addresses", "a-addresses", "b-addresses", "excludes"],
        address_rows=address_rows
    )

    payload = {"ui_schema": GROUP_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/api/group/{item_id}/form",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.GROUP, item_id=item_id)
        response_json = response.json
        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Address with id: {item_id} not found")

    payload = {
        "ui_schema": GROUP_UI_SCHEMA,
        "json_schema": GROUP_SCHEMA,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)
