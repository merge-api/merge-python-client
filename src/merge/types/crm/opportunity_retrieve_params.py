# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["OpportunityRetrieveParams"]


class OpportunityRetrieveParams(TypedDict, total=False):
    expand: List[Literal["account", "owner", "stage"]]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    include_remote_fields: bool
    """
    Whether to include all remote fields, including fields that Merge did not map to
    common models, in a normalized format.
    """

    remote_fields: Literal["status"]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal["status"]
    """Which fields should be returned in non-normalized form."""
