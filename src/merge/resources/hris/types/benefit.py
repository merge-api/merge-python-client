# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .benefit_employee import BenefitEmployee
from .remote_data import RemoteData


class Benefit(pydantic_v1.BaseModel):
    """
    # The Benefit Object

    ### Description

    The `Benefit` object is used to represent a benefit that an employee has enrolled in.

    ### Usage Example

    Fetch from the `LIST Benefits` endpoint and filter by `ID` to show all benefits.
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

    employee: typing.Optional[BenefitEmployee] = pydantic_v1.Field()
    """
    The employee on the plan.
    """

    provider_name: typing.Optional[str] = pydantic_v1.Field()
    """
    The name of the benefit provider.
    """

    benefit_plan_type: typing.Optional[str] = pydantic_v1.Field()
    """
    The type of benefit plan
    """

    employee_contribution: typing.Optional[float] = pydantic_v1.Field()
    """
    The employee's contribution.
    """

    company_contribution: typing.Optional[float] = pydantic_v1.Field()
    """
    The company's contribution.
    """

    start_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The day and time the benefit started.
    """

    end_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The day and time the benefit ended.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic_v1.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

    employer_benefit: typing.Optional[str] = pydantic_v1.Field()
    """
    The employer benefit plan the employee is enrolled in.
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

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
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
