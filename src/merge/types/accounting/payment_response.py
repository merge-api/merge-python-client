# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.accounting import payment

__all__ = ["PaymentResponse"]


class PaymentResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: payment.Payment
    """# The Payment Object

    ### Description

    The `Payment` object represents general payments made towards a specific
    transaction.

    ### Usage Example

    Fetch from the `GET Payment` endpoint and view an invoice's payment.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
