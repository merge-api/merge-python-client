# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Task", "RemoteField"]


class RemoteField(BaseModel):
    remote_field_class: shared.RemoteFieldClass

    value: Optional[object]


class Task(BaseModel):
    account: Optional[str]
    """The task's account."""

    completed_date: Optional[datetime]
    """When the task is completed."""

    content: Optional[str]
    """The task's content."""

    due_date: Optional[datetime]
    """When the task is due."""

    field_mappings: Optional[object]

    id: Optional[str]

    owner: Optional[str]
    """The task's owner."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_fields: Optional[List[RemoteField]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    status: Optional[Literal["OPEN", "CLOSED"]]
    """
    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    """

    subject: Optional[str]
    """The task's subject."""
