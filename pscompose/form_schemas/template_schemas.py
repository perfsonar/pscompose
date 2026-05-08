TEMPLATE_SCHEMA = {
    "title": "Schema for creating a new template",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Name",
            "description": "A string to identify this template",
        },
        "tasks": {
            "type": "array",
            "title": "Tasks",
            "items": {"oneOf": []},
        },
        "_meta": {
            "type": "object",
            "title": "Other Meta",
        },
    },
    "required": ["name", "tasks"],
    "renderers": {},
}

TEMPLATE_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {"type": "Control", "scope": "#/properties/name", "customComponent": "ps-input-text"},
        {
            "type": "Control",
            "scope": "#/properties/tasks",
            "customComponent": "ps-select-multi",
        },
        {"type": "Control", "scope": "#/properties/_meta", "customComponent": "ps-textarea-json"},
    ],
}

TEMPLATE_IMPORT_SCHEMA = {
    "title": "Schema for creating a new template via import",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Name",
            "description": "A name to identify this template.",
        },
        "resolveConflict": {
            "type": "string",
            "title": "Conflict Resolution Strategy",
            "oneOf": [
                {"const": "overwrite", "title": "Overwrite (Keep New)"},
                {"const": "keep-existing", "title": "Keep Existing"},
                {"const": "keep-both", "title": "Keep Both (Auto Rename)"},
            ],
            "description": "Choose how to resolve datatypes with same name",
        },
        "orphanData": {
            "type": "boolean",
            "title": "Import Orphan Datas",
            "description": "Any child data types that aren’t referenced in the parent template will be created if checked.",
        },
        "importVia": {
            "type": "string",
            "title": "Import Via",
            "oneOf": [
                {"const": "upload", "title": "Upload JSON File"},
                {"const": "url", "title": "Import from URL"},
                {"const": "paste", "title": "Paste JSON"},
            ],
        },
        "upload": {
            "type": "string",
            "title": "Upload JSON File",
        },
        "url": {
            "type": "string",
            "title": "URL",
        },
        "paste": {
            "type": "object",
            "title": "Paste JSON",
        },
        "_meta": {
            "type": "object",
            "title": "Other Meta",
        },
    },
    "required": ["name", "importVia"],
    "allOf": [
        {
            "if": {"properties": {"importVia": {"const": "upload"}}},
            "then": {"required": ["upload"]},
        },
        {
            "if": {"properties": {"importVia": {"const": "url"}}},
            "then": {"required": ["url"]},
        },
        {
            "if": {"properties": {"importVia": {"const": "paste"}}},
            "then": {"required": ["paste"]},
        },
    ],
}


TEMPLATE_IMPORT_UI_SCHEMA = {
    "type": "VerticalLayout",
    "elements": [
        {
            "type": "Control",
            "scope": "#/properties/name",
            "customComponent": "ps-input-text",
        },
        {
            "type": "HorizontalLayout",
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/resolveConflict",
                    "customComponent": "ps-select",
                },
                {
                    "type": "Control",
                    "scope": "#/properties/orphanData",
                    "customComponent": "ps-input-checkbox",
                },
            ],
        },
        {
            "type": "Control",
            "scope": "#/properties/importVia",
            "customComponent": "ps-select",
        },
        {
            "type": "Template",
            "rule": {
                "effect": "SHOW",
                "condition": {
                    "scope": "#/properties/importVia",
                    "schema": {"const": "upload"},
                },
            },
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/upload",
                    "customComponent": "ps-input-file",
                },
            ],
        },
        {
            "type": "Template",
            "rule": {
                "effect": "SHOW",
                "condition": {
                    "scope": "#/properties/importVia",
                    "schema": {"const": "url"},
                },
            },
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/url",
                    "customComponent": "ps-input-text",
                },
            ],
        },
        {
            "type": "Template",
            "rule": {
                "effect": "SHOW",
                "condition": {
                    "scope": "#/properties/importVia",
                    "schema": {"const": "paste"},
                },
            },
            "elements": [
                {
                    "type": "Control",
                    "scope": "#/properties/paste",
                    "customComponent": "ps-textarea-json",
                },
            ],
        },
        {
            "type": "Control",
            "scope": "#/properties/_meta",
            "customComponent": "ps-textarea-json",
        },
    ],
}
