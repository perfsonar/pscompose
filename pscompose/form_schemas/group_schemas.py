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
                        "type": "object",
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
                        "type": "object",
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
                        "type": "object",
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
                "condition": {"scope": "#/properties/type", "schema": {"const": "list"}},
            },
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/addresses",
                    "options": {"format": "select"},
                    "customComponent": "ps-select-multi",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/_meta",
                    "customComponent": "ps-textarea-json",
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
                    "scope": "#/properties/a-addresses",
                    "customComponent": "ps-select-multi",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/b-addresses",
                    "customComponent": "ps-select-multi",
                },
                {
                    "type": "HorizontalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/excludes-self",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/unidirectional",
                            "customComponent": "ps-input-checkbox",
                        },
                    ],
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes",
                    "customComponent": "ps-select-excludes",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/_meta",
                    "customComponent": "ps-textarea-json",
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
                    "customComponent": "ps-select-multi",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes-self",
                    "customComponent": "ps-select",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes",
                    "customComponent": "ps-select-excludes",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/_meta",
                    "options": {"multi": True},
                    "customComponent": "ps-textarea-json",
                },
            ],
        },
    ],
}
