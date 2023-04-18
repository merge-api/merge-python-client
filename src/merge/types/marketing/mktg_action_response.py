# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.marketing import action

__all__ = ["MktgActionResponse"]


class MktgActionResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: action.Action
    """# The Action Object

    ### Description

    The `Action` object is used to represent an action executed within an
    automation.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/actions` endpoint and view their types.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
