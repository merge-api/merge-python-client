# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .lead_owner import LeadOwner
from .address import Address
from .email_address import EmailAddress
from .phone_number import PhoneNumber
from .lead_converted_contact import LeadConvertedContact
from .lead_converted_account import LeadConvertedAccount
from .remote_data import RemoteData
from .remote_field import RemoteField
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Lead(UniversalBaseModel):
    """
    # The Lead Object

    ### Description

    The `Lead` object is used to represent an individual who is a potential customer.

    ### Usage Example

    TODO
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was modified by Merge.
    """

    owner: typing.Optional[LeadOwner] = pydantic.Field()
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

    addresses: typing.Optional[typing.List[Address]]
    email_addresses: typing.Optional[typing.List[EmailAddress]]
    phone_numbers: typing.Optional[typing.List[PhoneNumber]]
    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's lead was updated.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's lead was created.
    """

    converted_date: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the lead was converted.
    """

    converted_contact: typing.Optional[LeadConvertedContact] = pydantic.Field()
    """
    The contact of the converted lead.
    """

    converted_account: typing.Optional[LeadConvertedAccount] = pydantic.Field()
    """
    The account of the converted lead.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    remote_data: typing.Optional[typing.List[RemoteData]]
    remote_fields: typing.Optional[typing.List[RemoteField]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
