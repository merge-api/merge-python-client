# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.crm import custom_object

__all__ = ["CustomObjectResponse"]


class CustomObjectResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: custom_object.CustomObject
    """# The CustomObject Object

    ### Description

    The `Custom Object` record refers to an instance of a Custom Object Class.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
