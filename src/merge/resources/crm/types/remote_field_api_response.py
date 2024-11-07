# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .remote_field_api import RemoteFieldApi
import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class RemoteFieldApiResponse(UniversalBaseModel):
    account: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Account", default=None)
    contact: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Contact", default=None)
    lead: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Lead", default=None)
    note: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Note", default=None)
    opportunity: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Opportunity", default=None)
    stage: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Stage", default=None)
    user: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="User", default=None)
    task: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Task", default=None)
    engagement: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Engagement", default=None)

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
