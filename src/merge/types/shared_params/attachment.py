# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["Attachment"]


class Attachment(TypedDict, total=False):
    attachment_type: Literal["RESUME", "COVER_LETTER", "OFFER_LETTER", "OTHER"]
    """
    - `RESUME` - RESUME
    - `COVER_LETTER` - COVER_LETTER
    - `OFFER_LETTER` - OFFER_LETTER
    - `OTHER` - OTHER
    """

    candidate: Optional[str]

    content_type: Optional[str]
    """The attachment's file format."""

    file_name: Optional[str]
    """The attachment's name.

    It is required to include the file extension in the attachment's name.
    """

    file_url: Optional[str]
    """The attachment's url.

    It is required to include the file extension in the file's URL.
    """

    remote_created_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the third party's attachment was created."""

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    ticket: Optional[str]
    """The ticket associated with the attachment."""

    uploaded_by: Optional[str]
    """The user who uploaded the attachment."""
