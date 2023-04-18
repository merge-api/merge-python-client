# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...types import shared
from ..._models import BaseModel

__all__ = ["Campaign"]


class Campaign(BaseModel):
    emails_sent: Optional[int]
    """The campaign's number of emails sent."""

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The campaign's name."""

    remote_created_at: Optional[datetime]
    """When the campaign was created in the remote system."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    unique_opens: Optional[int]
    """The campaign's unique opens."""
