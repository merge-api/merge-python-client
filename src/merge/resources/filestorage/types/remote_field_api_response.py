# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .remote_field_api import RemoteFieldApi
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class RemoteFieldApiResponse(UniversalBaseModel):
    file: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="File")
    folder: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Folder")
    drive: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Drive")
    group: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Group")
    user: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="User")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
