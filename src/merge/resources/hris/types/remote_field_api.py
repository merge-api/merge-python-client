# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .advanced_metadata import AdvancedMetadata
from .remote_endpoint_info import RemoteEndpointInfo
from .remote_field_api_coverage import RemoteFieldApiCoverage


class RemoteFieldApi(UncheckedBaseModel):
    schema_: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field(alias="schema")
    remote_key_name: str
    remote_endpoint_info: RemoteEndpointInfo
    example_values: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    advanced_metadata: typing.Optional[AdvancedMetadata] = None
    coverage: typing.Optional[RemoteFieldApiCoverage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
