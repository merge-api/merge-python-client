# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .accounting_phone_number_request import AccountingPhoneNumberRequest
from .contact_request_addresses_item import ContactRequestAddressesItem
from .contact_request_status import ContactRequestStatus


class ContactRequest(UniversalBaseModel):
    """
    # The Contact Object

    ### Description

    A `Contact` is an individual or business entity to which products and services are sold to or purchased from. The `Contact` model contains both Customers, in which products and services are sold to, and Vendors (or Suppliers), in which products and services are purchased from.

    - A `Contact` is a Vendor/Supplier if the `is_supplier` property is true.
    - A `Contact` is a customer if the `is_customer` property is true.

    ### Usage Example

    Fetch from the `LIST Contacts` endpoint and view a company's contacts.
    """

    name: typing.Optional[str] = pydantic.Field()
    """
    The contact's name.
    """

    is_supplier: typing.Optional[bool] = pydantic.Field()
    """
    Whether the contact is a supplier.
    """

    is_customer: typing.Optional[bool] = pydantic.Field()
    """
    Whether the contact is a customer.
    """

    email_address: typing.Optional[str] = pydantic.Field()
    """
    The contact's email address.
    """

    tax_number: typing.Optional[str] = pydantic.Field()
    """
    The contact's tax number.
    """

    status: typing.Optional[ContactRequestStatus] = pydantic.Field()
    """
    The contact's status
    
    - `ACTIVE` - ACTIVE
    - `ARCHIVED` - ARCHIVED
    """

    currency: typing.Optional[str] = pydantic.Field()
    """
    The currency the contact's transactions are in.
    """

    company: typing.Optional[str] = pydantic.Field()
    """
    The company the contact belongs to.
    """

    addresses: typing.Optional[typing.List[typing.Optional[ContactRequestAddressesItem]]] = pydantic.Field()
    """
    `Address` object IDs for the given `Contacts` object.
    """

    phone_numbers: typing.Optional[typing.List[AccountingPhoneNumberRequest]] = pydantic.Field()
    """
    `AccountingPhoneNumber` object for the given `Contacts` object.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
