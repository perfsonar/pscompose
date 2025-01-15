# For static forms that need to be rendered without talking to pScheduler
# Each DataType will have it's own schema and UI Schema

TEMPLATE_SCHEMA = {
    "title": "Schema for creating a new host form",
    "type": "object",
    "properties": {
        # Should these be named as how they appear in the config JSON?
        # Eg : using display-name instead of name 
        "name": {
            "type": "string",
            "title": "Host Name",
            "description": "A string to identify this host",
            "default": ""
        },
        "description": {
            "type": "string",
            "title": "Description",
            "description": "A string to describe this host",
            "default": ""
        },
        "no-agent": {
            "type": "boolean",
            "title": "No Agent",
            "description": "Check this box if no agent is required"
        },
    },
    "required": [
        "name", 
        "description", 
        "no-agent"
    ]
}

TEMPLATE_UI_SCHEMA = {
    "name": {
        "ui:widget": "text"
    },
    "description": {
        "ui:widget": "text"
    },
    "no-agent": {
        "ui:widget": "checkbox",
        "ui:options": {
            "inline": True
        }
    },
}

HOST_SCHEMA = {
    "title": "Schema for creating a new host form",
    "type": "object",
    "properties": {
        # Should these be named as how they appear in the config JSON?
        # Eg : using display-name instead of name 
        "name": {
            "type": "string",
            "title": "Host Name",
            "description": "A string to identify this host",
            "default": ""
        },
        "description": {
            "type": "string",
            "title": "Description",
            "description": "A string to describe this host",
            "default": ""
        },
        "no-agent": {
            "type": "boolean",
            "title": "No Agent",
            "description": "Check this box if no agent is required"
        },
    },
    "required": [
        "name", 
        "description", 
        "no-agent"
    ]
}

HOST_UI_SCHEMA = {
    "name": {
        "ui:widget": "text"
    },
    "description": {
        "ui:widget": "text"
    },
    "no-agent": {
        "ui:widget": "checkbox",
        "ui:options": {
            "inline": True
        }
    },
}
