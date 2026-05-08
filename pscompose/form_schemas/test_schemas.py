TEST_SCHEMA = {
    "title": "Schema for creating a new test",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "title": "Test Name",
            "description": "A string to identify this test",
        },
        "type": {
            "type": "string",
            "title": "Type",
            "description": "Type of test to be performed",
            "oneOf": [],
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

idle_schema = {
    "schema": 1,
    "name": "idle",
    "description": "Consume time in the background",
    "version": "1.0",
    "maintainer": {
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
        "href": "http://www.perfsonar.net",
    },
    "scheduling-class": "background",
    "spec": {
        "jsonschema": {
            "versions": {
                1: {
                    "additionalProperties": False,
                    "properties": {
                        "duration": {
                            "title": "Duration",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "type": "string",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "host-node": {
                            "pattern": r"(^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])(:[0-9]+)?$)|(^\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\](:[0-9]+)?$)",  # noqa: E501
                            "type": "string",
                            "title": "Host Node",
                        },
                        "parting-comment": {
                            "type": "string",
                            "title": "Parting Comment",
                        },
                        "schema": {
                            "enum": [1],
                            "type": "integer",
                            "title": "Schema Version",
                            "default": 1,
                        },
                        "starting-comment": {
                            "type": "string",
                            "title": "Starting Comment",
                        },
                    },
                    "required": ["duration"],
                    "type": "object",
                },
                2: {
                    "additionalProperties": False,
                    "properties": {
                        "duration": {
                            "title": "Duration",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "type": "string",
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "parting-comment": {
                            "type": "string",
                            "title": "Parting Comment",
                        },
                        "schema": {
                            "enum": [2],
                            "type": "integer",
                            "title": "Schema Version",
                            "default": 2,
                        },
                        "starting-comment": {
                            "type": "string",
                            "title": "Starting Comment",
                        },
                    },
                    "required": ["duration", "schema"],
                    "type": "object",
                },
            },
        },
        "uischema": {
            "versions": {
                1: {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/duration",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/host-node",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/starting-comment",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parting-comment",
                            "customComponent": "ps-input-text",
                        },
                    ],
                },
                2: {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/duration",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/starting-comment",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/parting-comment",
                            "customComponent": "ps-input-text",
                        },
                    ],
                },
            },
        },
        "versions": [None, "1", "2"],
    },
}

throughput_schema = {
    "schema": 1,
    "name": "throughput",
    "description": "Measure network throughput between hosts",
    "version": "1.0",
    "maintainer": {
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
        "href": "http://www.perfsonar.net",
    },
    "scheduling-class": "exclusive",
    "spec": {
        "jsonschema": {
            "versions": {
                7: {
                    "title": "pScheduler Throughput Specification Schema",
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "schema": {
                            "type": "integer",
                            "enum": [7],
                            "title": "Schema Version",
                            "default": 7,
                        },
                        "source": {
                            "title": "Source",
                            "type": "string",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                            "default": "{% address[0] %}",
                        },
                        "source-node": {
                            "title": "Source Node",
                            "type": "string",
                            "default": "{% pscheduler_address[0] %}",
                        },
                        "dest": {
                            "title": "Destination",
                            "type": "string",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                            "default": "{% address[1] %}",
                        },
                        "dest-node": {
                            "title": "Destination Node",
                            "type": "string",
                            "default": "{% pscheduler_address[1] %}",
                        },
                        "duration": {
                            "title": "Duration",
                            "type": "string",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "title": "Interval",
                            "type": "string",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "link-rtt": {
                            "title": "Link RTT",
                            "type": "string",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "parallel": {
                            "title": "Number of Parallel Streams",
                            "type": "integer",
                            "minimum": 1,
                        },
                        "udp": {"title": "UDP", "type": "boolean", "default": False},
                        "bandwidth": {"title": "Bandwidth", "type": "integer", "minimum": 1},
                        "bandwidth-strict": {
                            "title": "Bandwidth Strict",
                            "type": "boolean",
                            "default": False,
                        },
                        "burst-size": {"title": "Burst Size", "type": "integer", "minimum": 1},
                        "fq-rate": {"title": "FQ Rate", "type": "integer", "minimum": 1},
                        "window-size": {
                            "title": "Window Size",
                            "type": "integer",
                            "minimum": 1,
                        },
                        "mss": {"title": "MSS", "type": "integer", "minimum": 1},
                        "buffer-length": {
                            "title": "Buffer Length",
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-tos": {
                            "title": "TOS Bits",
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 255,
                        },
                        "ip-version": {
                            "title": "IP Version",
                            "type": "integer",
                            "enum": [4, 6],
                        },
                        "local-address": {
                            "title": "Local Address",
                            "oneOf": [
                                {"type": "string", "format": "ipv4"},
                                {"type": "string", "format": "ipv6"},
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                },
                            ],
                        },
                        "omit": {
                            "title": "Omit Interval",
                            "type": "string",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "no-delay": {"title": "No Delay", "type": "boolean", "default": False},
                        "congestion": {"title": "Congestion", "type": "string"},
                        "zero-copy": {
                            "title": "Use Zero Copy",
                            "type": "boolean",
                            "default": False,
                        },
                        "flow-label": {"title": "Flow Label", "type": "integer", "minimum": 1},
                        "client-cpu-affinity": {
                            "title": "Client CPU Affinity",
                            "type": "integer",
                        },
                        "server-cpu-affinity": {
                            "title": "Server CPU Affinity",
                            "type": "integer",
                        },
                        "single-ended": {
                            "title": "Single-ended testing",
                            "type": "boolean",
                            "default": False,
                        },
                        "single-ended-port": {"title": "Single Ended Port", "type": "integer"},
                        "reverse": {"title": "Reverse", "type": "boolean", "default": False},
                        "reverse-connections": {
                            "title": "Reverse Connections",
                            "type": "boolean",
                            "default": False,
                        },
                        "loopback": {"title": "Loopback", "type": "boolean", "default": False},
                    },
                    "required": ["schema", "dest"],
                },
                6: {
                    "title": "pScheduler Throughput Specification Schema",
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "schema": {
                            "type": "integer",
                            "enum": [6],
                            "title": "Schema Version",
                            "default": 6,
                        },
                        "source": {
                            "title": "Source",
                            "type": "string",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                            "default": "{% address[0] %}",
                        },
                        "source-node": {
                            "title": "Source Node",
                            "type": "string",
                            "default": "{% pscheduler_address[0] %}",
                        },
                        "dest": {
                            "title": "Destination",
                            "type": "string",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                            "default": "{% address[1] %}",
                        },
                        "dest-node": {
                            "title": "Destination Node",
                            "type": "string",
                            "default": "{% pscheduler_address[1] %}",
                        },
                        "duration": {
                            "title": "Duration",
                            "type": "string",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "interval": {
                            "title": "Interval",
                            "type": "string",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "link-rtt": {
                            "title": "Link RTT",
                            "type": "string",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "parallel": {
                            "title": "Parallel Streams",
                            "type": "integer",
                            "minimum": 1,
                        },
                        "udp": {"title": "UDP", "type": "boolean", "default": False},
                        "bandwidth": {"title": "Bandwidth", "type": "integer", "minimum": 1},
                        "bandwidth-strict": {
                            "title": "Bandwidth Strict",
                            "type": "boolean",
                            "default": False,
                        },
                        "burst-size": {"title": "Burst Size", "type": "integer", "minimum": 1},
                        "window-size": {
                            "title": "Window Size",
                            "type": "integer",
                            "minimum": 1,
                        },
                        "mss": {"title": "MSS", "type": "integer", "minimum": 1},
                        "buffer-length": {
                            "title": "Buffer Length",
                            "type": "integer",
                            "minimum": 1,
                        },
                        "ip-tos": {
                            "title": "IP TOS",
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 255,
                        },
                        "ip-version": {
                            "title": "IP Version",
                            "type": "integer",
                            "enum": [4, 6],
                        },
                        "local-address": {
                            "title": "Local Address",
                            "oneOf": [
                                {"type": "string", "format": "ipv4"},
                                {"type": "string", "format": "ipv6"},
                                {
                                    "type": "string",
                                    "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                                },
                            ],
                        },
                        "omit": {
                            "title": "Omit",
                            "type": "string",
                            "pattern": r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$",  # noqa: E501
                            "x-invalid-message": "'%s' is not a valid ISO 8601 duration.",
                        },
                        "no-delay": {"title": "No Delay", "type": "boolean", "default": False},
                        "congestion": {"title": "Congestion", "type": "string"},
                        "zero-copy": {"title": "Zero Copy", "type": "boolean", "default": False},
                        "flow-label": {"title": "Flow Label", "type": "integer", "minimum": 1},
                        "client-cpu-affinity": {
                            "title": "Client CPU Affinity",
                            "type": "integer",
                        },
                        "server-cpu-affinity": {
                            "title": "Server CPU Affinity",
                            "type": "integer",
                        },
                        "single-ended": {
                            "title": "Single Ended",
                            "type": "boolean",
                            "default": False,
                        },
                        "single-ended-port": {"title": "Single Ended Port", "type": "integer"},
                        "reverse": {"title": "Reverse", "type": "boolean", "default": False},
                        "reverse-connections": {
                            "title": "Reverse Connections",
                            "type": "boolean",
                            "default": False,
                        },
                        "loopback": {"title": "Loopback", "type": "boolean", "default": False},
                    },
                    "required": ["schema", "dest"],
                },
            },
        },
        "uischema": {
            "versions": {
                7: {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/link-rtt",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/parallel",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/udp",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth-strict",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/zero-copy",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/no-delay",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/burst-size",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/fq-rate",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/window-size",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/mss",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/buffer-length",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-tos",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-version",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/local-address",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/omit",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/congestion",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/flow-label",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/client-cpu-affinity",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/server-cpu-affinity",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/single-ended-port",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse-connections",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/loopback",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                    ],
                },
                6: {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/duration",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/interval",
                                    "customComponent": "ps-input-text",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/link-rtt",
                                    "customComponent": "ps-input-text",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/parallel",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/udp",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/bandwidth-strict",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/zero-copy",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/no-delay",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/burst-size",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/fq-rate",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/window-size",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/mss",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/buffer-length",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-tos",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-version",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/local-address",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/omit",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/congestion",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/flow-label",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/client-cpu-affinity",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/server-cpu-affinity",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/single-ended-port",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/single-ended",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse-connections",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/loopback",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                    ],
                },
            },
        },
        "versions": [None, "6", "7"],
    },
}

latency_schema = {
    "schema": 1,
    "name": "latency",
    "description": "Measure network latency between hosts",
    "version": "1.0",
    "maintainer": {
        "name": "perfSONAR Development Team",
        "email": "perfsonar-developer@internet2.edu",
        "href": "http://www.perfsonar.net",
    },
    "scheduling-class": "normal",
    "spec": {
        "jsonschema": {
            "versions": {
                4: {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "schema": {
                            "description": "The version of the schema",
                            "type": "integer",
                            "enum": [4],
                            "title": "Schema Version",
                            "default": 4,
                        },
                        "source": {
                            "description": "The address of the entity sending packets in this test",  # noqa: E501
                            "title": "Source",
                            "type": "string",
                            "default": "{% address[0] %}",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                        },
                        "source-node": {
                            "description": "The address of the source pScheduler node, if different",  # noqa: E501
                            "title": "Source Node",
                            "type": "string",
                            "default": "{% pscheduler_address[0] %}",
                        },
                        "dest": {
                            "description": "The address of the entity receiving packets in this test",  # noqa: E501
                            "title": "Destination",
                            "type": "string",
                            "default": "{% address[1] %}",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                        },
                        "dest-node": {
                            "description": "The address of the destination pScheduler node, if different",  # noqa: E501
                            "title": "Destination Node",
                            "type": "string",
                            "default": "{% pscheduler_address[1] %}",
                        },
                        "protocol": {
                            "description": "The protocol to use in making the measurement",
                            "title": "Protocol",
                            "type": "string",
                        },
                        "packet-count": {
                            "description": "The number of packets to send",
                            "title": "Packet Count",
                            "type": "integer",
                            "minimum": 1,
                        },
                        "packet-interval": {
                            "description": "The number of seconds to delay between sending packets",  # noqa: E501
                            "title": "Packet Interval",
                            "type": "number",
                            "minimum": 0,
                        },
                        "packet-timeout": {
                            "description": "The number of seconds to wait before declaring a packet lost",  # noqa: E501
                            "title": "Packet Timeout",
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-padding": {
                            "description": "The size of padding to add to the packet in bytes",
                            "title": "Packet Padding",
                            "type": "integer",
                            "minimum": 0,
                        },
                        "ctrl-port": {
                            "description": "The control plane port to use for the entity acting as the server (the dest if flip is not set, the source otherwise)",  # noqa: E501
                            "title": "Control Port",
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 65535,
                        },
                        "ip-tos": {
                            "description": "DSCP value for TOS byte in the IP header as an integer",  # noqa: E501
                            "title": "IP TOS",
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 255,
                        },
                        "ip-version": {
                            "description": "Force a specific IP address type used performing the test. Useful when specifying hostnames as source or dest that may map to both IPv4 and IPv6 addresses.",  # noqa: E501
                            "title": "IP Version",
                            "type": "integer",
                            "enum": [4, 6],
                        },
                        "bucket-width": {
                            "description": "The bin size to use for histogram calculations. This value is divided into the result as reported in seconds and truncated to the nearest 2 decimal places.",  # noqa: E501
                            "title": "Bucket Width",
                            "type": "number",
                            "minimum": 0,
                        },
                        "output-raw": {
                            "description": "Output individual packet statistics. This will substantially increase the size of a successful result.",  # noqa: E501
                            "title": "Output Raw",
                            "type": "boolean",
                            "default": False,
                        },
                        "flip": {
                            "description": "In multi-participant mode, have the dest start the client and request a reverse test. Useful in some firewall and NAT environments.",  # noqa: E501
                            "title": "Flip",
                            "type": "boolean",
                            "default": False,
                        },
                        "reverse": {
                            "description": "Report results in the reverse direction (destination to source) if possible.",  # noqa: E501
                            "title": "Reverse",
                            "type": "boolean",
                            "default": False,
                        },
                        "traverse-nat": {
                            "description": "Make an effort to traverse outbound NAT,",
                            "title": "Traverse NAT",
                            "type": "boolean",
                            "default": False,
                        },
                    },
                    "required": ["schema", "dest"],
                },
                3: {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "schema": {
                            "description": "The version of the schema",
                            "type": "integer",
                            "enum": [3],
                            "title": "Schema Version",
                            "default": 3,
                        },
                        "source": {
                            "description": "The address of the entity sending packets in this test",  # noqa: E501
                            "title": "Source",
                            "type": "string",
                            "default": "{% address[0] %}",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                        },
                        "source-node": {
                            "description": "The address of the source pScheduler node, if different",  # noqa: E501
                            "title": "Source Node",
                            "type": "string",
                            "default": "{% pscheduler_address[0] %}",
                        },
                        "dest": {
                            "description": "The address of the entity receiving packets in this test",  # noqa: E501
                            "title": "Destination",
                            "type": "string",
                            "default": "{% address[1] %}",
                            # "oneOf": [
                            #     {"type": "string", "format": "ipv4"},
                            #     {"type": "string", "format": "ipv6"},
                            #     {
                            #         "type": "string",
                            #         "pattern": "^[A-Za-z0-9_][A-Za-z0-9\\-]{0,62}(\\.[A-Za-z0-9][A-Za-z0-9\\-]{1,62})*\\.?$",  # noqa: E501
                            #     },
                            # ],
                        },
                        "dest-node": {
                            "description": "The address of the destination pScheduler node, if different",  # noqa: E501
                            "title": "Destination Node",
                            "type": "string",
                            "default": "{% pscheduler_address[1] %}",
                        },
                        "packet-count": {
                            "description": "The number of packets to send",
                            "title": "Packet Count",
                            "type": "integer",
                            "minimum": 1,
                        },
                        "packet-interval": {
                            "description": "The number of seconds to delay between sending packets",  # noqa: E501
                            "title": "Packet Interval",
                            "type": "number",
                            "minimum": 0,
                        },
                        "packet-timeout": {
                            "description": "The number of seconds to wait before declaring a packet lost",  # noqa: E501
                            "title": "Packet Timeout",
                            "type": "integer",
                            "minimum": 0,
                        },
                        "packet-padding": {
                            "description": "The size of padding to add to the packet in bytes",
                            "title": "Packet Padding",
                            "type": "integer",
                            "minimum": 0,
                        },
                        "ctrl-port": {
                            "description": "The control plane port to use for the entity acting as the server (the dest if flip is not set, the source otherwise)",  # noqa: E501
                            "title": "Control Port",
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 65535,
                        },
                        "ip-tos": {
                            "description": "DSCP value for TOS byte in the IP header as an integer",  # noqa: E501
                            "title": "IP TOS",
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 255,
                        },
                        "ip-version": {
                            "description": "Force a specific IP address type used performing the test. Useful when specifying hostnames as source or dest that may map to both IPv4 and IPv6 addresses.",  # noqa: E501
                            "title": "IP Version",
                            "type": "integer",
                            "enum": [4, 6],
                        },
                        "bucket-width": {
                            "description": "The bin size to use for histogram calculations. This value is divided into the result as reported in seconds and truncated to the nearest 2 decimal places.",  # noqa: E501
                            "title": "Bucket Width",
                            "type": "number",
                            "minimum": 0,
                        },
                        "output-raw": {
                            "description": "Output individual packet statistics. This will substantially increase the size of a successful result.",  # noqa: E501
                            "title": "Output Raw",
                            "type": "boolean",
                            "default": False,
                        },
                        "flip": {
                            "description": "In multi-participant mode, have the dest start the client and request a reverse test. Useful in some firewall and NAT environments.",  # noqa: E501
                            "title": "Flip",
                            "type": "boolean",
                            "default": False,
                        },
                        "reverse": {
                            "description": "Report results in the reverse direction (destination to source) if possible.",  # noqa: E501
                            "title": "Reverse",
                            "type": "boolean",
                            "default": False,
                        },
                        "traverse-nat": {
                            "description": "Make an effort to traverse outbound NAT,",
                            "title": "Traverse NAT",
                            "type": "boolean",
                            "default": False,
                        },
                    },
                    "required": ["schema", "dest"],
                },
            },
        },
        "uischema": {
            "versions": {
                4: {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/source-node",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/dest-node",
                                    "customComponent": "ps-input-text-autocomplete",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/protocol",
                            "customComponent": "ps-input-text",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-count",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-interval",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-timeout",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/packet-padding",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ctrl-port",
                                    "customComponent": "ps-input-number",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/ip-tos",
                                    "customComponent": "ps-input-number",
                                },
                            ],
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-version",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bucket-width",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "HorizontalLayout",
                            "elements": [
                                {
                                    "type": "Control",
                                    "scope": "#/properties/output-raw",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/flip",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/reverse",
                                    "customComponent": "ps-input-checkbox",
                                },
                                {
                                    "type": "Control",
                                    "scope": "#/properties/traverse-nat",
                                    "customComponent": "ps-input-checkbox",
                                },
                            ],
                        },
                    ],
                },
                3: {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "scope": "#/properties/schema",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/source-node",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/dest",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/dest-node",
                            "customComponent": "ps-input-text-autocomplete",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/packet-count",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/packet-interval",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/packet-timeout",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/packet-padding",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ctrl-port",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-tos",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/ip-version",
                            "customComponent": "ps-select",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/bucket-width",
                            "customComponent": "ps-input-number",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/output-raw",
                            "customComponent": "ps-input-checkbox",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/flip",
                            "customComponent": "ps-input-checkbox",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/reverse",
                            "customComponent": "ps-input-checkbox",
                        },
                        {
                            "type": "Control",
                            "scope": "#/properties/traverse-nat",
                            "customComponent": "ps-input-checkbox",
                        },
                    ],
                },
            },
        },
        "versions": [None, "3", "4"],
    },
}
