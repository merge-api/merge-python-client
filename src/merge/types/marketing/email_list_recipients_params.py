# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["EmailListRecipientsParams"]


class EmailListRecipientsParams(TypedDict, total=False):
    cursor: str
    """The pagination cursor value."""

    include_deleted_data: bool
    """Whether to include data that was marked as deleted by third party webhooks."""

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    page_size: int
    """Number of results to return per page."""
