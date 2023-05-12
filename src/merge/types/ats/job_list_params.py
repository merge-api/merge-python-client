# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    code: Optional[str]
    """If provided, will only return jobs with this code."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    expand: List[Literal["departments", "hiring_managers", "offices", "recruiters"]]
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

    offices: str
    """
    If provided, will only return jobs for this office; multiple offices can be
    separated by commas.
    """

    page_size: int
    """Number of results to return per page."""

    remote_fields: Literal["status"]
    """Deprecated. Use show_enum_origins."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    show_enum_origins: Literal["status"]
    """Which fields should be returned in non-normalized form."""

    status: Optional[Literal["ARCHIVED", "CLOSED", "DRAFT", "OPEN", "PENDING"]]
    """If provided, will only return jobs with this status.

    Options: ('OPEN', 'CLOSED', 'DRAFT', 'ARCHIVED', 'PENDING')

    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    - `DRAFT` - DRAFT
    - `ARCHIVED` - ARCHIVED
    - `PENDING` - PENDING
    """
