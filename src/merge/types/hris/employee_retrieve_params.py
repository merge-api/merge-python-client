# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["EmployeeRetrieveParams"]


class EmployeeRetrieveParams(TypedDict, total=False):
    expand: List[
        Literal["company", "employments", "groups", "home_location", "manager", "pay_group", "team", "work_location"]
    ]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    include_sensitive_fields: bool
    """
    Whether to include sensitive fields (such as social security numbers) in the
    response.
    """

    remote_fields: Literal[
        "employment_status",
        "employment_status,ethnicity",
        "employment_status,ethnicity,gender",
        "employment_status,ethnicity,gender,marital_status",
        "employment_status,ethnicity,marital_status",
        "employment_status,gender",
        "employment_status,gender,marital_status",
        "employment_status,marital_status",
        "ethnicity",
        "ethnicity,gender",
        "ethnicity,gender,marital_status",
        "ethnicity,marital_status",
        "gender",
        "gender,marital_status",
        "marital_status",
    ]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal[
        "employment_status",
        "employment_status,ethnicity",
        "employment_status,ethnicity,gender",
        "employment_status,ethnicity,gender,marital_status",
        "employment_status,ethnicity,marital_status",
        "employment_status,gender",
        "employment_status,gender,marital_status",
        "employment_status,marital_status",
        "ethnicity",
        "ethnicity,gender",
        "ethnicity,gender,marital_status",
        "ethnicity,marital_status",
        "gender",
        "gender,marital_status",
        "marital_status",
    ]
    """Which fields should be returned in non-normalized form."""
