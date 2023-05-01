# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Lead", "EmailAddress", "PhoneNumber", "RemoteField"]


class EmailAddress(BaseModel):
    email_address: Optional[str]
    """The email address."""

    email_address_type: Optional[Literal["PERSONAL", "WORK", "OTHER"]]
    """
    - `PERSONAL` - PERSONAL
    - `WORK` - WORK
    - `OTHER` - OTHER
    """

    value: Optional[str]
    """The email address."""


class PhoneNumber(BaseModel):
    phone_number: Optional[str]
    """The phone number."""

    phone_number_type: Optional[Literal["HOME", "WORK", "MOBILE", "SKYPE", "OTHER"]]
    """
    - `HOME` - HOME
    - `WORK` - WORK
    - `MOBILE` - MOBILE
    - `SKYPE` - SKYPE
    - `OTHER` - OTHER
    """

    value: Optional[str]
    """The phone number."""


class RemoteField(BaseModel):
    remote_field_class: shared.RemoteFieldClass

    value: Optional[object]


class Lead(BaseModel):
    addresses: Optional[List[shared.Address]]

    company: Optional[str]
    """The lead's company."""

    converted_account: Optional[str]
    """The account of the converted lead."""

    converted_contact: Optional[str]
    """The contact of the converted lead."""

    converted_date: Optional[datetime]
    """When the lead was converted."""

    email_addresses: Optional[List[EmailAddress]]

    field_mappings: Optional[object]

    first_name: Optional[str]
    """The lead's first name."""

    id: Optional[str]

    last_name: Optional[str]
    """The lead's last name."""

    lead_source: Optional[str]
    """The lead's source."""

    owner: Optional[str]
    """The lead's owner."""

    phone_numbers: Optional[List[PhoneNumber]]

    remote_created_at: Optional[datetime]
    """When the third party's lead was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_fields: Optional[List[RemoteField]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the third party's lead was updated."""

    remote_was_deleted: Optional[bool]

    title: Optional[str]
    """The lead's title."""
