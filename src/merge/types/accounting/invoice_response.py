# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.accounting import invoice

__all__ = ["InvoiceResponse"]


class InvoiceResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: invoice.Invoice
    """# The Invoice Object

        ### Description
        The `Invoice` object represents an itemized record of goods and/or services sold to a customer.

    If type = accounts_payable `Invoice` is a bill, if type = accounts_receivable
    it's an invoice.

        ### Usage Example
        Fetch from the `LIST Invoices` endpoint and view a company's invoices.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
