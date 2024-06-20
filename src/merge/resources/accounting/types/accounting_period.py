# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .accounting_period_status import AccountingPeriodStatus


class AccountingPeriod(pydantic_v1.BaseModel):
    """
    # The AccountingPeriod Object

    ### Description

    The `AccountingPeriod` object is used to define a period of time in which events occurred.

    ### Usage Example

    Common models like `Invoice` and `Transaction` will have `AccountingPeriod` objects which will denote when they occurred.
    """

    id: typing.Optional[str]
    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was modified by Merge.
    """

    start_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    Beginning date of the period
    """

    end_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    End date of the period
    """

    status: typing.Optional[AccountingPeriodStatus]
    name: typing.Optional[str] = pydantic_v1.Field()
    """
    Name of the accounting period.
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
