# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....types import shared
from ...._models import BaseModel

__all__ = ["TimeOff"]


class TimeOff(BaseModel):
    amount: Optional[float]
    """The time off quantity measured by the prescribed “units”."""

    approver: Optional[str]
    """The Merge ID of the employee with the ability to approve the time off request."""

    employee: Optional[str]
    """The employee requesting time off."""

    employee_note: Optional[str]
    """The employee note for this time off request."""

    end_time: Optional[datetime]
    """The day and time of the end of the time requested off."""

    field_mappings: Optional[object]

    id: Optional[str]

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]

    request_type: Optional[Literal["VACATION", "SICK", "PERSONAL", "JURY_DUTY", "VOLUNTEER", "BEREAVEMENT"]]
    """
    - `VACATION` - VACATION
    - `SICK` - SICK
    - `PERSONAL` - PERSONAL
    - `JURY_DUTY` - JURY_DUTY
    - `VOLUNTEER` - VOLUNTEER
    - `BEREAVEMENT` - BEREAVEMENT
    """

    start_time: Optional[datetime]
    """The day and time of the start of the time requested off."""

    status: Optional[Literal["REQUESTED", "APPROVED", "DECLINED", "CANCELLED", "DELETED"]]
    """
    - `REQUESTED` - REQUESTED
    - `APPROVED` - APPROVED
    - `DECLINED` - DECLINED
    - `CANCELLED` - CANCELLED
    - `DELETED` - DELETED
    """

    units: Optional[Literal["HOURS", "DAYS"]]
    """
    - `HOURS` - HOURS
    - `DAYS` - DAYS
    """
