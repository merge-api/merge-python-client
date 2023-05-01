# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...types import shared
from ..._models import BaseModel

__all__ = ["Comment"]


class Comment(BaseModel):
    body: Optional[str]
    """The comment's text body."""

    contact: Optional[str]
    """The author of the Comment, if the author is a Contact."""

    field_mappings: Optional[object]

    html_body: Optional[str]
    """The comment's text body formatted as html."""

    id: Optional[str]

    is_private: Optional[bool]
    """Whether or not the comment is internal."""

    remote_created_at: Optional[datetime]
    """When the third party's comment was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]

    ticket: Optional[str]
    """The ticket associated with the comment."""

    user: Optional[str]
    """The author of the Comment, if the author is a User."""
