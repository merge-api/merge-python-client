# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .remote_field_api import RemoteFieldApi

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RemoteFieldApiResponse(pydantic.BaseModel):
    account: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Account")
    contact: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Contact")
    lead: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Lead")
    note: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Note")
    opportunity: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Opportunity")
    stage: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Stage")
    user: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="User")
    task: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Task")
    engagement: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Engagement")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
