# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["TimeOffBalance"]


class TimeOffBalance(BaseModel):
    balance: Optional[float]
    """The current remaining PTO balance, always measured in terms of hours."""

    employee: Optional[str]
    """The employee the balance belongs to."""

    field_mappings: Optional[object]

    id: Optional[str]

    policy_type: Optional[Literal["VACATION", "SICK", "PERSONAL", "JURY_DUTY", "VOLUNTEER", "BEREAVEMENT"]]
    """
    - `VACATION` - VACATION
    - `SICK` - SICK
    - `PERSONAL` - PERSONAL
    - `JURY_DUTY` - JURY_DUTY
    - `VOLUNTEER` - VOLUNTEER
    - `BEREAVEMENT` - BEREAVEMENT
    """

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    used: Optional[float]
    """The amount of PTO used in terms of hours."""
