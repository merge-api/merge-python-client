# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .remote_field_api import RemoteFieldApi
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class RemoteFieldApiResponse(UniversalBaseModel):
    account: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Account")
    contact: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Contact")
    lead: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Lead")
    note: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Note")
    opportunity: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Opportunity")
    stage: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Stage")
    user: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="User")
    task: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Task")
    engagement: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Engagement")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
