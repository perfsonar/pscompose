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
        },
        "address": {
            "type": "string",
            "title": "Address",
            "description": "The host address",
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
            "customComponent": "input-text-autocomplete",
        },
        {
            "type": "Control",
            "scope": "#/properties/pscheduler-address",
            "customComponent": "input-text-autocomplete",
        },
        {
            "type": "Control",
            "scope": "#/properties/contexts",
            "customComponent": "dropdown-multi-select",
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
                    "customComponent": "dropdown-multi-select",
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
                    "customComponent": "dropdown-multi-select",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/b-addresses",
                    "customComponent": "dropdown-multi-select",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes",
                    "customComponent": "dropdown-excludes",
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
                    "customComponent": "dropdown-multi-select",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes-self",
                    "customComponent": "dropdown-single-select",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes",
                    "customComponent": "dropdown-excludes",
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
        },
        "slip": {
            "type": "string",
            "title": "Slip",
            "description": "ISO8601 Duration that allows the start of each run to be as much as the Duration later than their ideal scheduled time. Default is 5 minutes (PT5M)",
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
            "description": "ISO8601 Duration that repeats runs at the specified duration.<br>Examples:<br> PT5M (5 minutes)<br> PT10M (10 minutes)",
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
            "description": "This field should be a JSON object with keys such as 'display-name' and 'display-set'",
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
            "type": "string",
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
                "condition": {"scope": "#/properties/type", "schema": {"const": ""}},
            },
            "elements": [],
        },
        {"type": "Control", "scope": "#/properties/label", "customComponent": "input-text"},
        {"type": "Control", "scope": "#/properties/ttl", "customComponent": "input-text"},
        {
            "type": "Control",
            "scope": "#/properties/transform",
            "customComponent": "input-text-area",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "input-text-area"},
    ],
}

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
            "type": "string",
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
        {"type": "Control", "scope": "#/properties/name", "customComponent": "input-text"},
        {
            "type": "Control",
            "scope": "#/properties/type",
            "customComponent": "dropdown-single-select",
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
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "input-text-area"},
    ],
}

CONTEXT_SCHEMA = {
    "title": "Schema for creating a new context",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Context Name",
            "description": "A string to identify this context",
        },
        "context": {
            "type": "string",
            "title": "Context Type",
            "description": "Type of context",
            "oneOf": [],
            # "oneOf": [
            #     {"const": "changefail", "title": "Change Fail"},
            #     {"const": "changenothing", "title": "Change Nothing"},
            #     {"const": "linuxnns", "title": "Linux NNS"},
            #     {"const": "linuxvrf", "title": "Linux VRF"},
            # ],
        },
        # "data": {
        #     "type": "string",
        #     "title": "Data",
        #     "description": "JSON object that specifies archive-specific parameters. Archive objects in pSConfig are taken directly from pScheduler. Eg: _url",
        # },
        "_meta": {
            "type": "string",
            "title": "Other Meta",
            "description": "Fill in information such as display-name and display-set as an object",
        },
    },
    "required": [
        "name",
        "context",
        "data",
    ],
    "renderers": {},
}

CONTEXT_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {"type": "Control", "scope": "#/properties/name", "customComponent": "input-text"},
        {
            "type": "Control",
            "scope": "#/properties/context",
            "customComponent": "dropdown-single-select",
        },
        # {"type": "Control", "scope": "#/properties/data", "customComponent": "input-text-area"},
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "input-text-area"},
    ],
}

# TODO: Check if we need scheduled-by property, subtasks property
TASK_SCHEMA = {
    "title": "Schema for creating a new task",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Task Name",
            "description": "A string to identify this task",
        },
        # "scheduled-by": {
        #     "title": "Scheduled By",
        #     "allOf": [
        #         {
        #             "type": "integer",
        #             "minimum": 0
        #         }
        #     ]
        # },
        "group": {
            "type": "string",
            "title": "Group",
            "oneOf": [],
        },
        "test": {
            "type": "string",
            "title": "Test",
            "oneOf": [],
        },
        "schedule": {
            "type": "string",
            "title": "Schedule",
            "oneOf": [],
        },
        "disabled": {
            "type": "boolean",
            "title": "Disabled",
            "description": "Check this box if this task is disabled. Set to False by default",
            "default": False,
        },
        "archives": {
            "type": "array",
            "title": "Archives",
            "items": {"oneOf": []},
        },
        "tools": {
            "type": "array",
            "title": "Tools",
            "items": {"oneOf": []},
        },
        # "subtasks": {
        #     "type": "array",
        #     "title": "Subtasks",
        #     "items": {"oneOf": []},
        # },
        "priority": {
            "type": "integer",
            "title": "Priority",
        },
        "reference": {
            "type": "string",
            "title": "Reference",
        },
        "_meta": {
            "type": "string",
            "title": "Other Meta",
            "description": "Fill in information such as display-name and display-set as an object",
        },
    },
    "required": ["name", "group", "test"],
    "renderers": {},
}

TASK_UI_SCHEMA = {
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
            "type": "Control",
            "scope": "#/properties/group",
            "customComponent": "dropdown-single-select",
        },
        {
            "type": "Control",
            "scope": "#/properties/test",
            "customComponent": "dropdown-single-select",
        },
        {
            "type": "Control",
            "scope": "#/properties/archives",
            "customComponent": "dropdown-multi-select",
        },
        {
            "type": "Control",
            "scope": "#/properties/schedule",
            "customComponent": "dropdown-single-select",
        },
        {
            "type": "Control",
            "scope": "#/properties/tools",
            "options": {"format": "select"},
            "customComponent": "dropdown-multi-select",
        },
        {
            "type": "HorizontalLayout",
            "elements": [
                # {
                #     "type": "Control",
                #     "scope": "#/properties/tools",
                #     "options": {"format": "select"},
                #     "customComponent": "dropdown-multi-select",
                # },
                {
                    "type": "Control",
                    "scope": "#/properties/priority",
                    "customComponent": "input-number",
                },
            ],
        },
        {
            "type": "Control",
            "scope": "#/properties/reference",
            "customComponent": "input-text-area",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "input-text-area"},
    ],
}

TEMPLATE_SCHEMA = {
    "title": "Schema for creating a new template",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Name",
            "description": "A string to identify this template",
        },
        "tasks": {
            "type": "array",
            "title": "Tasks",
            "items": {"oneOf": []},
        },
        "_meta": {
            "type": "string",
            "title": "Other Meta",
        },
    },
    "required": ["name", "tasks"],
    "renderers": {},
}

TEMPLATE_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {"type": "Control", "scope": "#/properties/name", "customComponent": "input-text"},
        {
            "type": "Control",
            "scope": "#/properties/tasks",
            "customComponent": "dropdown-multi-select",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "input-text-area"},
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
                            "customComponent": "dropdown-single-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "dropdown-single-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "input-text",
                        },
                        # {
                        #     "type": "Control",
                        #     "scope": "#/properties/retry-policy",
                        #     "customComponent": "input-text",
                        # },
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
                            "scope": "#/properties/_url",
                            "customComponent": "input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "dropdown-single-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_headers",
                            "customComponent": "input-text-area",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "input-text",
                        },
                        # {
                        #     "type": "Control",
                        #     "scope": "#/properties/retry-policy",
                        #     "customComponent": "input-text",
                        # },
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
                            "scope": "#/properties/_url",
                            "customComponent": "input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "dropdown-single-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/verify-ssl",
                            "customComponent": "input-checkbox",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_headers",
                            "customComponent": "input-text-area",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "input-text",
                        },
                        # {
                        #     "type": "Control",
                        #     "scope": "#/properties/retry-policy",
                        #     "customComponent": "input-text",
                        # },
                    ],
                },
                4: {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "dropdown-single-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_url",
                            "customComponent": "input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/op",
                            "customComponent": "dropdown-single-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/_headers",
                            "customComponent": "input-text-area",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/verify-ssl",
                            "customComponent": "input-checkbox",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/timeout",
                            "customComponent": "input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bind",
                            "customComponent": "input-text",
                        },
                        # {
                        #     "type": "Control",
                        #     "scope": "#/properties/retry-policy",
                        #     "customComponent": "input-text",
                        # },
                    ],
                },
            },
        },
        "versions": [None, "1", "2", "3", "4"],
    },
}

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
                            "type": "string",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                            "default": "{% address[0] %}",
                        },
                        "source-node": {
                            "title": "Source Node",
                            "type": "string",
                            "default": "{% pscheduler_address[0] %}",
                        },
                        "dest": {
                            "title": "Destination",
                            "type": "string",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
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
                        "udp": {"title": "UDP", "type": "boolean", "default": False},
                        "bandwidth": {"title": "Bandwidth", "type": "integer", "minimum": 1},
                        "bandwidth-strict": {
                            "title": "Bandwidth Strict",
                            "type": "boolean",
                            "default": False,
                        },
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
                        "no-delay": {"title": "No Delay", "type": "boolean", "default": False},
                        "congestion": {"title": "Congestion", "type": "string"},
                        "zero-copy": {
                            "title": "Use Zero Copy",
                            "type": "boolean",
                            "default": False,
                        },
                        "flow-label": {"title": "Flow Label", "type": "integer", "minimum": 1},
                        "client-cpu-affinity": {
                            "title": "Client CPU Affinity",
                            "type": "integer",
                        },
                        "server-cpu-affinity": {
                            "title": "Server CPU Affinity",
                            "type": "integer",
                        },
                        "single-ended": {
                            "title": "Single-ended testing",
                            "type": "boolean",
                            "default": False,
                        },
                        "single-ended-port": {"title": "Single Ended Port", "type": "integer"},
                        "reverse": {"title": "Reverse", "type": "boolean", "default": False},
                        "reverse-connections": {
                            "title": "Reverse Connections",
                            "type": "boolean",
                            "default": False,
                        },
                        "loopback": {"title": "Loopback", "type": "boolean", "default": False},
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
                            "type": "string",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                            "default": "{% address[0] %}",
                        },
                        "source-node": {
                            "title": "Source Node",
                            "type": "string",
                            "default": "{% pscheduler_address[0] %}",
                        },
                        "dest": {
                            "title": "Destination",
                            "type": "string",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
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
                        "udp": {"title": "UDP", "type": "boolean", "default": False},
                        "bandwidth": {"title": "Bandwidth", "type": "integer", "minimum": 1},
                        "bandwidth-strict": {
                            "title": "Bandwidth Strict",
                            "type": "boolean",
                            "default": False,
                        },
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
                        "no-delay": {"title": "No Delay", "type": "boolean", "default": False},
                        "congestion": {"title": "Congestion", "type": "string"},
                        "zero-copy": {"title": "Zero Copy", "type": "boolean", "default": False},
                        "flow-label": {"title": "Flow Label", "type": "integer", "minimum": 1},
                        "client-cpu-affinity": {
                            "title": "Client CPU Affinity",
                            "type": "integer",
                        },
                        "server-cpu-affinity": {
                            "title": "Server CPU Affinity",
                            "type": "integer",
                        },
                        "single-ended": {
                            "title": "Single Ended",
                            "type": "boolean",
                            "default": False,
                        },
                        "single-ended-port": {"title": "Single Ended Port", "type": "integer"},
                        "reverse": {"title": "Reverse", "type": "boolean", "default": False},
                        "reverse-connections": {
                            "title": "Reverse Connections",
                            "type": "boolean",
                            "default": False,
                        },
                        "loopback": {"title": "Loopback", "type": "boolean", "default": False},
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
                            "type": "string",
                            "default": "{% address[0] %}",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                        },
                        "source-node": {
                            "description": "The address of the source pScheduler node, if different",  # noqa: E501
                            "title": "Source Node",
                            "type": "string",
                            "default": "{% pscheduler_address[0] %}",
                        },
                        "dest": {
                            "description": "The address of the entity receiving packets in this test",  # noqa: E501
                            "title": "Destination",
                            "type": "string",
                            "default": "{% address[1] %}",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                        },
                        "dest-node": {
                            "description": "The address of the destination pScheduler node, if different",  # noqa: E501
                            "title": "Destination Node",
                            "type": "string",
                            "default": "{% pscheduler_address[1] %}",
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
                            "default": False,
                        },
                        "flip": {
                            "description": "In multi-participant mode, have the dest start the client and request a reverse test. Useful in some firewall and NAT environments.",  # noqa: E501
                            "title": "Flip",
                            "type": "boolean",
                            "default": False,
                        },
                        "reverse": {
                            "description": "Report results in the reverse direction (destination to source) if possible.",  # noqa: E501
                            "title": "Reverse",
                            "type": "boolean",
                            "default": False,
                        },
                        "traverse-nat": {
                            "description": "Make an effort to traverse outbound NAT,",
                            "title": "Traverse NAT",
                            "type": "boolean",
                            "default": False,
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
                            "type": "string",
                            "default": "{% address[0] %}",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                        },
                        "source-node": {
                            "description": "The address of the source pScheduler node, if different",  # noqa: E501
                            "title": "Source Node",
                            "type": "string",
                            "default": "{% pscheduler_address[0] %}",
                        },
                        "dest": {
                            "description": "The address of the entity receiving packets in this test",  # noqa: E501
                            "title": "Destination",
                            "type": "string",
                            "default": "{% address[1] %}",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                        },
                        "dest-node": {
                            "description": "The address of the destination pScheduler node, if different",  # noqa: E501
                            "title": "Destination Node",
                            "type": "string",
                            "default": "{% pscheduler_address[1] %}",
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
                            "default": False,
                        },
                        "flip": {
                            "description": "In multi-participant mode, have the dest start the client and request a reverse test. Useful in some firewall and NAT environments.",  # noqa: E501
                            "title": "Flip",
                            "type": "boolean",
                            "default": False,
                        },
                        "reverse": {
                            "description": "Report results in the reverse direction (destination to source) if possible.",  # noqa: E501
                            "title": "Reverse",
                            "type": "boolean",
                            "default": False,
                        },
                        "traverse-nat": {
                            "description": "Make an effort to traverse outbound NAT,",
                            "title": "Traverse NAT",
                            "type": "boolean",
                            "default": False,
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
