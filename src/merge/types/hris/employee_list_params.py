# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmployeeListParams"]


class EmployeeListParams(TypedDict, total=False):
    company_id: str
    """If provided, will only return employees for this company."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    display_full_name: Optional[str]
    """If provided, will only return employees with this display name."""

    employment_status: Optional[Literal["ACTIVE", "INACTIVE", "PENDING"]]
    """If provided, will only return employees with this employment status.

    - `ACTIVE` - ACTIVE
    - `PENDING` - PENDING
    - `INACTIVE` - INACTIVE
    """

    expand: List[
        Literal["company", "employments", "groups", "home_location", "manager", "pay_group", "team", "work_location"]
    ]
    """Which relations should be returned in expanded form.

    Multiple relation names should be comma separated without spaces.
    """

    first_name: Optional[str]
    """If provided, will only return employees with this first name."""

    groups: str
    """
    If provided, will only return employees matching the group ids; multiple groups
    can be separated by commas.
    """

    include_deleted_data: bool
    """Whether to include data that was marked as deleted by third party webhooks."""

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

    last_name: Optional[str]
    """If provided, will only return employees with this last name."""

    manager_id: str
    """If provided, will only return employees for this manager."""

    modified_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified after this datetime."""

    modified_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified before this datetime."""

    page_size: int
    """Number of results to return per page."""

    pay_group_id: str
    """If provided, will only return employees for this pay group"""

    personal_email: Optional[str]
    """If provided, will only return Employees with this personal email"""

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

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

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

    team_id: str
    """If provided, will only return employees for this team."""

    work_email: Optional[str]
    """If provided, will only return Employees with this work email"""

    work_location_id: str
    """If provided, will only return employees for this location."""
