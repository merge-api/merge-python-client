# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.marketing import contact_list

__all__ = ["ContactListCreateResponse"]


class ContactListCreateResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: contact_list.ContactList
    """# The List Object

    ### Description

    The `List` object is used to represent a list of contacts in the remote system.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/lists` endpoint and view their names.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
