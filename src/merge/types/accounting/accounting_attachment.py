# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel

__all__ = ["AccountingAttachment"]


class AccountingAttachment(BaseModel):
    company: Optional[str]
    """The company the accounting attachment belongs to."""

    field_mappings: Optional[object]

    file_name: Optional[str]
    """The attachment's name."""

    file_url: Optional[str]
    """The attachment's url."""

    id: Optional[str]

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""
