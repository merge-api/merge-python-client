# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SyncStatusListParams"]


class SyncStatusListParams(TypedDict, total=False):
    cursor: str
    """The pagination cursor value."""

    page_size: int
    """Number of results to return per page."""
