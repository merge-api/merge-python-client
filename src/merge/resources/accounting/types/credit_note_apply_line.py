# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .credit_note_apply_line_invoice import CreditNoteApplyLineInvoice

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CreditNoteApplyLine(pydantic.BaseModel):
    """
    # The CreditNoteApplyLine Object
    ### Description
    The `CreditNoteApplyLine` is attached to the CreditNote model.

    ### Usage Example
    Fetch from the `GET CreditNote` endpoint and view the invoice's applied to lines.
    """

    invoice: typing.Optional[CreditNoteApplyLineInvoice]
    applied_date: typing.Optional[dt.datetime] = pydantic.Field(
        description="Date that the credit note is applied to the invoice."
    )
    applied_amount: typing.Optional[str] = pydantic.Field(
        description="The amount of the Credit Note applied to the invoice."
    )
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}