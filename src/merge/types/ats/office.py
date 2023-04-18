# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel

__all__ = ["Office"]


class Office(BaseModel):
    field_mappings: Optional[object]

    id: Optional[str]

    location: Optional[str]
    """The office's location."""

    name: Optional[str]
    """The office's name."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""
