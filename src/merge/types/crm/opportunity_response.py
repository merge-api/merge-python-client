# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.crm import opportunity

__all__ = ["OpportunityResponse"]


class OpportunityResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: opportunity.Opportunity
    """# The Opportunity Object

    ### Description

    The `Opportunity` object is used to represent a deal opportunity in a CRM
    system.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
