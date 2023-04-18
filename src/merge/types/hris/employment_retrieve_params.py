# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["EmploymentRetrieveParams"]


class EmploymentRetrieveParams(TypedDict, total=False):
    expand: Literal["employee", "employee,pay_group", "pay_group"]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    remote_fields: Literal[
        "employment_type",
        "employment_type,flsa_status",
        "employment_type,flsa_status,pay_frequency",
        "employment_type,flsa_status,pay_frequency,pay_period",
        "employment_type,flsa_status,pay_period",
        "employment_type,pay_frequency",
        "employment_type,pay_frequency,pay_period",
        "employment_type,pay_period",
        "flsa_status",
        "flsa_status,pay_frequency",
        "flsa_status,pay_frequency,pay_period",
        "flsa_status,pay_period",
        "pay_frequency",
        "pay_frequency,pay_period",
        "pay_period",
    ]
    """Deprecated. Use show_enum_origins."""

    show_enum_origins: Literal[
        "employment_type",
        "employment_type,flsa_status",
        "employment_type,flsa_status,pay_frequency",
        "employment_type,flsa_status,pay_frequency,pay_period",
        "employment_type,flsa_status,pay_period",
        "employment_type,pay_frequency",
        "employment_type,pay_frequency,pay_period",
        "employment_type,pay_period",
        "flsa_status",
        "flsa_status,pay_frequency",
        "flsa_status,pay_frequency,pay_period",
        "flsa_status,pay_period",
        "pay_frequency",
        "pay_frequency,pay_period",
        "pay_period",
    ]
    """Which fields should be returned in non-normalized form."""
