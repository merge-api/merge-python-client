# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.accounting import purchase_order

__all__ = ["PurchaseOrderResponse"]


class PurchaseOrderResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: purchase_order.PurchaseOrder
    """# The PurchaseOrder Object

    ### Description

    The `PurchaseOrder` object is a record of request for a product or service
    between a buyer and seller.

    ### Usage Example

    Fetch from the `LIST PurchaseOrders` endpoint and view a company's purchase
    orders.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
