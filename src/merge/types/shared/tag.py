# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["Tag"]


class Tag(BaseModel):
    field_mappings: Optional[object]

    name: Optional[str]
    """The tag's name."""

    remote_data: Optional[List[Optional[Dict[str, object]]]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""
