# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .remote_field_request import RemoteFieldRequest
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class PaymentLineItemRequest(UniversalBaseModel):
    """
    # The PaymentLineItem Object

    ### Description

    The `PaymentLineItem` object is an applied-to-line on a `Payment` that can either be a `Invoice`, `CreditNote`, or `JournalEntry`.

    ### Usage Example

    `Payment` will have a field called `applied-to-lines` which will be an array of `PaymentLineItemInternalMappingSerializer` objects that can either be a `Invoice`, `CreditNote`, or `JournalEntry`.
    """

    remote_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The third-party API ID of the matching object.
    """

    applied_amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The amount being applied to the transaction.
    """

    applied_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the payment portion is applied.
    """

    related_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Merge ID of the transaction the payment portion is being applied to.
    """

    related_object_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of transaction the payment portion is being applied to. Possible values include: INVOICE, JOURNAL_ENTRY, or CREDIT_NOTE.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
