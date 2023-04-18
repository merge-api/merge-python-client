# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel

__all__ = ["CrmAccountResponse"]


class CrmAccountResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: shared.Account
    """# The Account Object

    ### Description

    The `Account` object is used to represent a company in a CRM system.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
