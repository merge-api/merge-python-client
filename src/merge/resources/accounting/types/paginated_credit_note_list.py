# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .credit_note import CreditNote
from .credit_note_apply_line_for_credit_note import CreditNoteApplyLineForCreditNote
from .credit_note_apply_line_for_invoice import CreditNoteApplyLineForInvoice
from .invoice import Invoice
from .vendor_credit import VendorCredit
from .vendor_credit_apply_line_for_invoice import VendorCreditApplyLineForInvoice
from .vendor_credit_apply_line_for_vendor_credit import VendorCreditApplyLineForVendorCredit
import typing
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ....core.pydantic_utilities import update_forward_refs


class PaginatedCreditNoteList(UniversalBaseModel):
    next: typing.Optional[str] = None
    previous: typing.Optional[str] = None
    results: typing.Optional[typing.List[CreditNote]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CreditNote, PaginatedCreditNoteList=PaginatedCreditNoteList)
update_forward_refs(CreditNoteApplyLineForCreditNote, PaginatedCreditNoteList=PaginatedCreditNoteList)
update_forward_refs(CreditNoteApplyLineForInvoice, PaginatedCreditNoteList=PaginatedCreditNoteList)
update_forward_refs(Invoice, PaginatedCreditNoteList=PaginatedCreditNoteList)
update_forward_refs(VendorCredit, PaginatedCreditNoteList=PaginatedCreditNoteList)
update_forward_refs(VendorCreditApplyLineForInvoice, PaginatedCreditNoteList=PaginatedCreditNoteList)
update_forward_refs(VendorCreditApplyLineForVendorCredit, PaginatedCreditNoteList=PaginatedCreditNoteList)
