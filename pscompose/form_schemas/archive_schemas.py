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
        },
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
    ],
    "renderers": {},
}

ARCHIVE_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {
            "type": "Control",
            "scope": "#/properties/name",
            "customComponent": "ps-input-text",
        },
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
        {
            "type": "Control",
            "scope": "#/properties/label",
            "customComponent": "ps-input-text",
        },
        {
            "type": "Control",
            "scope": "#/properties/ttl",
            "customComponent": "ps-input-text",
        },
        {
            "type": "Control",
            "scope": "#/properties/transform",
            "customComponent": "ps-textarea-json",
        },
        {
            "type": "Control",
            "scope": "#/properties/_meta",
            "customComponent": "ps-textarea-json",
        },
    ],
}

_RETRY_POLICY_UI = {
    "type": "Control",
    "scope": "#/properties/retry-policy",
    "options": {
        "detail": {
            "type": "HorizontalLayout",
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/wait",
                    "customComponent": "ps-input-text",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/attempts",
                    "customComponent": "ps-input-number",
                },
            ],
        }
    },
}


bitbucket_archiver = {
    "name": "bitbucket",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "properties": {
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
    "label": "Bit Bucket",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Discard results",
    "href": "https://localhost/pscheduler/archivers/bitbucket",
}


esmond_archiver = {
    "name": "esmond",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/_auth-token",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/verify-ssl",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/measurement-agent",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/data-formatting-policy",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/summaries",
                            "options": {
                                "detail": {
                                    "type": "HorizontalLayout",
                                    "elements": [
                                        {
                                            "type": "Control",
                                            "scope": "#/properties/event-type",
                                            "customComponent": "ps-input-text",
                                        },
                                        {
                                            "type": "Control",
                                            "scope": "#/properties/summary-type",
                                            "customComponent": "ps-input-text",
                                        },
                                        {
                                            "type": "Control",
                                            "scope": "#/properties/summary-window",
                                            "customComponent": "ps-input-number",
                                        },
                                    ],
                                }
                            },
                        },
                        _RETRY_POLICY_UI,
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "required": [
                        "url",
                    ],
                    "properties": {
                        "url": {
                            "type": "string",
                            "format": "uri",
                        },
                        "bind": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "maxLength": 255,
                                    "minLength": 1,
                                },
                                {
                                    "oneOf": [
                                        {
                                            "type": "string",
                                            "format": "ipv4",
                                        },
                                        {
                                            "type": "string",
                                            "format": "ipv6",
                                        },
                                    ],
                                },
                            ],
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "summaries": {
                            "type": "array",
                            "title": "Summaries",
                            "items": {
                                "type": "object",
                                "required": [
                                    "event-type",
                                    "summary-type",
                                    "summary-window",
                                ],
                                "properties": {
                                    "event-type": {
                                        "type": "string",
                                        "title": "Event Type",
                                    },
                                    "summary-type": {
                                        "type": "string",
                                        "title": "Summary Type",
                                    },
                                    "summary-window": {
                                        "type": "integer",
                                        "minimum": 0,
                                        "title": "Summary Window",
                                    },
                                },
                            },
                        },
                        "verify-ssl": {
                            "type": "boolean",
                        },
                        "_auth-token": {"type": "string"},
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "measurement-agent": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "maxLength": 255,
                                    "minLength": 1,
                                },
                                {
                                    "oneOf": [
                                        {
                                            "type": "string",
                                            "format": "ipv4",
                                        },
                                        {
                                            "type": "string",
                                            "format": "ipv6",
                                        },
                                    ],
                                },
                            ],
                        },
                        "data-formatting-policy": {
                            "enum": [
                                "prefer-mapped",
                                "mapped-and-raw",
                                "mapped-only",
                                "raw-only",
                            ],
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
    "label": "Esmond",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Send results to Esmond",
    "href": "https://localhost/pscheduler/archivers/esmond",
}


failer_archiver = {
    "name": "failer",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/fail",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/delay",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/retry",
                            "customComponent": "ps-input-number",
                        },
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/fail",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/delay",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/retry",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/badly",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "properties": {
                        "fail": {
                            "type": "number",
                            "maximum": 1.0,
                            "minimum": 0.0,
                        },
                        "delay": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "retry": {
                            "type": "number",
                            "maximum": 1.0,
                            "minimum": 0.0,
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                    ],
                    "properties": {
                        "fail": {
                            "type": "number",
                            "maximum": 1.0,
                            "minimum": 0.0,
                        },
                        "badly": {
                            "type": "boolean",
                        },
                        "delay": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "retry": {
                            "type": "number",
                            "maximum": 1.0,
                            "minimum": 0.0,
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
    "label": "Failer",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Dummy archiver that fails some of the time",
    "href": "https://localhost/pscheduler/archivers/failer",
}


http_archiver = {
    "name": "http",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        _RETRY_POLICY_UI,
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_headers",
                            "customComponent": "ps-input-text",
                        },
                        _RETRY_POLICY_UI,
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/_headers",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/verify-ssl",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        _RETRY_POLICY_UI,
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/_headers",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/verify-ssl",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        _RETRY_POLICY_UI,
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "required": [
                        "_url",
                    ],
                    "properties": {
                        "op": {
                            "enum": [
                                "put",
                                "post",
                            ],
                            "type": "string",
                        },
                        "_url": {"type": "string", "format": "uri"},
                        "bind": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "maxLength": 255,
                                    "minLength": 1,
                                },
                                {
                                    "oneOf": [
                                        {
                                            "type": "string",
                                            "format": "ipv4",
                                        },
                                        {
                                            "type": "string",
                                            "format": "ipv6",
                                        },
                                    ],
                                },
                            ],
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "_url",
                    ],
                    "properties": {
                        "op": {
                            "enum": [
                                "put",
                                "post",
                            ],
                            "type": "string",
                        },
                        "_url": {"type": "string", "format": "uri"},
                        "bind": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "maxLength": 255,
                                    "minLength": 1,
                                },
                                {
                                    "oneOf": [
                                        {
                                            "type": "string",
                                            "format": "ipv4",
                                        },
                                        {
                                            "type": "string",
                                            "format": "ipv6",
                                        },
                                    ],
                                },
                            ],
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "_headers": {
                            "type": "object",
                            "patternProperties": {"^.*$": {"type": "string"}},
                            "additionalProperties": False,
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "_url",
                    ],
                    "properties": {
                        "op": {
                            "enum": [
                                "put",
                                "post",
                            ],
                            "type": "string",
                        },
                        "_url": {"type": "string", "format": "uri"},
                        "bind": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "maxLength": 255,
                                    "minLength": 1,
                                },
                                {
                                    "oneOf": [
                                        {
                                            "type": "string",
                                            "format": "ipv4",
                                        },
                                        {
                                            "type": "string",
                                            "format": "ipv6",
                                        },
                                    ],
                                },
                            ],
                        },
                        "schema": {
                            "const": 3,
                            "type": "integer",
                        },
                        "_headers": {
                            "type": "object",
                            "patternProperties": {"^.*$": {"type": "string"}},
                            "additionalProperties": False,
                        },
                        "verify-ssl": {
                            "type": "boolean",
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "_url",
                    ],
                    "properties": {
                        "op": {
                            "enum": [
                                "put",
                                "post",
                            ],
                            "type": "string",
                        },
                        "_url": {"type": "string", "format": "uri"},
                        "bind": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "maxLength": 255,
                                    "minLength": 1,
                                },
                                {
                                    "oneOf": [
                                        {
                                            "type": "string",
                                            "format": "ipv4",
                                        },
                                        {
                                            "type": "string",
                                            "format": "ipv6",
                                        },
                                    ],
                                },
                            ],
                        },
                        "schema": {
                            "const": 4,
                            "type": "integer",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "_headers": {
                            "type": "object",
                            "patternProperties": {"^.*$": {"type": "string"}},
                            "additionalProperties": False,
                        },
                        "verify-ssl": {
                            "type": "boolean",
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
    "label": "HTTP",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Send a raw JSON result to a HTTP server",
    "href": "https://localhost/pscheduler/archivers/http",
}


kafka_archiver = {
    "name": "kafka",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/topic",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/server",
                            "customComponent": "ps-input-text",
                        },
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/topic",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/server",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/archiver-id",
                            "customComponent": "ps-input-text",
                        },
                        _RETRY_POLICY_UI,
                        {
                            "type": "Control",
                            "scope": "#/properties/kafka-retries",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/security-protocol",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Group",
                            "rule": {
                                "effect": "SHOW",
                                "condition": {
                                    "scope": "#/properties/security-protocol",
                                    "schema": {"const": "SSL"},
                                },
                            },
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/_ssl-key",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/_ssl-cert",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/_ssl-cacert",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/_ssl-password",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ssl-checkhostname",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "required": [
                        "topic",
                        "server",
                    ],
                    "properties": {
                        "topic": {
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "server": {
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "allOf": [
                        {
                            "if": {
                                "required": [
                                    "security-protocol",
                                ],
                                "properties": {
                                    "security-protocol": {
                                        "const": "SSL",
                                    },
                                },
                            },
                            "then": {
                                "properties": {
                                    "_ssl-key": {"type": "string"},
                                    "_ssl-cert": {"type": "string"},
                                    "_ssl-cacert": {"type": "string"},
                                    "_ssl-password": {"type": "string"},
                                    "ssl-checkhostname": {
                                        "type": "boolean",
                                    },
                                },
                            },
                        },
                    ],
                    "required": [
                        "schema",
                        "topic",
                        "server",
                        "security-protocol",
                    ],
                    "properties": {
                        "topic": {
                            "type": "string",
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "server": {
                            "type": "string",
                        },
                        "archiver-id": {
                            "type": "string",
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "kafka-retries": {
                            "type": "integer",
                        },
                        "security-protocol": {
                            "enum": [
                                "PLAINTEXT",
                                "SSL",
                            ],
                            "default": "PLAINTEXT",
                        },
                        "_ssl-key": {
                            "type": "string",
                        },
                        "_ssl-cert": {
                            "type": "string",
                        },
                        "_ssl-cacert": {
                            "type": "string",
                        },
                        "_ssl-password": {
                            "type": "string",
                        },
                        "ssl-checkhostname": {
                            "type": "boolean",
                        },
                    },
                    "additionalProperties": True,
                },
            ],
        },
    },
    "label": "Kafka",
    "schema": 2,
    "version": "1.2",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Archives data to an Apache Kafka message bus",
    "href": "https://localhost/pscheduler/archivers/kafka",
}


postgresql_archiver = {
    "name": "postgresql",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/_dsn",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/table",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/column",
                            "customComponent": "ps-input-text",
                        },
                        _RETRY_POLICY_UI,
                        {
                            "type": "Control",
                            "scope": "#/properties/connection-expires",
                            "customComponent": "ps-input-text",
                        },
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "required": [
                        "_dsn",
                        "table",
                        "column",
                    ],
                    "properties": {
                        "_dsn": {"type": "string"},
                        "table": {
                            "type": "string",
                            "pattern": "^[A-Za-z_][A-Za-z0-9_\\$]*$",
                            "maxLength": 63,
                            "minLength": 1,
                        },
                        "column": {
                            "type": "string",
                            "pattern": "^[A-Za-z_][A-Za-z0-9_\\$]*$",
                            "maxLength": 63,
                            "minLength": 1,
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "connection-expires": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
    "label": "PostgreSQL",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "PostgreSQL database archiver",
    "href": "https://localhost/pscheduler/archivers/postgresql",
}


rabbitmq_archiver = {
    "name": "rabbitmq",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/exchange",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/routing-key",
                            "customComponent": "ps-input-text",
                        },
                        _RETRY_POLICY_UI,
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/exchange",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/routing-key",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        _RETRY_POLICY_UI,
                        {
                            "type": "Control",
                            "scope": "#/properties/connection-expires",
                            "customComponent": "ps-input-text",
                        },
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/exchange",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/routing-key",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        _RETRY_POLICY_UI,
                        {
                            "type": "Control",
                            "scope": "#/properties/connection-expires",
                            "customComponent": "ps-input-text",
                        },
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "required": [
                        "_url",
                    ],
                    "properties": {
                        "_url": {"type": "string", "format": "uri"},
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "exchange": {
                            "type": "string",
                        },
                        "routing-key": {
                            "type": "string",
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "_url",
                    ],
                    "properties": {
                        "_url": {"type": "string", "format": "uri"},
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "exchange": {
                            "type": "string",
                        },
                        "routing-key": {
                            "anyOf": [
                                {
                                    "type": "string",
                                },
                                {
                                    "type": "object",
                                    "required": [
                                        "script",
                                    ],
                                    "properties": {
                                        "args": {},
                                        "script": {
                                            "anyOf": [
                                                {
                                                    "type": "string",
                                                },
                                                {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string",
                                                    },
                                                },
                                            ],
                                        },
                                        "output-raw": {
                                            "type": "boolean",
                                        },
                                    },
                                    "additionalProperties": False,
                                },
                            ],
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "connection-expires": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "_url",
                    ],
                    "properties": {
                        "_url": {"type": "string", "format": "uri"},
                        "schema": {
                            "const": 3,
                            "type": "integer",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "exchange": {
                            "type": "string",
                        },
                        "routing-key": {
                            "anyOf": [
                                {
                                    "type": "string",
                                },
                                {
                                    "type": "object",
                                    "required": [
                                        "script",
                                    ],
                                    "properties": {
                                        "args": {},
                                        "script": {
                                            "anyOf": [
                                                {
                                                    "type": "string",
                                                },
                                                {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string",
                                                    },
                                                },
                                            ],
                                        },
                                        "output-raw": {
                                            "type": "boolean",
                                        },
                                    },
                                    "additionalProperties": False,
                                },
                            ],
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "connection-expires": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
    "label": "RabbitMQ",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Send a JSON result to RabbitMQ",
    "href": "https://localhost/pscheduler/archivers/rabbitmq",
}


snmptrap_archiver = {
    "name": "snmptrap",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/dest",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/trap-oid",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_community",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/trap-varbinds",
                            "customComponent": "ps-input-array",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/instance-index",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_auth-key",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_priv-key",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/auth-protocol",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/priv-protocol",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/security-name",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/security-level",
                            "customComponent": "ps-select",
                        },
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "oneOf": [
                        {
                            "type": "object",
                            "required": [
                                "dest",
                                "_community",
                                "trap-oid",
                            ],
                            "properties": {
                                "dest": {
                                    "type": "string",
                                },
                                "trap-oid": {
                                    "type": "string",
                                    "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                },
                                "_community": {"type": "string"},
                                "trap-varbinds": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "oid": {
                                                "type": "string",
                                                "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                            },
                                            "value": {},
                                        },
                                        "additionalProperties": False,
                                    },
                                },
                                "instance-index": {
                                    "type": "integer",
                                },
                            },
                        },
                        {
                            "type": "object",
                            "required": [
                                "dest",
                                "security-name",
                                "trap-oid",
                            ],
                            "properties": {
                                "dest": {
                                    "type": "string",
                                },
                                "trap-oid": {
                                    "type": "string",
                                    "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                },
                                "_auth-key": {"type": "string"},
                                "_priv-key": {"type": "string"},
                                "auth-protocol": {
                                    "enum": [
                                        "MD5",
                                        "SHA",
                                    ],
                                    "type": "string",
                                },
                                "priv-protocol": {
                                    "enum": [
                                        "AES",
                                        "AES128",
                                        "AES192",
                                        "AES256",
                                        "DES",
                                        "3DES",
                                    ],
                                    "type": "string",
                                },
                                "security-name": {
                                    "type": "string",
                                },
                                "trap-varbinds": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "oid": {
                                                "type": "string",
                                                "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                            },
                                            "value": {},
                                        },
                                        "additionalProperties": False,
                                    },
                                },
                                "instance-index": {
                                    "type": "integer",
                                },
                                "security-level": {
                                    "enum": [
                                        "noAuthNoPriv",
                                        "authNoPriv",
                                        "authPriv",
                                    ],
                                    "type": "string",
                                },
                            },
                        },
                    ],
                    "properties": {
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                    },
                    "additionalProperties": True,
                },
            ],
        },
    },
    "label": "SNMP Trap",
    "schema": 2,
    "version": "1.0.0.3",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Send an SNMP trap to a destination.",
    "href": "https://localhost/pscheduler/archivers/snmptrap",
}


syslog_archiver = {
    "name": "syslog",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/ident",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/facility",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/priority",
                            "customComponent": "ps-select",
                        },
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "properties": {
                        "ident": {
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "facility": {
                            "enum": [
                                "kern",
                                "user",
                                "mail",
                                "daemon",
                                "auth",
                                "lpr",
                                "news",
                                "uucp",
                                "cron",
                                "syslog",
                                "local0",
                                "local1",
                                "local2",
                                "local3",
                                "local4",
                                "local5",
                                "local6",
                                "local7",
                            ],
                            "type": "string",
                        },
                        "priority": {
                            "enum": [
                                "emerg",
                                "alert",
                                "crit",
                                "err",
                                "warning",
                                "notice",
                                "info",
                                "debug",
                            ],
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
    "label": "Syslog",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Send a raw JSON result to Syslog",
    "href": "https://localhost/pscheduler/archivers/syslog",
}


tcp_archiver = {
    "name": "tcp",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/host",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/port",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-version",
                            "customComponent": "ps-select",
                        },
                        _RETRY_POLICY_UI,
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "required": [
                        "host",
                        "port",
                    ],
                    "properties": {
                        "bind": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "maxLength": 255,
                                    "minLength": 1,
                                },
                                {
                                    "oneOf": [
                                        {
                                            "type": "string",
                                            "format": "ipv4",
                                        },
                                        {
                                            "type": "string",
                                            "format": "ipv6",
                                        },
                                    ],
                                },
                            ],
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "maxLength": 255,
                                    "minLength": 1,
                                },
                                {
                                    "oneOf": [
                                        {
                                            "type": "string",
                                            "format": "ipv4",
                                        },
                                        {
                                            "type": "string",
                                            "format": "ipv6",
                                        },
                                    ],
                                },
                            ],
                        },
                        "port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
    "label": "TCP",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Send a raw JSON result to a TCP socket",
    "href": "https://localhost/pscheduler/archivers/tcp",
}


udp_archiver = {
    "name": "udp",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/host",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/port",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-version",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/payload-size",
                            "customComponent": "ps-input-number",
                        },
                        _RETRY_POLICY_UI,
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "required": [
                        "host",
                        "port",
                    ],
                    "properties": {
                        "bind": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "maxLength": 255,
                                    "minLength": 1,
                                },
                                {
                                    "oneOf": [
                                        {
                                            "type": "string",
                                            "format": "ipv4",
                                        },
                                        {
                                            "type": "string",
                                            "format": "ipv6",
                                        },
                                    ],
                                },
                            ],
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "maxLength": 255,
                                    "minLength": 1,
                                },
                                {
                                    "oneOf": [
                                        {
                                            "type": "string",
                                            "format": "ipv4",
                                        },
                                        {
                                            "type": "string",
                                            "format": "ipv6",
                                        },
                                    ],
                                },
                            ],
                        },
                        "port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "payload-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "retry-policy": {
                            "type": "array",
                            "title": "Retry Policy",
                            "items": {
                                "type": "object",
                                "required": [
                                    "attempts",
                                    "wait",
                                ],
                                "properties": {
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "minimum": 1,
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
    "label": "UDP",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Send a JSON result as a UDP datagram",
    "href": "https://localhost/pscheduler/archivers/udp",
}

ARCHIVE_SCHEMAS = {
    "bitbucket": bitbucket_archiver,
    "esmond": esmond_archiver,
    "failer": failer_archiver,
    "http": http_archiver,
    "kafka": kafka_archiver,
    "postgresql": postgresql_archiver,
    "rabbitmq": rabbitmq_archiver,
    "snmptrap": snmptrap_archiver,
    "syslog": syslog_archiver,
    "tcp": tcp_archiver,
    "udp": udp_archiver,
}
