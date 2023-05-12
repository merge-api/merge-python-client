# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["PayrollRun"]


class PayrollRun(BaseModel):
    check_date: Optional[datetime]
    """The day and time the payroll run was checked."""

    end_date: Optional[datetime]
    """The day and time the payroll run ended."""

    field_mappings: Optional[object]

    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    run_state: Optional[Literal["PAID", "DRAFT", "APPROVED", "FAILED", "CLOSED"]]
    """
    - `PAID` - PAID
    - `DRAFT` - DRAFT
    - `APPROVED` - APPROVED
    - `FAILED` - FAILED
    - `CLOSED` - CLOSED
    """

    run_type: Optional[Literal["REGULAR", "OFF_CYCLE", "CORRECTION", "TERMINATION", "SIGN_ON_BONUS"]]
    """
    - `REGULAR` - REGULAR
    - `OFF_CYCLE` - OFF_CYCLE
    - `CORRECTION` - CORRECTION
    - `TERMINATION` - TERMINATION
    - `SIGN_ON_BONUS` - SIGN_ON_BONUS
    """

    start_date: Optional[datetime]
    """The day and time the payroll run started."""
