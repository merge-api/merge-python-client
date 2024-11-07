# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .contact_status import ContactStatus
from .contact_addresses_item import ContactAddressesItem
from .accounting_phone_number import AccountingPhoneNumber
from .remote_data import RemoteData
from .remote_field import RemoteField
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Contact(UniversalBaseModel):
    """
    # The Contact Object

    ### Description

    A `Contact` is an individual or business entity to which products and services are sold to or purchased from. The `Contact` model contains both Customers, in which products and services are sold to, and Vendors (or Suppliers), in which products and services are purchased from.

    - A `Contact` is a Vendor/Supplier if the `is_supplier` property is true.
    - A `Contact` is a customer if the `is_customer` property is true.

    ### Usage Example

    Fetch from the `LIST Contacts` endpoint and view a company's contacts.
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

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The contact's name.
    """

    is_supplier: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the contact is a supplier.
    """

    is_customer: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the contact is a customer.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The contact's email address.
    """

    tax_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The contact's tax number.
    """

    status: typing.Optional[ContactStatus] = pydantic.Field(default=None)
    """
    The contact's status
    
    - `ACTIVE` - ACTIVE
    - `ARCHIVED` - ARCHIVED
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency the contact's transactions are in.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the third party's contact was updated.
    """

    company: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company the contact belongs to.
    """

    addresses: typing.Optional[typing.List[typing.Optional[ContactAddressesItem]]] = pydantic.Field(default=None)
    """
    `Address` object IDs for the given `Contacts` object.
    """

    phone_numbers: typing.Optional[typing.List[AccountingPhoneNumber]] = pydantic.Field(default=None)
    """
    `AccountingPhoneNumber` object for the given `Contacts` object.
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
