# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

from ....core.datetime_utils import serialize_datetime
from .application_credited_to import ApplicationCreditedTo
from .application_current_stage import ApplicationCurrentStage
from .application_job import ApplicationJob
from .application_reject_reason import ApplicationRejectReason
from .remote_data import RemoteData


class Application(pydantic.BaseModel):
    """
    # The Application Object
    ### Description
    The Application Object is used to represent a candidate's journey through a particular Job's recruiting process. If a Candidate applies for multiple Jobs, there will be a separate Application for each Job if the third-party integration allows it.

    ### Usage Example
    Fetch from the `LIST Applications` endpoint and filter by `ID` to show all applications.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    candidate: typing.Optional[ApplicationCandidate] = pydantic.Field(description="The candidate applying.")
    job: typing.Optional[ApplicationJob] = pydantic.Field(description="The job being applied for.")
    applied_at: typing.Optional[dt.datetime] = pydantic.Field(description="When the application was submitted.")
    rejected_at: typing.Optional[dt.datetime] = pydantic.Field(description="When the application was rejected.")
    source: typing.Optional[str] = pydantic.Field(description="The application's source.")
    credited_to: typing.Optional[ApplicationCreditedTo] = pydantic.Field(
        description="The user credited for this application."
    )
    current_stage: typing.Optional[ApplicationCurrentStage] = pydantic.Field(
        description="The application's current stage."
    )
    reject_reason: typing.Optional[ApplicationRejectReason] = pydantic.Field(
        description="The application's reason for rejection."
    )
    remote_was_deleted: typing.Optional[bool]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}


from .application_candidate import ApplicationCandidate  # noqa: E402

Application.update_forward_refs()
