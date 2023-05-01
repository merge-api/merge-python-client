# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["UserRetrieveParams"]


class UserRetrieveParams(TypedDict, total=False):
    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal["access_role"]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal["access_role"]
    """Which fields should be returned in non-normalized form."""
