# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...types import shared
from ..._models import BaseModel

__all__ = ["Message"]


class Message(BaseModel):
    body: Optional[str]
    """The message's body."""

    field_mappings: Optional[object]

    from_name: Optional[str]
    """The message's from-name."""

    id: Optional[str]

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    send_date: Optional[datetime]
    """When the message was sent."""
