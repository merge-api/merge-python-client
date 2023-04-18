# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.accounting import accounting_attachment

__all__ = ["AccountingAttachmentResponse"]


class AccountingAttachmentResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: accounting_attachment.AccountingAttachment
    """# The Accounting Attachment Object

    ### Description

    The `AccountingAttachment` object is used to represent a company's attachments.

    ### Usage Example

    Fetch from the `LIST AccountingAttachments` endpoint and view a company's
    attachments.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
