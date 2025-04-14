from fastapi_versioning import version
from pscompose.form_schemas import HOST_SCHEMA, HOST_UI_SCHEMA
from pscompose.utils import generate_router
from pscompose.settings import DataTypes
from pscompose.backends.postgres import backend

# Setup CRUD endpoints
router = generate_router("host")

# Custom endpoints
@router.get("/host/form", summary="Return the form to be rendered")
@version(1)
def get_form():
    # Talk to pScheduler API
    # In case we want to render static forms, do this
    return {
        "host_schema": HOST_SCHEMA,
        "host_ui_schema": HOST_UI_SCHEMA
    }

@router.get("/host/{hostId}/change")
@version(1)
def get_updated_entries(hostId: str):
    '''
    Get the entire list of things that will need to be updated when some information about a given host is changed.
    This will include host groups that reference this host, along with perhaps tests, tasks, templates and others
    '''
    results = backend.find_records(target_id=hostId)
    return results