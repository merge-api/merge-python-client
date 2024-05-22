# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .job_posting_job import JobPostingJob
from .job_posting_job_posting_urls_item import JobPostingJobPostingUrlsItem
from .job_posting_status_enum import JobPostingStatusEnum
from .remote_data import RemoteData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class JobPosting(pydantic.BaseModel):
    """
    # The JobPosting Object

    ### Description

    The `JobPosting` object represents an external announcement on a job board created by an organization to attract qualified candidates to apply for a specific `Job` opening

    ### Usage Example

    Fetch from the `LIST JobPostings` endpoint to show all job postings.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="The datetime that this object was created by Merge."
    )
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="The datetime that this object was modified by Merge."
    )
    title: typing.Optional[str] = pydantic.Field(description="The job posting’s title.")
    job_posting_urls: typing.Optional[typing.List[JobPostingJobPostingUrlsItem]] = pydantic.Field(
        description="The Url object is used to represent hyperlinks for a candidate to apply to a given job."
    )
    job: typing.Optional[JobPostingJob] = pydantic.Field(description="ID of `Job` object for this `JobPosting`.")
    status: typing.Optional[JobPostingStatusEnum] = pydantic.Field(
        description=(
            "The job posting's status.\n"
            "\n"
            "- `PUBLISHED` - PUBLISHED\n"
            "- `CLOSED` - CLOSED\n"
            "- `DRAFT` - DRAFT\n"
            "- `INTERNAL` - INTERNAL\n"
            "- `PENDING` - PENDING\n"
        )
    )
    content: typing.Optional[str] = pydantic.Field(description="The job posting’s content.")
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's job posting was created."
    )
    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's job posting was updated."
    )
    is_internal: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether the job posting is internal or external."
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted in the third party platform."
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
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
