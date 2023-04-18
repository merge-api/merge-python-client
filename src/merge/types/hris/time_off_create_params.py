# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TimeOffCreateParams", "Model"]


class Model(TypedDict, total=False):
    amount: Optional[float]
    """The time off quantity measured by the prescribed “units”."""

    approver: Optional[str]
    """The Merge ID of the employee with the ability to approve the time off request."""

    employee: Optional[str]
    """The employee requesting time off."""

    employee_note: Optional[str]
    """The employee note for this time off request."""

    end_time: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """The day and time of the end of the time requested off."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    request_type: Literal["VACATION", "SICK", "PERSONAL", "JURY_DUTY", "VOLUNTEER", "BEREAVEMENT"]
    """
    - `VACATION` - VACATION
    - `SICK` - SICK
    - `PERSONAL` - PERSONAL
    - `JURY_DUTY` - JURY_DUTY
    - `VOLUNTEER` - VOLUNTEER
    - `BEREAVEMENT` - BEREAVEMENT
    """

    start_time: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """The day and time of the start of the time requested off."""

    status: Literal["REQUESTED", "APPROVED", "DECLINED", "CANCELLED", "DELETED"]
    """
    - `REQUESTED` - REQUESTED
    - `APPROVED` - APPROVED
    - `DECLINED` - DECLINED
    - `CANCELLED` - CANCELLED
    - `DELETED` - DELETED
    """

    units: Literal["HOURS", "DAYS"]
    """
    - `HOURS` - HOURS
    - `DAYS` - DAYS
    """


class TimeOffCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The TimeOff Object

    ### Description

    The `TimeOff` object is used to represent all employees' Time Off entries.

    ### Usage Example

    Fetch from the `LIST TimeOffs` endpoint and filter by `ID` to show all time off
    requests.
    """
