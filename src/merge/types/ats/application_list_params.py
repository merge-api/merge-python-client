# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    candidate_id: str
    """If provided, will only return applications for this candidate."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    credited_to_id: str
    """If provided, will only return applications credited to this user."""

    current_stage_id: str
    """If provided, will only return applications at this interview stage."""

    cursor: str
    """The pagination cursor value."""

    expand: List[Literal["candidate", "credited_to", "current_stage", "job", "reject_reason"]]
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

    job_id: str
    """If provided, will only return applications for this job."""

    modified_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified after this datetime."""

    modified_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified before this datetime."""

    page_size: int
    """Number of results to return per page."""

    reject_reason_id: str
    """If provided, will only return applications with this reject reason."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    source: Optional[str]
    """If provided, will only return applications with this source."""
