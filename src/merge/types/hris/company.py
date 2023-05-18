# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...types import shared
from ..._models import BaseModel

__all__ = ["Company"]


class Company(BaseModel):
    display_name: Optional[str]
    """The company's display name."""

    eins: Optional[List[Optional[str]]]
    """The company's Employer Identification Numbers."""

    field_mappings: Optional[object]

    id: Optional[str]

    legal_name: Optional[str]
    """The company's legal name."""

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""
