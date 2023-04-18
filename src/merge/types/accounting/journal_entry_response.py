# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.accounting import journal_entry

__all__ = ["JournalEntryResponse"]


class JournalEntryResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: journal_entry.JournalEntry
    """# The JournalEntry Object

    ### Description

    The `JournalEntry` object is used to get a record of all manually created
    entries made in a company’s general ledger. The journal line items for each
    journal entry should sum to zero.

    ### Usage Example

    Fetch from the `GET JournalEntry` endpoint and view a company's journey entry.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
