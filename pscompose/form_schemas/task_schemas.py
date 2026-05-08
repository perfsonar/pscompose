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
            "type": "object",
            "title": "Reference",
        },
        "_meta": {
            "type": "object",
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
            "type": "Control",
            "scope": "#/properties/group",
            "customComponent": "ps-select-chip",
        },
        {
            "type": "Control",
            "scope": "#/properties/test",
            "customComponent": "ps-select-chip",
        },
        {
            "type": "Control",
            "scope": "#/properties/archives",
            "customComponent": "ps-select-multi",
        },
        {
            "type": "Control",
            "scope": "#/properties/schedule",
            "customComponent": "ps-select-chip",
        },
        {
            "type": "Control",
            "scope": "#/properties/tools",
            "options": {"format": "select"},
            "customComponent": "ps-select-multi",
        },
        {
            "type": "HorizontalLayout",
            "elements": [
                # {
                #     "type": "Control",
                #     "scope": "#/properties/tools",
                #     "options": {"format": "select"},
                #     "customComponent": "ps-select-multi",
                # },
                {
                    "type": "Control",
                    "scope": "#/properties/priority",
                    "customComponent": "ps-input-number",
                },
            ],
        },
        {
            "type": "Control",
            "scope": "#/properties/reference",
            "customComponent": "ps-textarea-json",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "ps-textarea-json"},
    ],
}
