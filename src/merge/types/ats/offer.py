# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Offer"]


class Offer(BaseModel):
    application: Optional[str]
    """The application who is receiving the offer."""

    closed_at: Optional[datetime]
    """When the offer was closed."""

    creator: Optional[str]
    """The user who created the offer."""

    field_mappings: Optional[object]

    id: Optional[str]

    remote_created_at: Optional[datetime]
    """When the third party's offer was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    sent_at: Optional[datetime]
    """When the offer was sent."""

    start_date: Optional[datetime]
    """The employment start date on the offer."""

    status: Optional[
        Literal[
            "DRAFT", "APPROVAL-SENT", "APPROVED", "SENT", "SENT-MANUALLY", "OPENED", "DENIED", "SIGNED", "DEPRECATED"
        ]
    ]
    """
    - `DRAFT` - DRAFT
    - `APPROVAL-SENT` - APPROVAL-SENT
    - `APPROVED` - APPROVED
    - `SENT` - SENT
    - `SENT-MANUALLY` - SENT-MANUALLY
    - `OPENED` - OPENED
    - `DENIED` - DENIED
    - `SIGNED` - SIGNED
    - `DEPRECATED` - DEPRECATED
    """
