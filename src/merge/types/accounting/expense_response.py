# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.accounting import expense

__all__ = ["ExpenseResponse"]


class ExpenseResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: expense.Expense
    """# The Expense Object

    ### Description

    The `Expense` object is used to represent a purchase made from a business which
    can be made with a check, credit card, or cash. Each expense object is dedicated
    to a grouping of expenses, with each expense recorded in the lines object.

    ### Usage Example

    Fetch from the `GET Expense` endpoint and view a company's expense.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
