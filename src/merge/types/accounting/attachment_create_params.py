# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AttachmentCreateParams", "Model"]


class Model(TypedDict, total=False):
    company: Optional[str]
    """The company the accounting attachment belongs to."""

    file_name: Optional[str]
    """The attachment's name."""

    file_url: Optional[str]
    """The attachment's url."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]


class AttachmentCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Accounting Attachment Object

    ### Description

    The `AccountingAttachment` object is used to represent a company's attachments.

    ### Usage Example

    Fetch from the `LIST AccountingAttachments` endpoint and view a company's
    attachments.
    """
