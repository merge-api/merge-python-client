# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel

__all__ = ["AttachmentResponse"]


class AttachmentResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: shared.Attachment
    """# The Attachment Object

    ### Description

    The `Attachment` object is used to represent an attachment for a ticket.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
