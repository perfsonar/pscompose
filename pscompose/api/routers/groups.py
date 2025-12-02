from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.backends.postgres import backend
from pscompose.form_schemas import GROUP_SCHEMA, GROUP_UI_SCHEMA
from pscompose.utils import generate_router, enrich_schema

# Setup CRUD endpoints
router = generate_router("group")


# Custom sanitize function to transform the data for the backend
def sanitize_data(data):
    json_data = data["json"]

    # Cleaning up the data
    if "schema" in data and "group_type" in data:
        schema = data["schema"]
        group_type = data["group_type"]

        # Find the matching schema for the relevant group type
        type_schema = next(
            (
                item
                for item in schema.get("allOf", [])
                if item.get("if", {}).get("properties", {}).get("type", {}).get("const")
                == group_type
            ),
            None,
        )

        if not type_schema:
            raise ValueError(f"No schema found for type {group_type}")

        # Filter json_data to only include properties that are allowed for this type
        allowed_keys = type_schema.get("then", {}).get("properties", {}).keys()
        filtered_json = {k: json_data[k] for k in allowed_keys if k in json_data}

        # Remove these keys from the main data dictionary
        if "schema" in data:
            del data["schema"]

        if "group_type" in data:
            del data["group_type"]

    ref_set = data["ref_set"]

    # for key in ("addresses", "a-addresses", "b-addresses"):
    #     if json_data.get(key) is not None:
    #         for address in json_data.get(key, []):
    #             name = address["name"]
    #             if name not in ref_set:
    #                 ref_set.append(name)

    for key in ("addresses", "a-addresses", "b-addresses"):
        if json_data.get(key) is not None:
            address_id_array = []
            for address in json_data.get(key, []):
                obj = { "name": address }  # or {name: id} based on your variables
                if address not in ref_set:
                    ref_set.append(address)
                address_id_array.append(obj)
            filtered_json[key] = address_id_array

    data["ref_set"] = ref_set
    data["json"] = filtered_json
    return data

def sanitize_reponse(response_json):
    json_data = response_json.copy()

    # Transform address fields from list of dicts to list of strings
    for key in ("addresses", "a-addresses", "b-addresses"):
        if json_data.get(key) is not None:
            json_data[key] = [addr["name"] for addr in json_data.get(key, [])]

    return json_data


router.sanitize = sanitize_data


# Custom endpoints
@router.get("/api/group/new/form", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    try:
        address_rows = backend.get_results(datatype=DataTypes.ADDRESS)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch addresses: {str(e)}")

    enriched_schema = enrich_schema(
        base_schema=GROUP_SCHEMA,
        updates={
            "addresses": address_rows,
            "a-addresses": address_rows,
            "b-addresses": address_rows,
            "excludes": address_rows,
        },
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
        response_json = {
            k: v for k, v in response_json.items() if v is not None
        }  # Need to remove null fields

        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Group with id: {item_id} not found")

    try:
        address_rows = backend.get_results(datatype=DataTypes.ADDRESS)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch addresses: {str(e)}")

    enriched_schema = enrich_schema(
        base_schema=GROUP_SCHEMA,
        updates={
            "addresses": address_rows,
            "a-addresses": address_rows,
            "b-addresses": address_rows,
            "excludes": address_rows,
        },
    )
    print('response_json for existing form:', sanitize_reponse(response_json))

    payload = {
        "ui_schema": GROUP_UI_SCHEMA,
        "json_schema": enriched_schema,
        "form_data": sanitize_reponse(response_json),
    }
    return JSONResponse(content=payload)
