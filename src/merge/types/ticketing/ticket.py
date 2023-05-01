# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Ticket", "RemoteField"]


class RemoteField(BaseModel):
    remote_field_class: shared.RemoteFieldClass

    value: Optional[object]


class Ticket(BaseModel):
    account: Optional[str]
    """The account associated with the ticket."""

    assignees: Optional[List[Optional[str]]]

    attachments: Optional[List[Optional[str]]]

    collections: Optional[List[Optional[str]]]

    completed_at: Optional[datetime]
    """When the ticket was completed."""

    contact: Optional[str]
    """The contact associated with the ticket."""

    creator: Optional[str]
    """The user who created this ticket."""

    description: Optional[str]
    """The ticket’s description.

    HTML version of description is mapped if supported by the third-party platform.
    """

    due_date: Optional[datetime]
    """The ticket's due date."""

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The ticket's name."""

    parent_ticket: Optional[str]
    """The ticket's parent ticket."""

    priority: Optional[Literal["URGENT", "HIGH", "NORMAL", "LOW"]]
    """
    - `URGENT` - URGENT
    - `HIGH` - HIGH
    - `NORMAL` - NORMAL
    - `LOW` - LOW
    """

    project: Optional[str]
    """The project the ticket belongs to."""

    remote_created_at: Optional[datetime]
    """When the third party's ticket was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_fields: Optional[List[RemoteField]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the third party's ticket was updated."""

    remote_was_deleted: Optional[bool]

    status: Optional[Literal["OPEN", "CLOSED", "IN_PROGRESS", "ON_HOLD"]]
    """
    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    - `IN_PROGRESS` - IN_PROGRESS
    - `ON_HOLD` - ON_HOLD
    """

    tags: Optional[List[Optional[str]]]

    ticket_type: Optional[str]
    """The ticket's type."""

    ticket_url: Optional[str]
    """The 3rd party url of the Ticket."""
