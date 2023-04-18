# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Candidate", "PhoneNumber", "EmailAddress", "URL"]


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


class URL(BaseModel):
    url_type: Optional[Literal["PERSONAL", "COMPANY", "PORTFOLIO", "BLOG", "SOCIAL_MEDIA", "OTHER", "JOB_POSTING"]]
    """
    - `PERSONAL` - PERSONAL
    - `COMPANY` - COMPANY
    - `PORTFOLIO` - PORTFOLIO
    - `BLOG` - BLOG
    - `SOCIAL_MEDIA` - SOCIAL_MEDIA
    - `OTHER` - OTHER
    - `JOB_POSTING` - JOB_POSTING
    """

    value: Optional[str]
    """The site's url."""


class Candidate(BaseModel):
    applications: Optional[List[Optional[str]]]
    """Array of `Application` object IDs."""

    attachments: Optional[List[Optional[str]]]
    """Array of `Attachment` object IDs."""

    can_email: Optional[bool]
    """Whether or not the candidate can be emailed."""

    company: Optional[str]
    """The candidate's current company."""

    email_addresses: Optional[List[EmailAddress]]

    field_mappings: Optional[object]

    first_name: Optional[str]
    """The candidate's first name."""

    id: Optional[str]

    is_private: Optional[bool]
    """Whether or not the candidate is private."""

    last_interaction_at: Optional[datetime]
    """When the most recent interaction with the candidate occurred."""

    last_name: Optional[str]
    """The candidate's last name."""

    locations: Optional[List[Optional[str]]]
    """The candidate's locations."""

    phone_numbers: Optional[List[PhoneNumber]]

    remote_created_at: Optional[datetime]
    """When the third party's candidate was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the third party's candidate was updated."""

    remote_was_deleted: Optional[bool]

    tags: Optional[List[Optional[str]]]
    """Array of `Tag` names as strings."""

    title: Optional[str]
    """The candidate's current title."""

    urls: Optional[List[URL]]
