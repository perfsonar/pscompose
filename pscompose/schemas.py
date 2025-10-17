# schemas.py is a curated version of schemas-codegen.py which is a file that was
# generated using datamodel-code-generator that creates pydantic models from just about any data source.
# In this case, the data source was psconfig-schema.json that can be found here -
# https://github.com/perfsonar/psconfig/blob/master/psconfig/perfsonar-psconfig/doc/psconfig-schema.json
# This was the command that was used
# datamodel-codegen  --input psconfig-schema.json --input-file-type jsonschema --output schemas-codegen.py

from __future__ import annotations

from enum import Enum
from ipaddress import IPv4Address, IPv6Address
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from pydantic import AnyUrl, BaseModel, Extra, Field, conint, constr


# Custom JSON type
class AnyJSON(BaseModel):
    __root__: Optional[Union[List, bool, int, float, Dict[str, Any], str]]


# Base types
class Cardinal(BaseModel):
    __root__: conint(ge=1)


class Duration(BaseModel):
    __root__: constr(
        regex=r"^P(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$"
    )


class IntegerZero(BaseModel):
    __root__: conint(ge=0)


class NameType(BaseModel):
    __root__: constr(regex=r"^[a-zA-Z0-9:._\-]+$")


class HostName(BaseModel):
    __root__: constr(
        regex=r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]{0,61}[A-Za-z0-9])\Z"
    )


class HostNamePort(BaseModel):
    __root__: constr(
        regex=r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])(:[0-9]+)?$"
    )


class IPAddress(BaseModel):
    __root__: Union[IPv4Address, IPv6Address]


class IPv6RFC2732(BaseModel):
    __root__: constr(
        regex=r"^\[(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))\](:[0-9]+)?$"
    )


class Timestamp(BaseModel):
    __root__: constr(
        regex=r"^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$"
    )


class Host(BaseModel):
    __root__: Union[HostName, IPAddress]


class TimestampAbsoluteRelative(BaseModel):
    __root__: Union[
        Timestamp,
        Duration,
        constr(
            regex=r"^@(R\d*/)?P(?:\d+(?:\.\d+)?Y)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?W)?(?:\d+(?:\.\d+)?D)?(?:T(?:\d+(?:\.\d+)?H)?(?:\d+(?:\.\d+)?M)?(?:\d+(?:\.\d+)?S)?)?$"
        ),
    ]


class URLHostPort(BaseModel):
    __root__: Union[HostNamePort, IPv6RFC2732]


# Selectors
class AddressSelectorClass(BaseModel):
    class Config:
        extra = Extra.forbid

    class_: NameType = Field(..., alias="class")
    disabled: Optional[bool] = None


class AddressSelectorNameLabel(BaseModel):
    class Config:
        extra = Extra.forbid

    name: NameType
    label: Optional[NameType] = None
    disabled: Optional[bool] = None


class AddressSelector(BaseModel):
    __root__: Union[AddressSelectorClass, AddressSelectorNameLabel]


# Enum categories
class GroupType(Enum):
    DISJOINT = "disjoint"
    LIST = "list"
    MESH = "mesh"


class ExcludesSelfScope(Enum):
    HOST = "host"
    ADDRESS = "address"
    DISABLED = "disabled"


# Core Models
class ArchiveJQTransformSpecification(BaseModel):
    class Config:
        extra = Extra.forbid

    script: Union[str, List[str]]
    output_raw: Optional[bool] = Field(None, alias="output-raw")
    args: Optional[AnyJSON] = None


class ArchiveSpecification(BaseModel):
    class Config:
        extra = Extra.forbid

    archiver: str
    data: AnyJSON
    transform: Optional[ArchiveJQTransformSpecification] = None
    ttl: Optional[Duration] = None
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")
    label: Optional[str] = None
    schema_: Optional[Cardinal] = Field(None, alias="schema")


class ContextSpecification(BaseModel):
    class Config:
        extra = Extra.forbid

    context: str
    data: AnyJSON
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


class TaskSpecification(BaseModel):
    class Config:
        extra = Extra.forbid

    scheduled_by: Optional[IntegerZero] = Field(None, alias="scheduled-by")
    group: NameType
    test: NameType
    schedule: Optional[NameType] = None
    disabled: Optional[bool] = None
    archives: Optional[List[NameType]] = None
    tools: Optional[List[str]] = None
    subtasks: Optional[List[NameType]] = None
    priority: Optional[int] = None
    reference: Optional[AnyJSON] = None
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


class TestSpecification(BaseModel):
    class Config:
        extra = Extra.forbid

    type: str
    spec: AnyJSON
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


class ScheduleSpecification(BaseModel):
    class Config:
        extra = Extra.forbid

    start: Optional[TimestampAbsoluteRelative] = None
    slip: Optional[Duration] = None
    sliprand: Optional[bool] = None
    repeat: Optional[Duration] = None
    until: Optional[TimestampAbsoluteRelative] = None
    max_runs: Optional[Cardinal] = Field(None, alias="max-runs")
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


class AddressSpecificationLabelMapItem(BaseModel):
    class Config:
        extra = Extra.forbid

    address: Host
    lead_bind_address: Optional[Host] = Field(None, alias="lead-bind-address")
    pscheduler_address: Optional[URLHostPort] = Field(None, alias="pscheduler-address")
    contexts: Optional[List[NameType]] = None
    disabled: Optional[bool] = None
    no_agent: Optional[bool] = Field(None, alias="no-agent")
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


class AddressSpecificationLabelMap(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Dict[constr(regex=r"^[a-zA-Z0-9:._\-]+$"), AddressSpecificationLabelMapItem]


class AddressSpecificationRemoteMapItem(BaseModel):
    class Config:
        extra = Extra.forbid

    address: Optional[Host] = None
    labels: Optional[AddressSpecificationLabelMap] = None
    lead_bind_address: Optional[Host] = Field(None, alias="lead-bind-address")
    pscheduler_address: Optional[URLHostPort] = Field(None, alias="pscheduler-address")
    contexts: Optional[List[NameType]] = None
    disabled: Optional[bool] = None
    no_agent: Optional[bool] = Field(None, alias="no-agent")
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


class AddressSpecificationRemoteMap(BaseModel):
    class Config:
        extra = Extra.forbid

    __root__: Dict[constr(regex=r"^[a-zA-Z0-9:._\-]+$"), AddressSpecificationRemoteMapItem]


class ExcludesAddressPair(BaseModel):
    class Config:
        extra = Extra.forbid

    local_address: AddressSelector = Field(..., alias="local-address")
    target_addresses: List[AddressSelector] = Field(..., alias="target-addresses")


class ExcludesAddressPairList(BaseModel):
    __root__: List[ExcludesAddressPair]


class GroupListSpecification(BaseModel):
    class Config:
        extra = Extra.forbid
        use_enum_values = True

    default_address_label: Optional[str] = Field(None, alias="default-address-label")
    type: GroupType
    addresses: List[AddressSelector]
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


class GroupDisjointSpecification(BaseModel):
    class Config:
        extra = Extra.forbid
        use_enum_values = True

    default_address_label: Optional[str] = Field(None, alias="default-address-label")
    unidirectional: Optional[bool] = None
    type: GroupType
    a_addresses: List[AddressSelector] = Field(..., alias="a-addresses")
    b_addresses: List[AddressSelector] = Field(..., alias="b-addresses")
    excludes_self: Optional[ExcludesSelfScope] = Field(None, alias="excludes-self")
    excludes: Optional[ExcludesAddressPairList] = None
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


class GroupMeshSpecification(BaseModel):
    class Config:
        extra = Extra.forbid
        use_enum_values = True

    default_address_label: Optional[str] = Field(None, alias="default-address-label")
    type: GroupType
    addresses: List[AddressSelector]
    excludes_self: Optional[ExcludesSelfScope] = Field(None, alias="excludes-self")
    excludes: Optional[ExcludesAddressPairList] = None
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


GroupSpecification = Union[
    GroupDisjointSpecification,
    GroupListSpecification,
    GroupMeshSpecification,
]


class AddressSpecification(BaseModel):
    class Config:
        extra = Extra.forbid

    address: Host
    host: Optional[NameType] = None
    labels: Optional[AddressSpecificationLabelMap] = None
    remote_addresses: Optional[AddressSpecificationRemoteMap] = Field(
        None, alias="remote-addresses"
    )
    lead_bind_address: Optional[Host] = Field(None, alias="lead-bind-address")
    pscheduler_address: Optional[URLHostPort] = Field(None, alias="pscheduler-address")
    contexts: Optional[List[NameType]] = None
    tags: Optional[List[str]] = None
    disabled: Optional[bool] = None
    no_agent: Optional[bool] = Field(None, alias="no-agent")
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


# TODO: I think it shouldn't be Dict[constr(regex=....), ]
# because the key in the dict is going to be the uuid. So, it should be Dict[str, ...]?
# This will be useful only for templates and when retrieving the json, it'll be generated in the API endpoint
class pSConfigSchema(BaseModel):
    class Config:
        extra = Extra.forbid

    addresses: Dict[constr(regex=r"^[a-zA-Z0-9:._\-]+$"), AddressSpecification]
    archives: Optional[Dict[constr(regex=r"^[a-zA-Z0-9:._\-]+$"), ArchiveSpecification]] = None
    contexts: Optional[Dict[constr(regex=r"^[a-zA-Z0-9:._\-]+$"), ContextSpecification]] = None
    groups: Dict[constr(regex=r"^[a-zA-Z0-9:._\-]+$"), GroupSpecification]
    includes: Optional[List[AnyUrl]] = None
    schedules: Optional[Dict[constr(regex=r"^[a-zA-Z0-9:._\-]+$"), ScheduleSpecification]] = None
    tasks: Dict[constr(regex=r"^[a-zA-Z0-9:._\-]+$"), TaskSpecification]
    tests: Dict[constr(regex=r"^[a-zA-Z0-9:._\-]+$"), TestSpecification]
    field_meta: Optional[AnyJSON] = Field(None, alias="_meta")


class DataTableBase(BaseModel):
    ref_set: Optional[List[str]]
    type: str
    json_data: Union[
        AddressSpecification,
        ArchiveSpecification,
        ContextSpecification,
        GroupSpecification,
        ScheduleSpecification,
        TaskSpecification,
        TestSpecification,
        pSConfigSchema,  # Full schema
    ] = Field(None, alias="json")
    name: str = Field(..., min_length=1)
    created_by: str
    created_at: Optional[datetime] = None
    last_edited_by: str
    last_edited_at: Optional[datetime] = None
    url: Optional[str] = None

    class Config:
        orm_mode = True


class DataTableUpdate(BaseModel):
    ref_set: Optional[List[str]] = None
    type: Optional[str] = None
    json_data: Optional[
        Union[
            AddressSpecification,
            ArchiveSpecification,
            ContextSpecification,
            GroupSpecification,
            ScheduleSpecification,
            TaskSpecification,
            TestSpecification,
            pSConfigSchema,
        ]
    ] = Field(None, alias="json")
    name: Optional[str] = None
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    last_edited_by: Optional[str] = None
    last_edited_at: Optional[datetime] = None
    url: Optional[str] = None


pSConfigSchema.update_forward_refs()
