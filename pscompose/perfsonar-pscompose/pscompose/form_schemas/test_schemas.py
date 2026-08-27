TEST_SCHEMA = {
    "title": "Schema for creating a new test",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Test Name",
            "description": "A string to identify this test.",
        },
        "type": {
            "type": "string",
            "title": "Type",
            "description": "Type of test to be performed.",
            "oneOf": [],
        },
        "_meta": {
            "type": "object",
            "title": "Other Meta",
            "description": "Fill in information such as display-name and display-set as an object.",
        },
    },
    "required": [
        "name",
        "type",
    ],
    "renderers": {},
}

TEST_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {"type": "Control", "scope": "#/properties/name", "customComponent": "ps-input-text"},
        {
            "type": "Control",
            "scope": "#/properties/type",
            "customComponent": "ps-select",
        },
        # Dynamically fill this out
        {
            "type": "Group",
            "rule": {
                "effect": "SHOW",
                "condition": {"scope": "#/properties/type", "schema": {"const": ""}},
            },
            "elements": [],
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "ps-textarea-json"},
    ],
}
