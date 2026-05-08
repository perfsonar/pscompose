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
            "type": "object",
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
        {"type": "Control", "scope": "#/properties/name", "customComponent": "ps-input-text"},
        {
            "type": "Control",
            "scope": "#/properties/context",
            "customComponent": "ps-select",
        },
        # {"type": "Control", "scope": "#/properties/data", "customComponent": "ps-textarea-json"},
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "ps-textarea-json"},
    ],
}
