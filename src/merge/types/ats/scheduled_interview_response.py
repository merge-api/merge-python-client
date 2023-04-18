# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.ats import scheduled_interview

__all__ = ["ScheduledInterviewResponse"]


class ScheduledInterviewResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: scheduled_interview.ScheduledInterview
    """# The ScheduledInterview Object

    ### Description

    The `ScheduledInterview` object is used to represent a scheduled interview for a
    given candidate’s application to a job. An `Application` can have multiple
    `ScheduledInterview`s depending on the particular hiring process.

    ### Usage Example

    Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers`
    to show all office locations.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
