# This file was auto-generated by Fern from our API Definition.

from ....core.unchecked_base_model import UncheckedBaseModel
from .credit_note import CreditNote
from .credit_note_apply_line_for_credit_note import CreditNoteApplyLineForCreditNote
from .credit_note_apply_line_for_invoice import CreditNoteApplyLineForInvoice
from .invoice import Invoice
from .vendor_credit import VendorCredit
from .vendor_credit_apply_line_for_invoice import VendorCreditApplyLineForInvoice
from .vendor_credit_apply_line_for_vendor_credit import VendorCreditApplyLineForVendorCredit
import typing
from .warning_validation_problem import WarningValidationProblem
from .error_validation_problem import ErrorValidationProblem
from .debug_mode_log import DebugModeLog
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class InvoiceResponse(UncheckedBaseModel):
    model: Invoice
    warnings: typing.List[WarningValidationProblem]
    errors: typing.List[ErrorValidationProblem]
    logs: typing.Optional[typing.List[DebugModeLog]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
