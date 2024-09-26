# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .application import Application
from .candidate import Candidate
from .offer import Offer
import typing
import pydantic
import datetime as dt
from .scheduled_interview_application import ScheduledInterviewApplication
from .scheduled_interview_job_interview_stage import ScheduledInterviewJobInterviewStage
from .scheduled_interview_organizer import ScheduledInterviewOrganizer
from .scheduled_interview_interviewers_item import ScheduledInterviewInterviewersItem
from .scheduled_interview_status import ScheduledInterviewStatus
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.pydantic_utilities import update_forward_refs


class ScheduledInterview(UniversalBaseModel):
    """
    # The ScheduledInterview Object

    ### Description

    The `ScheduledInterview` object is used to represent a scheduled interview for a given candidate’s application to a job. An `Application` can have multiple `ScheduledInterview`s depending on the particular hiring process.

    ### Usage Example

    Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers` to show all office locations.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was modified by Merge.
    """

    application: typing.Optional[ScheduledInterviewApplication] = pydantic.Field()
    """
    The application being interviewed.
    """

    job_interview_stage: typing.Optional[ScheduledInterviewJobInterviewStage] = pydantic.Field()
    """
    The stage of the interview.
    """

    organizer: typing.Optional[ScheduledInterviewOrganizer] = pydantic.Field()
    """
    The user organizing the interview.
    """

    interviewers: typing.Optional[typing.List[typing.Optional[ScheduledInterviewInterviewersItem]]] = pydantic.Field()
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

    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's interview was created.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's interview was updated.
    """

    status: typing.Optional[ScheduledInterviewStatus] = pydantic.Field()
    """
    The interview's status.
    
    - `SCHEDULED` - SCHEDULED
    - `AWAITING_FEEDBACK` - AWAITING_FEEDBACK
    - `COMPLETE` - COMPLETE
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Application, ScheduledInterview=ScheduledInterview)
update_forward_refs(Candidate, ScheduledInterview=ScheduledInterview)
update_forward_refs(Offer, ScheduledInterview=ScheduledInterview)
