# Eg: using display-name instead of name
ADDRESS_SCHEMA = {
    "title": "Schema for creating a new address",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Host Name",
            "description": "A string to identify this host.",
        },
        "address": {
            "type": "string",
            "title": "Address",
            "description": "The host address.",
        },
        "no-agent": {
            "type": "boolean",
            "title": "No Agent",
            "description": "Check this box if no agent is required.",
            "default": False,
        },
        "disabled": {
            "type": "boolean",
            "title": "Disabled",
            "description": "Check this box if address is disabled. Set to False by default.",
            "default": False,
        },
        "lead-bind-address": {
            "type": "string",
            "title": "Lead Bind Address",
            "description": "This property must be an IP or hostname. Any hostname, FQDN, IPv4 address or IPv6 address is valid",
            "pattern": "(^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{0,62})*\\.?$)|(^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$)|(^((?:[0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,7}:|:(?::[0-9A-Fa-f]{1,4}){1,7}|(?:[0-9A-Fa-f]{1,4}:){1,6}:[0-9A-Fa-f]{1,4}|(?:[0-9A-Fa-f]{1,4}:){1,5}(?::[0-9A-Fa-f]{1,4}){1,2}|(?:[0-9A-Fa-f]{1,4}:){1,4}(?::[0-9A-Fa-f]{1,4}){1,3}|(?:[0-9A-Fa-f]{1,4}:){1,3}(?::[0-9A-Fa-f]{1,4}){1,4}|(?:[0-9A-Fa-f]{1,4}:){1,2}(?::[0-9A-Fa-f]{1,4}){1,5}|[0-9A-Fa-f]{1,4}:(?:(?::[0-9A-Fa-f]{1,4}){1,6})|:(?:(?::[0-9A-Fa-f]{1,4}){1,6}))$)",
            "examples": ["host.example.net", "198.51.100.45", "2001:db8::c0de"],
            "x-invalid-message": "Invalid Lead Bind Address.",
        },
        "pscheduler-address": {
            "type": "string",
            "title": "pScheduler Address",
            "description": "This property is an IP or hostname with an optional port specification. Any host:port is valid",
            "pattern": "(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\\](:[0-9]+)?$)",
            "examples": ["www.example.org:20165"],
            "x-invalid-message": "'%s' is not a valid host:port.",
            "x-info": [
                {
                    "title": "RFC 3896 - Authority",
                    "href": "https://datatracker.ietf.org/doc/html/rfc3986#section-3.2",
                }
            ],
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
