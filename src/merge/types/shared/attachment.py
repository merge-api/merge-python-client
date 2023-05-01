# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .remote_data import RemoteData

__all__ = ["Attachment"]


class Attachment(BaseModel):
    attachment_type: Optional[Literal["RESUME", "COVER_LETTER", "OFFER_LETTER", "OTHER"]]
    """
    - `RESUME` - RESUME
    - `COVER_LETTER` - COVER_LETTER
    - `OFFER_LETTER` - OFFER_LETTER
    - `OTHER` - OTHER
    """

    candidate: Optional[str]

    content_type: Optional[str]
    """The attachment's file format."""

    field_mappings: Optional[object]

    file_name: Optional[str]
    """The attachment's name.

    It is required to include the file extension in the attachment's name.
    """

    file_url: Optional[str]
    """The attachment's url.

    It is required to include the file extension in the file's URL.
    """

    id: Optional[str]

    remote_created_at: Optional[datetime]
    """When the third party's attachment was created."""

    remote_data: Optional[List[RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]

    ticket: Optional[str]
    """The ticket associated with the attachment."""

    uploaded_by: Optional[str]
    """The user who uploaded the attachment."""
