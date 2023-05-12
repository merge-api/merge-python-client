# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmploymentListParams"]


class EmploymentListParams(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    employee_id: str
    """If provided, will only return employments for this employee."""

    expand: List[Literal["employee", "pay_group"]]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    include_deleted_data: bool
    """Whether to include data that was marked as deleted by third party webhooks."""

    include_remote_data: bool
    """
    Whether to include the original data Merge fetched from the third-party to
    produce these models.
    """

    modified_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    If provided, only objects synced by Merge after this date time will be returned.
    """

    modified_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    If provided, only objects synced by Merge before this date time will be
    returned.
    """

    order_by: Literal["-effective_date", "effective_date"]
    """Overrides the default ordering for this endpoint."""

    page_size: int
    """Number of results to return per page."""

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

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

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
