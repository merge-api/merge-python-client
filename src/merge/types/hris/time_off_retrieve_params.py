# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["TimeOffRetrieveParams"]


class TimeOffRetrieveParams(TypedDict, total=False):
    expand: List[Literal["approver", "employee"]]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal[
        "request_type",
        "request_type,status",
        "request_type,status,units",
        "request_type,units",
        "status",
        "status,units",
        "units",
    ]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal[
        "request_type",
        "request_type,status",
        "request_type,status,units",
        "request_type,units",
        "status",
        "status,units",
        "units",
    ]
    """Which fields should be returned in non-normalized form."""
