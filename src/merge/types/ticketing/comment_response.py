# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.ticketing import comment

__all__ = ["CommentResponse"]


class CommentResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: comment.Comment
    """# The Comment Object

    ### Description

    The `Comment` object is used to represent a comment on a ticket.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
