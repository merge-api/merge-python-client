# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...types import shared
from ..._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    emails: List[str]
    """The marketing emails about this event."""

    messages: List[str]
    """The messages about this event."""

    description: Optional[str]
    """The event's description."""

    end_time: Optional[datetime]
    """When the event ends."""

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The event's name."""

    remote_created_at: Optional[datetime]
    """When the event was created in the remote system."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    start_time: Optional[datetime]
    """When the event starts."""
