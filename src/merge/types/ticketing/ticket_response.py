# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.ticketing import ticket

__all__ = ["TicketResponse"]


class TicketResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: ticket.Ticket
    """# The Ticket Object

    ### Description

    The `Ticket` object is used to represent a ticket or a task within a system.

    ### Usage Example

    TODO
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
