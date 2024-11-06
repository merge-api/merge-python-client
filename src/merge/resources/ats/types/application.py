# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .application_job import ApplicationJob
from .application_credited_to import ApplicationCreditedTo
from .application_screening_question_answers_item import ApplicationScreeningQuestionAnswersItem
from .application_current_stage import ApplicationCurrentStage
from .application_reject_reason import ApplicationRejectReason
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.pydantic_utilities import update_forward_refs


class Application(UniversalBaseModel):
    """
    # The Application Object

    ### Description

    The Application Object is used to represent a candidate's journey through a particular Job's recruiting process. If a Candidate applies for multiple Jobs, there will be a separate Application for each Job if the third-party integration allows it.

    ### Usage Example

    Fetch from the `LIST Applications` endpoint and filter by `ID` to show all applications.
    """

    id: typing.Optional[str] = None
    remote_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was modified by Merge.
    """

    candidate: typing.Optional["ApplicationCandidate"] = pydantic.Field(default=None)
    """
    The candidate applying.
    """

    job: typing.Optional[ApplicationJob] = pydantic.Field(default=None)
    """
    The job being applied for.
    """

    applied_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the application was submitted.
    """

    rejected_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the application was rejected.
    """

    offers: typing.Optional[typing.List[typing.Optional["ApplicationOffersItem"]]] = None
    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The application's source.
    """

    credited_to: typing.Optional[ApplicationCreditedTo] = pydantic.Field(default=None)
    """
    The user credited for this application.
    """

    screening_question_answers: typing.Optional[typing.List[ApplicationScreeningQuestionAnswersItem]] = None
    current_stage: typing.Optional[ApplicationCurrentStage] = pydantic.Field(default=None)
    """
    The application's current stage.
    """

    reject_reason: typing.Optional[ApplicationRejectReason] = pydantic.Field(default=None)
    """
    The application's reason for rejection.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    remote_data: typing.Optional[typing.List[RemoteData]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .candidate import Candidate  # noqa: E402
from .offer import Offer  # noqa: E402
from .application_candidate import ApplicationCandidate  # noqa: E402
from .application_offers_item import ApplicationOffersItem  # noqa: E402

update_forward_refs(Candidate, Application=Application)
update_forward_refs(Offer, Application=Application)
update_forward_refs(Application)
