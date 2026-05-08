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
            "type": "object",
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
                {
                    "type": "Control",
                    "scope": "#/properties/name",
                    "customComponent": "ps-input-text",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/disabled",
                    "customComponent": "ps-input-checkbox",
                },
            ],
        },
        {
            "type": "HorizontalLayout",
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/address",
                    "customComponent": "ps-input-text",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/no-agent",
                    "customComponent": "ps-input-checkbox",
                },
            ],
        },
        {
            "type": "Control",
            "scope": "#/properties/lead-bind-address",
            "customComponent": "ps-input-text-autocomplete",
        },
        {
            "type": "Control",
            "scope": "#/properties/pscheduler-address",
            "customComponent": "ps-input-text-autocomplete",
        },
        {
            "type": "Control",
            "scope": "#/properties/contexts",
            "customComponent": "ps-select-multi",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "ps-textarea-json"},
    ],
}
