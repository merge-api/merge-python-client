# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .job_posting_job import JobPostingJob
from .job_posting_job_posting_urls_item import JobPostingJobPostingUrlsItem
from .job_posting_status import JobPostingStatus
from .remote_data import RemoteData


class JobPosting(UncheckedBaseModel):
    """
    # The JobPosting Object
    ### Description
    The `JobPosting` object represents an external announcement on a job board created by an organization to attract qualified candidates to apply for a specific `Job` opening
    ### Usage Example
    Fetch from the `LIST JobPostings` endpoint to show all job postings.
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

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The job posting’s title.
    """

    job_posting_urls: typing.Optional[typing.List[JobPostingJobPostingUrlsItem]] = pydantic.Field(default=None)
    """
    The Url object is used to represent hyperlinks for a candidate to apply to a given job.
    """

    job: typing.Optional[JobPostingJob] = pydantic.Field(default=None)
    """
    ID of `Job` object for this `JobPosting`.
    """

    status: typing.Optional[JobPostingStatus] = pydantic.Field(default=None)
    """
    The job posting's status.
    
    * `PUBLISHED` - PUBLISHED
    * `CLOSED` - CLOSED
    * `DRAFT` - DRAFT
    * `INTERNAL` - INTERNAL
    * `PENDING` - PENDING
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The job posting’s content.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the third party's job posting was created.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the third party's job posting was updated.
    """

    is_internal: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the job posting is internal or external.
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
