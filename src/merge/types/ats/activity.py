# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Activity"]


class Activity(BaseModel):
    activity_type: Optional[Literal["CALL", "MEETING", "EMAIL"]]
    """
    - `CALL` - CALL
    - `MEETING` - MEETING
    - `EMAIL` - EMAIL
    """

    body: Optional[str]
    """The activity's body."""

    field_mappings: Optional[object]

    id: Optional[str]

    remote_created_at: Optional[datetime]
    """When the third party's activity was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    subject: Optional[str]
    """The activity's subject."""

    user: Optional[str]
    """The user that performed the action."""

    visibility: Optional[Literal["ADMIN_ONLY", "PUBLIC", "PRIVATE"]]
    """
    - `ADMIN_ONLY` - ADMIN_ONLY
    - `PUBLIC` - PUBLIC
    - `PRIVATE` - PRIVATE
    """
