import requests
import json
from copy import deepcopy
from fastapi import HTTPException
from fastapi_versioning import version
from fastapi.responses import JSONResponse

from pscompose.settings import DataTypes
from pscompose.utils import generate_router
from pscompose.backends.postgres import backend
from pscompose.form_schemas import TEST_SCHEMA, TEST_UI_SCHEMA

# Setup CRUD endpoints
router = generate_router("test")


# Custom sanitize function to transform the data for the backend
def sanitize_data(data):
    json_data = data["json"]
    spec = {k: v for k, v in json_data.items() if k not in ("type", "_meta")}

    output = {"type": json_data["type"], "spec": spec}

    if "_meta" in json_data:
        output["_meta"] = json_data["_meta"]

    data["json"] = output

    print("Sanitized data:", data)
    return data


router.sanitize = sanitize_data


# Custom endpoints
# @router.get("/test/{testType}/new/form", summary="Return the form to be rendered")
# @version(1)
# def get_form():
#     # Talk to pScheduler API
#     pass

# @router.post(
#   "/test/{testType}/{testId}/form/validate",
#   summary="Validate the form data once user submits the form"
# )
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


def fetch_pscheduler_test_list() -> list[str]:
    """Fetch available test types from the pScheduler API"""
    url = "https://chic-ps-lat.es.net/pscheduler/tests"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return [el.split("/")[-1] for el in data]
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"Failed to fetch external data: {str(e)}",
        )


@router.get("/test/new/form/", summary="Return the form to be rendered")
@version(1)
def get_form():
    # Clone and enrich the schema dynamically
    # tests = fetch_pscheduler_test_list()
    tests = ["idle", "latency", "throughput"]
    enriched_schema = deepcopy(TEST_SCHEMA)
    enriched_schema["properties"]["type"]["oneOf"] = [
        {"const": name, "title": name.upper()} for name in tests
    ]

    # Remove "spec" from TEST_UI_SCHEMA for the new form
    # enriched_schema["properties"].pop("spec", None)

    enriched_ui_schema = deepcopy(TEST_UI_SCHEMA)
    enriched_ui_schema["elements"] = [
        elem for elem in enriched_ui_schema["elements"] if elem.get("scope") != "#/properties/spec"
    ]

    payload = {"ui_schema": enriched_ui_schema, "json_schema": enriched_schema, "form_data": {}}
    return JSONResponse(content=payload)


@router.get("/test/new/{testType}/form/", summary="Return schema for the relevant test type")
@version(1)
def retrieve_form(testType: str):
    print("Retrieving form for test type:", testType)

    idle_schema = {
        "schema": 1,
        "name": "idle",
        "description": "Consume time in the background",
        "version": "1.0",
        "maintainer": {
            "name": "perfSONAR Development Team",
            "email": "perfsonar-developer@internet2.edu",
            "href": "http://www.perfsonar.net",
        },
        "scheduling-class": "background",
        "spec": {
            "jsonschema": {
                "versions": {
                    1: {
                        "additionalProperties": False,
                        "properties": {
                            "duration": {
                                "title": "Duration",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "type": "string",
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "host-node": {
                                "pattern": r"(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\](:[0-9]+)?$)",  # noqa: E501
                                "type": "string",
                                "title": "Host Node",
                            },
                            "parting-comment": {
                                "type": "string",
                                "title": "Parting Comment",
                            },
                            "schema": {
                                "enum": [1],
                                "type": "integer",
                                "title": "Schema Version",
                                "default": 1,
                            },
                            "starting-comment": {
                                "type": "string",
                                "title": "Starting Comment",
                            },
                        },
                        "required": ["duration"],
                        "type": "object",
                    },
                    2: {
                        "additionalProperties": False,
                        "properties": {
                            "duration": {
                                "title": "Duration",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "type": "string",
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "parting-comment": {
                                "type": "string",
                                "title": "Parting Comment",
                            },
                            "schema": {
                                "enum": [2],
                                "type": "integer",
                                "title": "Schema",
                                "default": 2,
                            },
                            "starting-comment": {
                                "type": "string",
                                "title": "Starting Comment",
                            },
                        },
                        "required": ["duration", "schema"],
                        "type": "object",
                    },
                },
            },
            "uischema": {
                "versions": {
                    1: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/duration",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/host-node",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/starting-comment",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/parting-comment",
                                "customComponent": "input-text",
                            },
                        ],
                    },
                    2: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/duration",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/starting-comment",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/parting-comment",
                                "customComponent": "input-text",
                            },
                        ],
                    },
                },
            },
            "versions": [None, "1", "2"],
        },
    }

    throughput_schema = {
        "schema": 1,
        "name": "throughput",
        "description": "Measure network throughput between hosts",
        "version": "1.0",
        "maintainer": {
            "name": "perfSONAR Development Team",
            "email": "perfsonar-developer@internet2.edu",
            "href": "http://www.perfsonar.net",
        },
        "scheduling-class": "exclusive",
        "spec": {
            "jsonschema": {
                "versions": {
                    7: {
                        "title": "pScheduler Throughput Specification Schema",
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "schema": {
                                "type": "integer",
                                "enum": [7],
                                "title": "Schema Version",
                                "default": 7,
                            },
                            "source": {
                                "title": "Source",
                                "oneOf": [
                                    {"type": "string", "format": "ipv4"},
                                    {"type": "string", "format": "ipv6"},
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                    },
                                ],
                                "default": "{% address[0] %}",
                            },
                            "source-node": {
                                "title": "Source Node",
                                "type": "string",
                                "default": "{% pscheduler_address[0] %}",
                            },
                            "dest": {
                                "title": "Destination",
                                "oneOf": [
                                    {"type": "string", "format": "ipv4"},
                                    {"type": "string", "format": "ipv6"},
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                    },
                                ],
                                "default": "{% address[1] %}",
                            },
                            "dest-node": {
                                "title": "Destination Node",
                                "type": "string",
                                "default": "{% pscheduler_address[1] %}",
                            },
                            "duration": {
                                "title": "Duration",
                                "type": "string",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "interval": {
                                "title": "Interval",
                                "type": "string",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "link-rtt": {
                                "title": "Link RTT",
                                "type": "string",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "parallel": {
                                "title": "Number of Parallel Streams",
                                "type": "integer",
                                "minimum": 1,
                            },
                            "udp": {"title": "UDP", "type": "boolean"},
                            "bandwidth": {"title": "Bandwidth", "type": "integer", "minimum": 1},
                            "bandwidth-strict": {"title": "Bandwidth Strict", "type": "boolean"},
                            "burst-size": {"title": "Burst Size", "type": "integer", "minimum": 1},
                            "fq-rate": {"title": "FQ Rate", "type": "integer", "minimum": 1},
                            "window-size": {
                                "title": "Window Size",
                                "type": "integer",
                                "minimum": 1,
                            },
                            "mss": {"title": "MSS", "type": "integer", "minimum": 1},
                            "buffer-length": {
                                "title": "Buffer Length",
                                "type": "integer",
                                "minimum": 1,
                            },
                            "ip-tos": {
                                "title": "TOS Bits",
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 255,
                            },
                            "ip-version": {
                                "title": "IP Version",
                                "type": "integer",
                                "enum": [4, 6],
                            },
                            "local-address": {
                                "title": "Local Address",
                                "oneOf": [
                                    {"type": "string", "format": "ipv4"},
                                    {"type": "string", "format": "ipv6"},
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                    },
                                ],
                            },
                            "omit": {
                                "title": "Omit Interval",
                                "type": "string",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "no-delay": {"title": "No Delay", "type": "boolean"},
                            "congestion": {"title": "Congestion", "type": "string"},
                            "zero-copy": {"title": "Use Zero Copy", "type": "boolean"},
                            "flow-label": {"title": "Flow Label", "type": "integer", "minimum": 1},
                            "client-cpu-affinity": {
                                "title": "Client CPU Affinity",
                                "type": "integer",
                            },
                            "server-cpu-affinity": {
                                "title": "Server CPU Affinity",
                                "type": "integer",
                            },
                            "single-ended": {"title": "Single-ended testing", "type": "boolean"},
                            "single-ended-port": {"title": "Single Ended Port", "type": "integer"},
                            "reverse": {"title": "Reverse", "type": "boolean"},
                            "reverse-connections": {
                                "title": "Reverse Connections",
                                "type": "boolean",
                            },
                            "loopback": {"title": "Loopback", "type": "boolean"},
                        },
                        "required": ["schema", "dest"],
                    },
                    6: {
                        "title": "pScheduler Throughput Specification Schema",
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "schema": {
                                "type": "integer",
                                "enum": [6],
                                "title": "Schema Version",
                                "default": 6,
                            },
                            "source": {
                                "title": "Source",
                                "oneOf": [
                                    {"type": "string", "format": "ipv4"},
                                    {"type": "string", "format": "ipv6"},
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                    },
                                ],
                                "default": "{% address[0] %}",
                            },
                            "source-node": {
                                "title": "Source Node",
                                "type": "string",
                                "default": "{% pscheduler_address[0] %}",
                            },
                            "dest": {
                                "title": "Destination",
                                "oneOf": [
                                    {"type": "string", "format": "ipv4"},
                                    {"type": "string", "format": "ipv6"},
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                    },
                                ],
                                "default": "{% address[1] %}",
                            },
                            "dest-node": {
                                "title": "Destination Node",
                                "type": "string",
                                "default": "{% pscheduler_address[1] %}",
                            },
                            "duration": {
                                "title": "Duration",
                                "type": "string",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "interval": {
                                "title": "Interval",
                                "type": "string",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "link-rtt": {
                                "title": "Link RTT",
                                "type": "string",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "parallel": {
                                "title": "Parallel Streams",
                                "type": "integer",
                                "minimum": 1,
                            },
                            "udp": {"title": "UDP", "type": "boolean"},
                            "bandwidth": {"title": "Bandwidth", "type": "integer", "minimum": 1},
                            "bandwidth-strict": {"title": "Bandwidth Strict", "type": "boolean"},
                            "burst-size": {"title": "Burst Size", "type": "integer", "minimum": 1},
                            "window-size": {
                                "title": "Window Size",
                                "type": "integer",
                                "minimum": 1,
                            },
                            "mss": {"title": "MSS", "type": "integer", "minimum": 1},
                            "buffer-length": {
                                "title": "Buffer Length",
                                "type": "integer",
                                "minimum": 1,
                            },
                            "ip-tos": {
                                "title": "IP TOS",
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 255,
                            },
                            "ip-version": {
                                "title": "IP Version",
                                "type": "integer",
                                "enum": [4, 6],
                            },
                            "local-address": {
                                "title": "Local Address",
                                "oneOf": [
                                    {"type": "string", "format": "ipv4"},
                                    {"type": "string", "format": "ipv6"},
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                    },
                                ],
                            },
                            "omit": {
                                "title": "Omit",
                                "type": "string",
                                "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                                "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                            },
                            "no-delay": {"title": "No Delay", "type": "boolean"},
                            "congestion": {"title": "Congestion", "type": "string"},
                            "zero-copy": {"title": "Zero Copy", "type": "boolean"},
                            "flow-label": {"title": "Flow Label", "type": "integer", "minimum": 1},
                            "client-cpu-affinity": {
                                "title": "Client CPU Affinity",
                                "type": "integer",
                            },
                            "server-cpu-affinity": {
                                "title": "Server CPU Affinity",
                                "type": "integer",
                            },
                            "single-ended": {"title": "Single Ended", "type": "boolean"},
                            "single-ended-port": {"title": "Single Ended Port", "type": "integer"},
                            "reverse": {"title": "Reverse", "type": "boolean"},
                            "reverse-connections": {
                                "title": "Reverse Connections",
                                "type": "boolean",
                            },
                            "loopback": {"title": "Loopback", "type": "boolean"},
                        },
                        "required": ["schema", "dest"],
                    },
                },
            },
            "uischema": {
                "versions": {
                    7: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/source",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/dest",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                ],
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/source-node",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/dest-node",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                ],
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/duration",
                                        "customComponent": "input-text",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/interval",
                                        "customComponent": "input-text",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/link-rtt",
                                        "customComponent": "input-text",
                                    },
                                ],
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/parallel",
                                        "customComponent": "input-number",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/bandwidth",
                                        "customComponent": "input-number",
                                    },
                                ],
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/udp",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/bandwidth-strict",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/zero-copy",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/no-delay",
                                        "customComponent": "input-checkbox",
                                    },
                                ],
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/burst-size",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/fq-rate",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/window-size",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/mss",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/buffer-length",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/ip-tos",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/ip-version",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/local-address",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/omit",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/congestion",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/flow-label",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/client-cpu-affinity",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/server-cpu-affinity",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/single-ended-port",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/single-ended",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/reverse",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/reverse-connections",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/loopback",
                                        "customComponent": "input-checkbox",
                                    },
                                ],
                            },
                        ],
                    },
                    6: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/source",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/dest",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                ],
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/source-node",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/dest-node",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                ],
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/duration",
                                        "customComponent": "input-text",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/interval",
                                        "customComponent": "input-text",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/link-rtt",
                                        "customComponent": "input-text",
                                    },
                                ],
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/parallel",
                                        "customComponent": "input-number",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/bandwidth",
                                        "customComponent": "input-number",
                                    },
                                ],
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/udp",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/bandwidth-strict",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/zero-copy",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/no-delay",
                                        "customComponent": "input-checkbox",
                                    },
                                ],
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/burst-size",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/fq-rate",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/window-size",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/mss",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/buffer-length",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/ip-tos",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/ip-version",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/local-address",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/omit",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/congestion",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/flow-label",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/client-cpu-affinity",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/server-cpu-affinity",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/single-ended-port",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/single-ended",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/reverse",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/reverse-connections",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/loopback",
                                        "customComponent": "input-checkbox",
                                    },
                                ],
                            },
                        ],
                    },
                },
            },
            "versions": [None, "6", "7"],
        },
    }

    latency_schema = {
        "schema": 1,
        "name": "latency",
        "description": "Measure network latency between hosts",
        "version": "1.0",
        "maintainer": {
            "name": "perfSONAR Development Team",
            "email": "perfsonar-developer@internet2.edu",
            "href": "http://www.perfsonar.net",
        },
        "scheduling-class": "normal",
        "spec": {
            "jsonschema": {
                "versions": {
                    4: {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "schema": {
                                "description": "The version of the schema",
                                "type": "integer",
                                "enum": [4],
                                "title": "Schema Version",
                                "default": 4,
                            },
                            "source": {
                                "description": "The address of the entity sending packets in this test",  # noqa: E501
                                "title": "Source",
                                "oneOf": [
                                    {"type": "string", "format": "ipv4"},
                                    {"type": "string", "format": "ipv6"},
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                    },
                                ],
                            },
                            "source-node": {
                                "description": "The address of the source pScheduler node, if different",  # noqa: E501
                                "title": "Source Node",
                                "type": "string",
                            },
                            "dest": {
                                "description": "The address of the entity receiving packets in this test",  # noqa: E501
                                "title": "Destination",
                                "oneOf": [
                                    {"type": "string", "format": "ipv4"},
                                    {"type": "string", "format": "ipv6"},
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                    },
                                ],
                            },
                            "dest-node": {
                                "description": "The address of the destination pScheduler node, if different",  # noqa: E501
                                "title": "Destination Node",
                                "type": "string",
                            },
                            "protocol": {
                                "description": "The protocol to use in making the measurement",
                                "title": "Protocol",
                                "type": "string",
                            },
                            "packet-count": {
                                "description": "The number of packets to send",
                                "title": "Packet Count",
                                "type": "integer",
                                "minimum": 1,
                            },
                            "packet-interval": {
                                "description": "The number of seconds to delay between sending packets",  # noqa: E501
                                "title": "Packet Interval",
                                "type": "number",
                                "minimum": 0,
                            },
                            "packet-timeout": {
                                "description": "The number of seconds to wait before declaring a packet lost",  # noqa: E501
                                "title": "Packet Timeout",
                                "type": "integer",
                                "minimum": 0,
                            },
                            "packet-padding": {
                                "description": "The size of padding to add to the packet in bytes",
                                "title": "Packet Padding",
                                "type": "integer",
                                "minimum": 0,
                            },
                            "ctrl-port": {
                                "description": "The control plane port to use for the entity acting as the server (the dest if flip is not set, the source otherwise)",  # noqa: E501
                                "title": "Control Port",
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 65535,
                            },
                            "ip-tos": {
                                "description": "DSCP value for TOS byte in the IP header as an integer",  # noqa: E501
                                "title": "IP TOS",
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 255,
                            },
                            "ip-version": {
                                "description": "Force a specific IP address type used performing the test. Useful when specifying hostnames as source or dest that may map to both IPv4 and IPv6 addresses.",  # noqa: E501
                                "title": "IP Version",
                                "type": "integer",
                                "enum": [4, 6],
                            },
                            "bucket-width": {
                                "description": "The bin size to use for histogram calculations. This value is divided into the result as reported in seconds and truncated to the nearest 2 decimal places.",  # noqa: E501
                                "title": "Bucket Width",
                                "type": "number",
                                "minimum": 0,
                            },
                            "output-raw": {
                                "description": "Output individual packet statistics. This will substantially increase the size of a successful result.",  # noqa: E501
                                "title": "Output Raw",
                                "type": "boolean",
                            },
                            "flip": {
                                "description": "In multi-participant mode, have the dest start the client and request a reverse test. Useful in some firewall and NAT environments.",  # noqa: E501
                                "title": "Flip",
                                "type": "boolean",
                            },
                            "reverse": {
                                "description": "Report results in the reverse direction (destination to source) if possible.",  # noqa: E501
                                "title": "Reverse",
                                "type": "boolean",
                            },
                            "traverse-nat": {
                                "description": "Make an effort to traverse outbound NAT,",
                                "title": "Traverse NAT",
                                "type": "boolean",
                            },
                        },
                        "required": ["schema", "dest"],
                    },
                    3: {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "schema": {
                                "description": "The version of the schema",
                                "type": "integer",
                                "enum": [3],
                                "title": "Schema Version",
                                "default": 3,
                            },
                            "source": {
                                "description": "The address of the entity sending packets in this test",  # noqa: E501
                                "title": "Source",
                                "oneOf": [
                                    {"type": "string", "format": "ipv4"},
                                    {"type": "string", "format": "ipv6"},
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                    },
                                ],
                            },
                            "source-node": {
                                "description": "The address of the source pScheduler node, if different",  # noqa: E501
                                "title": "Source Node",
                                "type": "string",
                            },
                            "dest": {
                                "description": "The address of the entity receiving packets in this test",  # noqa: E501
                                "title": "Destination",
                                "oneOf": [
                                    {"type": "string", "format": "ipv4"},
                                    {"type": "string", "format": "ipv6"},
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                    },
                                ],
                            },
                            "dest-node": {
                                "description": "The address of the destination pScheduler node, if different",  # noqa: E501
                                "title": "Destination Node",
                                "type": "string",
                            },
                            "packet-count": {
                                "description": "The number of packets to send",
                                "title": "Packet Count",
                                "type": "integer",
                                "minimum": 1,
                            },
                            "packet-interval": {
                                "description": "The number of seconds to delay between sending packets",  # noqa: E501
                                "title": "Packet Interval",
                                "type": "number",
                                "minimum": 0,
                            },
                            "packet-timeout": {
                                "description": "The number of seconds to wait before declaring a packet lost",  # noqa: E501
                                "title": "Packet Timeout",
                                "type": "integer",
                                "minimum": 0,
                            },
                            "packet-padding": {
                                "description": "The size of padding to add to the packet in bytes",
                                "title": "Packet Padding",
                                "type": "integer",
                                "minimum": 0,
                            },
                            "ctrl-port": {
                                "description": "The control plane port to use for the entity acting as the server (the dest if flip is not set, the source otherwise)",  # noqa: E501
                                "title": "Control Port",
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 65535,
                            },
                            "ip-tos": {
                                "description": "DSCP value for TOS byte in the IP header as an integer",  # noqa: E501
                                "title": "IP TOS",
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 255,
                            },
                            "ip-version": {
                                "description": "Force a specific IP address type used performing the test. Useful when specifying hostnames as source or dest that may map to both IPv4 and IPv6 addresses.",  # noqa: E501
                                "title": "IP Version",
                                "type": "integer",
                                "enum": [4, 6],
                            },
                            "bucket-width": {
                                "description": "The bin size to use for histogram calculations. This value is divided into the result as reported in seconds and truncated to the nearest 2 decimal places.",  # noqa: E501
                                "title": "Bucket Width",
                                "type": "number",
                                "minimum": 0,
                            },
                            "output-raw": {
                                "description": "Output individual packet statistics. This will substantially increase the size of a successful result.",  # noqa: E501
                                "title": "Output Raw",
                                "type": "boolean",
                            },
                            "flip": {
                                "description": "In multi-participant mode, have the dest start the client and request a reverse test. Useful in some firewall and NAT environments.",  # noqa: E501
                                "title": "Flip",
                                "type": "boolean",
                            },
                            "reverse": {
                                "description": "Report results in the reverse direction (destination to source) if possible.",  # noqa: E501
                                "title": "Reverse",
                                "type": "boolean",
                            },
                            "traverse-nat": {
                                "description": "Make an effort to traverse outbound NAT,",
                                "title": "Traverse NAT",
                                "type": "boolean",
                            },
                        },
                        "required": ["schema", "dest"],
                    },
                },
            },
            "uischema": {
                "versions": {
                    4: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/source",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/dest",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                ],
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/source-node",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/dest-node",
                                        "customComponent": "input-text-autocomplete",
                                    },
                                ],
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/protocol",
                                "customComponent": "input-text",
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/packet-count",
                                        "customComponent": "input-number",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/packet-interval",
                                        "customComponent": "input-number",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/packet-timeout",
                                        "customComponent": "input-number",
                                    },
                                ],
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/packet-padding",
                                        "customComponent": "input-number",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/ctrl-port",
                                        "customComponent": "input-number",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/ip-tos",
                                        "customComponent": "input-number",
                                    },
                                ],
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/ip-version",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/bucket-width",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "HorizontalLayout",
                                "elements": [
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/output-raw",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/flip",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/reverse",
                                        "customComponent": "input-checkbox",
                                    },
                                    {
                                        "type": "Control",
                                        "scope": "#/properties/traverse-nat",
                                        "customComponent": "input-checkbox",
                                    },
                                ],
                            },
                        ],
                    },
                    3: {
                        "type": "VerticalLayout",
                        "elements": [
                            {
                                "type": "Control",
                                "scope": "#/properties/schema",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/source",
                                "customComponent": "input-text-autocomplete",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/source-node",
                                "customComponent": "input-text-autocomplete",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/dest",
                                "customComponent": "input-text-autocomplete",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/dest-node",
                                "customComponent": "input-text-autocomplete",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/packet-count",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/packet-interval",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/packet-timeout",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/packet-padding",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/ctrl-port",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/ip-tos",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/ip-version",
                                "customComponent": "dropdown-single-select",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/bucket-width",
                                "customComponent": "input-number",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/output-raw",
                                "customComponent": "input-checkbox",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/flip",
                                "customComponent": "input-checkbox",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/reverse",
                                "customComponent": "input-checkbox",
                            },
                            {
                                "type": "Control",
                                "scope": "#/properties/traverse-nat",
                                "customComponent": "input-checkbox",
                            },
                        ],
                    },
                },
            },
            "versions": [None, "3", "4"],
        },
    }

    if testType == "idle":
        return JSONResponse(content=idle_schema)
    elif testType == "throughput":
        return JSONResponse(content=throughput_schema)
    elif testType == "latency":
        return JSONResponse(content=latency_schema)
    else:
        return JSONResponse(content={})


@router.get(
    "/test/{item_id}/form/",
    summary="Get the JSON Data and form data identified by the uuid-slug",
)
@version(1)
def get_existing_form(item_id: str, edit: bool = False):
    try:
        response = backend.get_datatype(datatype=DataTypes.TEST, item_id=item_id)
        response_json = response.json
        response_json = {
            k: v for k, v in response_json.items() if v is not None
        }  # Need to remove null fields

        response_json["name"] = response.name  # Adding "name" since it's not present in the json
    except HTTPException:
        raise HTTPException(status_code=404, detail=f"Test with id: {item_id} not found")

    # Flatten the nested spec structure back to form format
    if "spec" in response_json and isinstance(response_json["spec"], dict):
        # Extract spec fields into the main object
        spec_data = response_json.pop("spec")
        response_json.update(spec_data)

    print("Existing form data:", response_json)
    print("Edit mode:", edit)

    # Get the test type and schema version from the existing data
    test_type = response_json.get("type")
    schema_version = response_json.get("schema")  # This is the numeric version (1, 2, 6, 7, etc.)

    if not test_type or schema_version is None:
        # Fallback to generic schema if no type or schema version specified
        tests = fetch_pscheduler_test_list()
        enriched_schema = deepcopy(TEST_SCHEMA)
        enriched_schema["properties"]["type"]["oneOf"] = [
            {"const": name, "title": name.upper()} for name in tests
        ]

        payload = {
            "ui_schema": TEST_UI_SCHEMA,
            "json_schema": enriched_schema,
            "form_data": response_json,
        }
        return JSONResponse(content=payload)

    # Get the full test schema by calling retrieve_form
    test_schema_response = retrieve_form(test_type)
    full_test_schema = json.loads(test_schema_response.body)

    print(
        "Available versions in schema:",
        list(full_test_schema["spec"]["jsonschema"]["versions"].keys()),
    )
    print("Looking for version:", schema_version, "type:", type(schema_version))

    # Extract the specific version's jsonschema and uischema
    # JSON keys are always strings, so convert schema_version to string
    schema_version_key = str(schema_version)

    version_jsonschema = full_test_schema["spec"]["jsonschema"]["versions"].get(schema_version_key)
    version_uischema = full_test_schema["spec"]["uischema"]["versions"].get(schema_version_key)

    if not version_jsonschema or not version_uischema:
        raise HTTPException(
            status_code=400, detail=f"Version {schema_version} not found for test type {test_type}"
        )

    # Build the enriched schema by merging base schema with version-specific schema
    tests = fetch_pscheduler_test_list()
    base_schema = deepcopy(TEST_SCHEMA)
    base_schema["properties"]["type"]["oneOf"] = [
        {"const": name, "title": name.upper()} for name in tests
    ]

    # Merge version-specific properties into base schema
    base_schema["properties"].update(version_jsonschema["properties"])

    # Merge required fields
    if "required" in version_jsonschema:
        base_schema["required"] = list(
            set(base_schema.get("required", []) + version_jsonschema["required"])
        )

    # Build the enriched UI schema
    base_ui_schema = deepcopy(TEST_UI_SCHEMA)

    # Find the Group element in the layout and update it
    for element in base_ui_schema["elements"]:
        if element.get("type") == "Group" and "rule" in element:
            # Set the condition to match the current test type
            element["rule"]["condition"]["schema"]["const"] = test_type
            # Replace the group's elements with the version-specific UI elements
            element["elements"] = version_uischema["elements"]
            break

    print("Returning enriched schema for type:", test_type, "version:", schema_version)
    print("json_schema:", base_schema)
    print("ui_schema:", base_ui_schema)
    print("form_data:", response_json)

    payload = {
        "ui_schema": base_ui_schema,
        "json_schema": base_schema,
        "form_data": response_json,
    }
    return JSONResponse(content=payload)
