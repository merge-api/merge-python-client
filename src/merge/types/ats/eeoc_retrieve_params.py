# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["EEOCRetrieveParams"]


class EEOCRetrieveParams(TypedDict, total=False):
    expand: List[Literal["candidate"]]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal[
        "disability_status",
        "disability_status,gender",
        "disability_status,gender,race",
        "disability_status,gender,race,veteran_status",
        "disability_status,gender,veteran_status",
        "disability_status,race",
        "disability_status,race,veteran_status",
        "disability_status,veteran_status",
        "gender",
        "gender,race",
        "gender,race,veteran_status",
        "gender,veteran_status",
        "race",
        "race,veteran_status",
        "veteran_status",
    ]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal[
        "disability_status",
        "disability_status,gender",
        "disability_status,gender,race",
        "disability_status,gender,race,veteran_status",
        "disability_status,gender,veteran_status",
        "disability_status,race",
        "disability_status,race,veteran_status",
        "disability_status,veteran_status",
        "gender",
        "gender,race",
        "gender,race,veteran_status",
        "gender,veteran_status",
        "race",
        "race,veteran_status",
        "veteran_status",
    ]
    """Which fields should be returned in non-normalized form."""
