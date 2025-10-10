# For static forms that need to be rendered without talking to pScheduler
# Each DataType will have it's own schema and UI Schema

# TODO: Should the properties be named as how they appear in the config JSON?
# Eg: using display-name instead of name
ADDRESS_SCHEMA = {
    "title": "Schema for creating a new address",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Host Name",
            "description": "A string to identify this host",
            "default": "",
        },
        "address": {
            "type": "string",
            "title": "Address",
            "description": "The host address",
            "default": "",
        },
        "no-agent": {
            "type": "boolean",
            "title": "No Agent",
            "description": "Check this box if no agent is required",
            "default": False,
        },
        "disabled": {
            "type": "boolean",
            "title": "Disabled",
            "description": "Check this box if address is disabled. Set to False by default",
            "default": False,
        },
        "lead-bind-address": {
            "type": "string",
            "title": "Lead Bind Address",
            "description": "This property must be an IP or hostname",
        },
        "pscheduler-address": {
            "type": "string",
            "title": "pScheduler Address",
            "description": "This property is an IP or hostname with an optional port specification",
        },
        "contexts": {
            "type": "array",
            "title": "Contexts",
            "items": {"oneOf": []},
        },
        "_meta": {
            "type": "string",
            "title": "Other Meta",
            "description": "Fill in information such as display-name and display-set as an object",
            "default": "",
        },
    },
    "required": [
        "name",
        "address",
    ],
    "renderers": {},
}

ADDRESS_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {
            "type": "HorizontalLayout",
            "elements": [
                {"type": "Control", "scope": "#/properties/name", "customComponent": "input-text"},
                {
                    "type": "Control",
                    "scope": "#/properties/disabled",
                    "customComponent": "input-checkbox",
                },
            ],
        },
        {
            "type": "HorizontalLayout",
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/address",
                    "customComponent": "input-text",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/no-agent",
                    "customComponent": "input-checkbox",
                },
            ],
        },
        {
            "type": "Control",
            "scope": "#/properties/lead-bind-address",
            "customComponent": "input-text",
        },
        {
            "type": "Control",
            "scope": "#/properties/pscheduler-address",
            "customComponent": "input-text",
        },
        {
            "type": "Control",
            "scope": "#/properties/contexts",
            "customComponent": "dropdown-multi-select-list",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "input-text-area"},
    ],
}

GROUP_SCHEMA = {
    "title": "Schema for creating a new group",
    "type": "object",
    "properties": {
        "name": {"type": "string", "title": "Name"},
        "type": {
            "type": "string",
            "title": "Type",
            "oneOf": [
                {"const": "list", "title": "List"},
                {"const": "disjoint", "title": "Disjoint"},
                {"const": "mesh", "title": "Mesh"},
            ],
        },
    },
    "required": ["name", "type"],
    "allOf": [
        {
            "if": {"properties": {"type": {"const": "list"}}},
            "then": {
                "properties": {
                    "type": {"const": "list"},
                    "addresses": {"type": "array", "title": "Addresses", "items": {"oneOf": []}},
                    "_meta": {
                        "type": "string",
                        "title": "Other Meta",
                        "description": "Fill in information such as display-name and display-set as an object",
                        "default": "",
                    },
                },
                "required": ["addresses"],
            },
        },
        {
            "if": {"properties": {"type": {"const": "disjoint"}}},
            "then": {
                "properties": {
                    "type": {"const": "disjoint"},
                    "unidirectional": {
                        "type": "boolean",
                        "title": "Unidirectional",
                        "description": "Check this box if it's unidirectional",
                        "default": False,
                    },
                    "a-addresses": {
                        "type": "array",
                        "title": "A-Addresses",
                        "items": {"oneOf": []},
                    },
                    "b-addresses": {
                        "type": "array",
                        "title": "B-Addresses",
                        "items": {"oneOf": []},
                    },
                    "excludes-self": {
                        "type": "string",
                        "title": "Excludes Self",
                        "oneOf": [
                            {"const": "host", "title": "Host"},
                            {"const": "address", "title": "Address"},
                            {"const": "disabled", "title": "Disabled"},
                        ],
                    },
                    "excludes": {"type": "array", "title": "Excludes", "items": {"oneOf": []}},
                    "_meta": {
                        "type": "string",
                        "title": "Other Meta",
                        "description": "Fill in information such as display-name and display-set as an object",
                        "default": "",
                    },
                },
                "required": ["a-addresses", "b-addresses"],
            },
        },
        {
            "if": {"properties": {"type": {"const": "mesh"}}},
            "then": {
                "properties": {
                    "type": {"const": "mesh"},
                    "addresses": {"type": "array", "title": "Addresses", "items": {"oneOf": []}},
                    "excludes-self": {
                        "type": "string",
                        "title": "Excludes Self",
                        "oneOf": [
                            {"const": "host", "title": "Host"},
                            {"const": "address", "title": "Address"},
                            {"const": "disabled", "title": "Disabled"},
                        ],
                    },
                    "excludes": {"type": "array", "title": "Excludes", "items": {"oneOf": []}},
                    "_meta": {
                        "type": "string",
                        "title": "Other Meta",
                        "description": "Fill in information such as display-name and display-set as an object",
                        "default": "",
                    },
                },
                "required": ["addresses"],
            },
        },
    ],
}

GROUP_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {"type": "Control", "scope": "#/properties/name", "customComponent": "input-text"},
        {
            "type": "Control",
            "scope": "#/properties/type",
            "customComponent": "dropdown-single-select",
        },
        {
            "type": "Group",
            "rule": {
                "effect": "SHOW",
                "condition": {"scope": "#/properties/type", "schema": {"const": "list"}},
            },
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/addresses",
                    "options": {"format": "select"},
                    "customComponent": "dropdown-multi-select-object",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/_meta",
                    "customComponent": "input-text-area",
                },
            ],
        },
        {
            "type": "Group",
            "rule": {
                "effect": "SHOW",
                "condition": {"scope": "#/properties/type", "schema": {"const": "disjoint"}},
            },
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/unidirectional",
                    "customComponent": "input-checkbox",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes-self",
                    "customComponent": "dropdown-single-select",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/a-addresses",
                    "customComponent": "dropdown-multi-select-object",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/b-addresses",
                    "customComponent": "dropdown-multi-select-object",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes",
                    "customComponent": "dropdown-exclude",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/_meta",
                    "customComponent": "input-text-area",
                },
            ],
        },
        {
            "type": "Group",
            "rule": {
                "effect": "SHOW",
                "condition": {"scope": "#/properties/type", "schema": {"const": "mesh"}},
            },
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/addresses",
                    "options": {"format": "select"},
                    "customComponent": "dropdown-multi-select-object",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes-self",
                    "customComponent": "dropdown-single-select",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes",
                    "customComponent": "dropdown-exclude",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/_meta",
                    "options": {"multi": True},
                    "customComponent": "input-text-area",
                },
            ],
        },
    ],
}

SCHEDULE_SCHEMA = {
    "title": "Schema for creating a new schedule",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Schedule Name",
            "description": "A string to identify this schedule",
            "default": "",
        },
        "slip": {
            "type": "string",
            "title": "Slip",
            "description": "ISO8601 DURATION that allows the start of each run to be as much as the DURATION later than their ideal scheduled time. Default is 5 minutes (PT5M)",
            "default": "PT5M",
        },
        "sliprand": {
            "type": "boolean",
            "title": "Randomize Slip",
            "description": "Randomly choose a timeslot within the allowed slip instead of choosing earliest available",
            "default": True,
        },
        "repeat": {
            "type": "string",
            "title": "Repeat",
            "description": "ISO8601 duration that repeats runs at the specified duration",
        },
        # "start": {
        #     "type": "string",
        #     "title": "Start",
        #     "description": "",
        # },
        # "until": {
        #     "type": "string",
        #     "title": "Until",
        #     "description": "",
        # },
        "max-runs": {
            "type": "integer",
            "title": "Max Runs",
            "description": "Allow the task to run up to N times",
            "minimum": 1,
        },
        "_meta": {
            "type": "string",
            "title": "Other Meta",
            "description": "Fill in information such as display-name and display-set as an object",
            "default": "",
        },
    },
    "required": [
        "name",
    ],
    "renderers": {},
}

SCHEDULE_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {"type": "Control", "scope": "#/properties/name", "customComponent": "input-text"},
        {"type": "Control", "scope": "#/properties/repeat", "customComponent": "input-text"},
        {
            "type": "HorizontalLayout",
            "elements": [
                {"type": "Control", "scope": "#/properties/slip", "customComponent": "input-text"},
                {
                    "type": "Control",
                    "scope": "#/properties/sliprand",
                    "customComponent": "input-checkbox",
                },
            ],
        },
        # {
        #     "type": "Control",
        #     "scope": "#/properties/start",
        # },
        # {
        #     "type": "Control",
        #     "scope": "#/properties/until",
        # },
        {"type": "Control", "scope": "#/properties/max-runs", "customComponent": "input-number"},
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "input-text-area"},
    ],
}

ARCHIVE_SCHEMA = {
    "title": "Schema for creating a new archive",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Archive Name",
            "description": "A string to identify this archive",
            "default": "",
        },
        # TODO: Make this a dropdown with options fetched from pScheduler
        "archiver": {
            "type": "string",
            "title": "Archiver",
            "description": "A string that type of archive",
            "default": "",
        },
        "data": {
            "type": "string",
            "title": "Data",
            "description": "JSON object that specifies archive-specific parameters. Archive objects in pSConfig are taken directly from pScheduler. Eg: _url",
            "default": "",
        },
        "schema": {
            "type": "integer",
            "title": "Schema Version",
            "description": "The schema version number",
        },
        "ttl": {
            "type": "string",
            "title": "TTL",
            "description": "ISO8601 duration that specifies the ttl",
            "default": "",
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
            "default": "",
        },
        "_meta": {
            "type": "string",
            "title": "Other Meta",
            "description": "Fill in information such as display-name and display-set as an object",
            "default": "",
        },
    },
    "required": [
        "name",
        "archiver",
        "data",
    ],
    "renderers": {},
}

ARCHIVE_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {"type": "Control", "scope": "#/properties/name", "customComponent": "input-text"},
        {"type": "Control", "scope": "#/properties/archiver", "customComponent": "input-text"},
        {"type": "Control", "scope": "#/properties/data", "customComponent": "input-text-area"},
        {"type": "Control", "scope": "#/properties/label", "customComponent": "input-text"},
        {
            "type": "HorizontalLayout",
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/schema",
                    "customComponent": "input-number",
                },
                {"type": "Control", "scope": "#/properties/ttl", "customComponent": "input-text"},
            ],
        },
        {
            "type": "Control",
            "scope": "#/properties/transform",
            "customComponent": "input-text-area",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "input-text-area"},
    ],
}
