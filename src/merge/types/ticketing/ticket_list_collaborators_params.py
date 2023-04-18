# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TicketListCollaboratorsParams"]


class TicketListCollaboratorsParams(TypedDict, total=False):
    cursor: str
    """The pagination cursor value."""

    expand: Literal["teams"]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_deleted_data: bool
    """Whether to include data that was marked as deleted by third party webhooks."""

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    page_size: int
    """Number of results to return per page."""
