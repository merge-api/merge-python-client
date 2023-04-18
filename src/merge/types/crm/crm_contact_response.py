# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel

__all__ = ["CrmContactResponse"]


class CrmContactResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: shared.Contact
    """# The Contact Object

    ### Description

    The `Contact` object is used to represent a contact in the remote system.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/contact` endpoint and view their phone numbers.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
