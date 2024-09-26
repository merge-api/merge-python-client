# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
from .lead_request_owner import LeadRequestOwner
import pydantic
from .address_request import AddressRequest
from .email_address_request import EmailAddressRequest
from .phone_number_request import PhoneNumberRequest
import datetime as dt
from .lead_request_converted_contact import LeadRequestConvertedContact
from .lead_request_converted_account import LeadRequestConvertedAccount
from .remote_field_request import RemoteFieldRequest
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class LeadRequest(UniversalBaseModel):
    """
    # The Lead Object

    ### Description

    The `Lead` object is used to represent an individual who is a potential customer.

    ### Usage Example

    TODO
    """

    owner: typing.Optional[LeadRequestOwner] = pydantic.Field()
    """
    The lead's owner.
    """

    lead_source: typing.Optional[str] = pydantic.Field()
    """
    The lead's source.
    """

    title: typing.Optional[str] = pydantic.Field()
    """
    The lead's title.
    """

    company: typing.Optional[str] = pydantic.Field()
    """
    The lead's company.
    """

    first_name: typing.Optional[str] = pydantic.Field()
    """
    The lead's first name.
    """

    last_name: typing.Optional[str] = pydantic.Field()
    """
    The lead's last name.
    """

    addresses: typing.Optional[typing.List[AddressRequest]]
    email_addresses: typing.Optional[typing.List[EmailAddressRequest]]
    phone_numbers: typing.Optional[typing.List[PhoneNumberRequest]]
    converted_date: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the lead was converted.
    """

    converted_contact: typing.Optional[LeadRequestConvertedContact] = pydantic.Field()
    """
    The contact of the converted lead.
    """

    converted_account: typing.Optional[LeadRequestConvertedAccount] = pydantic.Field()
    """
    The account of the converted lead.
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
