ARCHIVE_SCHEMA = {
    "title": "Schema for creating a new archive",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Archive Name",
            "description": "A string to identify this archive",
        },
        "type": {
            "type": "string",
            "title": "Type",
            "description": "The type of archive",
            "oneOf": [],
            # "oneOf": [
            #     {"const": "bitbucket", "title": "Bitbucket"},
            #     {"const": "esmond", "title": "ESmond"},
            #     {"const": "failer", "title": "Failer"},
            #     {"const": "http", "title": "HTTP"},
            #     {"const": "kafka", "title": "Kafka"},
            #     {"const": "postgresql", "title": "PostgreSQL"},
            #     {"const": "rabbitmq", "title": "RabbitMQ"},
            #     {"const": "snmptrap", "title": "SNMP Trap"},
            #     {"const": "syslog", "title": "Syslog"},
            #     {"const": "tcp", "title": "TCP"},
            #     {"const": "udp", "title": "UDP"},
            # ],
        },
        # "data": {
        #     "type": "string",
        #     "title": "Data",
        #     "description": "JSON object that specifies archive-specific parameters. Archive objects in pSConfig are taken directly from pScheduler. Eg: _url",
        # },
        # "schema": {
        #     "type": "integer",
        #     "title": "Schema Version",
        #     "description": "The schema version number",
        # },
        "ttl": {
            "type": "string",
            "title": "TTL",
            "description": "ISO8601 duration that specifies the ttl",
        },
        "label": {
            "type": "string",
            "title": "Label",
            "description": "",
        },
        "transform": {
            "type": "string",
            "title": "Transform",
            "description": "",
        },
        "_meta": {
            "type": "object",
            "title": "Other Meta",
            "description": "Fill in information such as display-name and display-set as an object",
        },
    },
    "required": [
        "name",
        "type",
        # "data",
    ],
    "renderers": {},
}

ARCHIVE_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {"type": "Control", "scope": "#/properties/name", "customComponent": "ps-input-text"},
        {
            "type": "Control",
            "scope": "#/properties/type",
            "customComponent": "ps-select",
        },
        {
            "type": "Group",
            "rule": {
                "effect": "SHOW",
                "condition": {"scope": "#/properties/type", "schema": {"const": ""}},
            },
            "elements": [],
        },
        {"type": "Control", "scope": "#/properties/label", "customComponent": "ps-input-text"},
        {"type": "Control", "scope": "#/properties/ttl", "customComponent": "ps-input-text"},
        {
            "type": "Control",
            "scope": "#/properties/transform",
            "customComponent": "ps-textarea-json",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "ps-textarea-json"},
    ],
}

http_schema = {
    "json_schema": ARCHIVE_SCHEMA,
    "ui_schema": ARCHIVE_UI_SCHEMA,
    "schema": 1,
    "name": "http",
    "description": "Send a raw JSON result to a HTTP server",
    "version": "1.0",
    "maintainer": {
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
        "href": "http://www.perfsonar.net",
    },
    "spec": {
        "jsonschema": {
            "versions": {
                1: {
                    "type": "object",
                    "properties": {
                        "schema": {"title": "Schema Version", "type": "integer", "enum": [1]},
                        "_url": {
                            "title": "URL",
                            "type": "string",
                            "format": "uri",
                        },
                        "op": {
                            "title": "Operation",
                            "type": "string",
                            "enum": [
                                "put",
                                "post",
                            ],
                        },
                        "bind": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 255,
                            "pattern": r"^[A-Za-z0-9_][A-Za-z0-9\-]{0,62}(\.[A-Za-z0-9][A-Za-z0-9\-]{1,62})*\.?$",  # noqa: E501
                        },
                        # "retry-policy": {
                        #     "type": "array",
                        #     "items": {
                        #         "$ref": "#/pScheduler/RetryPolicyEntry"
                        #     }
                        # }
                    },
                    "required": ["_url"],
                    "additionalProperties": False,
                },
                2: {
                    "type": "object",
                    "properties": {
                        "schema": {"title": "Schema Version", "type": "integer", "enum": [2]},
                        "_url": {
                            "title": "URL",
                            "type": "string",
                            "format": "uri",
                        },
                        "op": {
                            "title": "Operation",
                            "type": "string",
                            "enum": [
                                "put",
                                "post",
                            ],
                        },
                        "_headers": {
                            "title": "Headers",
                            "type": "object",
                        },
                        # Not complete
                        "bind": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 255,
                            "pattern": r"^[A-Za-z0-9_][A-Za-z0-9\-]{0,62}(\.[A-Za-z0-9][A-Za-z0-9\-]{1,62})*\.?$",  # noqa: E501
                        },
                        # "retry-policy": {
                        #     "type": "array",
                        #     "items": {
                        #         "$ref": "#/pScheduler/RetryPolicyEntry"
                        #     }
                        # }
                    },
                    "required": ["schema", "_url"],
                    "additionalProperties": False,
                },
                3: {
                    "type": "object",
                    "properties": {
                        "schema": {"title": "Schema Version", "type": "integer", "enum": [3]},
                        "_url": {
                            "title": "URL",
                            "type": "string",
                            "format": "uri",
                        },
                        "op": {
                            "title": "Operation",
                            "type": "string",
                            "enum": [
                                "put",
                                "post",
                            ],
                        },
                        "verify-ssl": {
                            "title": "Verify SSL Certificate",
                            "type": "boolean",
                            "default": False,
                        },
                        "_headers": {
                            "type": "object",
                        },
                        # Not complete
                        "bind": {
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 255,
                            "pattern": r"^[A-Za-z0-9_][A-Za-z0-9\-]{0,62}(\.[A-Za-z0-9][A-Za-z0-9\-]{1,62})*\.?$",  # noqa: E501
                        },
                        # "retry-policy": {
                        #     "type": "array",
                        #     "items": {
                        #         "$ref": "#/pScheduler/RetryPolicyEntry"
                        #     }
                        # }
                    },
                    "required": ["schema", "_url"],
                    "additionalProperties": False,
                },
                4: {
                    "type": "object",
                    "properties": {
                        "schema": {"title": "Schema Version", "type": "integer", "enum": [4]},
                        "_url": {
                            "title": "URL",
                            "type": "string",
                            "format": "uri",
                        },
                        "op": {
                            "title": "Operation",
                            "type": "string",
                            "enum": [
                                "put",
                                "post",
                            ],
                        },
                        "verify-ssl": {
                            "title": "Verify SSL Certificate",
                            "type": "boolean",
                            "default": False,
                        },
                        "_headers": {
                            "title": "Headers",
                            "type": "object",
                        },
                        "timeout": {
                            "title": "Timeout",
                            "type": "string",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        # Not complete
                        "bind": {
                            "title": "Bind Address",
                            "type": "string",
                            "minLength": 1,
                            "maxLength": 255,
                            "pattern": r"^[A-Za-z0-9_][A-Za-z0-9\-]{0,62}(\.[A-Za-z0-9][A-Za-z0-9\-]{1,62})*\.?$",  # noqa: E501
                        },
                        # "retry-policy": {
                        #     "type": "array",
                        #     "items": {
                        #         "$ref": "#/pScheduler/RetryPolicyEntry"
                        #     }
                        # }
                    },
                    "required": ["schema", "_url"],
                    "additionalProperties": False,
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
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text",
                        },
                        # {
                        #     "type": "Control",
                        #     "scope": "#/properties/retry-policy",
                        #     "customComponent": "ps-input-text",
                        # },
                    ],
                },
                2: {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_headers",
                            "customComponent": "ps-textarea-json",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text",
                        },
                        # {
                        #     "type": "Control",
                        #     "scope": "#/properties/retry-policy",
                        #     "customComponent": "ps-input-text",
                        # },
                    ],
                },
                3: {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/verify-ssl",
                            "customComponent": "ps-input-checkbox",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_headers",
                            "customComponent": "ps-textarea-json",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text",
                        },
                        # {
                        #     "type": "Control",
                        #     "scope": "#/properties/retry-policy",
                        #     "customComponent": "ps-input-text",
                        # },
                    ],
                },
                4: {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_headers",
                            "customComponent": "ps-textarea-json",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/verify-ssl",
                            "customComponent": "ps-input-checkbox",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text",
                        },
                        # {
                        #     "type": "Control",
                        #     "scope": "#/properties/retry-policy",
                        #     "customComponent": "ps-input-text",
                        # },
                    ],
                },
            },
        },
        "versions": [None, "1", "2", "3", "4"],
    },
}
