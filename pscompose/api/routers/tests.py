from fastapi_versioning import version
from pscompose.form_schemas import HOST_SCHEMA, HOST_UI_SCHEMA
from pscompose.utils import generate_router
from pscompose.settings import DataTypes
from pscompose.backends.postgres import backend

# Setup CRUD endpoints
router = generate_router("test")

# Custom endpoints
@router.get("/test/form", summary="Return the form to be rendered")
@version(1)
def get_form():
    # Talk to pScheduler API
    pass

@router.get("/test/{testId}/change")
@version(1)
def get_updated_entries(testId: str):
    results = backend.find_records(target_id=testId)
    return results

@router.post("/test/{testType}/{testId}/form/validate", summary="Validate the form data once user submits the form")
@version(1)
def validate_form(testType: str, testId: str):
    # Talk to pScheduler API
    # pScheduler API will look at the form data and then append a version number as well
    pass
