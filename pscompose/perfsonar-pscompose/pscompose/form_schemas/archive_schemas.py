ARCHIVE_SCHEMA = {
    "title": "Schema for creating a new archive",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Archive Name",
            "description": "A string to identify this archive.",
        },
        "type": {
            "type": "string",
            "title": "Type",
            "description": "The type of archive.",
            "oneOf": [],
        },
        "ttl": {
            "type": "string",
            "title": "TTL",
            "description": "ISO8601 duration that specifies the TTL",
            "examples": ["PT10S", "PT45.67S", "PT1H30M", "P1D", "P2D3H37M"],
            "pattern": "^P(?:\\d+(?:\\.\\d+)?W)?(?:\\d+(?:\\.\\d+)?D)?(?:T(?:\\d+(?:\\.\\d+)?H)?(?:\\d+(?:\\.\\d+)?M)?(?:\\d+(?:\\.\\d+)?S)?)?$",
            "x-info": [
                {
                    "href": "https://en.wikipedia.org/wiki/ISO_8601#Durations",
                    "title": "ISO 8601 Durations",
                }
            ],
            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
        },
        "label": {
            "type": "string",
            "title": "Label",
        },
        "transform": {
            "type": "array",
            "title": "Transform",
            "maxItems": 1,
            "items": {
                "additionalProperties": False,
                "properties": {
                    "script": {
                        "title": "Script",
                        "type": "string",
                    },
                    "output-raw": {
                        "title": "Output Raw",
                        "type": "boolean",
                    },
                    "args": {
                        "title": "Args",
                        "type": "object",
                    },
                },
                "required": [
                    "script",
                ],
                "type": "object",
            },
        },
        "_meta": {
            "type": "object",
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

ARCHIVE_UI_SCHEMA = {
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
            "scope": "#/properties/label",
            "customComponent": "ps-input-text",
        },
        {
            "type": "Control",
            "scope": "#/properties/ttl",
            "customComponent": "ps-input-text",
        },
        {
            "type": "Control",
            "scope": "#/properties/transform",
            "options": {
                "detail": {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/script",
                                    "customComponent": "ps-textarea",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/output-raw",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/args",
                            "customComponent": "ps-textarea-json",
                        },
                    ],
                }
            },
        },
        {
            "type": "Control",
            "scope": "#/properties/_meta",
            "customComponent": "ps-textarea-json",
        },
    ],
}
