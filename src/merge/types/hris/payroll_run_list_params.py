# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PayrollRunListParams"]


class PayrollRunListParams(TypedDict, total=False):
    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    ended_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return payroll runs ended after this datetime."""

    ended_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return payroll runs ended before this datetime."""

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

    page_size: int
    """Number of results to return per page."""

    remote_fields: Literal["run_state", "run_state,run_type", "run_type"]
    """Deprecated. Use show_enum_origins."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    run_type: Optional[Literal["CORRECTION", "OFF_CYCLE", "REGULAR", "SIGN_ON_BONUS", "TERMINATION"]]
    """If provided, will only return PayrollRun's with this status.

    Options: ('REGULAR', 'OFF_CYCLE', 'CORRECTION', 'TERMINATION', 'SIGN_ON_BONUS')

    - `REGULAR` - REGULAR
    - `OFF_CYCLE` - OFF_CYCLE
    - `CORRECTION` - CORRECTION
    - `TERMINATION` - TERMINATION
    - `SIGN_ON_BONUS` - SIGN_ON_BONUS
    """

    show_enum_origins: Literal["run_state", "run_state,run_type", "run_type"]
    """Which fields should be returned in non-normalized form."""

    started_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return payroll runs started after this datetime."""

    started_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return payroll runs started before this datetime."""
