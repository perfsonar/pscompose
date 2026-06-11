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
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
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
    "json-forms-compatible": True,
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
                            "customComponent": "ps-input-text",
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
                            "customComponent": "ps-input-text",
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
                    "required": ["url"],
                    "properties": {
                        "_auth-token": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "bind": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "description": "Any hostname as described in RFCs 952, 1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "x-invalid-message": "'%s' is not a valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"type": "string", "format": "ipv4"},
                                        {"type": "string", "format": "ipv6"},
                                    ],
                                },
                            ],
                        },
                        "data-formatting-policy": {
                            "type": "string",
                            "enum": ["prefer-mapped", "mapped-and-raw", "mapped-only", "raw-only"],
                        },
                        "measurement-agent": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "description": "Any hostname as described in RFCs 952, 1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "x-invalid-message": "'%s' is not a valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"type": "string", "format": "ipv4"},
                                        {"type": "string", "format": "ipv6"},
                                    ],
                                },
                            ],
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "description": "Any positive integer is valid.",
                                        "examples": [1],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Duration",
                                        "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                        "summaries": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["event-type", "summary-type", "summary-window"],
                                "properties": {
                                    "event-type": {
                                        "type": "string",
                                        "description": "Any string is valid.",
                                    },
                                    "summary-type": {
                                        "type": "string",
                                        "description": "Any string is valid.",
                                    },
                                    "summary-window": {
                                        "type": "integer",
                                        "description": "Zero or any positive integer is valid.",
                                        "examples": [1],
                                        "minimum": 0,
                                        "x-invalid-message": "This must be zero or any positive integer.",
                                    },
                                },
                            },
                        },
                        "url": {
                            "type": "string",
                            "format": "uri",
                        },
                        "verify-ssl": {
                            "type": "boolean",
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
    "json-forms-compatible": True,
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
                        "delay": {
                            "type": "string",
                            "title": "Delay",
                            "description": "How long to delay before completing.  This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M", "P1D", "P2D3H37M"],
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "fail": {
                            "type": "number",
                            "title": "Fail",
                            "description": "Probability that any attempt will fail.  Any value in [0.0..1.0] is valid.",
                            "maximum": 1.0,
                            "minimum": 0.0,
                            "x-invalid-message": "Value must be in [0.0..1.0].",
                        },
                        "retry": {
                            "type": "number",
                            "title": "Retry",
                            "description": "Probability that a retry will be requested after a failure.  Any value in [0.0..1.0] is valid.",
                            "maximum": 1.0,
                            "minimum": 0.0,
                            "x-invalid-message": "Value must be in [0.0..1.0].",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema"],
                    "properties": {
                        "badly": {
                            "type": "boolean",
                            "title": "Fail Badly",
                            "description": "When failing, fail badly with an internal error.",
                        },
                        "delay": {
                            "type": "string",
                            "title": "Delay",
                            "description": "How long to delay before completing.  This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M", "P1D", "P2D3H37M"],
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "fail": {
                            "type": "number",
                            "title": "Fail",
                            "description": "Probability that any attempt will fail.  Any value in [0.0..1.0] is valid.",
                            "maximum": 1.0,
                            "minimum": 0.0,
                            "x-invalid-message": "Value must be in [0.0..1.0].",
                        },
                        "retry": {
                            "type": "number",
                            "title": "Retry",
                            "description": "Probability that a retry will be requested after a failure.  Any value in [0.0..1.0] is valid.",
                            "maximum": 1.0,
                            "minimum": 0.0,
                            "x-invalid-message": "Value must be in [0.0..1.0].",
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
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
    "json-forms-compatible": True,
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
                            "customComponent": "ps-input-text",
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
                            "customComponent": "ps-input-text",
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
                    "required": ["_url"],
                    "properties": {
                        "_url": {
                            "type": "string",
                            "title": "URL",
                            "description": "URL for archive.  Any uniform resource identifier (URI) is valid.",
                            "format": "uri",
                            "examples": ["https://www.example.org"],
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc3986",
                                    "title": "Uniform Resource Identifiers",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid URI.",
                        },
                        "bind": {
                            "type": "string",
                            "title": "bind",
                            "description": "Source address for outgoing request.  Any hostname, FQDN, IPv4 address or IPv6 address is valid.",
                            "examples": ["host.example.net", "198.51.100.45", "2001:db8::c0de"],
                            "pattern": "(^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$)|(^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$)|(^((?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,7}:|:(?::[0-9A-Fa-f]{1,4}){1,7}|(?:[0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,5}(?::[0-9A-Fa-f]{1,4}){1,2}|(?:[0-9A-Fa-f]{1,4}:){1,4}(?::[0-9A-Fa-f]{1,4}){1,3}|(?:[0-9A-Fa-f]{1,4}:){1,3}(?::[0-9A-Fa-f]{1,4}){1,4}|(?:[0-9A-Fa-f]{1,4}:){1,2}(?::[0-9A-Fa-f]{1,4}){1,5}|[0-9A-Fa-f]{1,4}:(?:(?::[0-9A-Fa-f]{1,4}){1,6})|:(?:(?::[0-9A-Fa-f]{1,4}){1,6}))$)",
                            "x-invalid-message": "Invalid host name.",
                        },
                        "op": {
                            "type": "string",
                            "title": "Operation",
                            "description": 'HTTP operation.  Must be "put" or "post".',
                            "enum": ["put", "post"],
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "description": "How many times to try.  Any positive integer is valid.",
                                        "examples": ["5"],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "description": "How long to wait between tries.  This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": [
                                            "PT10S",
                                            "PT45.67S",
                                            "PT1H30M",
                                            "P1D",
                                            "P2D3H37M",
                                        ],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "_url"],
                    "properties": {
                        "_headers": {
                            "type": "object",
                            "patternProperties": {
                                "^.*$": {
                                    "type": "string",
                                    "title": "Header",
                                    "description": "A HTTP header value  Any string is valid.",
                                    "examples": ["xyzzy", "foo", "bar", "baz"],
                                }
                            },
                            "additionalProperties": False,
                        },
                        "_url": {
                            "type": "string",
                            "title": "URL",
                            "description": "URL for archive.  Any uniform resource identifier (URI) is valid.",
                            "format": "uri",
                            "examples": ["https://www.example.org"],
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc3986",
                                    "title": "Uniform Resource Identifiers",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid URI.",
                        },
                        "bind": {
                            "type": "string",
                            "title": "Bind",
                            "description": "Source address for outgoing request.  Any hostname, FQDN, IPv4 address or IPv6 address is valid.",
                            "examples": ["host.example.net", "198.51.100.45", "2001:db8::c0de"],
                            "pattern": "(^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$)|(^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$)|(^((?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,7}:|:(?::[0-9A-Fa-f]{1,4}){1,7}|(?:[0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,5}(?::[0-9A-Fa-f]{1,4}){1,2}|(?:[0-9A-Fa-f]{1,4}:){1,4}(?::[0-9A-Fa-f]{1,4}){1,3}|(?:[0-9A-Fa-f]{1,4}:){1,3}(?::[0-9A-Fa-f]{1,4}){1,4}|(?:[0-9A-Fa-f]{1,4}:){1,2}(?::[0-9A-Fa-f]{1,4}){1,5}|[0-9A-Fa-f]{1,4}:(?:(?::[0-9A-Fa-f]{1,4}){1,6})|:(?:(?::[0-9A-Fa-f]{1,4}){1,6}))$)",
                            "x-invalid-message": "Invalid host name.",
                        },
                        "op": {
                            "type": "string",
                            "title": "Operation",
                            "description": 'HTTP operation.  Must be "put" or "post".',
                            "enum": ["put", "post"],
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "description": "How many times to try.  Any positive integer is valid.",
                                        "examples": ["5"],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "description": "How long to wait between tries.  This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": [
                                            "PT10S",
                                            "PT45.67S",
                                            "PT1H30M",
                                            "P1D",
                                            "P2D3H37M",
                                        ],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "_url"],
                    "properties": {
                        "_headers": {
                            "type": "object",
                            "patternProperties": {
                                "^.*$": {
                                    "type": "string",
                                    "title": "Header",
                                    "description": "A HTTP header value  Any string is valid.",
                                    "examples": ["xyzzy", "foo", "bar", "baz"],
                                }
                            },
                            "additionalProperties": False,
                        },
                        "_url": {
                            "type": "string",
                            "title": "URL",
                            "description": "URL for archive.  Any uniform resource identifier (URI) is valid.",
                            "format": "uri",
                            "examples": ["https://www.example.org"],
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc3986",
                                    "title": "Uniform Resource Identifiers",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid URI.",
                        },
                        "bind": {
                            "type": "string",
                            "title": "Bind",
                            "description": "Source address for outgoing request.  Any hostname, FQDN, IPv4 address or IPv6 address is valid.",
                            "examples": ["host.example.net", "198.51.100.45", "2001:db8::c0de"],
                            "pattern": "(^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$)|(^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$)|(^((?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,7}:|:(?::[0-9A-Fa-f]{1,4}){1,7}|(?:[0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,5}(?::[0-9A-Fa-f]{1,4}){1,2}|(?:[0-9A-Fa-f]{1,4}:){1,4}(?::[0-9A-Fa-f]{1,4}){1,3}|(?:[0-9A-Fa-f]{1,4}:){1,3}(?::[0-9A-Fa-f]{1,4}){1,4}|(?:[0-9A-Fa-f]{1,4}:){1,2}(?::[0-9A-Fa-f]{1,4}){1,5}|[0-9A-Fa-f]{1,4}:(?:(?::[0-9A-Fa-f]{1,4}){1,6})|:(?:(?::[0-9A-Fa-f]{1,4}){1,6}))$)",
                            "x-invalid-message": "Invalid host name.",
                        },
                        "op": {
                            "type": "string",
                            "title": "Operation",
                            "description": 'HTTP operation.  Must be "put" or "post".',
                            "enum": ["put", "post"],
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "description": "How many times to try.  Any positive integer is valid.",
                                        "examples": ["5"],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "description": "How long to wait between tries.  This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": [
                                            "PT10S",
                                            "PT45.67S",
                                            "PT1H30M",
                                            "P1D",
                                            "P2D3H37M",
                                        ],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "schema": {
                            "const": 3,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                        "verify-ssl": {
                            "type": "boolean",
                            "title": "Verify SSL",
                            "description": "Require that the server present a valid SSL certificate.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "_url"],
                    "properties": {
                        "_headers": {
                            "type": "object",
                            "patternProperties": {
                                "^.*$": {
                                    "type": "string",
                                    "title": "Header",
                                    "description": "A HTTP header value  Any string is valid.",
                                    "examples": ["xyzzy", "foo", "bar", "baz"],
                                }
                            },
                            "additionalProperties": False,
                        },
                        "_url": {
                            "type": "string",
                            "title": "URL",
                            "description": "URL for archive.  Any uniform resource identifier (URI) is valid.",
                            "format": "uri",
                            "examples": ["https://www.example.org"],
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc3986",
                                    "title": "Uniform Resource Identifiers",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid URI.",
                        },
                        "bind": {
                            "type": "string",
                            "title": "Bind",
                            "description": "Source address for outgoing request.  Any hostname, FQDN, IPv4 address or IPv6 address is valid.",
                            "examples": ["host.example.net", "198.51.100.45", "2001:db8::c0de"],
                            "pattern": "(^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$)|(^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$)|(^((?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,7}:|:(?::[0-9A-Fa-f]{1,4}){1,7}|(?:[0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,5}(?::[0-9A-Fa-f]{1,4}){1,2}|(?:[0-9A-Fa-f]{1,4}:){1,4}(?::[0-9A-Fa-f]{1,4}){1,3}|(?:[0-9A-Fa-f]{1,4}:){1,3}(?::[0-9A-Fa-f]{1,4}){1,4}|(?:[0-9A-Fa-f]{1,4}:){1,2}(?::[0-9A-Fa-f]{1,4}){1,5}|[0-9A-Fa-f]{1,4}:(?:(?::[0-9A-Fa-f]{1,4}){1,6})|:(?:(?::[0-9A-Fa-f]{1,4}){1,6}))$)",
                            "x-invalid-message": "Invalid host name.",
                        },
                        "op": {
                            "type": "string",
                            "title": "Operation",
                            "description": 'HTTP operation.  Must be "put" or "post".',
                            "enum": ["put", "post"],
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "title": "Attempts",
                                        "description": "How many times to try.  Any positive integer is valid.",
                                        "examples": ["5"],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Wait",
                                        "description": "How long to wait between tries.  This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": [
                                            "PT10S",
                                            "PT45.67S",
                                            "PT1H30M",
                                            "P1D",
                                            "P2D3H37M",
                                        ],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "schema": {
                            "const": 4,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                        "timeout": {
                            "type": "string",
                            "title": "Timeout",
                            "description": "How long to wait before giving up.  This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M", "P1D", "P2D3H37M"],
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "verify-ssl": {
                            "type": "boolean",
                            "title": "Verify SSL",
                            "description": "Require that the server present a valid SSL certificate.",
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
    "json-forms-compatible": True,
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
                    "required": ["topic", "server"],
                    "properties": {
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                        "server": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "additionalProperties": True,
                    "allOf": [
                        {
                            "if": {
                                "properties": {"security-protocol": {"const": "SSL"}},
                                "required": ["security-protocol"],
                            },
                            "then": {
                                "properties": {
                                    "_ssl-cacert": {
                                        "type": "string",
                                        "description": "Any string is valid.",
                                    },
                                    "_ssl-cert": {
                                        "type": "string",
                                        "description": "Any string is valid.",
                                    },
                                    "_ssl-key": {
                                        "type": "string",
                                        "description": "Any string is valid.",
                                    },
                                    "_ssl-password": {
                                        "type": "string",
                                        "description": "Any string is valid.",
                                    },
                                    "ssl-checkhostname": {"type": "boolean"},
                                },
                            },
                        },
                    ],
                    "required": ["schema", "topic", "server", "security-protocol"],
                    "properties": {
                        "archiver-id": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "kafka-retries": {
                            "type": "integer",
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "x-invalid-message": "'%s' is not a valid integer.",
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "description": "Any positive integer is valid.",
                                        "examples": [1],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Duration",
                                        "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                        "security-protocol": {
                            "default": "PLAINTEXT",
                            "enum": ["PLAINTEXT", "SSL"],
                        },
                        "server": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                    },
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
    "json-forms-compatible": False,
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
                    "required": ["_dsn", "table", "column"],
                    "properties": {
                        "_dsn": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "column": {
                            "type": "string",
                            "maxLength": 63,
                            "minLength": 1,
                            "pattern": "^[A-Za-z_][A-Za-z0-9_\\$]*$",
                        },
                        "connection-expires": {
                            "type": "string",
                            "title": "Duration",
                            "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "description": "Any positive integer is valid.",
                                        "examples": [1],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Duration",
                                        "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                        "table": {
                            "type": "string",
                            "maxLength": 63,
                            "minLength": 1,
                            "pattern": "^[A-Za-z_][A-Za-z0-9_\\$]*$",
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
    "json-forms-compatible": True,
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
                    "required": ["_url"],
                    "properties": {
                        "_url": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "exchange": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "description": "Any positive integer is valid.",
                                        "examples": [1],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Duration",
                                        "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "routing-key": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "_url"],
                    "properties": {
                        "_url": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "connection-expires": {
                            "type": "string",
                            "title": "Duration",
                            "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "exchange": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "description": "Any positive integer is valid.",
                                        "examples": [1],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Duration",
                                        "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "routing-key": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "description": "Any string is valid.",
                                },
                                {
                                    "type": "object",
                                    "required": ["script"],
                                    "properties": {
                                        "args": {
                                            "description": "This can be any valid JSON.",
                                            "examples": [
                                                {"foo": "bar"},
                                                "perfSONAR",
                                                True,
                                                97,
                                                None,
                                            ],
                                            "x-info": [
                                                {"href": "https://www.json.org", "title": "JSON"}
                                            ],
                                            "x-invalid-message": "'%s' is not valid JSON.",
                                        },
                                        "output-raw": {"type": "boolean"},
                                        "script": {
                                            "anyOf": [
                                                {
                                                    "type": "string",
                                                    "description": "Any string is valid.",
                                                },
                                                {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string",
                                                        "description": "Any string is valid.",
                                                    },
                                                },
                                            ],
                                        },
                                    },
                                    "additionalProperties": False,
                                },
                            ],
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "_url"],
                    "properties": {
                        "_url": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "connection-expires": {
                            "type": "string",
                            "title": "Duration",
                            "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "exchange": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "description": "Any positive integer is valid.",
                                        "examples": [1],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Duration",
                                        "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "routing-key": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "description": "Any string is valid.",
                                },
                                {
                                    "type": "object",
                                    "required": ["script"],
                                    "properties": {
                                        "args": {
                                            "description": "This can be any valid JSON.",
                                            "examples": [
                                                {"foo": "bar"},
                                                "perfSONAR",
                                                True,
                                                97,
                                                None,
                                            ],
                                            "x-info": [
                                                {"href": "https://www.json.org", "title": "JSON"}
                                            ],
                                            "x-invalid-message": "'%s' is not valid JSON.",
                                        },
                                        "output-raw": {"type": "boolean"},
                                        "script": {
                                            "anyOf": [
                                                {
                                                    "type": "string",
                                                    "description": "Any string is valid.",
                                                },
                                                {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string",
                                                        "description": "Any string is valid.",
                                                    },
                                                },
                                            ],
                                        },
                                    },
                                    "additionalProperties": False,
                                },
                            ],
                        },
                        "schema": {
                            "const": 3,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                        "timeout": {
                            "type": "string",
                            "title": "Duration",
                            "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
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
    "json-forms-compatible": False,
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
                            "customComponent": "ps-input-text",
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
                    "additionalProperties": True,
                    "oneOf": [
                        {
                            "type": "object",
                            "required": ["dest", "_community", "trap-oid"],
                            "properties": {
                                "_community": {
                                    "type": "string",
                                    "description": "Any string is valid.",
                                },
                                "dest": {"type": "string", "description": "Any string is valid."},
                                "instance-index": {
                                    "type": "integer",
                                    "description": "Any integer is valid.",
                                    "examples": [5],
                                    "x-invalid-message": "'%s' is not a valid integer.",
                                },
                                "trap-oid": {
                                    "type": "string",
                                    "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
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
                                            "value": {
                                                "description": "This can be any valid JSON.",
                                                "examples": [
                                                    {"foo": "bar"},
                                                    "perfSONAR",
                                                    True,
                                                    97,
                                                    None,
                                                ],
                                                "x-info": [
                                                    {
                                                        "href": "https://www.json.org",
                                                        "title": "JSON",
                                                    }
                                                ],
                                                "x-invalid-message": "'%s' is not valid JSON.",
                                            },
                                        },
                                        "additionalProperties": False,
                                    },
                                },
                            },
                        },
                        {
                            "type": "object",
                            "required": ["dest", "security-name", "trap-oid"],
                            "properties": {
                                "_auth-key": {
                                    "type": "string",
                                    "description": "Any string is valid.",
                                },
                                "_priv-key": {
                                    "type": "string",
                                    "description": "Any string is valid.",
                                },
                                "auth-protocol": {"type": "string", "enum": ["MD5", "SHA"]},
                                "dest": {"type": "string", "description": "Any string is valid."},
                                "instance-index": {
                                    "type": "integer",
                                    "description": "Any integer is valid.",
                                    "examples": [5],
                                    "x-invalid-message": "'%s' is not a valid integer.",
                                },
                                "priv-protocol": {
                                    "type": "string",
                                    "enum": ["AES", "AES128", "AES192", "AES256", "DES", "3DES"],
                                },
                                "security-level": {
                                    "type": "string",
                                    "enum": ["noAuthNoPriv", "authNoPriv", "authPriv"],
                                },
                                "security-name": {
                                    "type": "string",
                                    "description": "Any string is valid.",
                                },
                                "trap-oid": {
                                    "type": "string",
                                    "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
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
                                            "value": {
                                                "description": "This can be any valid JSON.",
                                                "examples": [
                                                    {"foo": "bar"},
                                                    "perfSONAR",
                                                    True,
                                                    97,
                                                    None,
                                                ],
                                                "x-info": [
                                                    {
                                                        "href": "https://www.json.org",
                                                        "title": "JSON",
                                                    }
                                                ],
                                                "x-invalid-message": "'%s' is not valid JSON.",
                                            },
                                        },
                                        "additionalProperties": False,
                                    },
                                },
                            },
                        },
                    ],
                    "properties": {
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
                        },
                    },
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
    "json-forms-compatible": False,
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
                        "facility": {
                            "type": "string",
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
                        },
                        "ident": {
                            "type": "string",
                            "description": "Any string is valid.",
                        },
                        "priority": {
                            "type": "string",
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
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
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
    "json-forms-compatible": True,
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
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/host",
                            "customComponent": "ps-input-text",
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
                    "required": ["host", "port"],
                    "properties": {
                        "bind": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "description": "Any hostname as described in RFCs 952, 1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "x-invalid-message": "'%s' is not a valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"type": "string", "format": "ipv4"},
                                        {"type": "string", "format": "ipv6"},
                                    ],
                                },
                            ],
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "description": "Any hostname as described in RFCs 952, 1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "x-invalid-message": "'%s' is not a valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"type": "string", "format": "ipv4"},
                                        {"type": "string", "format": "ipv6"},
                                    ],
                                },
                            ],
                        },
                        "ip-version": {
                            "type": "integer",
                            "enum": [4, 6],
                        },
                        "port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "description": "Any positive integer is valid.",
                                        "examples": [1],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Duration",
                                        "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
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
    "json-forms-compatible": True,
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
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/host",
                            "customComponent": "ps-input-text",
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
                    "required": ["host", "port"],
                    "properties": {
                        "bind": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "description": "Any hostname as described in RFCs 952, 1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "x-invalid-message": "'%s' is not a valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"type": "string", "format": "ipv4"},
                                        {"type": "string", "format": "ipv6"},
                                    ],
                                },
                            ],
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "description": "Any hostname as described in RFCs 952, 1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "x-invalid-message": "'%s' is not a valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"type": "string", "format": "ipv4"},
                                        {"type": "string", "format": "ipv6"},
                                    ],
                                },
                            ],
                        },
                        "ip-version": {
                            "type": "integer",
                            "enum": [4, 6],
                        },
                        "payload-size": {
                            "type": "integer",
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "retry-policy": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "required": ["attempts", "wait"],
                                "properties": {
                                    "attempts": {
                                        "type": "integer",
                                        "description": "Any positive integer is valid.",
                                        "examples": [1],
                                        "minimum": 1,
                                        "x-invalid-message": "'%s' is not a positive integer.",
                                    },
                                    "wait": {
                                        "type": "string",
                                        "title": "Duration",
                                        "description": "This can be any valid ISO 8601 duration not involving months or years, which are inexact.",
                                        "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                        "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                        "x-info": [
                                            {
                                                "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                                "title": "ISO 8601 Durations",
                                            }
                                        ],
                                        "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                    },
                                },
                                "additionalProperties": False,
                            },
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema number.",
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
    "json-forms-compatible": True,
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
