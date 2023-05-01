# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...types import shared
from ..._models import BaseModel

__all__ = ["ContactList"]


class ContactList(BaseModel):
    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The list's name."""

    remote_created_at: Optional[datetime]
    """When the list was created in the remote system."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the list was last updated in the remote system."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    type: Optional[str]
    """The list's type."""
