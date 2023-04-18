# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.marketing import automation

__all__ = ["MktgAutomationResponse"]


class MktgAutomationResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: automation.Automation
    """# The Automation Object

    ### Description

    The `Automation` object is used to represent an automation, workflow or custom
    event in the remote system.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/automations` endpoint and view their
    automation_trigger configurations.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
