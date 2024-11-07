# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .account_owner import AccountOwner
from .address import Address
from .phone_number import PhoneNumber
from .remote_data import RemoteData
from .remote_field import RemoteField
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Account(UniversalBaseModel):
    """
    # The Account Object

    ### Description

    The `Account` object is used to represent a company in a CRM system.

    ### Usage Example

    TODO
    """

    id: typing.Optional[str] = None
    remote_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was modified by Merge.
    """

    owner: typing.Optional[AccountOwner] = pydantic.Field(default=None)
    """
    The account's owner.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account's name.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account's description.
    """

    industry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account's industry.
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account's website.
    """

    number_of_employees: typing.Optional[int] = pydantic.Field(default=None)
    """
    The account's number of employees.
    """

    addresses: typing.Optional[typing.List[Address]] = None
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    last_activity_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The last date (either most recent or furthest in the future) of when an activity occurs in an account.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the CRM system account data was last modified by a user with a login.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the third party's account was created.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    remote_data: typing.Optional[typing.List[RemoteData]] = None
    remote_fields: typing.Optional[typing.List[RemoteField]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
