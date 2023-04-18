# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JournalEntryListParams"]


class JournalEntryListParams(TypedDict, total=False):
    company_id: str
    """If provided, will only return journal entries for this company."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    expand: List[Literal["company", "lines", "payments"]]
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

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    transaction_date_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    transaction_date_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""
