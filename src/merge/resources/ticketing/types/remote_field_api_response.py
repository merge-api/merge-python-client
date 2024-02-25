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
    ticket: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Ticket")
    comment: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Comment")
    project: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Project")
    collection: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Collection")
    user: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="User")
    role: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Role")
    account: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Account")
    team: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Team")
    attachment: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Attachment")
    tag: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Tag")
    contact: typing.Optional[typing.List[RemoteFieldApi]] = pydantic.Field(alias="Contact")

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
