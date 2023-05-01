# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.hris import time_off

__all__ = ["TimeOffResponse"]


class TimeOffResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: time_off.TimeOff
    """# The TimeOff Object

    ### Description

    The `TimeOff` object is used to represent all employees' Time Off entries.

    ### Usage Example

    Fetch from the `LIST TimeOffs` endpoint and filter by `ID` to show all time off
    requests.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
