# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .payroll_run_run_state import PayrollRunRunState
from .payroll_run_run_type import PayrollRunRunType
from .remote_data import RemoteData


class PayrollRun(pydantic_v1.BaseModel):
    """
    # The PayrollRun Object

    ### Description

    The `PayrollRun` object is used to represent a group of pay statements for a specific pay schedule.

    ### Usage Example

    Fetch from the `LIST PayrollRuns` endpoint and filter by `ID` to show all payroll runs.
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

    run_state: typing.Optional[PayrollRunRunState] = pydantic_v1.Field()
    """
    The state of the payroll run
    
    - `PAID` - PAID
    - `DRAFT` - DRAFT
    - `APPROVED` - APPROVED
    - `FAILED` - FAILED
    - `CLOSED` - CLOSED
    """

    run_type: typing.Optional[PayrollRunRunType] = pydantic_v1.Field()
    """
    The type of the payroll run
    
    - `REGULAR` - REGULAR
    - `OFF_CYCLE` - OFF_CYCLE
    - `CORRECTION` - CORRECTION
    - `TERMINATION` - TERMINATION
    - `SIGN_ON_BONUS` - SIGN_ON_BONUS
    """

    start_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The day and time the payroll run started.
    """

    end_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The day and time the payroll run ended.
    """

    check_date: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The day and time the payroll run was checked.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic_v1.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
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
