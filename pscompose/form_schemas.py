# For static forms that need to be rendered without talking to pScheduler
# Each DataType will have it's own schema and UI Schema

# TODO: Should the properties be named as how they appear in the config JSON?
# Eg: using display-name instead of name 
ADDRESS_SCHEMA = {
    "title": "Schema for creating a new host form",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Host Name",
            "description": "A string to identify this host",
            "default": ""
        },
        "address": {
            "type": "string",
            "title": "Address",
            "description": "The host address",
            "default": ""
        },
        "no-agent": {
            "type": "boolean",
            "title": "No Agent",
            "description": "Check this box if no agent is required",
            "default": False
        },
        "disabled": {
            "type": "boolean",
            "title": "Disabled",
            "description": "Check this box if address is disabled. Set to False by default",
            "default": False
        },
        "lead-bind-address": {
            "type": "string",
            "title": "Lead Bind Address",
            "description": "This property must be an IP or hostname",
            "default": ""
        },
        "pscheduler-address": {
            "type": "string",
            "title": "pScheduler Address",
            "description": "This property is an IP or hostname with an optional port specification",
            "default": ""
        },
        "contexts": {
            "type": "object",
            "properties": {
                "languages": {
                    "type": "array",
                    "uniqueItems": True, # This makes it into a multi select rather than a dropdown
                    "items": {
                        "type": "string",
                        "enum": ["English", "Spanish", "French", "German"]
                    }
                }
            }
        },
        "_meta": {
            "type": "string",
            "title": "Other Meta",
            "description": "Fill in information such as display-name and display-set as an object",
            "default": ""
        },
    },
    "required": [
        "name",
        "address"
    ],
    "renderers": {}
}

ADDRESS_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {
            "type": "HorizontalLayout",
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/name"
                },
                {
                    "type": "Control",
                    "scope": "#/properties/disabled"
                }
            ]
        },
        {
            "type": "HorizontalLayout",
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/address"
                },
                {
                    "type": "Control",
                    "scope": "#/properties/no-agent",
                }
            ]
        },
        {
            "type": "Control",
            "scope": "#/properties/lead-bind-address"
        },
        {
            "type": "Control",
            "scope": "#/properties/pscheduler-address",
        },
        {
            "type": "Control",
            "scope": "#/properties/contexts",
        },
        {
            "type": "Control",
            "scope": "#/properties/_meta",
            "options": {
                "multi": True
            }
        }
    ]
}

GROUP_SCHEMA = {
    "title": "Schema for creating a new group",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Name"
        },
        "type": {
            "type": "string",
            "title": "Type",
            "enum": ["list", "disjoint", "mesh"]
        }
    },
    "required": ["name", "type"],
    "allOf": [
        {
            "if": {
                "properties": { "type": { "const": "list" } }
            },
            "then": {
                "properties": {
                    "type": { "const": "list" },
                    "addresses": {
                        "type": "array",
                        "title": "Addresses",
                        "items": {
                            "oneOf": [
                                {"const": "all", "title": "All Addresses"},
                            ]
                        }
                    },
                    "_meta": {
                        "type": "string",
                        "title": "Other Meta",
                        "description": "Fill in information such as display-name and display-set as an object",
                        "default": ""
                    }
                },
                "required": ["addresses"]
            }
        },
        {
            "if": {
                "properties": { "type": { "const": "disjoint" } }
            },
            "then": {
                "properties": {
                    "type": { "const": "disjoint" },
                    "unidirectional": {
                        "type": "boolean",
                        "title": "Unidirectional",
                        "description": "Check this box if it's unidirectional",
                        "default": False
                    },
                    "a-addresses": {
                        "type": "array",
                        "title": "A-Addresses",
                        "items": {
                            "oneOf": []
                        }
                    },
                    "b-addresses": {
                        "type": "array",
                        "title": "B-Addresses",
                        "items": {
                            "oneOf": []
                        }
                    },
                    "excludes-self": {
                        "type": "boolean",
                        "title": "Excludes Self"
                    },
                    "excludes": {
                        "type": "array",
                        "title": "Excludes",
                        "items": { "type": "string" }
                    },
                    "_meta": {
                        "type": "string",
                        "title": "Other Meta",
                        "description": "Fill in information such as display-name and display-set as an object",
                        "default": ""
                    }
                },
                "required": [
                    "a-addresses",
                    "b-addresses"
                ]
            }
        },
        {
            "if": {
                "properties": { "type": { "const": "mesh" } }
            },
            "then": {
                "properties": {
                    "type": { "const": "mesh" },
                    "addresses": {
                        "type": "array",
                        "title": "Addresses",
                        "items": {
                            "oneOf": []
                        }
                    },
                    "excludes-self": {
                        "type": "boolean",
                        "title": "Excludes Self"
                    },
                    "excludes": {
                        "type": "array",
                        "title": "Excludes",
                        "items": { "type": "string" }
                    },
                    "_meta": {
                        "type": "string",
                        "title": "Other Meta",
                        "description": "Fill in information such as display-name and display-set as an object",
                        "default": ""
                    }
                },
                "required": ["addresses"]
            }
        }
    ]
}

GROUP_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {
            "type": "Control",
            "scope": "#/properties/name"
        },
        {
            "type": "Control",
            "scope": "#/properties/type"
        },
        {
            "type": "Group",
            "rule": {
                "effect": "SHOW",
                "condition": {
                    "scope": "#/properties/type",
                    "schema": { "const": "list" }
                }
            },
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/addresses",
                    "options": {"format": "select"}
                },
                {
                    "type": "Control",
                    "scope": "#/properties/_meta"
                }
            ]
        },
        {
            "type": "Group",
            "rule": {
                "effect": "SHOW",
                "condition": {
                    "scope": "#/properties/type",
                    "schema": { "const": "disjoint" }
                }
            },
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/unidirectional"
                },
                {
                    "type": "Control",
                    "scope": "#/properties/a-addresses"
                },
                {
                    "type": "Control",
                    "scope": "#/properties/b-addresses"
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes-self"
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes"
                },
                {
                    "type": "Control",
                    "scope": "#/properties/_meta"
                }
            ]
        },
        {
            "type": "Group",
            "rule": {
                "effect": "SHOW",
                "condition": {
                    "scope": "#/properties/type",
                    "schema": { "const": "mesh" }
                }
            },
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/addresses",
                    "options": {"format": "select"}
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes-self"
                },
                {
                    "type": "Control",
                    "scope": "#/properties/excludes"
                },
                {
                    "type": "Control",
                    "scope": "#/properties/_meta",
                    "options": { "multi": True }
                }
            ]
        }
    ]
}