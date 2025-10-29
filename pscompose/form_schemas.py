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
            "customComponent": "dropdown-multi-select",
            "output": "list",
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
    "required": ["name", "type", "addresses", "a-addresses", "b-addresses"],
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
                    "output": "object",
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
                    "output": "object",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/b-addresses",
                    "customComponent": "dropdown-multi-select",
                    "output": "object",
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
                    "output": "object",
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
        # TODO: Fetch these options from pScheduler
        "archiver": {
            "type": "string",
            "title": "Archiver",
            "description": "A string that type of archive",
            "oneOf": [
                {"const": "bitbucket", "title": "Bitbucket"},
                {"const": "esmond", "title": "ESmond"},
                {"const": "failer", "title": "Failer"},
                {"const": "http", "title": "HTTP"},
                {"const": "kafka", "title": "Kafka"},
                {"const": "postgresql", "title": "PostgreSQL"},
                {"const": "rabbitmq", "title": "RabbitMQ"},
                {"const": "snmptrap", "title": "SNMP Trap"},
                {"const": "syslog", "title": "Syslog"},
                {"const": "tcp", "title": "TCP"},
                {"const": "udp", "title": "UDP"},
            ],
        },
        "data": {
            "type": "string",
            "title": "Data",
            "description": "JSON object that specifies archive-specific parameters. Archive objects in pSConfig are taken directly from pScheduler. Eg: _url",
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
        "archiver",
        "data",
    ],
    "renderers": {},
}

ARCHIVE_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {"type": "Control", "scope": "#/properties/name", "customComponent": "input-text"},
        {
            "type": "Control",
            "scope": "#/properties/archiver",
            "customComponent": "dropdown-single-select",
        },
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

TEST_SCHEMA = {
    "title": "Schema for creating a new test",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Test Name",
            "description": "A string to identify this test",
        },
        # TODO: Fetch these options from pScheduler
        "type": {
            "type": "string",
            "title": "Type",
            "description": "Type of test to be performed",
            "oneOf": [
                {"const": "clock", "title": "Clock"},
                {"const": "dhcp", "title": "DHCP"},
                {"const": "disk-to-disk", "title": "Disk To Disk"},
                {"const": "dns", "title": "DNS"},
                {"const": "dot1x", "title": "Dot1x"},
                {"const": "http", "title": "HTTP"},
                {"const": "idle", "title": "Idle"},
                {"const": "idlebgm", "title": "Idlebgm"},
                {"const": "idleex", "title": "Idleex"},
                {"const": "latency", "title": "Latency"},
                {"const": "latencybg", "title": "Latencybg"},
                {"const": "mtu", "title": "MTU"},
                {"const": "netreach", "title": "Netreach"},
                {"const": "noop", "title": "Noop"},
                {"const": "openports", "title": "Openports"},
                {"const": "psresponse", "title": "Psresponse"},
                {"const": "rtt", "title": "RTT"},
                {"const": "s3throughput", "title": "S3throughput"},
                {"const": "simplestream", "title": "Simplestream"},
                {"const": "snmpget", "title": "SNMPget"},
                {"const": "snmpgetbgm", "title": "Snmpgetbgm"},
                {"const": "snmpset", "title": "SNMPset"},
                {"const": "throughput", "title": "Throughput"},
                {"const": "trace", "title": "Trace"},
                {"const": "wifibssid", "title": "Wifibssid"},
            ],
        },
        # "spec": {
        #     "type": "string",
        #     "title": "Spec",
        # },
        "_meta": {
            "type": "string",
            "title": "Other Meta",
            "description": "Fill in information such as display-name and display-set as an object",
        },
    },
    "required": [
        "name",
        "type",
        "spec",
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
        # {"type": "Control", "scope": "#/properties/spec", "customComponent": "input-text-area"},
        {
            "type": "Group",
            "rule": {
                "effect": "SHOW",
                "condition": {"scope": "#/properties/type", "schema": {"const": "idle"}},
            },
            "elements": [
                # {"type": "Control", "scope": "#/properties/host", "customComponent": "dropdown-single-select"},
                {
                    "type": "Control",
                    "scope": "#/properties/host-node",
                    "customComponent": "input-text",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/parting-comment",
                    "customComponent": "input-text",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/schema",
                    "customComponent": "input-text",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/starting-comment",
                    "customComponent": "input-text",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/duration",
                    "customComponent": "input-text",
                },
            ],
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "input-text-area"},
        # {"type": "Control", "scope": "#/properties/host", "customComponent": "dropdown-single-select"},
        # {"type": "Control", "scope": "#/properties/host-node", "customComponent": "input-text"},
        # {"type": "Control", "scope": "#/properties/parting-comment", "customComponent": "input-text"},
        # {"type": "Control", "scope": "#/properties/schema", "customComponent": "input-text"},
        # {"type": "Control", "scope": "#/properties/starting-comment", "customComponent": "input-text"},
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
        # TODO: Fetch these options from pScheduler
        "context": {
            "type": "string",
            "title": "Context Type",
            "description": "Type of context",
            "oneOf": [
                {"const": "changefail", "title": "Change Fail"},
                {"const": "changenothing", "title": "Change Nothing"},
                {"const": "linuxnns", "title": "Linux NNS"},
                {"const": "linuxvrf", "title": "Linux VRF"},
            ],
        },
        "data": {
            "type": "string",
            "title": "Data",
            "description": "JSON object that specifies archive-specific parameters. Archive objects in pSConfig are taken directly from pScheduler. Eg: _url",
        },
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
        {"type": "Control", "scope": "#/properties/data", "customComponent": "input-text-area"},
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
            "output": "list",
        },
        {
            "type": "Control",
            "scope": "#/properties/schedule",
            "customComponent": "dropdown-single-select",
        },
        {
            "type": "HorizontalLayout",
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/tools",
                    "customComponent": "dropdown-multi-select",
                    "output": "list",
                },
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
            "title": "Template Name",
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
            "output": "list",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "input-text-area"},
    ],
}
