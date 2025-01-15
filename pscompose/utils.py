from fastapi import APIRouter, HTTPException, Security
from fastapi_versioning import version

from pscompose.backends.postgres import backend
from pscompose.settings import DataTypes
from pscompose.models import User, DataTable
from pscompose.auth import auth_check
from pscompose.backends.postgres import backend
from pscompose.settings import DataTypes, TOKEN_SCOPES
from pscompose.form_schemas import HOST_SCHEMA, HOST_UI_SCHEMA
from pscompose.schemas import DataTableBase

from sqlalchemy.exc import IntegrityError

def generate_router(datatype: str, user: User):
    """
    Generates a FastAPI router with list and item-specific endpoints for a given datatype.
    
    :param datatype: The name of the datatype (e.g., "template", "host").
    :return: A FastAPI router.
    """

    router = APIRouter(tags=[f"{datatype}"])

    # List endpoint (e.g., GET /templates)
    @router.get(f"/{datatype}s/", summary=f"List all {datatype}s")
    @version(1)
    def list_items():
        rows = backend.get_results(type=datatype)
        if not rows:
            raise HTTPException(status_code=404, detail=f"No {datatype}s found")
        return rows

    @router.post(f"/{datatype}", summary=f"Create a new {datatype}")
    @version(1)
    def create_datatype(
        record: DataTableBase,
        user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
    ):
        try:
            response = backend.create_datatype(
                ref_set=record.ref_set,
                type=datatype,
                json=record.json,
                name=record.name,
                created_by=user.name,
                # created_at = ""
                last_edited_by=user.name,
                # last_edited_at = ""
            )
            return {
                "message": f"{datatype} created successfully", 
                "id": response.id
            }
        except IntegrityError as e:
            backend.session.rollback()  # Roll back transaction in case of failure
            raise HTTPException(status_code=400, detail=f"Integrity error: {str(e)}")
        except Exception as e:
            backend.session.rollback()
    
    # Create endpoint (e.g., POST /template)
    # router.post(f"/{datatype}/", summary=f"Create a new {datatype}")(
    #     create_item_endpoint(datatype, item_handler, "create")
    # )

    return router