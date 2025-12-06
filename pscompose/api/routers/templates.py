from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router, enrich_schema
from pscompose.backends.postgres import backend
from pscompose.form_schemas import TEMPLATE_SCHEMA, TEMPLATE_UI_SCHEMA

# Setup CRUD endpoints
router = generate_router("template")


def remove_null_values(obj):
    """
    Recursively remove keys with null/None values from dictionaries.
    Also removes empty lists and empty dicts.
    """
    if isinstance(obj, dict):
        return {
            k: remove_null_values(v)
            for k, v in obj.items()
            if v is not None and v != [] and v != {}
        }
    elif isinstance(obj, list):
        return [remove_null_values(item) for item in obj if item is not None]
    else:
        return obj


def expand_template_to_psconfig(template_id: str):
    """
    Expand a template into a full pScheduler mesh configuration.
    """
    # Fetch the template
    try:
        template = backend.get_datatype(datatype=DataTypes.TEMPLATE, item_id=template_id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"Template with id {template_id} not found")

    task_ids = template.json.get("tasks", [])

    # Initialize the pScheduler config structure matching pSConfigSchema
    psconfig = {
        "addresses": {},
        "groups": {},
        "tests": {},
        "tasks": {},
    }

    # Optional sections - only add if we have data for them
    # archives, contexts, schedules will be added only if needed

    # Track what we've already added to avoid duplicates
    added_archives = set()
    added_addresses = set()
    added_groups = set()
    added_tests = set()
    added_schedules = set()

    # Process each task
    for task_id in task_ids:
        try:
            task = backend.get_datatype(datatype=DataTypes.TASK, item_id=task_id)
            task_json = task.json
            task_name = task.name

            print(f"Processing task: {task_name} (ID: {task_id})")
            print(f"Task JSON: {task_json}")

            # Build task spec - only include fields that have values
            task_spec = {}

            # Add optional task fields only if they have non-null/non-empty values
            if task_json.get("scheduled-by") is not None:
                task_spec["scheduled-by"] = task_json.get("scheduled-by")
            if task_json.get("disabled") is not None:
                task_spec["disabled"] = task_json.get("disabled")
            if task_json.get("tools") and len(task_json.get("tools")) > 0:
                task_spec["tools"] = task_json.get("tools")

            # Process subtasks - convert task IDs to task names
            subtask_ids = task_json.get("subtasks", [])
            if subtask_ids and len(subtask_ids) > 0:
                subtask_names = []
                for subtask_id in subtask_ids:
                    try:
                        subtask = backend.get_datatype(datatype=DataTypes.TASK, item_id=subtask_id)
                        subtask_names.append(subtask.name)
                    except Exception as e:
                        print(f"Error fetching subtask {subtask_id}: {e}")
                        continue
                if subtask_names:
                    task_spec["subtasks"] = subtask_names
            if task_json.get("priority") is not None:
                task_spec["priority"] = task_json.get("priority")
            if task_json.get("reference"):
                task_spec["reference"] = task_json.get("reference")
            if task_json.get("_meta"):
                task_spec["_meta"] = task_json.get("_meta")

            psconfig["tasks"][task_name] = task_spec

            # Process test
            test_id = task_json.get("test")
            if test_id:
                if test_id not in added_tests:
                    test = backend.get_datatype(datatype=DataTypes.TEST, item_id=test_id)
                    psconfig["tests"][test.name] = test.json
                    added_tests.add(test_id)
                else:
                    test = backend.get_datatype(datatype=DataTypes.TEST, item_id=test_id)
                task_spec["test"] = test.name

            # Process schedule
            schedule_id = task_json.get("schedule")
            if schedule_id:
                if "schedules" not in psconfig:
                    psconfig["schedules"] = {}
                if schedule_id not in added_schedules:
                    schedule = backend.get_datatype(
                        datatype=DataTypes.SCHEDULE, item_id=schedule_id
                    )
                    psconfig["schedules"][schedule.name] = schedule.json
                    added_schedules.add(schedule_id)
                else:
                    schedule = backend.get_datatype(
                        datatype=DataTypes.SCHEDULE, item_id=schedule_id
                    )
                task_spec["schedule"] = schedule.name

            # Process archives
            archive_ids = task_json.get("archives", [])
            if archive_ids and len(archive_ids) > 0:
                task_archives = []
                for archive_id in archive_ids:
                    if "archives" not in psconfig:
                        psconfig["archives"] = {}
                    if archive_id not in added_archives:
                        archive = backend.get_datatype(
                            datatype=DataTypes.ARCHIVE, item_id=archive_id
                        )
                        psconfig["archives"][archive.name] = archive.json
                        added_archives.add(archive_id)
                    else:
                        archive = backend.get_datatype(
                            datatype=DataTypes.ARCHIVE, item_id=archive_id
                        )
                    task_archives.append(archive.name)
                task_spec["archives"] = task_archives

            # Process group and its addresses
            group_id = task_json.get("group")
            print(f"Task {task_name} - group_id: {group_id}")
            if group_id:
                if group_id not in added_groups:
                    print(f"Adding new group: {group_id}")
                    group = backend.get_datatype(datatype=DataTypes.GROUP, item_id=group_id)
                    group_json = group.json.copy()

                    # Helper function to convert address IDs to address names
                    def convert_address_ids_to_names(address_list):
                        """Convert address ID references to address name references"""
                        converted = []
                        if not address_list:
                            return converted

                        for address_ref in address_list:
                            print(
                                f"Processing address_ref: {address_ref}, type: {type(address_ref)}"
                            )
                            # Handle dict format like {"name": "id"}
                            if isinstance(address_ref, dict):
                                address_id = address_ref.get("name") or address_ref.get("id")
                                print(
                                    f"extracted address_id: {address_id}, type: {type(address_id)}"
                                )
                                # Preserve other fields in the dict
                                # (like "label", "disabled", etc.)
                                new_ref = address_ref.copy()
                            else:
                                address_id = address_ref
                                print(
                                    f"String - address_id: {address_id}, type: {type(address_id)}"
                                )
                                new_ref = {}

                            # Only process if address_id is a string
                            if address_id and isinstance(address_id, str):
                                # Fetch the address to get its actual name
                                if address_id not in added_addresses:
                                    print(f"Fetching address with ID: {address_id}")
                                    address = backend.get_datatype(
                                        datatype=DataTypes.ADDRESS, item_id=address_id
                                    )
                                    psconfig["addresses"][address.name] = address.json
                                    added_addresses.add(address_id)
                                else:
                                    print(
                                        f"Address already added, \
                                        fetching from backend: {address_id}"
                                    )
                                    address = backend.get_datatype(
                                        datatype=DataTypes.ADDRESS, item_id=address_id
                                    )

                                # Replace the ID with the actual address name
                                if isinstance(address_ref, dict):
                                    new_ref["name"] = address.name
                                    converted.append(new_ref)
                                else:
                                    # If it was a string, convert to dict format
                                    converted.append({"name": address.name})

                        return converted

                    # Process addresses - convert IDs to names
                    if "addresses" in group_json:
                        group_json["addresses"] = convert_address_ids_to_names(
                            group_json.get("addresses", [])
                        )
                    if "a-addresses" in group_json:
                        group_json["a-addresses"] = convert_address_ids_to_names(
                            group_json.get("a-addresses", [])
                        )
                    if "b-addresses" in group_json:
                        group_json["b-addresses"] = convert_address_ids_to_names(
                            group_json.get("b-addresses", [])
                        )

                    # Process excludes - convert address IDs to names in
                    # local-address and target-addresses
                    if "excludes" in group_json and group_json["excludes"]:
                        try:
                            for exclude_pair in group_json["excludes"]:
                                # Convert local-address
                                if "local-address" in exclude_pair:
                                    local_addr = exclude_pair["local-address"]
                                    print(
                                        f"Processing local-address in excludes: {local_addr}, type: {type(local_addr)}"  # noqa: E501
                                    )

                                    if isinstance(local_addr, dict):
                                        addr_id = local_addr.get("name") or local_addr.get("id")
                                    else:
                                        addr_id = local_addr

                                    print(f"Extracted addr_id: {addr_id}, type: {type(addr_id)}")

                                    # Only process if addr_id is a string
                                    if addr_id and isinstance(addr_id, str):
                                        if addr_id not in added_addresses:
                                            address = backend.get_datatype(
                                                datatype=DataTypes.ADDRESS, item_id=addr_id
                                            )
                                            psconfig["addresses"][address.name] = address.json
                                            added_addresses.add(addr_id)
                                        else:
                                            address = backend.get_datatype(
                                                datatype=DataTypes.ADDRESS, item_id=addr_id
                                            )

                                        if isinstance(local_addr, dict):
                                            exclude_pair["local-address"]["name"] = address.name
                                        else:
                                            exclude_pair["local-address"] = {"name": address.name}

                                # Convert target-addresses
                                if "target-addresses" in exclude_pair:
                                    exclude_pair["target-addresses"] = (
                                        convert_address_ids_to_names(
                                            exclude_pair["target-addresses"]
                                        )
                                    )
                        except Exception as e:
                            print(f"Error processing excludes for group {group.name}: {e}")
                            # Continue without excludes conversion if there's an error
                            pass

                    psconfig["groups"][group.name] = group_json
                    added_groups.add(group_id)
                    task_spec["group"] = group.name
                    print(f"Set task {task_name} group to: {group.name}")
                else:
                    # Already added, just get the name
                    print(f"Group {group_id} already added, fetching name")
                    group = backend.get_datatype(datatype=DataTypes.GROUP, item_id=group_id)
                    task_spec["group"] = group.name
                    print(f"Set task {task_name} group to: {group.name}")

        except Exception as e:
            print(f"Error processing task {task_id}: {e}")
            continue

    # Clean up null values from the entire structure
    psconfig = remove_null_values(psconfig)

    return psconfig


# Custom endpoints
@router.get("/template/new/form/", summary="Return the new form to be rendered")
@version(1)
def get_new_form():
    try:
        tasks = backend.get_results(datatype=DataTypes.TASK)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

    enriched_schema = enrich_schema(base_schema=TEMPLATE_SCHEMA, updates={"tasks": tasks})

    payload = {"ui_schema": TEMPLATE_UI_SCHEMA, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get(
    "/template/{item_id}/form/",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str):
    try:
        response = backend.get_datatype(datatype=DataTypes.TEMPLATE, item_id=item_id)
        response_json = response.json
        response_json = {
            k: v for k, v in response_json.items() if v is not None
        }  # Need to remove null fields
        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Template with id: {item_id} not found")

    try:
        tasks = backend.get_results(datatype=DataTypes.TASK)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

    enriched_schema = enrich_schema(base_schema=TEMPLATE_SCHEMA, updates={"tasks": tasks})

    payload = {
        "ui_schema": TEMPLATE_UI_SCHEMA,
        "json_schema": enriched_schema,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)


@router.get(
    "/template/{item_id}/json/",
    summary="Get expanded pScheduler mesh configuration JSON",
)
@version(1)
def get_template_json(item_id: str):
    """
    Returns the full expanded pScheduler mesh configuration for this template.
    Includes all referenced tests, archives, schedules, groups, and addresses.
    """
    psconfig = expand_template_to_psconfig(item_id)
    return JSONResponse(content=psconfig)
