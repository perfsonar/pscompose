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
            "type": "object",
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
        {"type": "Control", "scope": "#/properties/name", "customComponent": "ps-input-text"},
        {"type": "Control", "scope": "#/properties/repeat", "customComponent": "ps-input-text"},
        {
            "type": "HorizontalLayout",
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/slip",
                    "customComponent": "ps-input-text",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/sliprand",
                    "customComponent": "ps-input-checkbox",
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
        {
            "type": "Control",
            "scope": "#/properties/max-runs",
            "customComponent": "ps-input-number",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "ps-textarea-json"},
    ],
}
