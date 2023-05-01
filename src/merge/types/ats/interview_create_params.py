# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InterviewCreateParams", "Model"]


class Model(TypedDict, total=False):
    application: Optional[str]
    """The application being interviewed."""

    end_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the interview was ended."""

    integration_params: Optional[object]

    interviewers: List[Optional[str]]
    """Array of `RemoteUser` IDs."""

    job_interview_stage: Optional[str]
    """The stage of the interview."""

    linked_account_params: Optional[object]

    location: Optional[str]
    """The interview's location."""

    organizer: Optional[str]
    """The user organizing the interview."""

    start_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the interview was started."""

    status: Literal["SCHEDULED", "AWAITING_FEEDBACK", "COMPLETE"]
    """
    - `SCHEDULED` - SCHEDULED
    - `AWAITING_FEEDBACK` - AWAITING_FEEDBACK
    - `COMPLETE` - COMPLETE
    """


class InterviewCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The ScheduledInterview Object

    ### Description

    The `ScheduledInterview` object is used to represent a scheduled interview for a
    given candidate’s application to a job. An `Application` can have multiple
    `ScheduledInterview`s depending on the particular hiring process.

    ### Usage Example

    Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers`
    to show all office locations.
    """

    remote_user_id: Required[str]
