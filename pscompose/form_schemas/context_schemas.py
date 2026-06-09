CONTEXT_SCHEMA = {
    "title": "Schema for creating a new context",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Context Name",
            "description": "A string to identify this context",
        },
        "type": {
            "type": "string",
            "title": "Type",
            "description": "The type of context plugin",
            "oneOf": [],
        },
        "_meta": {
            "type": "object",
            "title": "Other Meta",
            "description": "Fill in information such as display-name and display-set as an object",
        },
    },
    "required": ["name", "type"],
    "renderers": {},
}

CONTEXT_UI_SCHEMA = {
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
            "scope": "#/properties/_meta",
            "customComponent": "ps-textarea-json",
        },
    ],
}

changefail_context = {
    "name": "changefail",
    "label": "Changefail",
    "description": "Fail to change contexts - NOT FOR PRODUCTION",
    "href": "https://localhost/pscheduler/contexts/changefail",
    "version": "1.0",
    "schema": 2,
    "maintainer": {
        "email": "perfsonar-developer@internet2.edu",
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
    },
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
}

changenothing_context = {
    "name": "changenothing",
    "label": "Change Nothing",
    "description": "Make no changes - NOT FOR PRODUCTION",
    "href": "https://localhost/pscheduler/contexts/changenothing",
    "version": "1.0",
    "schema": 2,
    "maintainer": {
        "email": "perfsonar-developer@internet2.edu",
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
    },
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
}

linuxnns_context = {
    "name": "linuxnns",
    "label": "Linux Network Namespace",
    "description": "Change Linux network namespace",
    "href": "https://localhost/pscheduler/contexts/linuxnns",
    "version": "1.0",
    "schema": 2,
    "maintainer": {
        "email": "perfsonar-developer@internet2.edu",
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
    },
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
                            "scope": "#/properties/namespace",
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
                    "required": ["namespace"],
                    "properties": {
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "namespace": {
                            "type": "string",
                            "title": "Namespace",
                            "description": "Linux network namespace to switch to",
                            "pattern": "^[^/\\0]+$",
                            "x-invalid-message": "'%s' is not a valid namespace name.",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
}

linuxvrf_context = {
    "name": "linuxvrf",
    "label": "Linux VRF",
    "description": "Change Linux VRF",
    "href": "https://localhost/pscheduler/contexts/linuxvrf",
    "version": "1.0",
    "schema": 2,
    "maintainer": {
        "email": "perfsonar-developer@internet2.edu",
        "href": "http://www.perfsonar.net",
        "name": "perfSONAR Development Team",
    },
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
                            "scope": "#/properties/vrf",
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
                    "required": ["vrf"],
                    "properties": {
                        "schema": {
                            "const": 1,
                            "type": "integer",
                        },
                        "vrf": {
                            "type": "string",
                            "title": "VRF Name",
                            "description": "Linux VRF (Virtual Routing and Forwarding) name",
                            "pattern": "^[^/\\0]+$",
                            "x-invalid-message": "'%s' is not a valid VRF name.",
                        },
                    },
                    "additionalProperties": False,
                },
            ],
        },
    },
}

CONTEXT_SCHEMAS = {
    "changefail": changefail_context,
    "changenothing": changenothing_context,
    "linuxnns": linuxnns_context,
    "linuxvrf": linuxvrf_context,
}
