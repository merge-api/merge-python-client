# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .application_credited_to import ApplicationCreditedTo
from .application_current_stage import ApplicationCurrentStage
from .application_job import ApplicationJob
from .application_reject_reason import ApplicationRejectReason
from .application_screening_question_answers_item import ApplicationScreeningQuestionAnswersItem
from .remote_data import RemoteData


class Application(pydantic_v1.BaseModel):
    """
    # The Application Object

    ### Description

    The Application Object is used to represent a candidate's journey through a particular Job's recruiting process. If a Candidate applies for multiple Jobs, there will be a separate Application for each Job if the third-party integration allows it.

    ### Usage Example

    Fetch from the `LIST Applications` endpoint and filter by `ID` to show all applications.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic_v1.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was modified by Merge.
    """

    candidate: typing.Optional[ApplicationCandidate] = pydantic_v1.Field()
    """
    The candidate applying.
    """

    job: typing.Optional[ApplicationJob] = pydantic_v1.Field()
    """
    The job being applied for.
    """

    applied_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the application was submitted.
    """

    rejected_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the application was rejected.
    """

    offers: typing.Optional[typing.List[typing.Optional[ApplicationOffersItem]]]
    source: typing.Optional[str] = pydantic_v1.Field()
    """
    The application's source.
    """

    credited_to: typing.Optional[ApplicationCreditedTo] = pydantic_v1.Field()
    """
    The user credited for this application.
    """

    screening_question_answers: typing.Optional[typing.List[ApplicationScreeningQuestionAnswersItem]]
    current_stage: typing.Optional[ApplicationCurrentStage] = pydantic_v1.Field()
    """
    The application's current stage.
    """

    reject_reason: typing.Optional[ApplicationRejectReason] = pydantic_v1.Field()
    """
    The application's reason for rejection.
    """

    remote_was_deleted: typing.Optional[bool]
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


from .application_candidate import ApplicationCandidate  # noqa: E402
from .application_offers_item import ApplicationOffersItem  # noqa: E402

Application.update_forward_refs()
