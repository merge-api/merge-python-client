# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .remote_data import RemoteData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Account(pydantic.BaseModel):
    """
    # The Account Object

    ### Description

    The `Account` object is used to represent the account that a ticket is associated with.

    The account is a company that may be a customer. This does not represent the company that is receiving the ticket.

    ### Usage Example

    TODO
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="The datetime that this object was created by Merge."
    )
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="The datetime that this object was modified by Merge."
    )
    name: typing.Optional[str] = pydantic.Field(description="The account's name.")
    domains: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field(
        description="The account's domain names."
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted in the third party platform."
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
