# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["MarketingEmail"]


class MarketingEmail(BaseModel):
    campaigns: List[str]
    """The campaigns receiving this marketing email."""

    body: Optional[str]
    """The marketing email's body."""

    field_mappings: Optional[object]

    from_email: Optional[str]
    """The marketing email's from email."""

    from_name: Optional[str]
    """The marketing email's from name."""

    html_body: Optional[str]
    """The marketing email's html body."""

    id: Optional[str]

    name: Optional[str]
    """The marketing email's name."""

    preview: Optional[str]
    """The marketing email's preview."""

    remote_created_at: Optional[datetime]
    """When the marketing email was created in the remote system."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the marketing email was last updated in the remote system."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    reply_to: Optional[str]
    """The marketing email's reply-to."""

    send_date: Optional[datetime]
    """When the marketing email was sent."""

    status: Optional[Literal["DRAFT", "QUEUED", "SENT"]]
    """
    - `DRAFT` - DRAFT
    - `QUEUED` - QUEUED
    - `SENT` - SENT
    """

    subject: Optional[str]
    """The marketing email's subject."""

    template: Optional[str]
    """The marketing email's template."""
