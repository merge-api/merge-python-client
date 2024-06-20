# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .remote_field_api import RemoteFieldApi


class RemoteFieldApiResponse(pydantic_v1.BaseModel):
    ticket: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Ticket")
    comment: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Comment")
    project: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Project")
    collection: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Collection")
    user: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="User")
    role: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Role")
    account: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Account")
    team: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Team")
    attachment: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Attachment")
    tag: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Tag")
    contact: typing.Optional[typing.List[RemoteFieldApi]] = pydantic_v1.Field(alias="Contact")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
