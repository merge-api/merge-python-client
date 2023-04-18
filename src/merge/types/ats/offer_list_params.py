# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OfferListParams"]


class OfferListParams(TypedDict, total=False):
    application_id: str
    """If provided, will only return offers for this application."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    creator_id: str
    """If provided, will only return offers created by this user."""

    cursor: str
    """The pagination cursor value."""

    expand: List[Literal["application", "creator"]]
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

    remote_fields: Literal["status"]
    """Deprecated. Use show_enum_origins."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    show_enum_origins: Literal["status"]
    """Which fields should be returned in non-normalized form."""
