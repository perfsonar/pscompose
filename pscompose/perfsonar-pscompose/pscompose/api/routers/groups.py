from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.backends.postgres import backend
from pscompose.form_schemas.group_schemas import GROUP_SCHEMA, GROUP_UI_SCHEMA
from pscompose.utils import generate_router, enrich_schema

# Setup CRUD endpoints
router = generate_router("group")


# Custom sanitize function to transform the data for the backend
def sanitize_data(data):
    json_data = data["json"]
    ref_set = data["ref_set"]

    # Formatting Excludes
    # FROM {'local-address': id, 'target-addresses': [id, id]}
    # TO {"local-address": {"name": id }, "target-addresses": [{"name": id}, ...]}
    exclude_addresses = []
    if json_data.get("excludes"):
        for exclude in json_data["excludes"]:
            local = exclude["local-address"]
            targets = exclude["target-addresses"]

            exclude_addresses.append(
                {
                    "local-address": {"name": local},
                    "target-addresses": [{"name": t} for t in targets],
                }
            )

            # update ref_set
            if local not in ref_set:
                ref_set.append(local)
            for t in targets:
                if t not in ref_set:
                    ref_set.append(t)
        json_data["excludes"] = exclude_addresses

    for key in ("addresses", "a-addresses", "b-addresses"):
        if json_data.get(key) is not None:
            address_id_array = []
            for address in json_data.get(key, []):
                obj = {"name": address}  # or {name: id} based on your variables
                if address not in ref_set:
                    ref_set.append(address)
                address_id_array.append(obj)
            json_data[key] = address_id_array

    data["ref_set"] = ref_set
    data["json"] = json_data
    return data


def sanitize_response(response_json):
    json_data = response_json.copy()

    # Transform address fields from list of dicts to list of strings
    for key in ("addresses", "a-addresses", "b-addresses"):
        if json_data.get(key) is not None:
            json_data[key] = [addr["name"] for addr in json_data.get(key, [])]

    # Transform exclude address fields from list of dicts to list of strings
    # FROM {"local-address": {"name": id}, "target-addresses": [{"name": id}, ...]}
    # TO {'local-address': id, 'target-addresses': [id, id]}
    if json_data.get("excludes") is not None:
        back_excludes = json_data["excludes"]
        front_excludes = []
        for back_exclude in back_excludes:
            front_exclude = {}

            front_exclude["local-address"] = back_exclude["local-address"]["name"]
            front_exclude["target-addresses"] = [
                target["name"] for target in back_exclude["target-addresses"]
            ]
            front_excludes.append(front_exclude)
        json_data["excludes"] = front_excludes

    return json_data


router.sanitize = sanitize_data


# Custom endpoints
@router.get("/group/new/form/", summary="Return the new form to be rendered")
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
            "local-address": address_rows,
            "target-addresses": address_rows,
        },
    )
    print("json_schema: ", enriched_schema)

    payload = {"ui_schema": GROUP_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/group/{item_id}/form/",
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
            "local-address": address_rows,
            "target-addresses": address_rows,
        },
    )

    payload = {
        "ui_schema": GROUP_UI_SCHEMA,
        "json_schema": enriched_schema,
        "form_data": sanitize_response(response_json),
    }
    return JSONResponse(content=payload)
