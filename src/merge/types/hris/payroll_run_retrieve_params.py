# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PayrollRunRetrieveParams"]


class PayrollRunRetrieveParams(TypedDict, total=False):
    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal["run_state", "run_state,run_type", "run_type"]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal["run_state", "run_state,run_type", "run_type"]
    """Which fields should be returned in non-normalized form."""
