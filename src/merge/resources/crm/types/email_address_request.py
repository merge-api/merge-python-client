# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

from ....core.datetime_utils import serialize_datetime


class EmailAddressRequest(pydantic.BaseModel):
    """
    # The EmailAddress Object
    ### Description
    The `EmailAddress` object is used to represent an entity's email address.
    ### Usage Example
    Fetch from the `GET Contact` endpoint and view their email addresses.
    """

    email_address: typing.Optional[str] = pydantic.Field(description="The email address.")
    email_address_type: typing.Optional[str] = pydantic.Field(description="The email address's type.")
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
