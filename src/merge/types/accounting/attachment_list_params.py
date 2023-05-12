# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AttachmentListParams"]


class AttachmentListParams(TypedDict, total=False):
    company_id: str
    """If provided, will only return accounting attachments for this company."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

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

    remote_id: Optional[str]
    """The API provider's ID for the given object."""
