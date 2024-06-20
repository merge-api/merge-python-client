# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class PaymentLineItem(pydantic_v1.BaseModel):
    """
    # The PaymentLineItem Object

    ### Description

    The `PaymentLineItem` object is an applied-to-line on a `Payment` that can either be a `Invoice`, `CreditNote`, or `JournalEntry`.

    ### Usage Example

    `Payment` will have a field called `applied-to-lines` which will be an array of `PaymentLineItemInternalMappingSerializer` objects that can either be a `Invoice`, `CreditNote`, or `JournalEntry`.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic_v1.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was modified by Merge.
    """

    applied_amount: typing.Optional[str] = pydantic_v1.Field()
    """
    The amount being applied to the transaction.
    """

    applied_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The date the payment portion is applied.
    """

    related_object_id: typing.Optional[str] = pydantic_v1.Field()
    """
    The Merge ID of the transaction the payment portion is being applied to.
    """

    related_object_type: typing.Optional[str] = pydantic_v1.Field()
    """
    The type of transaction the payment portion is being applied to. Possible values include: INVOICE, JOURNAL_ENTRY, or CREDIT_NOTE.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}
