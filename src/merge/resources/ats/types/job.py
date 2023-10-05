# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

try:
    import pydantic.v1 as pydantic
except ImportError:
    import pydantic

from ....core.datetime_utils import serialize_datetime
from .job_departments_item import JobDepartmentsItem
from .job_hiring_managers_item import JobHiringManagersItem
from .job_offices_item import JobOfficesItem
from .job_recruiters_item import JobRecruitersItem
from .job_status import JobStatus
from .remote_data import RemoteData
from .url import Url


class Job(pydantic.BaseModel):
    """
    # The Job Object
    ### Description
    The `Job` object can be used to track any jobs that are currently or will be open/closed for applications.
    ### Usage Example
    Fetch from the `LIST Jobs` endpoint to show all job postings.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    name: typing.Optional[str] = pydantic.Field(description="The job's name.")
    description: typing.Optional[str] = pydantic.Field(description="The job's description.")
    code: typing.Optional[str] = pydantic.Field(
        description="The job's code. Typically an additional identifier used to reference the particular job that is displayed on the ATS."
    )
    status: typing.Optional[JobStatus] = pydantic.Field(
        description=(
            "The job's status.\n"
            "\n"
            "* `OPEN` - OPEN\n"
            "* `CLOSED` - CLOSED\n"
            "* `DRAFT` - DRAFT\n"
            "* `ARCHIVED` - ARCHIVED\n"
            "* `PENDING` - PENDING\n"
        )
    )
    job_posting_urls: typing.Optional[typing.List[Url]]
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's job was created."
    )
    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's job was updated."
    )
    confidential: typing.Optional[bool] = pydantic.Field(description="Whether the job is confidential.")
    departments: typing.Optional[typing.List[typing.Optional[JobDepartmentsItem]]] = pydantic.Field(
        description="IDs of `Department` objects for this `Job`."
    )
    offices: typing.Optional[typing.List[typing.Optional[JobOfficesItem]]] = pydantic.Field(
        description="IDs of `Office` objects for this `Job`."
    )
    hiring_managers: typing.Optional[typing.List[typing.Optional[JobHiringManagersItem]]] = pydantic.Field(
        description="IDs of `RemoteUser` objects that serve as hiring managers for this `Job`."
    )
    recruiters: typing.Optional[typing.List[typing.Optional[JobRecruitersItem]]] = pydantic.Field(
        description="IDs of `RemoteUser` objects that serve as recruiters for this `Job`."
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted by third party webhooks."
    )
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
