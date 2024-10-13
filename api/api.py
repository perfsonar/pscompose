from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI(title="psCompose API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React app origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TestThroughputParams(BaseModel):
    type: str
    name: str
    status: bool
    interface: str
    timeBetweenTests: int
    timeBetweenTestsUnit: str
    testDuration: int
    testDurationUnit: str
    protocol: str
    udpBandwidth: str | None
    tools: Optional[str]
    direction: str
    autotuning: bool
    windowSize: int | None
    numParallelStreams: int
    omitInterval: int
    useZeroCopy: bool
    tosBits: int
    singleEndedTesting: bool


async def mock_external_api_call():
    # Simulate an API call delay
    await asyncio.sleep(1)
    
    # Mock response from external API

    # what about validation, should we have list of lists to determine if something needs to be on the same row
    return [
        {
            "name": "type",
            "display_name": "Test Type",
            "description": "Indicates the current test type",
            "type": "string",
            "required": True,
            "default": "Throughput"
        },
        {
            "name": "name",
            "display_name": "Test name",
            "description": "A string to identify this test",
            "type": "string",
            "required": True,
            "default": ""
        },
        {
            "name": "status",
            "display_name": "Test Status",
            "description": "Indicates if the test is enabled",
            "type": "bool",
            "required": True,
            "default": True
        },
        {
            "name": "interface",
            "display_name": "Interface",
            "description": "The network interface on which to run the test. The default is the default interface of the host. Use this field if you have multiple interfaces and want to specify the interface where this test runs.",
            "type": "str",
            "required": True,
            "default": "Default"
        },
        {
            "name": "timeBetweenTests",
            "display_name": "Time between tests",
            "description": "The amount of time in between tests. Throughput tests consume bandwidth so usually only run a few times a day. The default is every 6 hours. Note that the tests will not run exactly every 6 hours as some randomization occurs to prevent tests from running in sequence at the beginning of the interval.",
            "type": "int",
            "required": True,
            "default": 6
        },
        {
            "name": "timeBetweenTestsUnit",
            "display_name": "Units",
            "description": "Indicates units of time",
            "type": "str",
            "required": True,
            "default": "Hours"
        },
        {
            "name": "testDuration",
            "display_name": "Test duration",
            "description": "The length of the tests to be run. TCP requires time to ramp up, especially as the latency increases. Consider using a larger value if the test subjects are further away.",
            "type": "int",
            "required": True,
            "default": 20
        },
        {
            "name": "testDurationUnit",
            "display_name": "Units",
            "description": "Indicates units of time",
            "type": "str",
            "required": True,
            "default": "Seconds"
        },
        {
            "name": "protocol",
            "display_name": "Protocol",
            "description": "The transport protocol to be used. It can be TCP or UDP.",
            "type": "str",
            "required": True,
            "default": "TCP"
        },
        {
            "name": "udpBandwidth",
            "display_name": "UDP Bandwidth (MB)",
            "description": "Field only appears if Protocol is set to UDP. For UDP this sets the target bandwidth in Mbps. Note that you should be careful with high values since UDP is not a “fair” protocol (in contrast to TCP) and will not back-off on bandwidth if it encounters other traffic. Also note that many perfSONAR instances disallow UDP by default, setting this option may require coordination with remote testers to allow the test to complete.",
            "type": "str",
            "required": False,
            "default": ""
        },
        {
            "name": "tools",
            "display_name": "Tool(s)",
            "description": "The underlying tool to perform throughput tests. By default it prefers the newest version of iperf3, but will fallback to an older iperf version automatically if the remote endpoint does not support it.",
            "type": "list",
            "required": False,
            "default": "[iperf3, iperf]"
        },
        {
            "name": "direction",
            "display_name": "Direction",
            "description": "The direction of the tests to be run from/to this host. Use this field to indicate send only, receive only or both directions.",
            "type": "str",
            "required": True,
            "default": "Send and Receive"
        },
        {
            "name": "autotuning",
            "display_name": "Use Autotuning",
            "description": "Allows the TCP window size to be automatically calculated.",
            "type": "bool",
            "required": True,
            "default": True
        },
        {
            "name": "windowSize",
            "display_name": "Window Size(MB)",
            "description": "If Use Autotuning is not checked then this field appears. Manually sets the value of the TCP window size.",
            "type": "int",
            "required": False,
            "default": 0
        },
        {
            "name": "numParallelStreams",
            "display_name": "Number of Parallel Streams",
            "description": "Number of concurrent streams for the test to run.",
            "type": "int",
            "required": True,
            "default": 1
        },
        {
            "name": "omitInterval",
            "display_name": "Omit Interval (sec)",
            "description": "Initial period of data to omit from the final statistics. This is so that you can skip past initial conditions such as TCP slow start. Currently only implemented by the iperf3 tool.",
            "type": "int",
            "required": True,
            "default": 0
        },
        {
            "name": "useZeroCopy",
            "display_name": "Use Zero Copy",
            "description": "Allows to set using a “zero copy” method of sending data, such as sendfile() system call. This uses much less CPU to put the data. Currently only implemented by the iperf3 tool.",
            "type": "bool",
            "required": True,
            "default": False
        },
        {
            "name": "tosBits",
            "display_name": "TOS bits",
            "description": "A value between 0 and 255 that will be set in the TOS field of the IP header, and will only have impact on networks that support QoS specifications. If you are unsure about this field, leave the default.",
            "type": "int",
            "required": True,
            "default": 0
        },
        {
            "name": "singleEndedTesting",
            "display_name": "Single-ended testing",
            "description": "Tells test to assume that pScheduler is not on the remote host and to run test without coordination. This requires a server such as iperf, iperf3 or nuttcp to be running on the far-end. It also has the limitation that there is no way to guarantee the far end is not running other tests.",
            "type": "bool",
            "required": True,
            "default": False
        },
    ]

@app.get("/pscompose/test/throughput")
async def get_test_throughput_params():
    # Call the mock external API
    external_api_response = await mock_external_api_call()
    return external_api_response

@app.post("/pscompose/test/throughput")
async def create_test_throughput(params: list[TestThroughputParams]):
    # Here you would typically process the received data
    # For now, we'll just return it
    return {"message": "Test created", "params": [param.dict() for param in params]}

@app.get("/pscompose/test/throughput2")
async def get_test_throughput2_params():
    schema = {
        "type": "object",
        "properties": {
            "type": {
                "type": "string",
                "title": "Test Type",
                "description": "Indicates the current test type",
                "default": "Throughput"
            },
            "name": {
                "type": "string",
                "title": "Test name",
                "description": "A string to identify this test",
                "default": ""
            },
            "status": {
                "type": "boolean",
                "title": "Test Status",
                "description": "Indicates if the test is enabled",
                "default": True
            },
            "interface": {
                "type": "string",
                "title": "Interface",
                "description": "The network interface on which to run the test.",
                "default": "Default"
            },
            "timeBetweenTests": {
                "type": "object",
                "title": "Time Between Tests",
                "properties": {
                    "value": {
                        "type": "integer",
                        "title": "Time",
                        "description": "The time to wait between consecutive tests",
                        "default": 6
                    },
                    "unit": {
                        "type": "string",
                        "title": "Unit",
                        "description": "The unit for time between tests",
                        "default": "Hours",
                        "enum": ["Seconds", "Minutes", "Hours", "Days"]
                    }
                }
            },
            # "timeBetweenTests": {
            #     "type": "integer",
            #     "title": "Time between tests",
            #     "description": "The time to wait between consecutive tests",
            #     "default": 3600
            # },
            # "timeBetweenTestsUnit": {
            #     "type": "string",
            #     "title": "Time between tests unit",
            #     "description": "The unit for time between tests",
            #     "default": "Seconds"
            # },
            "testDuration": {
                "type": "integer",
                "title": "Test Duration",
                "description": "The duration of each individual test",
                "default": 20
            },
            "testDurationUnit": {
                "type": "string",
                "title": "Test Duration Unit",
                "description": "The unit for test duration",
                "default": "Seconds"
            },
            "protocol": {
                "type": "string",
                "title": "Protocol",
                "description": "The transport protocol to be used. It can be TCP or UDP.",
                "default": "TCP"
            },
            "udpBandwidth": {
                "type": "string",
                "title": "UDP Bandwidth (MB)",
                "description": "For UDP this sets the target bandwidth in Mbps.",
                "default": ""
            },
            "tools": {
                "type": "array",
                "items": {"type": "string"},
                "title": "Tool(s)",
                "description": "The underlying tool to perform throughput tests.",
                "default": ["iperf3", "iperf"]
            },
            "direction": {
                "type": "string",
                "title": "Direction",
                "description": "The direction of the tests to be run from/to this host.",
                "default": "Send and Receive"
            },
            "autotuning": {
                "type": "boolean",
                "title": "Use Autotuning",
                "description": "Allows the TCP window size to be automatically calculated.",
                "default": True
            },
            "windowSize": {
                "type": "integer",
                "title": "Window Size(MB)",
                "description": "If Use Autotuning is not checked then this field appears. Manually sets the value of the TCP window size.",
                "default": 0
            },
            "numParallelStreams": {
                "type": "integer",
                "title": "Number of Parallel Streams",
                "description": "Number of concurrent streams for the test to run.",
                "default": 1
            },
            "omitInterval": {
                "type": "integer",
                "title": "Omit Interval (sec)",
                "description": "Initial period of data to omit from the final statistics.",
                "default": 0
            },
            "useZeroCopy": {
                "type": "boolean",
                "title": "Use Zero Copy",
                "description": "Use a 'zero copy' method of sending data, such as sendfile() system call.",
                "default": False
            },
            "tosBits": {
                "type": "integer",
                "title": "TOS bits",
                "description": "A value between 0 and 255 that will be set in the TOS field of the IP header.",
                "default": 0,
                "minimum": 0,
                "maximum": 255
            },
            "singleEndedTesting": {
                "type": "boolean",
                "title": "Single-ended testing",
                "description": "Run test without coordination, assuming pScheduler is not on the remote host.",
                "default": False
            }
        },
        "required": ["type", "name", "status", "interface", "timeBetweenTests", "testDuration", "testDurationUnit", "protocol", "direction", "autotuning", "numParallelStreams", "omitInterval", "useZeroCopy", "tosBits", "singleEndedTesting"]
    }
    
    uiSchema = {
        "status": {
            "ui:widget": "checkbox",
            "ui:options": {
                "inline": True
            }
        },
        "timeBetweenTests": {
            "ui:field": "timeBetweenTestsField",
            "ui:options": {
                "inline": True
            }
        },
        "tools": {
            "ui:widget": "checkboxes"
        },
        "udpBandwidth": {
            "ui:widget": "text"
        },
        "windowSize": {
            "ui:widget": "updown"
        },
        "numParallelStreams": {
            "ui:widget": "updown"
        },
        "omitInterval": {
            "ui:widget": "updown"
        },
        "tosBits": {
            "ui:widget": "updown"
        }
    }
    
    return {
        "schema": schema, 
        "uiSchema": uiSchema
    }