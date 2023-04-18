# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["ScheduledInterview"]


class ScheduledInterview(BaseModel):
    application: Optional[str]
    """The application being interviewed."""

    end_at: Optional[datetime]
    """When the interview was ended."""

    field_mappings: Optional[object]

    id: Optional[str]

    interviewers: Optional[List[Optional[str]]]
    """Array of `RemoteUser` IDs."""

    job_interview_stage: Optional[str]
    """The stage of the interview."""

    location: Optional[str]
    """The interview's location."""

    organizer: Optional[str]
    """The user organizing the interview."""

    remote_created_at: Optional[datetime]
    """When the third party's interview was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the third party's interview was updated."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    start_at: Optional[datetime]
    """When the interview was started."""

    status: Optional[Literal["SCHEDULED", "AWAITING_FEEDBACK", "COMPLETE"]]
    """
    - `SCHEDULED` - SCHEDULED
    - `AWAITING_FEEDBACK` - AWAITING_FEEDBACK
    - `COMPLETE` - COMPLETE
    """
