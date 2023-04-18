# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
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

    expand: Literal[
        "account",
        "account,contact",
        "account,contact,creator",
        "account,contact,creator,parent_ticket",
        "account,contact,parent_ticket",
        "account,creator",
        "account,creator,parent_ticket",
        "account,parent_ticket",
        "assignees",
        "assignees,account",
        "assignees,account,contact",
        "assignees,account,contact,creator",
        "assignees,account,contact,creator,parent_ticket",
        "assignees,account,contact,parent_ticket",
        "assignees,account,creator",
        "assignees,account,creator,parent_ticket",
        "assignees,account,parent_ticket",
        "assignees,collections",
        "assignees,collections,account",
        "assignees,collections,account,contact",
        "assignees,collections,account,contact,creator",
        "assignees,collections,account,contact,creator,parent_ticket",
        "assignees,collections,account,contact,parent_ticket",
        "assignees,collections,account,creator",
        "assignees,collections,account,creator,parent_ticket",
        "assignees,collections,account,parent_ticket",
        "assignees,collections,contact",
        "assignees,collections,contact,creator",
        "assignees,collections,contact,creator,parent_ticket",
        "assignees,collections,contact,parent_ticket",
        "assignees,collections,creator",
        "assignees,collections,creator,parent_ticket",
        "assignees,collections,parent_ticket",
        "assignees,collections,project",
        "assignees,collections,project,account",
        "assignees,collections,project,account,contact",
        "assignees,collections,project,account,contact,creator",
        "assignees,collections,project,account,contact,creator,parent_ticket",
        "assignees,collections,project,account,contact,parent_ticket",
        "assignees,collections,project,account,creator",
        "assignees,collections,project,account,creator,parent_ticket",
        "assignees,collections,project,account,parent_ticket",
        "assignees,collections,project,contact",
        "assignees,collections,project,contact,creator",
        "assignees,collections,project,contact,creator,parent_ticket",
        "assignees,collections,project,contact,parent_ticket",
        "assignees,collections,project,creator",
        "assignees,collections,project,creator,parent_ticket",
        "assignees,collections,project,parent_ticket",
        "assignees,contact",
        "assignees,contact,creator",
        "assignees,contact,creator,parent_ticket",
        "assignees,contact,parent_ticket",
        "assignees,creator",
        "assignees,creator,parent_ticket",
        "assignees,parent_ticket",
        "assignees,project",
        "assignees,project,account",
        "assignees,project,account,contact",
        "assignees,project,account,contact,creator",
        "assignees,project,account,contact,creator,parent_ticket",
        "assignees,project,account,contact,parent_ticket",
        "assignees,project,account,creator",
        "assignees,project,account,creator,parent_ticket",
        "assignees,project,account,parent_ticket",
        "assignees,project,contact",
        "assignees,project,contact,creator",
        "assignees,project,contact,creator,parent_ticket",
        "assignees,project,contact,parent_ticket",
        "assignees,project,creator",
        "assignees,project,creator,parent_ticket",
        "assignees,project,parent_ticket",
        "attachments",
        "attachments,account",
        "attachments,account,contact",
        "attachments,account,contact,creator",
        "attachments,account,contact,creator,parent_ticket",
        "attachments,account,contact,parent_ticket",
        "attachments,account,creator",
        "attachments,account,creator,parent_ticket",
        "attachments,account,parent_ticket",
        "attachments,assignees",
        "attachments,assignees,account",
        "attachments,assignees,account,contact",
        "attachments,assignees,account,contact,creator",
        "attachments,assignees,account,contact,creator,parent_ticket",
        "attachments,assignees,account,contact,parent_ticket",
        "attachments,assignees,account,creator",
        "attachments,assignees,account,creator,parent_ticket",
        "attachments,assignees,account,parent_ticket",
        "attachments,assignees,collections",
        "attachments,assignees,collections,account",
        "attachments,assignees,collections,account,contact",
        "attachments,assignees,collections,account,contact,creator",
        "attachments,assignees,collections,account,contact,creator,parent_ticket",
        "attachments,assignees,collections,account,contact,parent_ticket",
        "attachments,assignees,collections,account,creator",
        "attachments,assignees,collections,account,creator,parent_ticket",
        "attachments,assignees,collections,account,parent_ticket",
        "attachments,assignees,collections,contact",
        "attachments,assignees,collections,contact,creator",
        "attachments,assignees,collections,contact,creator,parent_ticket",
        "attachments,assignees,collections,contact,parent_ticket",
        "attachments,assignees,collections,creator",
        "attachments,assignees,collections,creator,parent_ticket",
        "attachments,assignees,collections,parent_ticket",
        "attachments,assignees,collections,project",
        "attachments,assignees,collections,project,account",
        "attachments,assignees,collections,project,account,contact",
        "attachments,assignees,collections,project,account,contact,creator",
        "attachments,assignees,collections,project,account,contact,creator,parent_ticket",
        "attachments,assignees,collections,project,account,contact,parent_ticket",
        "attachments,assignees,collections,project,account,creator",
        "attachments,assignees,collections,project,account,creator,parent_ticket",
        "attachments,assignees,collections,project,account,parent_ticket",
        "attachments,assignees,collections,project,contact",
        "attachments,assignees,collections,project,contact,creator",
        "attachments,assignees,collections,project,contact,creator,parent_ticket",
        "attachments,assignees,collections,project,contact,parent_ticket",
        "attachments,assignees,collections,project,creator",
        "attachments,assignees,collections,project,creator,parent_ticket",
        "attachments,assignees,collections,project,parent_ticket",
        "attachments,assignees,contact",
        "attachments,assignees,contact,creator",
        "attachments,assignees,contact,creator,parent_ticket",
        "attachments,assignees,contact,parent_ticket",
        "attachments,assignees,creator",
        "attachments,assignees,creator,parent_ticket",
        "attachments,assignees,parent_ticket",
        "attachments,assignees,project",
        "attachments,assignees,project,account",
        "attachments,assignees,project,account,contact",
        "attachments,assignees,project,account,contact,creator",
        "attachments,assignees,project,account,contact,creator,parent_ticket",
        "attachments,assignees,project,account,contact,parent_ticket",
        "attachments,assignees,project,account,creator",
        "attachments,assignees,project,account,creator,parent_ticket",
        "attachments,assignees,project,account,parent_ticket",
        "attachments,assignees,project,contact",
        "attachments,assignees,project,contact,creator",
        "attachments,assignees,project,contact,creator,parent_ticket",
        "attachments,assignees,project,contact,parent_ticket",
        "attachments,assignees,project,creator",
        "attachments,assignees,project,creator,parent_ticket",
        "attachments,assignees,project,parent_ticket",
        "attachments,collections",
        "attachments,collections,account",
        "attachments,collections,account,contact",
        "attachments,collections,account,contact,creator",
        "attachments,collections,account,contact,creator,parent_ticket",
        "attachments,collections,account,contact,parent_ticket",
        "attachments,collections,account,creator",
        "attachments,collections,account,creator,parent_ticket",
        "attachments,collections,account,parent_ticket",
        "attachments,collections,contact",
        "attachments,collections,contact,creator",
        "attachments,collections,contact,creator,parent_ticket",
        "attachments,collections,contact,parent_ticket",
        "attachments,collections,creator",
        "attachments,collections,creator,parent_ticket",
        "attachments,collections,parent_ticket",
        "attachments,collections,project",
        "attachments,collections,project,account",
        "attachments,collections,project,account,contact",
        "attachments,collections,project,account,contact,creator",
        "attachments,collections,project,account,contact,creator,parent_ticket",
        "attachments,collections,project,account,contact,parent_ticket",
        "attachments,collections,project,account,creator",
        "attachments,collections,project,account,creator,parent_ticket",
        "attachments,collections,project,account,parent_ticket",
        "attachments,collections,project,contact",
        "attachments,collections,project,contact,creator",
        "attachments,collections,project,contact,creator,parent_ticket",
        "attachments,collections,project,contact,parent_ticket",
        "attachments,collections,project,creator",
        "attachments,collections,project,creator,parent_ticket",
        "attachments,collections,project,parent_ticket",
        "attachments,contact",
        "attachments,contact,creator",
        "attachments,contact,creator,parent_ticket",
        "attachments,contact,parent_ticket",
        "attachments,creator",
        "attachments,creator,parent_ticket",
        "attachments,parent_ticket",
        "attachments,project",
        "attachments,project,account",
        "attachments,project,account,contact",
        "attachments,project,account,contact,creator",
        "attachments,project,account,contact,creator,parent_ticket",
        "attachments,project,account,contact,parent_ticket",
        "attachments,project,account,creator",
        "attachments,project,account,creator,parent_ticket",
        "attachments,project,account,parent_ticket",
        "attachments,project,contact",
        "attachments,project,contact,creator",
        "attachments,project,contact,creator,parent_ticket",
        "attachments,project,contact,parent_ticket",
        "attachments,project,creator",
        "attachments,project,creator,parent_ticket",
        "attachments,project,parent_ticket",
        "collections",
        "collections,account",
        "collections,account,contact",
        "collections,account,contact,creator",
        "collections,account,contact,creator,parent_ticket",
        "collections,account,contact,parent_ticket",
        "collections,account,creator",
        "collections,account,creator,parent_ticket",
        "collections,account,parent_ticket",
        "collections,contact",
        "collections,contact,creator",
        "collections,contact,creator,parent_ticket",
        "collections,contact,parent_ticket",
        "collections,creator",
        "collections,creator,parent_ticket",
        "collections,parent_ticket",
        "collections,project",
        "collections,project,account",
        "collections,project,account,contact",
        "collections,project,account,contact,creator",
        "collections,project,account,contact,creator,parent_ticket",
        "collections,project,account,contact,parent_ticket",
        "collections,project,account,creator",
        "collections,project,account,creator,parent_ticket",
        "collections,project,account,parent_ticket",
        "collections,project,contact",
        "collections,project,contact,creator",
        "collections,project,contact,creator,parent_ticket",
        "collections,project,contact,parent_ticket",
        "collections,project,creator",
        "collections,project,creator,parent_ticket",
        "collections,project,parent_ticket",
        "contact",
        "contact,creator",
        "contact,creator,parent_ticket",
        "contact,parent_ticket",
        "creator",
        "creator,parent_ticket",
        "parent_ticket",
        "project",
        "project,account",
        "project,account,contact",
        "project,account,contact,creator",
        "project,account,contact,creator,parent_ticket",
        "project,account,contact,parent_ticket",
        "project,account,creator",
        "project,account,creator,parent_ticket",
        "project,account,parent_ticket",
        "project,contact",
        "project,contact,creator",
        "project,contact,creator,parent_ticket",
        "project,contact,parent_ticket",
        "project,creator",
        "project,creator,parent_ticket",
        "project,parent_ticket",
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
