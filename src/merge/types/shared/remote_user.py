# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .remote_data import RemoteData

__all__ = ["RemoteUser"]


class RemoteUser(BaseModel):
    access_role: Optional[Literal["SUPER_ADMIN", "ADMIN", "TEAM_MEMBER", "LIMITED_TEAM_MEMBER", "INTERVIEWER"]]
    """
    - `SUPER_ADMIN` - SUPER_ADMIN
    - `ADMIN` - ADMIN
    - `TEAM_MEMBER` - TEAM_MEMBER
    - `LIMITED_TEAM_MEMBER` - LIMITED_TEAM_MEMBER
    - `INTERVIEWER` - INTERVIEWER
    """

    disabled: Optional[bool]
    """Whether the user's account had been disabled."""

    email: Optional[str]
    """The user's email."""

    field_mappings: Optional[object]

    first_name: Optional[str]
    """The user's first name."""

    id: Optional[str]

    last_name: Optional[str]
    """The user's last name."""

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    remote_created_at: Optional[datetime]
    """When the third party's user was created."""

    remote_data: Optional[List[RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""
