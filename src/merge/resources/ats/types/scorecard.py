# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_data import RemoteData
from .scorecard_application import ScorecardApplication
from .scorecard_interview import ScorecardInterview
from .scorecard_interviewer import ScorecardInterviewer
from .scorecard_overall_recommendation import ScorecardOverallRecommendation


class Scorecard(UniversalBaseModel):
    """
    # The Scorecard Object

    ### Description

    The `Scorecard` object is used to represent an interviewer's candidate recommendation based on a particular interview.

    ### Usage Example

    Fetch from the `LIST Scorecards` endpoint and filter by `application` to show all scorecard for an applicant.
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

    application: typing.Optional[ScorecardApplication] = pydantic.Field()
    """
    The application being scored.
    """

    interview: typing.Optional[ScorecardInterview] = pydantic.Field()
    """
    The interview being scored.
    """

    interviewer: typing.Optional[ScorecardInterviewer] = pydantic.Field()
    """
    The interviewer doing the scoring.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's scorecard was created.
    """

    submitted_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the scorecard was submitted.
    """

    overall_recommendation: typing.Optional[ScorecardOverallRecommendation] = pydantic.Field()
    """
    The inteviewer's recommendation.
    
    - `DEFINITELY_NO` - DEFINITELY_NO
    - `NO` - NO
    - `YES` - YES
    - `STRONG_YES` - STRONG_YES
    - `NO_DECISION` - NO_DECISION
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
