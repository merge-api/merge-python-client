# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmployeePayrollRunListParams"]


class EmployeePayrollRunListParams(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    employee_id: str
    """If provided, will only return employee payroll runs for this employee."""

    ended_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return employee payroll runs ended after this datetime."""

    ended_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return employee payroll runs ended before this datetime."""

    expand: Literal["employee", "employee,payroll_run", "payroll_run"]
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
    """If provided, will only return objects modified after this datetime."""

    modified_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified before this datetime."""

    page_size: int
    """Number of results to return per page."""

    payroll_run_id: str
    """If provided, will only return employee payroll runs for this employee."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    started_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    If provided, will only return employee payroll runs started after this datetime.
    """

    started_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    If provided, will only return employee payroll runs started before this
    datetime.
    """
