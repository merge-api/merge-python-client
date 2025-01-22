# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.pydantic_utilities import update_forward_refs


class VendorCreditApplyLineForVendorCredit(UniversalBaseModel):
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

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was modified by Merge.
    """

    invoice: typing.Optional["VendorCreditApplyLineForVendorCreditInvoice"] = None
    applied_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date that the vendor credit is applied to the invoice.
    """

    applied_amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The amount of the VendorCredit applied to the invoice.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .credit_note import CreditNote  # noqa: E402
from .credit_note_apply_line_for_credit_note import CreditNoteApplyLineForCreditNote  # noqa: E402
from .credit_note_apply_line_for_invoice import CreditNoteApplyLineForInvoice  # noqa: E402
from .invoice import Invoice  # noqa: E402
from .vendor_credit import VendorCredit  # noqa: E402
from .vendor_credit_apply_line_for_invoice import VendorCreditApplyLineForInvoice  # noqa: E402
from .vendor_credit_apply_line_for_vendor_credit_invoice import VendorCreditApplyLineForVendorCreditInvoice  # noqa: E402

update_forward_refs(CreditNote, VendorCreditApplyLineForVendorCredit=VendorCreditApplyLineForVendorCredit)
update_forward_refs(
    CreditNoteApplyLineForCreditNote, VendorCreditApplyLineForVendorCredit=VendorCreditApplyLineForVendorCredit
)
update_forward_refs(
    CreditNoteApplyLineForInvoice, VendorCreditApplyLineForVendorCredit=VendorCreditApplyLineForVendorCredit
)
update_forward_refs(Invoice, VendorCreditApplyLineForVendorCredit=VendorCreditApplyLineForVendorCredit)
update_forward_refs(VendorCredit, VendorCreditApplyLineForVendorCredit=VendorCreditApplyLineForVendorCredit)
update_forward_refs(
    VendorCreditApplyLineForInvoice, VendorCreditApplyLineForVendorCredit=VendorCreditApplyLineForVendorCredit
)
update_forward_refs(VendorCreditApplyLineForVendorCredit)
