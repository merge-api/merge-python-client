# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AttachmentCreateParams", "Model"]


class Model(TypedDict, total=False):
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

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    ticket: Optional[str]
    """The ticket associated with the attachment."""

    uploaded_by: Optional[str]
    """The user who uploaded the attachment."""


class AttachmentCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Attachment Object

    ### Description

    The `Attachment` object is used to represent an attachment for a ticket.

    ### Usage Example

    TODO
    """

    remote_user_id: Required[str]
