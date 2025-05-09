from fastapi_versioning import version
from fastapi.responses import JSONResponse, HTMLResponse

from pscompose.utils import generate_router
from pscompose.settings import DataTypes
from pscompose.backends.postgres import backend

# Setup CRUD endpoints
router = generate_router("test")

# Custom endpoints
# @router.get("/test/{testType}/new/form", summary="Return the form to be rendered")
# @version(1)
# def get_form():
#     # Talk to pScheduler API
#     pass

# @router.post("/test/{testType}/{testId}/form/validate", summary="Validate the form data once user submits the form")
# @version(1)
# def validate_form(testType: str, testId: str):
#     # Talk to pScheduler API
#     # pScheduler API will look at the form data and then append a version number as well
#     pass

# @router.get("/test/{testId}/change")
# @version(1)
# def get_updated_entries(testId: str):
#     results = backend.find_records(target_id=testId)
#     return results

@router.get("/test/idle/new/form", summary="Return the IDLE form")
@version(1)
def validate_form(testType: str):
    json_schema = {
        "additionalProperties": False,
        "properties": {
            "duration": {
                "#": "Modified not to accept months or years, which are inexact.",
                "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                "type": "string",
                "x-invalid-message": "'%s' is not a valid ISO 8601 duration."
            },
            "host": {
                "items": {
                    "anyOf": [
                        {
                            "#": "See #1514.",
                            "maxLength": 255,
                            "minLength": 1,
                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
                            "type": "string"
                        },
                        {
                            "oneOf": [
                                {
                                    "format": "ipv4",
                                    "type": "string"
                                },
                                {
                                    "format": "ipv6",
                                    "type": "string"
                                }
                            ]
                        }
                    ]
                },
                "minItems": 1,
                "type": "array"
            },
            "parting-comment": {
                "type": "string"
            },
            "schema": {
                "enum": [
                    2
                ],
                "type": "integer"
            },
            "starting-comment": {
                "type": "string"
            }
        },
        "required": [
            "duration"
        ],
        "type": "object"
    }

    payload = {
        "ui_schema": {},
        "json_schema": json_schema,
        "form_data": {}
    }

    return JSONResponse(content=payload)