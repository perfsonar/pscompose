from fastapi import APIRouter, HTTPException, Security
from fastapi_versioning import version
from pscompose.models import User, DataTable
from pscompose.auth import auth_check
from pscompose.backends.postgres_backend_alternate import backend
from pscompose.settings import DataTypes, TOKEN_SCOPES

router = APIRouter(tags=["Hosts"])


@router.get("/host/form", summary="Return the form to be rendered on the host page")
@version(1)
def get_form():
    # Talk to pScheduler API
    pass