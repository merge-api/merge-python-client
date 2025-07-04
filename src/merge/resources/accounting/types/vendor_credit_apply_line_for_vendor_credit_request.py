# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, update_forward_refs
from ....core.unchecked_base_model import UncheckedBaseModel
from .vendor_credit_apply_line_for_vendor_credit_request_invoice import (
    VendorCreditApplyLineForVendorCreditRequestInvoice,
)


class VendorCreditApplyLineForVendorCreditRequest(UncheckedBaseModel):
    """
    # The VendorCreditApplyLine Object
    ### Description
    The `VendorCreditApplyLine` object is used to represent a applied vendor credit.

    ### Usage Example
    Fetch from the `GET VendorCredit` endpoint and view the vendor credit's applied to lines.
    """

    remote_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The third-party API ID of the matching object.
    """

    invoice: typing.Optional[VendorCreditApplyLineForVendorCreditRequestInvoice] = None
    applied_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date that the vendor credit is applied to the invoice.
    """

    applied_amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The amount of the VendorCredit applied to the invoice.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .credit_note import CreditNote  # noqa: E402, F401, I001
from .credit_note_apply_line_for_credit_note import CreditNoteApplyLineForCreditNote  # noqa: E402, F401, I001
from .credit_note_apply_line_for_invoice import CreditNoteApplyLineForInvoice  # noqa: E402, F401, I001
from .invoice import Invoice  # noqa: E402, F401, I001
from .vendor_credit import VendorCredit  # noqa: E402, F401, I001
from .vendor_credit_apply_line_for_invoice import VendorCreditApplyLineForInvoice  # noqa: E402, F401, I001
from .vendor_credit_apply_line_for_vendor_credit import VendorCreditApplyLineForVendorCredit  # noqa: E402, F401, I001

update_forward_refs(VendorCreditApplyLineForVendorCreditRequest)
