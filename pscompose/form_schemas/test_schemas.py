TEST_SCHEMA = {
    "title": "Schema for creating a new test",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Test Name",
            "description": "A string to identify this test",
        },
        "type": {
            "type": "string",
            "title": "Type",
            "description": "Type of test to be performed",
            "oneOf": [],
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

TEST_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {"type": "Control", "scope": "#/properties/name", "customComponent": "ps-input-text"},
        {
            "type": "Control",
            "scope": "#/properties/type",
            "customComponent": "ps-select",
        },
        # Dynamically fill this out
        {
            "type": "Group",
            "rule": {
                "effect": "SHOW",
                "condition": {"scope": "#/properties/type", "schema": {"const": ""}},
            },
            "elements": [],
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "ps-textarea-json"},
    ],
}


clock_schema = {
    "name": "clock",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
                            "customComponent": "ps-input-text",
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
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
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
                    "required": ["dest"],
                    "properties": {
                        "dest": {
                            "description": "Destination pScheduler host.  Any "
                            "host:port is valid.",
                            "examples": ["www.example.org:20165"],
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "title": "Destination",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc3986#section-3.2",
                                    "title": "RFC 3896 - Authority",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid host:port.",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "description": "Source pScheduler host.  Any " "host:port is valid.",
                            "examples": ["www.example.org:20165"],
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "title": "Source",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc3986#section-3.2",
                                    "title": "RFC 3896 - Authority",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid host:port.",
                        },
                        "timeout": {
                            "description": "Timeout for clock state request.  "
                            "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M", "P1D", "P2D3H37M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Timeout",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "dest": {
                            "description": "Destination pScheduler host.  Any "
                            "host:port is valid.",
                            "examples": ["www.example.org:20165"],
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "title": "Destination",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc3986#section-3.2",
                                    "title": "RFC 3896 - Authority",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid host:port.",
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "description": "Source pScheduler host.  Any " "host:port is valid.",
                            "examples": ["www.example.org:20165"],
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "title": "Source",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc3986#section-3.2",
                                    "title": "RFC 3896 - Authority",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid host:port.",
                        },
                        "source-node": {
                            "description": "Source pScheduler host, if "
                            "different.  Any host:port is "
                            "valid.",
                            "examples": ["www.example.org:20165"],
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "title": "Source Node",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc3986#section-3.2",
                                    "title": "RFC 3896 - Authority",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid " "host:port.",
                        },
                        "timeout": {
                            "description": "Timeout for clock state request.  "
                            "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M", "P1D", "P2D3H37M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Timeout",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "Clock",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Measure the clock difference between hosts",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/clock",
}

dhcp_schema = {
    "name": "dhcp",
    "json-forms-compatible": True,
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
                            "scope": "#/properties/host",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/host-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/interface",
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
                    "required": [],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "interface": {
                            "description": "This can be any valid JSON.",
                            "examples": [{"foo": "bar"}, "perfSONAR", True, 97, None],
                            "x-info": [{"href": "https://www.json.org", "title": "JSON"}],
                            "x-invalid-message": "'%s' is not valid JSON.",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "DHCP",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Tests the response time for getting a new dhcp lease.",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/dhcp",
}

disk_to_disk_schema = {
    "name": "disk-to-disk",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/parallel",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/cleanup",
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
                    "required": ["dest", "source"],
                    "properties": {
                        "cleanup": {"type": "boolean"},
                        "dest": {"description": "Any string is valid.", "type": "string"},
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "parallel": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {"description": "Any string is valid.", "type": "string"},
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "Disk-to-Disk",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Network testing of throughput and Read/Write speeds",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/disk-to-disk",
}

dns_schema = {
    "name": "dns",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/query",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/record",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/nameserver",
                                    "customComponent": "ps-input-text",
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
                    "required": ["query", "record"],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "nameserver": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "query": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "record": {
                            "enum": ["a", "aaaa", "ns", "cname", "soa", "ptr", "mx", "txt"],
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "DNS",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Measure DNS transaction time",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/dns",
}

dns64_schema = {
    "name": "dns64",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/query",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/nameserver",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/translation-prefix",
                                    "customComponent": "ps-input-text",
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
                    "required": ["query"],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "nameserver": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "query": {"format": "uri", "type": "string"},
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "translation-prefix": {
                            "description": "Any string is valid.",
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "DNS64",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Test that checks for the correct functioning of a DNS64 server",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/dns64",
}

dot1x_schema = {
    "name": "dot1x",
    "json-forms-compatible": True,
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
                            "scope": "#/properties/interface",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ssid",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bssid",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/driver",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/_username",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/_password",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/key-management",
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
                    "required": ["interface"],
                    "properties": {
                        "_password": {"description": "Any string is valid.", "type": "string"},
                        "_username": {"description": "Any string is valid.", "type": "string"},
                        "bssid": {"description": "Any string is valid.", "type": "string"},
                        "driver": {"description": "Any string is valid.", "type": "string"},
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "interface": {"description": "Any string is valid.", "type": "string"},
                        "key-management": {
                            "description": "Any string is valid.",
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "ssid": {"description": "Any string is valid.", "type": "string"},
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "Dot 1x",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "802.1x authentication using wpa_supplicant and a wpa_supplicant config file",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/dot1x",
}

http_schema = {
    "name": "http",
    "json-forms-compatible": True,
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
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parse",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
                            "customComponent": "ps-input-text",
                        },
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parse",
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
                                    "scope": "#/properties/keep-content",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/always-succeed",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parse",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-version",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/keep-content",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/always-succeed",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/url",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parse",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/headers",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-version",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/keep-content",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/always-succeed",
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
                    "required": ["url"],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "parse": {"description": "Any string is valid.", "type": "string"},
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "url": {"format": "uri", "type": "string"},
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "url"],
                    "properties": {
                        "always-succeed": {"type": "boolean"},
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "keep-content": {
                            "description": "Zero or any positive integer is " "valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or any " "positive integer.",
                        },
                        "parse": {"description": "Any string is valid.", "type": "string"},
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "url": {"format": "uri", "type": "string"},
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "url"],
                    "properties": {
                        "always-succeed": {"type": "boolean"},
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "keep-content": {
                            "description": "Zero or any positive integer is " "valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or any " "positive integer.",
                        },
                        "parse": {"description": "Any string is valid.", "type": "string"},
                        "schema": {
                            "const": 3,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "url": {"format": "uri", "type": "string"},
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "url"],
                    "properties": {
                        "always-succeed": {"type": "boolean"},
                        "headers": {
                            "additionalProperties": False,
                            "patternProperties": {
                                "^[!#\\$%&'*+\\-.\\^`|~0-9A-Za-z]+$": {
                                    "description": "Any " "string " "is " "valid.",
                                    "type": "string",
                                }
                            },
                            "type": "object",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "keep-content": {
                            "description": "Zero or any positive integer is " "valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or any " "positive integer.",
                        },
                        "parse": {"description": "Any string is valid.", "type": "string"},
                        "schema": {
                            "const": 4,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "url": {"format": "uri", "type": "string"},
                    },
                    "additionalProperties": False,
                },
            ]
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
    "description": "Measure HTTP Response Time",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/http",
}

idle_schema = {
    "name": "idle",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/duration",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/host-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/starting-comment",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parting-comment",
                            "customComponent": "ps-input-text",
                        },
                    ],
                },
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/duration",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/starting-comment",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parting-comment",
                            "customComponent": "ps-input-text",
                        },
                    ],
                },
            ]
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "required": ["duration"],
                    "properties": {
                        "duration": {
                            "description": "How long to be idle.  This can be "
                            "any valid ISO 8601 duration not "
                            "involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M", "P1D", "P2D3H37M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "host": {
                            "description": "The host that will be idle.  Any "
                            "hostname, FQDN, IPv4 address or IPv6 "
                            "address is valid.",
                            "examples": ["host.example.net", "198.51.100.45", "2001:db8::c0de"],
                            "pattern": "(^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$)|(^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$)|(^((?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,7}:|:(?::[0-9A-Fa-f]{1,4}){1,7}|(?:[0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,5}(?::[0-9A-Fa-f]{1,4}){1,2}|(?:[0-9A-Fa-f]{1,4}:){1,4}(?::[0-9A-Fa-f]{1,4}){1,3}|(?:[0-9A-Fa-f]{1,4}:){1,3}(?::[0-9A-Fa-f]{1,4}){1,4}|(?:[0-9A-Fa-f]{1,4}:){1,2}(?::[0-9A-Fa-f]{1,4}){1,5}|[0-9A-Fa-f]{1,4}:(?:(?::[0-9A-Fa-f]{1,4}){1,6})|:(?:(?::[0-9A-Fa-f]{1,4}){1,6}))$)",
                            "title": "Host",
                            "type": "string",
                            "x-invalid-message": "Invalid host name.",
                        },
                        "host-node": {
                            "description": "The pScheduler node to contact for "
                            "the host.  Any host:port is valid.",
                            "examples": ["www.example.org:20165"],
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "title": "Host Node",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc3986#section-3.2",
                                    "title": "RFC 3896 - Authority",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid " "host:port.",
                        },
                        "parting-comment": {
                            "description": "Commentary for after idling "
                            "is done.  Any string is "
                            "valid.",
                            "examples": ["xyzzy", "foo", "bar", "baz"],
                            "title": "Parting Comment",
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "starting-comment": {
                            "description": "Commentary for before "
                            "idling starts.  Any string "
                            "is valid.",
                            "examples": ["xyzzy", "foo", "bar", "baz"],
                            "title": "Starting Comment",
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "duration"],
                    "properties": {
                        "duration": {
                            "description": "How long to be idle.  This can be "
                            "any valid ISO 8601 duration not "
                            "involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M", "P1D", "P2D3H37M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "host": {
                            "items": {
                                "description": "Host(s) that will be idle.  "
                                "Any hostname, FQDN, IPv4 "
                                "address or IPv6 address is "
                                "valid.",
                                "examples": [
                                    "host.example.net",
                                    "198.51.100.45",
                                    "2001:db8::c0de",
                                ],
                                "pattern": "(^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$)|(^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$)|(^((?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,7}:|:(?::[0-9A-Fa-f]{1,4}){1,7}|(?:[0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,5}(?::[0-9A-Fa-f]{1,4}){1,2}|(?:[0-9A-Fa-f]{1,4}:){1,4}(?::[0-9A-Fa-f]{1,4}){1,3}|(?:[0-9A-Fa-f]{1,4}:){1,3}(?::[0-9A-Fa-f]{1,4}){1,4}|(?:[0-9A-Fa-f]{1,4}:){1,2}(?::[0-9A-Fa-f]{1,4}){1,5}|[0-9A-Fa-f]{1,4}:(?:(?::[0-9A-Fa-f]{1,4}){1,6})|:(?:(?::[0-9A-Fa-f]{1,4}){1,6}))$)",
                                "title": "Host",
                                "type": "string",
                                "x-invalid-message": "Invalid host name.",
                            },
                            "minItems": 1,
                            "type": "array",
                        },
                        "parting-comment": {
                            "description": "Commentary for after idling "
                            "is done.  Any string is "
                            "valid.",
                            "examples": ["xyzzy", "foo", "bar", "baz"],
                            "title": "Parting Comment",
                            "type": "string",
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "starting-comment": {
                            "description": "Commentary for before "
                            "idling starts.  Any string "
                            "is valid.",
                            "examples": ["xyzzy", "foo", "bar", "baz"],
                            "title": "Starting Comment",
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "Idle",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Consume time in the background",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/idle",
}

idlebgm_schema = {
    "name": "idlebgm",
    "json-forms-compatible": True,
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
                            "scope": "#/properties/duration",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/interval",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parting-comment",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/starting-comment",
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
                    "required": ["duration"],
                    "properties": {
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "parting-comment": {
                            "description": "Any string is valid.",
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "starting-comment": {
                            "description": "Any string is valid.",
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "Idle Background-Multi",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Consume time in the background - NOT FOR PRODUCTION",
    "scheduling-class": "background-multi",
    "href": "https://localhost/pscheduler/tests/idlebgm",
}

idleex_schema = {
    "name": "idleex",
    "json-forms-compatible": True,
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
                            "scope": "#/properties/duration",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parting-comment",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/starting-comment",
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
                    "required": ["duration"],
                    "properties": {
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "parting-comment": {
                            "description": "Any string is valid.",
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "starting-comment": {
                            "description": "Any string is valid.",
                            "type": "string",
                        },
                    },
                },
            ]
        },
    },
    "label": "Idle Exclusive",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Consume time exclusively - NOT FOR PRODUCTION",
    "scheduling-class": "exclusive",
    "href": "https://localhost/pscheduler/tests/idleex",
}

latency_schema = {
    "name": "latency",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/data-ports",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-count",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-interval",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-timeout",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-padding",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ctrl-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bucket-width",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flip",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/output-raw",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/data-ports",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-count",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-interval",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-timeout",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-padding",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ctrl-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bucket-width",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/output-raw",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flip",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-count",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-interval",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-timeout",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-padding",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ctrl-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bucket-width",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/output-raw",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flip",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/traverse-nat",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/protocol",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-count",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-interval",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-timeout",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-padding",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ctrl-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bucket-width",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/output-raw",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flip",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/traverse-nat",
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
                    "required": ["dest"],
                    "properties": {
                        "bucket-width": {
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                            "type": "number",
                        },
                        "ctrl-port": {"maximum": 65535, "minimum": 0, "type": "integer"},
                        "data-ports": {
                            "additionalProperties": False,
                            "properties": {
                                "lower": {"maximum": 65535, "minimum": 0, "type": "integer"},
                                "upper": {"maximum": 65535, "minimum": 0, "type": "integer"},
                            },
                            "required": ["lower", "upper"],
                            "type": "object",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "flip": {"type": "boolean"},
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "output-raw": {"type": "boolean"},
                        "packet-count": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "packet-interval": {"exclusiveMinimum": 0.0, "type": "number"},
                        "packet-padding": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "packet-timeout": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "bucket-width": {
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                            "type": "number",
                        },
                        "ctrl-port": {"maximum": 65535, "minimum": 0, "type": "integer"},
                        "data-ports": {
                            "additionalProperties": False,
                            "properties": {
                                "lower": {"maximum": 65535, "minimum": 0, "type": "integer"},
                                "upper": {"maximum": 65535, "minimum": 0, "type": "integer"},
                            },
                            "required": ["lower", "upper"],
                            "type": "object",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "flip": {"type": "boolean"},
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "output-raw": {"type": "boolean"},
                        "packet-count": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "packet-interval": {"exclusiveMinimum": 0.0, "type": "number"},
                        "packet-padding": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "packet-timeout": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "reverse": {"type": "boolean"},
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "bucket-width": {
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                            "type": "number",
                        },
                        "ctrl-port": {"maximum": 65535, "minimum": 0, "type": "integer"},
                        "data-ports": {
                            "additionalProperties": False,
                            "properties": {
                                "lower": {"maximum": 65535, "minimum": 0, "type": "integer"},
                                "upper": {"maximum": 65535, "minimum": 0, "type": "integer"},
                            },
                            "required": ["lower", "upper"],
                            "type": "object",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "flip": {"type": "boolean"},
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "output-raw": {"type": "boolean"},
                        "packet-count": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "packet-interval": {"exclusiveMinimum": 0.0, "type": "number"},
                        "packet-padding": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "packet-timeout": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "schema": {
                            "const": 3,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "reverse": {"type": "boolean"},
                        "traverse-nat": {"type": "boolean"},
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "bucket-width": {
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                            "type": "number",
                        },
                        "ctrl-port": {"maximum": 65535, "minimum": 0, "type": "integer"},
                        "data-ports": {
                            "additionalProperties": False,
                            "properties": {
                                "lower": {"maximum": 65535, "minimum": 0, "type": "integer"},
                                "upper": {"maximum": 65535, "minimum": 0, "type": "integer"},
                            },
                            "required": ["lower", "upper"],
                            "type": "object",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "flip": {"type": "boolean"},
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "output-raw": {"type": "boolean"},
                        "packet-count": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "packet-interval": {"exclusiveMinimum": 0.0, "type": "number"},
                        "packet-padding": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "packet-timeout": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "schema": {
                            "const": 4,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "protocol": {"description": "Any string is valid.", "type": "string"},
                        "reverse": {"type": "boolean"},
                        "traverse-nat": {"type": "boolean"},
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "Latency",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Measure network latency between hosts",
    "scheduling-class": "normal",
    "href": "https://localhost/pscheduler/tests/latency",
}

latencybg_schema = {
    "name": "latencybg",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/data-ports",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/duration",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-count",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-interval",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-timeout",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-padding",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ctrl-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bucket-width",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flip",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/output-raw",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/data-ports",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/duration",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-count",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-interval",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-timeout",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-padding",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ctrl-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/protocol",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bucket-width",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flip",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/output-raw",
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
                    "required": ["dest"],
                    "properties": {
                        "bucket-width": {
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                            "type": "number",
                        },
                        "ctrl-port": {"maximum": 65535, "minimum": 0, "type": "integer"},
                        "data-ports": {
                            "additionalProperties": False,
                            "properties": {
                                "lower": {"maximum": 65535, "minimum": 0, "type": "integer"},
                                "upper": {"maximum": 65535, "minimum": 0, "type": "integer"},
                            },
                            "required": ["lower", "upper"],
                            "type": "object",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "flip": {"type": "boolean"},
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "output-raw": {"type": "boolean"},
                        "packet-count": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "packet-interval": {"exclusiveMinimum": 0.0, "type": "number"},
                        "packet-padding": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "packet-timeout": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                    },
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "bucket-width": {
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                            "type": "number",
                        },
                        "ctrl-port": {"maximum": 65535, "minimum": 0, "type": "integer"},
                        "data-ports": {
                            "additionalProperties": False,
                            "properties": {
                                "lower": {"maximum": 65535, "minimum": 0, "type": "integer"},
                                "upper": {"maximum": 65535, "minimum": 0, "type": "integer"},
                            },
                            "required": ["lower", "upper"],
                            "type": "object",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "flip": {"type": "boolean"},
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "output-raw": {"type": "boolean"},
                        "packet-count": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "packet-interval": {"exclusiveMinimum": 0.0, "type": "number"},
                        "packet-padding": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "packet-timeout": {
                            "description": "Zero or any positive integer " "is valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or " "any positive integer.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "protocol": {"description": "Any string is valid.", "type": "string"},
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                    },
                },
            ]
        },
    },
    "label": "Latency Background-Multi",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Run one-way latency tests in the background",
    "scheduling-class": "background-multi",
    "href": "https://localhost/pscheduler/tests/latencybg",
}

mtu_schema = {
    "name": "mtu",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/port",
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source-node",
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
                    ],
                },
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "required": ["dest"],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ],
                            "description": "Destination point for the test",
                            "hint": "ps.example.net",
                            "title": "Destination",
                        },
                        "port": {
                            "description": "Port number to use for the test",
                            "hint": "12345",
                            "maximum": 65535,
                            "minimum": 0,
                            "title": "Port",
                            "type": "integer",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version of the specification "
                            "for this test  This can be any "
                            "positive integer.",
                            "minimum": 1,
                            "title": "Schema Version",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ],
                            "description": "Origin point for the test",
                            "hint": "ps.example.org",
                            "title": "Source",
                        },
                        "source-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs "
                                    "952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ],
                            "description": "perfSONAR node for origin point " "for the test",
                            "hint": "ps.example.org",
                            "title": "Source Node",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ],
                            "description": "Destination point for the test",
                            "hint": "ps.example.net",
                            "title": "Destination",
                        },
                        "ip-version": {
                            "description": "What version of the IP protocol "
                            "to use for the test (4 or 6)",
                            "enum": [4, 6],
                            "hint": "ps.example.net",
                            "title": "IP Version",
                            "type": "integer",
                        },
                        "port": {
                            "description": "Port number to use for the test",
                            "hint": "12345",
                            "maximum": 65535,
                            "minimum": 0,
                            "title": "Port",
                            "type": "integer",
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version of the specification "
                            "for this test  This can be any "
                            "positive integer.",
                            "minimum": 1,
                            "title": "Schema Version",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ],
                            "description": "Origin point for the test",
                            "hint": "ps.example.org",
                            "title": "Source",
                        },
                        "source-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs "
                                    "952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ],
                            "description": "perfSONAR node for origin point " "for the test",
                            "hint": "ps.example.org",
                            "title": "Source Node",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "MTU",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Measure Maximum Transmission Unit (MTU)",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/mtu",
}

netreach_schema = {
    "name": "netreach",
    "json-forms-compatible": False,
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
                            "scope": "#/properties/network",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/scan",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/limit",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/gateway",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parallel",
                            "customComponent": "ps-input-number",
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
                    "required": ["network"],
                    "properties": {
                        "gateway": {
                            "oneOf": [
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                                {
                                    "oneOf": [
                                        {
                                            "description": "Any positive " "integer is " "valid.",
                                            "examples": [1],
                                            "minimum": 1,
                                            "type": "integer",
                                            "x-invalid-message": "'%s' is "
                                            "not a "
                                            "positive "
                                            "integer.",
                                        },
                                        {"maximum": -1, "type": "integer"},
                                    ]
                                },
                            ]
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "limit": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "network": {
                            "pattern": "(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/([0-9]|[1-2][0-9]|3[0-2]))$)|(^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*(\\/([0-9]|[1-9][0-9]|1[0-1][0-9]|12[0-8]))$)",
                            "type": "string",
                        },
                        "parallel": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "scan": {"enum": ["up", "down", "edges", "random"], "type": "string"},
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                },
            ]
        },
    },
    "label": "Network Reachability",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Determine if any host on a network is reachable",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/netreach",
}

noop_schema = {
    "name": "noop",
    "json-forms-compatible": True,
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
                            "scope": "#/properties/data",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/fail",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
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
                    "required": [],
                    "properties": {
                        "data": {
                            "description": "This can be any valid JSON.",
                            "examples": [{"foo": "bar"}, "perfSONAR", True, 97, None],
                            "x-info": [{"href": "https://www.json.org", "title": "JSON"}],
                            "x-invalid-message": "'%s' is not valid JSON.",
                        },
                        "fail": {
                            "description": "Any value in [0.0..1.0] is valid.",
                            "maximum": 1.0,
                            "minimum": 0.0,
                            "type": "number",
                            "x-invalid-message": "Value must be in [0.0..1.0].",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "No-Op",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Do nothing",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/noop",
}

psresponse_schema = {
    "name": "psresponse",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
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
                    "required": ["dest"],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs "
                                    "952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "pScheduler Response",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Measure pScheduler Response Time",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/psresponse",
}

rtt_schema = {
    "name": "rtt",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ttl",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/count",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/deadline",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/hostnames",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/suppress-loopback",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ttl",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/count",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/deadline",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/protocol",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/hostnames",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/suppress-loopback",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ttl",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/count",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/deadline",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/protocol",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/fragment",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/hostnames",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/suppress-loopback",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ttl",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/count",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/deadline",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/protocol",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/fragment",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/hostnames",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/suppress-loopback",
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
                    "required": ["dest"],
                    "properties": {
                        "count": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "deadline": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "flow-label": {
                            "description": "Zero or any positive integer is " "valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or any " "positive integer.",
                        },
                        "hostnames": {"type": "boolean"},
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "suppress-loopback": {"type": "boolean"},
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ttl": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "count": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "deadline": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "flow-label": {
                            "description": "Zero or any positive integer is " "valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or any " "positive integer.",
                        },
                        "hostnames": {"type": "boolean"},
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "suppress-loopback": {"type": "boolean"},
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ttl": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "protocol": {"enum": ["icmp", "twamp"], "type": "string"},
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "count": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "deadline": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "flow-label": {
                            "description": "Zero or any positive integer is " "valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or any " "positive integer.",
                        },
                        "hostnames": {"type": "boolean"},
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "schema": {
                            "const": 3,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "suppress-loopback": {"type": "boolean"},
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ttl": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "fragment": {"type": "boolean"},
                        "protocol": {"enum": ["icmp", "twamp"], "type": "string"},
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "count": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "deadline": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "flow-label": {
                            "description": "Zero or any positive integer is " "valid.",
                            "examples": [1],
                            "minimum": 0,
                            "type": "integer",
                            "x-invalid-message": "This must be zero or any " "positive integer.",
                        },
                        "hostnames": {"type": "boolean"},
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "schema": {
                            "const": 4,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "suppress-loopback": {"type": "boolean"},
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ttl": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "fragment": {"type": "boolean"},
                        "port": {"maximum": 65535, "minimum": 0, "type": "integer"},
                        "protocol": {"description": "Any string is valid.", "type": "string"},
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "RTT",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Measure the round trip time between hosts",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/rtt",
}

s3throughput_schema = {
    "name": "s3throughput",
    "json-forms-compatible": True,
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
                            "scope": "#/properties/bucket",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/object-size",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_access-key",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_secret-key",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/iterations",
                                    "customComponent": "ps-input-number",
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
                    "required": ["_access-key", "bucket", "_secret-key", "url", "object-size"],
                    "properties": {
                        "_access-key": {"description": "Any string is valid.", "type": "string"},
                        "_secret-key": {"description": "Any string is valid.", "type": "string"},
                        "bucket": {"description": "Any string is valid.", "type": "string"},
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "iterations": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "object-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "url": {"format": "uri", "pattern": "^https?://", "type": "string"},
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "S3 Throughput",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Test throughput of S3 web service storage",
    "scheduling-class": "exclusive",
    "href": "https://localhost/pscheduler/tests/s3throughput",
}

simplestream_schema = {
    "name": "simplestream",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/fail",
                                    "customComponent": "ps-input-number",
                                }
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dawdle",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/test-material",
                            "customComponent": "ps-input-text",
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
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
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dawdle",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/test-material",
                            "customComponent": "ps-input-text",
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
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
                                    "scope": "#/properties/port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dawdle",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/test-material",
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
                    "required": ["dest"],
                    "properties": {
                        "dawdle": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "fail": {
                            "description": "Any value in [0.0..1.0] is valid.",
                            "maximum": 1.0,
                            "minimum": 0.0,
                            "type": "number",
                            "x-invalid-message": "Value must be in [0.0..1.0].",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "test-material": {"description": "Any string is valid.", "type": "string"},
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "dawdle": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "fail": {
                            "description": "Any value in [0.0..1.0] is valid.",
                            "maximum": 1.0,
                            "minimum": 0.0,
                            "type": "number",
                            "x-invalid-message": "Value must be in [0.0..1.0].",
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "test-material": {"description": "Any string is valid.", "type": "string"},
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                    },
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "dawdle": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "fail": {
                            "description": "Any value in [0.0..1.0] is valid.",
                            "maximum": 1.0,
                            "minimum": 0.0,
                            "type": "number",
                            "x-invalid-message": "Value must be in [0.0..1.0].",
                        },
                        "schema": {
                            "const": 3,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "test-material": {"description": "Any string is valid.", "type": "string"},
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "port": {"maximum": 65535, "minimum": 0, "type": "integer"},
                    },
                },
            ]
        },
    },
    "label": "Simple Stream",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Test communication between two hosts using TCP",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/simplestream",
}

snmpget_schema = {
    "name": "snmpget",
    "json-forms-compatible": False,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [None, {}],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "oneOf": [
                        {
                            "additionalProperties": False,
                            "required": ["version", "_community", "dest", "oid", "polls"],
                            "properties": {
                                "dest": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname "
                                            "as described "
                                            "in RFCs 952, "
                                            "1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' "
                                            "is not "
                                            "a "
                                            "valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "oid": {
                                    "items": {
                                        "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                        "type": "string",
                                    },
                                    "minItems": 1,
                                    "type": "array",
                                },
                                "period": {
                                    "description": "Any integer is valid.",
                                    "examples": [5],
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "integer.",
                                },
                                "polls": {
                                    "description": "Any integer is valid.",
                                    "examples": [5],
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "integer.",
                                },
                                "protocol": {"enum": ["tcp", "udp"], "type": "string"},
                                "schema": {
                                    "const": 1,
                                    "description": "Schema version.  This can "
                                    "be any positive integer.",
                                    "minimum": 1,
                                    "title": "Schema",
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "schema number.",
                                },
                                "timeout": {
                                    "description": "This can be any valid ISO "
                                    "8601 duration not "
                                    "involving months or "
                                    "years, which are inexact.",
                                    "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "title": "Duration",
                                    "type": "string",
                                    "x-info": [
                                        {
                                            "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                            "title": "ISO 8601 " "Durations",
                                        }
                                    ],
                                    "x-invalid-message": "'%s' is not a valid "
                                    "ISO 8601 duration.",
                                },
                                "_community": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "version": {"enum": ["1", "2c"], "type": "string"},
                            },
                        },
                        {
                            "additionalProperties": False,
                            "required": ["version", "dest", "oid", "polls"],
                            "properties": {
                                "dest": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname "
                                            "as described "
                                            "in RFCs 952, "
                                            "1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' "
                                            "is not "
                                            "a "
                                            "valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "oid": {
                                    "items": {
                                        "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                        "type": "string",
                                    },
                                    "minItems": 1,
                                    "type": "array",
                                },
                                "period": {
                                    "description": "Any integer is valid.",
                                    "examples": [5],
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "integer.",
                                },
                                "polls": {
                                    "description": "Any integer is valid.",
                                    "examples": [5],
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "integer.",
                                },
                                "protocol": {"enum": ["tcp", "udp"], "type": "string"},
                                "schema": {
                                    "const": 1,
                                    "description": "Schema version.  This can "
                                    "be any positive integer.",
                                    "minimum": 1,
                                    "title": "Schema",
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "schema number.",
                                },
                                "timeout": {
                                    "description": "This can be any valid ISO "
                                    "8601 duration not "
                                    "involving months or "
                                    "years, which are inexact.",
                                    "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "title": "Duration",
                                    "type": "string",
                                    "x-info": [
                                        {
                                            "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                            "title": "ISO 8601 " "Durations",
                                        }
                                    ],
                                    "x-invalid-message": "'%s' is not a valid "
                                    "ISO 8601 duration.",
                                },
                                "_auth-key": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "_priv-key": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "auth-protocol": {"enum": ["MD5", "SHA"], "type": "string"},
                                "context": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "priv-protocol": {
                                    "enum": ["AES", "AES128", "AES192", "AES256", "DES", "3DES"],
                                    "type": "string",
                                },
                                "security-level": {
                                    "enum": ["noAuthNoPriv", "authNoPriv", "authPriv"],
                                    "type": "string",
                                },
                                "security-name": {
                                    "description": "Any string is " "valid.",
                                    "type": "string",
                                },
                                "version": {"enum": ["3"], "type": "string"},
                            },
                        },
                    ],
                    "properties": {
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        }
                    },
                },
            ]
        },
    },
    "label": "SNMP Get",
    "schema": 2,
    "version": "1.0.0.3",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Make an/multiple SNMP get query(ies) to a destination and (optionally) calculate delta values between "
    "polls.",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/snmpget",
}

snmpgetbgm_schema = {
    "name": "snmpgetbgm",
    "json-forms-compatible": False,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [None, {}],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "oneOf": [
                        {
                            "required": ["version", "_community", "dest", "oid", "polls"],
                            "type": "object",
                            "properties": {
                                "dest": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname "
                                            "as described "
                                            "in RFCs 952, "
                                            "1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' "
                                            "is not "
                                            "a "
                                            "valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "oid": {
                                    "items": {
                                        "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                        "type": "string",
                                    },
                                    "minItems": 1,
                                    "type": "array",
                                },
                                "period": {
                                    "description": "Any integer is valid.",
                                    "examples": [5],
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "integer.",
                                },
                                "polls": {
                                    "description": "Any integer is valid.",
                                    "examples": [5],
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "integer.",
                                },
                                "schema": {
                                    "const": 1,
                                    "description": "Schema version.  This can "
                                    "be any positive integer.",
                                    "minimum": 1,
                                    "title": "Schema",
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "schema number.",
                                },
                                "timeout": {
                                    "description": "This can be any valid ISO "
                                    "8601 duration not "
                                    "involving months or "
                                    "years, which are inexact.",
                                    "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "title": "Duration",
                                    "type": "string",
                                    "x-info": [
                                        {
                                            "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                            "title": "ISO 8601 " "Durations",
                                        }
                                    ],
                                    "x-invalid-message": "'%s' is not a valid "
                                    "ISO 8601 duration.",
                                },
                                "_community": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "protocol": {"enum": ["tcp", "udp"], "type": "string"},
                                "version": {"enum": ["1", "2c"], "type": "string"},
                            },
                        },
                        {
                            "required": [
                                "version",
                                "dest",
                                "oid",
                                "polls",
                                "auth-protocol",
                                "_auth-key",
                            ],
                            "type": "object",
                            "properties": {
                                "dest": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname "
                                            "as described "
                                            "in RFCs 952, "
                                            "1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' "
                                            "is not "
                                            "a "
                                            "valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "oid": {
                                    "items": {
                                        "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                        "type": "string",
                                    },
                                    "minItems": 1,
                                    "type": "array",
                                },
                                "period": {
                                    "description": "Any integer is valid.",
                                    "examples": [5],
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "integer.",
                                },
                                "polls": {
                                    "description": "Any integer is valid.",
                                    "examples": [5],
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "integer.",
                                },
                                "schema": {
                                    "const": 1,
                                    "description": "Schema version.  This can "
                                    "be any positive integer.",
                                    "minimum": 1,
                                    "title": "Schema",
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "schema number.",
                                },
                                "timeout": {
                                    "description": "This can be any valid ISO "
                                    "8601 duration not "
                                    "involving months or "
                                    "years, which are inexact.",
                                    "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "title": "Duration",
                                    "type": "string",
                                    "x-info": [
                                        {
                                            "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                            "title": "ISO 8601 " "Durations",
                                        }
                                    ],
                                    "x-invalid-message": "'%s' is not a valid "
                                    "ISO 8601 duration.",
                                },
                                "_auth-key": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "_priv-key": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "auth-protocol": {"enum": ["MD5", "SHA"], "type": "string"},
                                "context": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "priv-protocol": {
                                    "enum": ["AES", "AES128", "AES192", "AES256", "DES", "3DES"],
                                    "type": "string",
                                },
                                "security-level": {
                                    "enum": ["noAuthNoPriv", "authNoPriv", "authPriv"],
                                    "type": "string",
                                },
                                "security-name": {
                                    "description": "Any string is " "valid.",
                                    "type": "string",
                                },
                                "version": {"const": "3", "type": "string"},
                            },
                        },
                    ],
                    "properties": {
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        }
                    },
                },
            ]
        },
    },
    "label": "SNMP Get Background-Multi",
    "schema": 2,
    "version": "1.0.0.3",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Make an/multiple SNMP get query(ies) to a destination and (optionally) calculate the delta between "
    "each poll.",
    "scheduling-class": "background-multi",
    "href": "https://localhost/pscheduler/tests/snmpgetbgm",
}

snmpset_schema = {
    "name": "snmpset",
    "json-forms-compatible": False,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [None, {}],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "additionalProperties": False,
                    "oneOf": [
                        {
                            "required": ["version", "_community", "dest", "oid"],
                            "type": "object",
                            "properties": {
                                "dest": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname "
                                            "as described "
                                            "in RFCs 952, "
                                            "1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' "
                                            "is not "
                                            "a "
                                            "valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "schema": {
                                    "const": 1,
                                    "description": "Schema version.  This can "
                                    "be any positive integer.",
                                    "minimum": 1,
                                    "title": "Schema",
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "schema number.",
                                },
                                "timeout": {
                                    "description": "This can be any valid ISO "
                                    "8601 duration not "
                                    "involving months or "
                                    "years, which are inexact.",
                                    "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "title": "Duration",
                                    "type": "string",
                                    "x-info": [
                                        {
                                            "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                            "title": "ISO 8601 " "Durations",
                                        }
                                    ],
                                    "x-invalid-message": "'%s' is not a valid "
                                    "ISO 8601 duration.",
                                },
                                "_community": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "oid": {
                                    "items": {
                                        "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                        "type": "string",
                                    },
                                    "type": "array",
                                },
                                "protocol": {"enum": ["tcp", "udp"], "type": "string"},
                                "version": {"enum": ["1", "2c", "3"], "type": "string"},
                            },
                        },
                        {
                            "required": ["version", "dest", "oid"],
                            "type": "object",
                            "properties": {
                                "dest": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname as "
                                            "described in RFCs "
                                            "952, 1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' is not "
                                            "a valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "description": "Any hostname "
                                            "as described "
                                            "in RFCs 952, "
                                            "1123 or 2181 "
                                            "is valid.",
                                            "examples": ["host.example.edu"],
                                            "maxLength": 255,
                                            "minLength": 1,
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                            "type": "string",
                                            "x-invalid-message": "'%s' "
                                            "is not "
                                            "a "
                                            "valid "
                                            "hostname.",
                                        },
                                        {
                                            "oneOf": [
                                                {"format": "ipv4", "type": "string"},
                                                {"format": "ipv6", "type": "string"},
                                            ]
                                        },
                                    ]
                                },
                                "schema": {
                                    "const": 1,
                                    "description": "Schema version.  This can "
                                    "be any positive integer.",
                                    "minimum": 1,
                                    "title": "Schema",
                                    "type": "integer",
                                    "x-invalid-message": "'%s' is not a valid " "schema number.",
                                },
                                "timeout": {
                                    "description": "This can be any valid ISO "
                                    "8601 duration not "
                                    "involving months or "
                                    "years, which are inexact.",
                                    "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "title": "Duration",
                                    "type": "string",
                                    "x-info": [
                                        {
                                            "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                            "title": "ISO 8601 " "Durations",
                                        }
                                    ],
                                    "x-invalid-message": "'%s' is not a valid "
                                    "ISO 8601 duration.",
                                },
                                "auth-key": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "auth-protocol": {"enum": ["md5", "sha"], "type": "string"},
                                "context": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "oid": {
                                    "items": {
                                        "pattern": "^((\\.\\d)|\\d)+(\\. " "\\d+)*$",
                                        "type": "string",
                                    },
                                    "type": "array",
                                },
                                "priv-key": {
                                    "description": "Any string is valid.",
                                    "type": "string",
                                },
                                "priv-protocol": {"enum": ["aes", "des"], "type": "string"},
                                "protocol": {"enum": ["tcp", "udp"], "type": "string"},
                                "security-level": {
                                    "enum": ["noauthnopriv", "authnopriv", "authpriv"],
                                    "type": "string",
                                },
                                "security-name": {
                                    "description": "Any string is " "valid.",
                                    "type": "string",
                                },
                                "version": {"enum": ["1", "2c", "3"], "type": "string"},
                            },
                        },
                    ],
                    "properties": {
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        }
                    },
                },
            ]
        },
    },
    "label": "SNMP Set",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Set SNMP Variables",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/snmpset",
}

throughput_schema = {
    "name": "throughput",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/local-address",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/omit",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/parallel",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/mss",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/window-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/buffer-length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/client-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/server-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/congestion",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/udp",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/no-delay",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/zero-copy",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/local-address",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/omit",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/parallel",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/mss",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/window-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/buffer-length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/client-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/server-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/congestion",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/udp",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/no-delay",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/zero-copy",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/local-address",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/omit",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/link-rtt",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/parallel",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/mss",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/window-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/buffer-length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/client-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/server-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/congestion",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/udp",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/no-delay",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/zero-copy",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/local-address",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/omit",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/link-rtt",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/parallel",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/burst-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/mss",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/window-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/buffer-length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/client-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/server-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/congestion",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/udp",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/no-delay",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/zero-copy",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth-strict",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/local-address",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/omit",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/link-rtt",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/parallel",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/burst-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/mss",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/window-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/buffer-length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/client-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/server-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/congestion",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/udp",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/no-delay",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/zero-copy",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/loopback",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth-strict",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/local-address",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/omit",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/link-rtt",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/parallel",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/burst-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/mss",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/window-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/buffer-length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/client-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/server-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/congestion",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/udp",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/no-delay",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/zero-copy",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/loopback",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth-strict",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse-connections",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/local-address",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/omit",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/link-rtt",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/fq-rate",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/parallel",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/burst-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/mss",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/window-size",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/buffer-length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/client-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/server-cpu-affinity",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/congestion",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/udp",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/no-delay",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/zero-copy",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/loopback",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth-strict",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse-connections",
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
                    "title": "pScheduler Throughput Specification Schema",
                    "required": ["dest"],
                    "properties": {
                        "bandwidth": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "buffer-length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "client-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "flow-label": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "local-address": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs "
                                    "952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "mss": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "no-delay": {"type": "boolean"},
                        "omit": {
                            "description": "This can be any valid ISO 8601 duration "
                            "not involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "parallel": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "reverse": {"type": "boolean"},
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "server-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "udp": {"type": "boolean"},
                        "window-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "zero-copy": {"type": "boolean"},
                        "congestion": {
                            "enum": [
                                "bbr",
                                "bic",
                                "cubic",
                                "htcp",
                                "reno",
                                "vegas",
                                "westwood",
                                "yeah",
                            ],
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": ["schema", "dest"],
                    "properties": {
                        "bandwidth": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "buffer-length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "client-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "flow-label": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "local-address": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs "
                                    "952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "mss": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "no-delay": {"type": "boolean"},
                        "omit": {
                            "description": "This can be any valid ISO 8601 duration "
                            "not involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "parallel": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "reverse": {"type": "boolean"},
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "server-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "udp": {"type": "boolean"},
                        "window-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "zero-copy": {"type": "boolean"},
                        "congestion": {
                            "enum": [
                                "bbr",
                                "bic",
                                "cubic",
                                "htcp",
                                "reno",
                                "vegas",
                                "westwood",
                                "yeah",
                            ],
                            "type": "string",
                        },
                        "single-ended": {"type": "boolean"},
                        "single-ended-port": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid " "integer.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": ["schema", "dest"],
                    "properties": {
                        "bandwidth": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "buffer-length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "client-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "flow-label": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "local-address": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs "
                                    "952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "mss": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "no-delay": {"type": "boolean"},
                        "omit": {
                            "description": "This can be any valid ISO 8601 duration "
                            "not involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "parallel": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "reverse": {"type": "boolean"},
                        "schema": {
                            "const": 3,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "server-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "udp": {"type": "boolean"},
                        "window-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "zero-copy": {"type": "boolean"},
                        "congestion": {
                            "enum": [
                                "bbr",
                                "bic",
                                "cubic",
                                "htcp",
                                "reno",
                                "vegas",
                                "westwood",
                                "yeah",
                            ],
                            "type": "string",
                        },
                        "single-ended": {"type": "boolean"},
                        "single-ended-port": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid " "integer.",
                        },
                        "link-rtt": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": ["schema", "dest"],
                    "properties": {
                        "bandwidth": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "buffer-length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "client-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "flow-label": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "local-address": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs "
                                    "952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "mss": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "no-delay": {"type": "boolean"},
                        "omit": {
                            "description": "This can be any valid ISO 8601 duration "
                            "not involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "parallel": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "reverse": {"type": "boolean"},
                        "schema": {
                            "const": 4,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "server-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "udp": {"type": "boolean"},
                        "window-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "zero-copy": {"type": "boolean"},
                        "congestion": {"minLength": 1, "type": "string"},
                        "single-ended": {"type": "boolean"},
                        "single-ended-port": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid " "integer.",
                        },
                        "link-rtt": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "burst-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "bandwidth-strict": {"type": "boolean"},
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": ["schema", "dest"],
                    "properties": {
                        "bandwidth": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "buffer-length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "client-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "flow-label": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "local-address": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs "
                                    "952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "mss": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "no-delay": {"type": "boolean"},
                        "omit": {
                            "description": "This can be any valid ISO 8601 duration "
                            "not involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "parallel": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "reverse": {"type": "boolean"},
                        "schema": {
                            "const": 5,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "server-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "udp": {"type": "boolean"},
                        "window-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "zero-copy": {"type": "boolean"},
                        "congestion": {"minLength": 1, "type": "string"},
                        "single-ended": {"type": "boolean"},
                        "single-ended-port": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid " "integer.",
                        },
                        "link-rtt": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "burst-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "bandwidth-strict": {"type": "boolean"},
                        "loopback": {"type": "boolean"},
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": ["schema", "dest"],
                    "properties": {
                        "bandwidth": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "buffer-length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "client-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "flow-label": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "local-address": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs "
                                    "952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "mss": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "no-delay": {"type": "boolean"},
                        "omit": {
                            "description": "This can be any valid ISO 8601 duration "
                            "not involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "parallel": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "reverse": {"type": "boolean"},
                        "schema": {
                            "const": 6,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "server-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "udp": {"type": "boolean"},
                        "window-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "zero-copy": {"type": "boolean"},
                        "congestion": {"minLength": 1, "type": "string"},
                        "single-ended": {"type": "boolean"},
                        "single-ended-port": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid " "integer.",
                        },
                        "link-rtt": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "burst-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "bandwidth-strict": {"type": "boolean"},
                        "loopback": {"type": "boolean"},
                        "reverse-connections": {"type": "boolean"},
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": ["schema", "dest"],
                    "properties": {
                        "bandwidth": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "buffer-length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "client-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "flow-label": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "interval": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "ip-tos": {
                            "description": "IP type of service.  Any value in "
                            "[0..255] is valid.",
                            "examples": [0, 42],
                            "maximum": 255,
                            "minimum": 0,
                            "title": "TOS",
                            "type": "integer",
                            "x-info": [
                                {
                                    "href": "https://datatracker.ietf.org/doc/html/rfc1349",
                                    "title": "RFC 1349",
                                }
                            ],
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "local-address": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs "
                                    "952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "mss": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "no-delay": {"type": "boolean"},
                        "omit": {
                            "description": "This can be any valid ISO 8601 duration "
                            "not involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "parallel": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "reverse": {"type": "boolean"},
                        "schema": {
                            "const": 7,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "server-cpu-affinity": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a " "valid integer.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "udp": {"type": "boolean"},
                        "window-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "zero-copy": {"type": "boolean"},
                        "congestion": {"minLength": 1, "type": "string"},
                        "single-ended": {"type": "boolean"},
                        "single-ended-port": {
                            "description": "Any integer is valid.",
                            "examples": [5],
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid " "integer.",
                        },
                        "link-rtt": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "burst-size": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "bandwidth-strict": {"type": "boolean"},
                        "loopback": {"type": "boolean"},
                        "reverse-connections": {"type": "boolean"},
                        "fq-rate": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "Throughput",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Measure network throughput between hosts",
    "scheduling-class": "exclusive",
    "href": "https://localhost/pscheduler/tests/throughput",
}

trace_schema = {
    "name": "trace",
    "json-forms-compatible": True,
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/wait",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/sendwait",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/hops",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/first-ttl",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/queries",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/length",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-port",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/probe-type",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/algorithm",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/as",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/fragment",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/hostnames",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
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
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/wait",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/sendwait",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/hops",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/first-ttl",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/queries",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/length",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flow-label",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/probe-type",
                                    "customComponent": "ps-select",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-version",
                                    "customComponent": "ps-select",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/algorithm",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/as",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/fragment",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/hostnames",
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
                    "required": ["dest"],
                    "properties": {
                        "algorithm": {"description": "Any string is valid.", "type": "string"},
                        "as": {"type": "boolean"},
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-port": {"maximum": 65535, "minimum": 0, "type": "integer"},
                        "first-ttl": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "fragment": {"type": "boolean"},
                        "hops": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "hostnames": {"type": "boolean"},
                        "ip-tos": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "probe-type": {"enum": ["icmp", "udp", "tcp"], "type": "string"},
                        "queries": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "sendwait": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "wait": {
                            "description": "This can be any valid ISO 8601 duration "
                            "not involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                },
                {
                    "type": "object",
                    "required": ["schema", "dest"],
                    "properties": {
                        "algorithm": {"description": "Any string is valid.", "type": "string"},
                        "as": {"type": "boolean"},
                        "dest": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "dest-port": {"maximum": 65535, "minimum": 0, "type": "integer"},
                        "first-ttl": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "fragment": {"type": "boolean"},
                        "hops": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive integer.",
                        },
                        "hostnames": {"type": "boolean"},
                        "ip-tos": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "ip-version": {"enum": [4, 6], "type": "integer"},
                        "length": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "probe-type": {"enum": ["icmp", "udp", "tcp"], "type": "string"},
                        "queries": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                        "schema": {
                            "const": 2,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "sendwait": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described "
                                    "in RFCs 952, 1123 or 2181 "
                                    "is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "source-node": {
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                            "type": "string",
                        },
                        "wait": {
                            "description": "This can be any valid ISO 8601 duration "
                            "not involving months or years, which "
                            "are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "flow-label": {
                            "description": "Any positive integer is valid.",
                            "examples": [1],
                            "minimum": 1,
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a positive " "integer.",
                        },
                    },
                },
            ]
        },
    },
    "label": "Trace",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Trace the path between IP hosts",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/trace",
}

wifibssid_schema = {
    "name": "wifibssid",
    "json-forms-compatible": True,
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
                            "scope": "#/properties/ssid",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/interface",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/host-node",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/timeout",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
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
                    "required": ["interface", "ssid"],
                    "properties": {
                        "duration": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as described in "
                                    "RFCs 952, 1123 or 2181 is "
                                    "valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a valid " "hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "description": "Any hostname as "
                                    "described in RFCs 952, "
                                    "1123 or 2181 is valid.",
                                    "examples": ["host.example.edu"],
                                    "maxLength": 255,
                                    "minLength": 1,
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$",
                                    "type": "string",
                                    "x-invalid-message": "'%s' is not a " "valid hostname.",
                                },
                                {
                                    "oneOf": [
                                        {"format": "ipv4", "type": "string"},
                                        {"format": "ipv6", "type": "string"},
                                    ]
                                },
                            ]
                        },
                        "interface": {"description": "Any string is valid.", "type": "string"},
                        "schema": {
                            "const": 1,
                            "description": "Schema version.  This can be any " "positive integer.",
                            "minimum": 1,
                            "title": "Schema",
                            "type": "integer",
                            "x-invalid-message": "'%s' is not a valid schema " "number.",
                        },
                        "ssid": {"description": "Any string is valid.", "type": "string"},
                        "timeout": {
                            "description": "This can be any valid ISO 8601 "
                            "duration not involving months or "
                            "years, which are inexact.",
                            "examples": ["PT10S", "PT45.67S", "PT1H30M"],
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "title": "Duration",
                            "type": "string",
                            "x-info": [
                                {
                                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                                    "title": "ISO 8601 Durations",
                                }
                            ],
                            "x-invalid-message": "'%s' is not a valid ISO 8601 " "duration.",
                        },
                    },
                    "additionalProperties": False,
                },
            ]
        },
    },
    "label": "WiFi BSSID",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Outputs a list of BSSIDs in json format with the given SSID",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/wifibssid",
}


TEST_SCHEMAS = {
    "clock": clock_schema,
    "dhcp": dhcp_schema,
    "disk-to-disk": disk_to_disk_schema,
    "dns": dns_schema,
    "dns64": dns64_schema,
    "dot1x": dot1x_schema,
    "http": http_schema,
    "idle": idle_schema,
    "idlebgm": idlebgm_schema,
    "idleex": idleex_schema,
    "latency": latency_schema,
    "latencybg": latencybg_schema,
    "mtu": mtu_schema,
    "netreach": netreach_schema,
    "noop": noop_schema,
    "psresponse": psresponse_schema,
    "rtt": rtt_schema,
    "s3throughput": s3throughput_schema,
    "simplestream": simplestream_schema,
    "snmpget": snmpget_schema,
    "snmpgetbgm": snmpgetbgm_schema,
    "snmpset": snmpset_schema,
    "throughput": throughput_schema,
    "trace": trace_schema,
    "wifibssid": wifibssid_schema,
}
