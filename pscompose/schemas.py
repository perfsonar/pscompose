from pydantic import BaseModel, Field
from typing import List, Optional, Union, Literal, Dict
from datetime import datetime

class AdminData(BaseModel):
    email: str
    name: str


class Meta(BaseModel):
    administrator: Optional[List[AdminData]]
    display_name: str = Field(..., alias="display-name")


class ArchiveData(BaseModel):
    measurement_agent: str = Field(..., alias="measurement-agent")
    # measurement-agent: str
    url: str


class Archives(BaseModel):
    archiver: str
    data: ArchiveData


class HostData(BaseModel):
    # ... makes the Field as required
    # by_alias=True does the conversion
    display_name: str = Field(..., alias="display-name")
    organization_display_name: str = Field(..., alias="organization-display-name")
    site_display_name: str = Field(..., alias="site-display-name")
    display_set: str = Field(..., alias="display-set")


class Hosts(BaseModel):
    _meta: Optional[HostData]
    no_agent: bool = Field(..., alias="no-agent")


class GroupData(BaseModel):
    name: str


class Groups(BaseModel):
    a_addresses: List[GroupData] = Field(alias="a-addresses")
    b_addresses: List[GroupData] = Field(alias="b-addresses")
    addresses: Optional[List[GroupData]]
    type: Literal["disjoint", "mesh"]
    unidirectional: Optional[bool]


class Schedules(BaseModel):
    repeat: str
    slip: str
    sliprand: bool


class AddressData(BaseModel):
    display_name: str = Field(..., alias="display-name")
    display_set: str = Field(..., alias="display-set")


# What is this?
class Addresses(BaseModel):
    host: Optional[str]
    address: Optional[str]
    _meta: Optional[AddressData]


class TaskMeta(BaseModel):
    display_name: str = Field(..., alias="display-name")


class TaskReference(BaseModel):
    display_set_source: str = Field(..., alias="display-set-source")
    display_set_dest: str = Field(..., alias="display-set-dest")
    display_task_name: str = Field(..., alias="display-task-name")
    display_task_group: List[str] = Field(..., alias="display-task-group")


class Tasks(BaseModel):
    _meta: Optional[TaskMeta]
    reference: Optional[TaskReference]
    group: str
    schedule: str
    archives: List[str]
    test: str
    tools: List[str]

# Will vary based on test type?
# class TestData(BaseModel):


class Tests(BaseModel):
    # spec: Optional[TestData]
    spec: Optional[dict]
    type: str


class Templates(BaseModel):
    _meta:  Meta
    archives: Archives
    addresses: Addresses
    groups: Groups
    hosts: Hosts
    schedules: Schedules
    tasks: Tasks
    tests: Tests


class DataTableBase(BaseModel):
    ref_set: Optional[List[str]]
    type: str
    json: Union[Dict[str, Archives], Dict[str, Hosts], Dict[str, Groups], Dict[str, Schedules], Dict[str, Meta], Dict[str, Tasks], Dict[str, Tests], Templates]
    name: str
    created_by: str
    created_at: datetime
    last_edited_by: str
    last_edited_at: datetime
    url: str