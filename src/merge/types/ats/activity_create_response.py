# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.ats import activity

__all__ = ["ActivityCreateResponse"]


class ActivityCreateResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: activity.Activity
    """# The Activity Object

    ### Description

    The `Activity` object is used to represent an activity for a candidate performed
    by a user.

    ### Usage Example

    Fetch from the `LIST Activities` endpoint and filter by `ID` to show all
    activities.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
