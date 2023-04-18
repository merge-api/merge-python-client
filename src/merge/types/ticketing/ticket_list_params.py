# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TicketListParams"]


class TicketListParams(TypedDict, total=False):
    account_id: str
    """If provided, will only return tickets for this account."""

    assignee_ids: str
    """
    If provided, will only return tickets assigned to the assignee_ids; multiple
    assignee_ids can be separated by commas.
    """

    collection_ids: str
    """
    If provided, will only return tickets assigned to the collection_ids; multiple
    collection_ids can be separated by commas.
    """

    completed_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return tickets completed after this datetime."""

    completed_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return tickets completed before this datetime."""

    contact_id: str
    """If provided, will only return tickets for this contact."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created after this datetime."""

    created_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects created before this datetime."""

    cursor: str
    """The pagination cursor value."""

    due_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return tickets due after this datetime."""

    due_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """If provided, will only return tickets due before this datetime."""

    expand: List[
        Literal["account", "assignees", "attachments", "collections", "contact", "creator", "parent_ticket", "project"]
    ]
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

    include_remote_fields: bool
    """
    Whether to include all remote fields, including fields that Merge did not map to
    common models, in a normalized format.
    """

    modified_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified after this datetime."""

    modified_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """If provided, will only return objects modified before this datetime."""

    page_size: int
    """Number of results to return per page."""

    parent_ticket_id: str
    """If provided, will only return sub tickets of the parent_ticket_id."""

    priority: Optional[Literal["HIGH", "LOW", "NORMAL", "URGENT"]]
    """If provided, will only return tickets of this priority.

    - `URGENT` - URGENT
    - `HIGH` - HIGH
    - `NORMAL` - NORMAL
    - `LOW` - LOW
    """

    project_id: str
    """If provided, will only return tickets for this project."""

    remote_created_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    If provided, will only return tickets created in the third party platform after
    this datetime.
    """

    remote_created_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    If provided, will only return tickets created in the third party platform before
    this datetime.
    """

    remote_fields: Literal[
        "priority",
        "priority,status",
        "priority,status,ticket_type",
        "priority,ticket_type",
        "status",
        "status,ticket_type",
        "ticket_type",
    ]
    """Deprecated. Use show_enum_origins."""

    remote_id: Optional[str]
    """The API provider's ID for the given object."""

    remote_updated_after: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    If provided, will only return tickets updated in the third party platform after
    this datetime.
    """

    remote_updated_before: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    If provided, will only return tickets updated in the third party platform before
    this datetime.
    """

    show_enum_origins: Literal[
        "priority",
        "priority,status",
        "priority,status,ticket_type",
        "priority,ticket_type",
        "status",
        "status,ticket_type",
        "ticket_type",
    ]
    """Which fields should be returned in non-normalized form."""

    status: Optional[Literal["CLOSED", "IN_PROGRESS", "ON_HOLD", "OPEN"]]
    """If provided, will only return tickets of this status.

    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    - `IN_PROGRESS` - IN_PROGRESS
    - `ON_HOLD` - ON_HOLD
    """

    tags: str
    """
    If provided, will only return tickets matching the tags; multiple tags can be
    separated by commas.
    """

    ticket_type: Optional[str]
    """If provided, will only return tickets of this type."""
