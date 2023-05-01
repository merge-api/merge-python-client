# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel

__all__ = ["TicketingUser"]


class TicketingUser(BaseModel):
    avatar: Optional[str]
    """The user's avatar picture."""

    email_address: Optional[str]
    """The user's email address."""

    field_mappings: Optional[object]

    id: Optional[str]

    is_active: Optional[bool]
    """Whether or not the user is active."""

    name: Optional[str]
    """The user's name."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    teams: Optional[List[Optional[str]]]
