# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.crm import note

__all__ = ["NoteResponse"]


class NoteResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: note.Note
    """# The Note Object

    ### Description

    The `Note` object is used to represent a note on another object.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
