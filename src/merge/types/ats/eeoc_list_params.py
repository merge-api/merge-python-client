# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EEOCListParams"]


class EEOCListParams(TypedDict, total=False):
    candidate_id: str
    """If provided, will only return EEOC info for this candidate."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    expand: Literal["candidate"]
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

    remote_fields: Literal[
        "disability_status",
        "disability_status,gender",
        "disability_status,gender,race",
        "disability_status,gender,race,veteran_status",
        "disability_status,gender,veteran_status",
        "disability_status,race",
        "disability_status,race,veteran_status",
        "disability_status,veteran_status",
        "gender",
        "gender,race",
        "gender,race,veteran_status",
        "gender,veteran_status",
        "race",
        "race,veteran_status",
        "veteran_status",
    ]
    """Deprecated. Use show_enum_origins."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    show_enum_origins: Literal[
        "disability_status",
        "disability_status,gender",
        "disability_status,gender,race",
        "disability_status,gender,race,veteran_status",
        "disability_status,gender,veteran_status",
        "disability_status,race",
        "disability_status,race,veteran_status",
        "disability_status,veteran_status",
        "gender",
        "gender,race",
        "gender,race,veteran_status",
        "gender,veteran_status",
        "race",
        "race,veteran_status",
        "veteran_status",
    ]
    """Which fields should be returned in non-normalized form."""
