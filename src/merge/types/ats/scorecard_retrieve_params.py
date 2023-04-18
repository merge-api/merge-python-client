# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ScorecardRetrieveParams"]


class ScorecardRetrieveParams(TypedDict, total=False):
    expand: Literal[
        "application",
        "application,interview",
        "application,interview,interviewer",
        "application,interviewer",
        "interview",
        "interview,interviewer",
        "interviewer",
    ]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal["overall_recommendation"]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal["overall_recommendation"]
    """Which fields should be returned in non-normalized form."""
