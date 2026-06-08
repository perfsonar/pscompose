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
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "source": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "timeout": {
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
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "source": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "interface": {},
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "dest",
                        "source",
                    ],
                    "properties": {
                        "dest": {
                            "type": "string",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "source": {
                            "type": "string",
                        },
                        "cleanup": {
                            "type": "boolean",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "parallel": {
                            "type": "integer",
                            "minimum": 1,
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "query",
                        "record",
                    ],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "query": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "record": {
                            "enum": [
                                "a",
                                "aaaa",
                                "ns",
                                "cname",
                                "soa",
                                "ptr",
                                "mx",
                                "txt",
                            ],
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "nameserver": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "query",
                    ],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "query": {
                            "type": "string",
                            "format": "uri",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "nameserver": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "translation-prefix": {
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "interface",
                    ],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "ssid": {
                            "type": "string",
                        },
                        "bssid": {
                            "type": "string",
                        },
                        "driver": {
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "_password": {"type": "string"},
                        "_username": {"type": "string"},
                        "host-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "interface": {
                            "type": "string",
                        },
                        "key-management": {
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "url",
                    ],
                    "properties": {
                        "url": {
                            "type": "string",
                            "format": "uri",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "parse": {
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "url",
                    ],
                    "properties": {
                        "url": {
                            "type": "string",
                            "format": "uri",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "parse": {
                            "type": "string",
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "keep-content": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "always-succeed": {
                            "type": "boolean",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "url",
                    ],
                    "properties": {
                        "url": {
                            "type": "string",
                            "format": "uri",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "parse": {
                            "type": "string",
                        },
                        "schema": {
                            "const": 3,
                            "type": "integer",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "keep-content": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "always-succeed": {
                            "type": "boolean",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "url",
                    ],
                    "properties": {
                        "url": {
                            "type": "string",
                            "format": "uri",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "parse": {
                            "type": "string",
                        },
                        "schema": {
                            "const": 4,
                            "type": "integer",
                        },
                        "headers": {
                            "type": "object",
                            "patternProperties": {
                                "^[!#\\$%&'*+\\-.\\^`|~0-9A-Za-z]+$": {
                                    "type": "string",
                                },
                            },
                            "additionalProperties": False,
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "keep-content": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "always-succeed": {
                            "type": "boolean",
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
    "description": "Measure HTTP Response Time",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/http",
}


idle_schema = {
    "name": "idle",
    "spec": {
        "uischema": {
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
            ],
        },
        "jsonschema": {
            "versions": [
                None,
                {
                    "type": "object",
                    "required": [
                        "duration",
                    ],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "parting-comment": {
                            "type": "string",
                        },
                        "starting-comment": {
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "duration",
                    ],
                    "properties": {
                        "host": {
                            "type": "array",
                            "items": {
                                "anyOf": [
                                    {
                                        "type": "string",
                                        "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                            "minItems": 1,
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "parting-comment": {
                            "type": "string",
                        },
                        "starting-comment": {
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "duration",
                    ],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "parting-comment": {
                            "type": "string",
                        },
                        "starting-comment": {
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "duration",
                    ],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "parting-comment": {
                            "type": "string",
                        },
                        "starting-comment": {
                            "type": "string",
                        },
                    },
                },
            ],
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
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "flip": {
                            "type": "boolean",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                            "description": "The version of the schema",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "ctrl-port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "data-ports": {
                            "type": "object",
                            "required": [
                                "lower",
                                "upper",
                            ],
                            "properties": {
                                "lower": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                                "upper": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                            },
                            "additionalProperties": False,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "output-raw": {
                            "type": "boolean",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "bucket-width": {
                            "type": "number",
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                        },
                        "packet-count": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "packet-padding": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-timeout": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-interval": {
                            "type": "number",
                            "exclusiveMinimum": 0.0,
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "flip": {
                            "type": "boolean",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                            "description": "The version of the schema",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "reverse": {
                            "type": "boolean",
                        },
                        "ctrl-port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "data-ports": {
                            "type": "object",
                            "required": [
                                "lower",
                                "upper",
                            ],
                            "properties": {
                                "lower": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                                "upper": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                            },
                            "additionalProperties": False,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "output-raw": {
                            "type": "boolean",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "bucket-width": {
                            "type": "number",
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                        },
                        "packet-count": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "packet-padding": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-timeout": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-interval": {
                            "type": "number",
                            "exclusiveMinimum": 0.0,
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "flip": {
                            "type": "boolean",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 3,
                            "type": "integer",
                            "description": "The version of the schema",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "reverse": {
                            "type": "boolean",
                        },
                        "ctrl-port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "data-ports": {
                            "type": "object",
                            "required": [
                                "lower",
                                "upper",
                            ],
                            "properties": {
                                "lower": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                                "upper": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                            },
                            "additionalProperties": False,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "output-raw": {
                            "type": "boolean",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "bucket-width": {
                            "type": "number",
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                        },
                        "packet-count": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "traverse-nat": {
                            "type": "boolean",
                        },
                        "packet-padding": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-timeout": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-interval": {
                            "type": "number",
                            "exclusiveMinimum": 0.0,
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "flip": {
                            "type": "boolean",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 4,
                            "type": "integer",
                            "description": "The version of the schema",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "reverse": {
                            "type": "boolean",
                        },
                        "protocol": {
                            "type": "string",
                        },
                        "ctrl-port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "data-ports": {
                            "type": "object",
                            "required": [
                                "lower",
                                "upper",
                            ],
                            "properties": {
                                "lower": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                                "upper": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                            },
                            "additionalProperties": False,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "output-raw": {
                            "type": "boolean",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "bucket-width": {
                            "type": "number",
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                        },
                        "packet-count": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "traverse-nat": {
                            "type": "boolean",
                        },
                        "packet-padding": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-timeout": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-interval": {
                            "type": "number",
                            "exclusiveMinimum": 0.0,
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "flip": {
                            "type": "boolean",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "ctrl-port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "data-ports": {
                            "type": "object",
                            "required": [
                                "lower",
                                "upper",
                            ],
                            "properties": {
                                "lower": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                                "upper": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                            },
                            "additionalProperties": False,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "output-raw": {
                            "type": "boolean",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "bucket-width": {
                            "type": "number",
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                        },
                        "packet-count": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "packet-padding": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-timeout": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-interval": {
                            "type": "number",
                            "exclusiveMinimum": 0.0,
                        },
                    },
                },
                {
                    "type": "object",
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "flip": {
                            "type": "boolean",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "protocol": {
                            "type": "string",
                        },
                        "ctrl-port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "data-ports": {
                            "type": "object",
                            "required": [
                                "lower",
                                "upper",
                            ],
                            "properties": {
                                "lower": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                                "upper": {
                                    "type": "integer",
                                    "maximum": 65535,
                                    "minimum": 0,
                                },
                            },
                            "additionalProperties": False,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "output-raw": {
                            "type": "boolean",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "bucket-width": {
                            "type": "number",
                            "exclusiveMaximum": 1.0,
                            "exclusiveMinimum": 0.0,
                        },
                        "packet-count": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "packet-padding": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-timeout": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-interval": {
                            "type": "number",
                            "exclusiveMinimum": 0.0,
                        },
                    },
                },
            ],
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
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "source-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "network",
                    ],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "scan": {
                            "enum": [
                                "up",
                                "down",
                                "edges",
                                "random",
                            ],
                            "type": "string",
                        },
                        "limit": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "gateway": {
                            "oneOf": [
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
                                {
                                    "oneOf": [
                                        {
                                            "type": "integer",
                                            "minimum": 1,
                                        },
                                        {
                                            "type": "integer",
                                            "maximum": -1,
                                        },
                                    ],
                                },
                            ],
                        },
                        "network": {
                            "type": "string",
                            "pattern": "(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/([0-9]|[1-2][0-9]|3[0-2]))$)|(^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*(\\/([0-9]|[1-9][0-9]|1[0-1][0-9]|12[0-8]))$)",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "parallel": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                    },
                },
            ],
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
                        "data": {},
                        "fail": {
                            "type": "number",
                            "maximum": 1.0,
                            "minimum": 0.0,
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "host-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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


openports_schema = {
    "name": "openports",
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
                            "type": "Control",
                            "scope": "#/properties/ports",
                            "customComponent": "ps-input-text",
                        },
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
                                    "scope": "#/properties/source-node",
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
                                    "scope": "#/properties/services",
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
                        "network",
                    ],
                    "properties": {
                        "ports": {
                            "type": "string",
                            "pattern": "^(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[0-9]{1,4})((,(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[0-9]{1,4}))|(-(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[0-9]{1,4})))*$",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "network": {
                            "oneOf": [
                                {
                                    "type": "string",
                                    "pattern": "(^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/([0-9]|[1-2][0-9]|3[0-2]))$)|(^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*(\\/([0-9]|[1-9][0-9]|1[0-1][0-9]|12[0-8]))$)",
                                },
                                {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                            ],
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "services": {
                            "type": "boolean",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
    "label": "Open Ports",
    "schema": 2,
    "version": "1.0",
    "maintainer": {
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
    },
    "description": "Identifies open ports on a given host/subnet",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/openports",
}


psresponse_schema = {
    "name": "psresponse",
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
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "source-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "ttl": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "count": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "deadline": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "hostnames": {
                            "type": "boolean",
                        },
                        "flow-label": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "suppress-loopback": {
                            "type": "boolean",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "ttl": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "count": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "deadline": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "protocol": {
                            "enum": [
                                "icmp",
                                "twamp",
                            ],
                            "type": "string",
                        },
                        "hostnames": {
                            "type": "boolean",
                        },
                        "flow-label": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "suppress-loopback": {
                            "type": "boolean",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "ttl": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "count": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "schema": {
                            "const": 3,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "deadline": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "fragment": {
                            "type": "boolean",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "protocol": {
                            "enum": [
                                "icmp",
                                "twamp",
                            ],
                            "type": "string",
                        },
                        "hostnames": {
                            "type": "boolean",
                        },
                        "flow-label": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "suppress-loopback": {
                            "type": "boolean",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "ttl": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "count": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "schema": {
                            "const": 4,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "deadline": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "fragment": {
                            "type": "boolean",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "protocol": {
                            "enum": [
                                "icmp",
                                "twamp",
                            ],
                            "type": "string",
                        },
                        "hostnames": {
                            "type": "boolean",
                        },
                        "flow-label": {
                            "type": "integer",
                            "minimum": 0,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "suppress-loopback": {
                            "type": "boolean",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "_access-key",
                        "bucket",
                        "_secret-key",
                        "url",
                        "object-size",
                    ],
                    "properties": {
                        "url": {
                            "type": "string",
                            "format": "uri",
                            "pattern": "^https?://",
                        },
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "bucket": {
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "iterations": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "_access-key": {"type": "string"},
                        "_secret-key": {"type": "string"},
                        "object-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "fail": {
                            "type": "number",
                            "maximum": 1.0,
                            "minimum": 0.0,
                        },
                        "dawdle": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "test-material": {
                            "type": "string",
                        },
                    },
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "fail": {
                            "type": "number",
                            "maximum": 1.0,
                            "minimum": 0.0,
                        },
                        "dawdle": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "test-material": {
                            "type": "string",
                        },
                    },
                },
                {
                    "type": "object",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "fail": {
                            "type": "number",
                            "maximum": 1.0,
                            "minimum": 0.0,
                        },
                        "port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "dawdle": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "schema": {
                            "const": 3,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "test-material": {
                            "type": "string",
                        },
                    },
                },
            ],
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
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {},
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
                                "version",
                                "_community",
                                "dest",
                                "oid",
                                "polls",
                            ],
                            "properties": {
                                "oid": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                        "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                    },
                                    "minItems": 1,
                                },
                                "dest": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "polls": {
                                    "type": "integer",
                                },
                                "period": {
                                    "type": "integer",
                                },
                                "schema": {
                                    "const": 1,
                                    "type": "integer",
                                },
                                "timeout": {
                                    "type": "string",
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                },
                                "version": {
                                    "enum": [
                                        "1",
                                        "2c",
                                    ],
                                    "type": "string",
                                },
                                "protocol": {
                                    "enum": [
                                        "tcp",
                                        "udp",
                                    ],
                                    "type": "string",
                                },
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "_community": {"type": "string"},
                            },
                            "additionalProperties": False,
                        },
                        {
                            "type": "object",
                            "required": [
                                "version",
                                "dest",
                                "oid",
                                "polls",
                            ],
                            "properties": {
                                "oid": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                        "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                    },
                                    "minItems": 1,
                                },
                                "dest": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "polls": {
                                    "type": "integer",
                                },
                                "period": {
                                    "type": "integer",
                                },
                                "schema": {
                                    "const": 1,
                                    "type": "integer",
                                },
                                "context": {
                                    "type": "string",
                                },
                                "timeout": {
                                    "type": "string",
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                },
                                "version": {
                                    "enum": [
                                        "3",
                                    ],
                                    "type": "string",
                                },
                                "protocol": {
                                    "enum": [
                                        "tcp",
                                        "udp",
                                    ],
                                    "type": "string",
                                },
                                "_auth-key": {"type": "string"},
                                "_priv-key": {"type": "string"},
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "security-level": {
                                    "enum": [
                                        "noAuthNoPriv",
                                        "authNoPriv",
                                        "authPriv",
                                    ],
                                    "type": "string",
                                },
                            },
                            "additionalProperties": False,
                        },
                    ],
                },
            ],
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
    "description": "Make an/multiple SNMP get query(ies) to a destination and (optionally) calculate delta values between polls.",
    "scheduling-class": "background",
    "href": "https://localhost/pscheduler/tests/snmpget",
}


snmpgetbgm_schema = {
    "name": "snmpgetbgm",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {},
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
                                "version",
                                "_community",
                                "dest",
                                "oid",
                                "polls",
                            ],
                            "properties": {
                                "oid": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                        "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                    },
                                    "minItems": 1,
                                },
                                "dest": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "polls": {
                                    "type": "integer",
                                },
                                "period": {
                                    "type": "integer",
                                },
                                "schema": {
                                    "const": 1,
                                    "type": "integer",
                                },
                                "timeout": {
                                    "type": "string",
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                },
                                "version": {
                                    "enum": [
                                        "1",
                                        "2c",
                                        "3",
                                    ],
                                    "type": "string",
                                },
                                "protocol": {
                                    "enum": [
                                        "tcp",
                                        "udp",
                                    ],
                                    "type": "string",
                                },
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "_community": {"type": "string"},
                            },
                        },
                        {
                            "type": "object",
                            "required": [
                                "version",
                                "dest",
                                "oid",
                                "polls",
                            ],
                            "properties": {
                                "oid": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                        "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                    },
                                    "minItems": 1,
                                },
                                "dest": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "polls": {
                                    "type": "integer",
                                },
                                "period": {
                                    "type": "integer",
                                },
                                "schema": {
                                    "const": 1,
                                    "type": "integer",
                                },
                                "context": {
                                    "type": "string",
                                },
                                "timeout": {
                                    "type": "string",
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                },
                                "version": {
                                    "enum": [
                                        "1",
                                        "2c",
                                        "3",
                                    ],
                                    "type": "string",
                                },
                                "_auth-key": {"type": "string"},
                                "_priv-key": {"type": "string"},
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                    "additionalProperties": False,
                },
            ],
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
    "description": "Make an/multiple SNMP get query(ies) to a destination and (optionally) calculate the delta between each poll.",
    "scheduling-class": "background-multi",
    "href": "https://localhost/pscheduler/tests/snmpgetbgm",
}


snmpset_schema = {
    "name": "snmpset",
    "spec": {
        "uischema": {
            "#": "The zeroth element of this is always null since there is no version 0.",
            "versions": [
                None,
                {},
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
                                "version",
                                "_community",
                                "dest",
                                "oid",
                            ],
                            "properties": {
                                "oid": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                        "pattern": "^(((\\.\\d)|\\d)+(\\.\\d+)*)|([a-z][A-Z]*)$",
                                    },
                                },
                                "dest": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "timeout": {
                                    "type": "string",
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                },
                                "version": {
                                    "enum": [
                                        "1",
                                        "2c",
                                        "3",
                                    ],
                                    "type": "string",
                                },
                                "protocol": {
                                    "enum": [
                                        "tcp",
                                        "udp",
                                    ],
                                    "type": "string",
                                },
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "_community": {"type": "string"},
                            },
                        },
                        {
                            "type": "object",
                            "required": [
                                "version",
                                "dest",
                                "oid",
                            ],
                            "properties": {
                                "oid": {
                                    "type": "array",
                                    "items": {
                                        "type": "string",
                                        "pattern": "^((\\.\\d)|\\d)+(\\.\\d+)*$",
                                    },
                                },
                                "dest": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "context": {
                                    "type": "string",
                                },
                                "timeout": {
                                    "type": "string",
                                    "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                                    "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                                },
                                "version": {
                                    "enum": [
                                        "1",
                                        "2c",
                                        "3",
                                    ],
                                    "type": "string",
                                },
                                "auth-key": {
                                    "type": "string",
                                },
                                "priv-key": {
                                    "type": "string",
                                },
                                "protocol": {
                                    "enum": [
                                        "tcp",
                                        "udp",
                                    ],
                                    "type": "string",
                                },
                                "host-node": {
                                    "anyOf": [
                                        {
                                            "type": "string",
                                            "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                                "auth-protocol": {
                                    "enum": [
                                        "md5",
                                        "sha",
                                    ],
                                    "type": "string",
                                },
                                "priv-protocol": {
                                    "enum": [
                                        "aes",
                                        "des",
                                    ],
                                    "type": "string",
                                },
                                "security-name": {
                                    "type": "string",
                                },
                                "security-level": {
                                    "enum": [
                                        "noauthnopriv",
                                        "authnopriv",
                                        "authpriv",
                                    ],
                                    "type": "string",
                                },
                            },
                        },
                    ],
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "mss": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "udp": {
                            "type": "boolean",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "omit": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "reverse": {
                            "type": "boolean",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "no-delay": {
                            "type": "boolean",
                        },
                        "parallel": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "bandwidth": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "zero-copy": {
                            "type": "boolean",
                        },
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
                        "flow-label": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "window-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "buffer-length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "local-address": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "client-cpu-affinity": {
                            "type": "integer",
                        },
                        "server-cpu-affinity": {
                            "type": "integer",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "mss": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "udp": {
                            "type": "boolean",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "omit": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "reverse": {
                            "type": "boolean",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "no-delay": {
                            "type": "boolean",
                        },
                        "parallel": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "bandwidth": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "zero-copy": {
                            "type": "boolean",
                        },
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
                        "flow-label": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "window-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "single-ended": {
                            "type": "boolean",
                        },
                        "buffer-length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "local-address": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "single-ended-port": {
                            "type": "integer",
                        },
                        "client-cpu-affinity": {
                            "type": "integer",
                        },
                        "server-cpu-affinity": {
                            "type": "integer",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "mss": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "udp": {
                            "type": "boolean",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "omit": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 3,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "reverse": {
                            "type": "boolean",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "link-rtt": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "no-delay": {
                            "type": "boolean",
                        },
                        "parallel": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "bandwidth": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "zero-copy": {
                            "type": "boolean",
                        },
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
                        "flow-label": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "window-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "single-ended": {
                            "type": "boolean",
                        },
                        "buffer-length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "local-address": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "single-ended-port": {
                            "type": "integer",
                        },
                        "client-cpu-affinity": {
                            "type": "integer",
                        },
                        "server-cpu-affinity": {
                            "type": "integer",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "mss": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "udp": {
                            "type": "boolean",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "omit": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 4,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "reverse": {
                            "type": "boolean",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "link-rtt": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "no-delay": {
                            "type": "boolean",
                        },
                        "parallel": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "bandwidth": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "zero-copy": {
                            "type": "boolean",
                        },
                        "burst-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "congestion": {
                            "type": "string",
                            "minLength": 1,
                        },
                        "flow-label": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "window-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "single-ended": {
                            "type": "boolean",
                        },
                        "buffer-length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "local-address": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "bandwidth-strict": {
                            "type": "boolean",
                        },
                        "single-ended-port": {
                            "type": "integer",
                        },
                        "client-cpu-affinity": {
                            "type": "integer",
                        },
                        "server-cpu-affinity": {
                            "type": "integer",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "mss": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "udp": {
                            "type": "boolean",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "omit": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 5,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "reverse": {
                            "type": "boolean",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "link-rtt": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "loopback": {
                            "type": "boolean",
                        },
                        "no-delay": {
                            "type": "boolean",
                        },
                        "parallel": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "bandwidth": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "zero-copy": {
                            "type": "boolean",
                        },
                        "burst-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "congestion": {
                            "type": "string",
                            "minLength": 1,
                        },
                        "flow-label": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "window-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "single-ended": {
                            "type": "boolean",
                        },
                        "buffer-length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "local-address": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "bandwidth-strict": {
                            "type": "boolean",
                        },
                        "single-ended-port": {
                            "type": "integer",
                        },
                        "client-cpu-affinity": {
                            "type": "integer",
                        },
                        "server-cpu-affinity": {
                            "type": "integer",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "mss": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "udp": {
                            "type": "boolean",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "omit": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 6,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "reverse": {
                            "type": "boolean",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "link-rtt": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "loopback": {
                            "type": "boolean",
                        },
                        "no-delay": {
                            "type": "boolean",
                        },
                        "parallel": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "bandwidth": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "zero-copy": {
                            "type": "boolean",
                        },
                        "burst-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "congestion": {
                            "type": "string",
                            "minLength": 1,
                        },
                        "flow-label": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "window-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "single-ended": {
                            "type": "boolean",
                        },
                        "buffer-length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "local-address": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "bandwidth-strict": {
                            "type": "boolean",
                        },
                        "single-ended-port": {
                            "type": "integer",
                        },
                        "client-cpu-affinity": {
                            "type": "integer",
                        },
                        "reverse-connections": {
                            "type": "boolean",
                        },
                        "server-cpu-affinity": {
                            "type": "integer",
                        },
                    },
                    "additionalProperties": False,
                },
                {
                    "type": "object",
                    "title": "pScheduler Throughput Specification Schema",
                    "required": [
                        "schema",
                        "dest",
                    ],
                    "properties": {
                        "mss": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "udp": {
                            "type": "boolean",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "omit": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "maximum": 255,
                            "minimum": 0,
                        },
                        "schema": {
                            "const": 7,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "fq-rate": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "reverse": {
                            "type": "boolean",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "link-rtt": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "loopback": {
                            "type": "boolean",
                        },
                        "no-delay": {
                            "type": "boolean",
                        },
                        "parallel": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "bandwidth": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "dest-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "zero-copy": {
                            "type": "boolean",
                        },
                        "burst-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "congestion": {
                            "type": "string",
                            "minLength": 1,
                        },
                        "flow-label": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                        "window-size": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "single-ended": {
                            "type": "boolean",
                        },
                        "buffer-length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "local-address": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "bandwidth-strict": {
                            "type": "boolean",
                        },
                        "single-ended-port": {
                            "type": "integer",
                        },
                        "client-cpu-affinity": {
                            "type": "integer",
                        },
                        "reverse-connections": {
                            "type": "boolean",
                        },
                        "server-cpu-affinity": {
                            "type": "integer",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "as": {
                            "type": "boolean",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "hops": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "wait": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "queries": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "fragment": {
                            "type": "boolean",
                        },
                        "sendwait": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "algorithm": {
                            "type": "string",
                        },
                        "dest-port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "first-ttl": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "hostnames": {
                            "type": "boolean",
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "probe-type": {
                            "enum": [
                                "icmp",
                                "udp",
                                "tcp",
                            ],
                            "type": "string",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                    },
                },
                {
                    "type": "object",
                    "required": [
                        "dest",
                    ],
                    "properties": {
                        "as": {
                            "type": "boolean",
                        },
                        "dest": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "hops": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "wait": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "ip-tos": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "length": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "schema": {
                            "const": 2,
                            "type": "integer",
                        },
                        "source": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "queries": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "fragment": {
                            "type": "boolean",
                        },
                        "sendwait": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "algorithm": {
                            "type": "string",
                        },
                        "dest-port": {
                            "type": "integer",
                            "maximum": 65535,
                            "minimum": 0,
                        },
                        "first-ttl": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "hostnames": {
                            "type": "boolean",
                        },
                        "flow-label": {
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-version": {
                            "enum": [
                                4,
                                6,
                            ],
                            "type": "integer",
                        },
                        "probe-type": {
                            "enum": [
                                "icmp",
                                "udp",
                                "tcp",
                            ],
                            "type": "string",
                        },
                        "source-node": {
                            "type": "string",
                            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
                        },
                    },
                },
            ],
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
                    "required": [
                        "interface",
                        "ssid",
                    ],
                    "properties": {
                        "host": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "ssid": {
                            "type": "string",
                        },
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "timeout": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "duration": {
                            "type": "string",
                            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "anyOf": [
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",
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
                        "interface": {
                            "type": "string",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
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
    "openports": openports_schema,
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
