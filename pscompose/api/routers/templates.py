from fastapi_versioning import version
# from pscompose.form_schemas import TEMPLATE_SCHEMA, TEMPLATE_UI_SCHEMA
from pscompose.utils import generate_router

# Setup CRUD endpoints
router = generate_router("template")

# Custom endpoints
# @router.get("/template/form", summary="Return the form to be rendered")
# @version(1)
# def get_form():
#     # Talk to pScheduler API
#     # In case we want to render static forms, do this
#     return {
#         "template_schema": TEMPLATE_SCHEMA,
#         "template_ui_schema": TEMPLATE_UI_SCHEMA
#     }
