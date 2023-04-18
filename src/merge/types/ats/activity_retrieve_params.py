# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ActivityRetrieveParams"]


class ActivityRetrieveParams(TypedDict, total=False):
    expand: List[Literal["user"]]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal["activity_type", "activity_type,visibility", "visibility"]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal["activity_type", "activity_type,visibility", "visibility"]
    """Which fields should be returned in non-normalized form."""
