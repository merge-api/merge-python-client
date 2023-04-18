# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Template"]


class Template(BaseModel):
    contents: Optional[str]
    """The template contents."""

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The template's name."""

    owner: Optional[str]
    """The template's owner."""

    remote_created_at: Optional[datetime]
    """When the template was created in the remote system."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the template was last updated in the remote system."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    type: Optional[Literal["EMAIL", "MESSAGE"]]
    """
    - `EMAIL` - EMAIL
    - `MESSAGE` - MESSAGE
    """
