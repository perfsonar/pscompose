from fastapi import APIRouter, HTTPException, Security
from fastapi_versioning import version
from pscompose.models import User, DataTable
from pscompose.auth import auth_check
from pscompose.backends.postgres import backend
from pscompose.settings import DataTypes, TOKEN_SCOPES
from pscompose.form_schemas import HOST_SCHEMA, HOST_UI_SCHEMA

router = generate_router("template")



# router = APIRouter(tags=["Templates"])

# @router.get("/templates", summary="List all templates")
# @version(1)
# def list_templates():
#     rows = backend.get_results(type=DataTypes.TEMPLATE)
#     if not rows:
#         raise HTTPException(status_code=404, detail="No templates found")
#     return rows


# @router.get("/template/form", summary="Return the form to be rendered")
# @version(1)
# def get_form():
#     # Talk to pScheduler API
#     # Talk to pScheduler API
#     # In case we want to render static forms

#     # return [HOST_SCHEMA, HOST_UI_SCHEMA]
#     return {
#         "template_schema": HOST_SCHEMA,
#         "template_ui_schema": HOST_UI_SCHEMA
#     }


# @router.get("/template/form/vaidate", summary="Validate the form data once user submits the form")
# @version(1)
# def validate_form():
#     # Talk to pScheduler API
#     # pScheduler API will look at the form data and then append a version number as well?
#     pass


# @router.post("/template", summary="Submit a new template")
# @version(1)
# def create_template(
#     new_template: DataTable,
#     user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
# ):
#     response = backend.create_datatype(
#         ref_set=new_template.ref_set,
#         type=DataTypes.TEMPLATE,
#         json=new_template.json,
#         name=new_template.name,
#         created_by=user.name,
#         # created_at="",
#         last_edited_by=user.name,
#         # last_edited_at=""
#     )
#     return response


# @router.get("/template/{templateId}/json", summary="Get the corresponding template JSON")
# @version(1)
# def get_json(
#     templateId: str,
# ):
#     response = backend.get_datatype_json(type=DataTypes.TEMPLATE, templateId=templateId)
#     return response


# @router.get("/template/{templateId}/url", summary="Get the corresponding template URL")
# @version(1)
# def get_template_url(
#     templateId: str,
# ):
#     pass


# @router.put("/template/{templateId}", summary="Update the relevant template")
# @version(1)
# def update_template(
#     templateId: str,
#     update_template: DataTable,
#     user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
# ):
#     try:
#         template = backend.get_datatype(type=DataTypes.TEMPLATE, templateId=templateId)
#     except Exception:
#         raise HTTPException(422)
#     response = backend.update_datatype(
#         template,
#         ref_set=update_template.ref_set,
#         json=update_template.json,
#         name=update_template.name,
#         last_edited_by=user.name
#     )
#     return response


# @router.delete("/template/{templateId}", summary="Delete the template from the database")
# @version(1)
# def delete_template(
#     templateId: str,
#     user: User = Security(auth_check, scopes=[TOKEN_SCOPES["admin"]]),
# ):
#     try:
#         template = backend.get_datatype(type=DataTypes.TEMPLATE, templateId=templateId)
#     except Exception:
#         raise HTTPException(422)
#     response = backend.delete_datatype(template)
#     return response

