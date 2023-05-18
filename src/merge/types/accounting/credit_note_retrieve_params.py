# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["CreditNoteRetrieveParams"]


class CreditNoteRetrieveParams(TypedDict, total=False):
    expand: List[Literal["line_items", "payments", "tracking_categories"]]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal["status", "status,type", "type"]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal["status", "status,type", "type"]
    """Which fields should be returned in non-normalized form."""
