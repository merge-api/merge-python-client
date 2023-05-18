# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["EngagementType", "RemoteField"]


class RemoteField(BaseModel):
    remote_field_class: shared.RemoteFieldClass

    value: Optional[object]


class EngagementType(BaseModel):
    activity_type: Optional[Literal["CALL", "MEETING", "EMAIL"]]
    """
    - `CALL` - CALL
    - `MEETING` - MEETING
    - `EMAIL` - EMAIL
    """

    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    name: Optional[str]
    """The engagement type's name."""

    remote_fields: Optional[List[RemoteField]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""
