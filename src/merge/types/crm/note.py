# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...types import shared
from ..._models import BaseModel

__all__ = ["Note", "RemoteField"]


class RemoteField(BaseModel):
    remote_field_class: shared.RemoteFieldClass

    value: Optional[object]


class Note(BaseModel):
    account: Optional[str]
    """The note's account."""

    contact: Optional[str]
    """The note's contact."""

    content: Optional[str]
    """The note's content."""

    field_mappings: Optional[object]

    id: Optional[str]

    opportunity: Optional[str]
    """The note's opportunity."""

    owner: Optional[str]
    """The note's owner."""

    remote_created_at: Optional[datetime]
    """When the third party's lead was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_fields: Optional[List[RemoteField]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the third party's lead was updated."""

    remote_was_deleted: Optional[bool]
