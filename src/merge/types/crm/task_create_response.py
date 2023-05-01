# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.crm import task

__all__ = ["TaskCreateResponse"]


class TaskCreateResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: task.Task
    """# The Task Object

    ### Description

    The `Task` object is used to represent a task, such as a to-do item.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
