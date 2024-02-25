# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .field_mapping_api_instance import FieldMappingApiInstance

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class FieldMappingApiInstanceResponse(pydantic.BaseModel):
    activity: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Activity")
    application: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Application")
    attachment: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Attachment")
    candidate: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Candidate")
    department: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Department")
    eeoc: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="EEOC")
    scheduled_interview: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="ScheduledInterview"
    )
    job: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Job")
    job_interview_stage: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(
        alias="JobInterviewStage"
    )
    offer: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Offer")
    office: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Office")
    reject_reason: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="RejectReason")
    scorecard: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Scorecard")
    tag: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="Tag")
    remote_user: typing.Optional[typing.List[FieldMappingApiInstance]] = pydantic.Field(alias="RemoteUser")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
