# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .application import Application
from .candidate import Candidate
from .offer import Offer
import typing
from .scheduled_interview_request_application import ScheduledInterviewRequestApplication
import pydantic
from .scheduled_interview_request_job_interview_stage import ScheduledInterviewRequestJobInterviewStage
from .scheduled_interview_request_organizer import ScheduledInterviewRequestOrganizer
from .scheduled_interview_request_interviewers_item import ScheduledInterviewRequestInterviewersItem
import datetime as dt
from .scheduled_interview_request_status import ScheduledInterviewRequestStatus
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.pydantic_utilities import update_forward_refs


class ScheduledInterviewRequest(UniversalBaseModel):
    """
    # The ScheduledInterview Object

    ### Description

    The `ScheduledInterview` object is used to represent a scheduled interview for a given candidate’s application to a job. An `Application` can have multiple `ScheduledInterview`s depending on the particular hiring process.

    ### Usage Example

    Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers` to show all office locations.
    """

    application: typing.Optional[ScheduledInterviewRequestApplication] = pydantic.Field()
    """
    The application being interviewed.
    """

    job_interview_stage: typing.Optional[ScheduledInterviewRequestJobInterviewStage] = pydantic.Field()
    """
    The stage of the interview.
    """

    organizer: typing.Optional[ScheduledInterviewRequestOrganizer] = pydantic.Field()
    """
    The user organizing the interview.
    """

    interviewers: typing.Optional[typing.List[typing.Optional[ScheduledInterviewRequestInterviewersItem]]] = (
        pydantic.Field()
    )
    """
    Array of `RemoteUser` IDs.
    """

    location: typing.Optional[str] = pydantic.Field()
    """
    The interview's location.
    """

    start_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the interview was started.
    """

    end_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the interview was ended.
    """

    status: typing.Optional[ScheduledInterviewRequestStatus] = pydantic.Field()
    """
    The interview's status.
    
    - `SCHEDULED` - SCHEDULED
    - `AWAITING_FEEDBACK` - AWAITING_FEEDBACK
    - `COMPLETE` - COMPLETE
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Application, ScheduledInterviewRequest=ScheduledInterviewRequest)
update_forward_refs(Candidate, ScheduledInterviewRequest=ScheduledInterviewRequest)
update_forward_refs(Offer, ScheduledInterviewRequest=ScheduledInterviewRequest)
