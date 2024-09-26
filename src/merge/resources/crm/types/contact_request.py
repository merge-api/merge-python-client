# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .contact_request_account import ContactRequestAccount
from .contact_request_owner import ContactRequestOwner
from .address_request import AddressRequest
from .email_address_request import EmailAddressRequest
from .phone_number_request import PhoneNumberRequest
import datetime as dt
from .remote_field_request import RemoteFieldRequest
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class ContactRequest(UniversalBaseModel):
    """
    # The Contact Object

    ### Description

    The `Contact` object is used to represent an existing point of contact at a company in a CRM system.

    ### Usage Example

    TODO
    """

    first_name: typing.Optional[str] = pydantic.Field()
    """
    The contact's first name.
    """

    last_name: typing.Optional[str] = pydantic.Field()
    """
    The contact's last name.
    """

    account: typing.Optional[ContactRequestAccount] = pydantic.Field()
    """
    The contact's account.
    """

    owner: typing.Optional[ContactRequestOwner] = pydantic.Field()
    """
    The contact's owner.
    """

    addresses: typing.Optional[typing.List[AddressRequest]]
    email_addresses: typing.Optional[typing.List[EmailAddressRequest]]
    phone_numbers: typing.Optional[typing.List[PhoneNumberRequest]]
    last_activity_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the contact's last activity occurred.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
