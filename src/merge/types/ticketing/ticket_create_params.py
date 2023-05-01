# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TicketCreateParams", "Model"]


class Model(TypedDict, total=False):
    account: Optional[str]
    """The account associated with the ticket."""

    assignees: List[Optional[str]]

    attachments: List[Optional[str]]

    collections: List[Optional[str]]

    completed_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the ticket was completed."""

    contact: Optional[str]
    """The contact associated with the ticket."""

    creator: Optional[str]
    """The user who created this ticket."""

    description: Optional[str]
    """The ticket’s description.

    HTML version of description is mapped if supported by the third-party platform.
    """

    due_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """The ticket's due date."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    name: Optional[str]
    """The ticket's name."""

    parent_ticket: Optional[str]
    """The ticket's parent ticket."""

    priority: Literal["URGENT", "HIGH", "NORMAL", "LOW"]
    """
    - `URGENT` - URGENT
    - `HIGH` - HIGH
    - `NORMAL` - NORMAL
    - `LOW` - LOW
    """

    project: Optional[str]
    """The project the ticket belongs to."""

    status: Literal["OPEN", "CLOSED", "IN_PROGRESS", "ON_HOLD"]
    """
    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    - `IN_PROGRESS` - IN_PROGRESS
    - `ON_HOLD` - ON_HOLD
    """

    tags: List[Optional[str]]

    ticket_type: Optional[str]
    """The ticket's type."""

    ticket_url: Optional[str]
    """The 3rd party url of the Ticket."""


class TicketCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Ticket Object

    ### Description

    The `Ticket` object is used to represent a ticket or a task within a system.

    ### Usage Example

    TODO
    """
