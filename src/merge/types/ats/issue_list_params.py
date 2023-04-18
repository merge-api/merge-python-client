# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["IssueListParams"]


class IssueListParams(TypedDict, total=False):
    account_token: str

    cursor: str
    """The pagination cursor value."""

    end_date: str
    """
    If included, will only include issues whose most recent action occurred before
    this time
    """

    end_user_organization_name: str

    first_incident_time_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    If provided, will only return issues whose first incident time was after this
    datetime.
    """

    first_incident_time_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    If provided, will only return issues whose first incident time was before this
    datetime.
    """

    include_muted: str
    """If True, will include muted issues"""

    integration_name: str

    last_incident_time_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    If provided, will only return issues whose first incident time was after this
    datetime.
    """

    last_incident_time_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    If provided, will only return issues whose first incident time was before this
    datetime.
    """

    page_size: int
    """Number of results to return per page."""

    start_date: str
    """
    If included, will only include issues whose most recent action occurred after
    this time
    """

    status: Literal["ONGOING", "RESOLVED"]
    """- `ONGOING` - ONGOING
    - `RESOLVED` - RESOLVED

    - `ONGOING` - ONGOING
    - `RESOLVED` - RESOLVED
    """
