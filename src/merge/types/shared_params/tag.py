# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["Tag"]


class Tag(TypedDict, total=False):
    name: Optional[str]
    """The tag's name."""

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: bool
    """Indicates whether or not this object has been deleted by third party webhooks."""
