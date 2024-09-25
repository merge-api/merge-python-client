# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
from .remote_field_remote_field_class import RemoteFieldRemoteFieldClass
import typing
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class RemoteField(UniversalBaseModel):
    remote_field_class: RemoteFieldRemoteFieldClass
    value: typing.Optional[typing.Optional[typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
