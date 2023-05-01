# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.crm import lead

__all__ = ["LeadResponse"]


class LeadResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: lead.Lead
    """# The Lead Object

    ### Description

    The `Lead` object is used to represent an individual who is a potential
    customer.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
