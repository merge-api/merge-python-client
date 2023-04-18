# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.crm import engagement

__all__ = ["EngagementResponse"]


class EngagementResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: engagement.Engagement
    """# The Engagement Object

    ### Description

    The `Engagement` object is used to represent an interaction noted in a CRM
    system.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
