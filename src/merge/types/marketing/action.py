# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Action"]


class Action(BaseModel):
    emails: List[str]
    """The marketing emails sent by this action."""

    messages: List[str]
    """The messages sent by this action."""

    field_mappings: Optional[object]

    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    name: Optional[str]
    """The action's name."""

    remote_data: Optional[List[Optional[object]]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    type: Optional[Literal["EMAIL", "MESSAGE"]]
    """
    - `EMAIL` - EMAIL
    - `MESSAGE` - MESSAGE
    """
