# For static forms that need to be rendered without talking to pScheduler
# Each DataType will have it's own schema and UI Schema

ADDRESS_SCHEMA = {
    "title": "Schema for creating a new host form",
    "type": "object",
    "properties": {
        # TODO : Should these be named as how they appear in the config JSON?
        # Eg : using display-name instead of name 
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
            "default": "true"
        }
    },
    "required": [
        "name",
        "address",
        "no-agent"
    ]
}

ADDRESS_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {
            "type": "Control",
            "scope": "#/properties/name"
        },
        {
            "type": "Control",
            "scope": "#/properties/address"
        },
        {
            "type": "Control",
            "scope": "#/properties/no-agent"
        }
    ]
}
