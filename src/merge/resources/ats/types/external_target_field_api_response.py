# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .external_target_field_api import ExternalTargetFieldApi


class ExternalTargetFieldApiResponse(UniversalBaseModel):
    activity: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="Activity")
    application: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="Application")
    attachment: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="Attachment")
    candidate: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="Candidate")
    department: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="Department")
    eeoc: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="EEOC")
    scheduled_interview: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(
        alias="ScheduledInterview"
    )
    job: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="Job")
    job_posting: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="JobPosting")
    job_interview_stage: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(
        alias="JobInterviewStage"
    )
    offer: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="Offer")
    office: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="Office")
    reject_reason: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="RejectReason")
    scorecard: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="Scorecard")
    tag: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="Tag")
    remote_user: typing.Optional[typing.List[ExternalTargetFieldApi]] = pydantic.Field(alias="RemoteUser")

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
