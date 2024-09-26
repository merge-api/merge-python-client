# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .job_status import JobStatus
from .job_type_enum import JobTypeEnum
from .url import Url
from .job_departments_item import JobDepartmentsItem
from .job_offices_item import JobOfficesItem
from .job_hiring_managers_item import JobHiringManagersItem
from .job_recruiters_item import JobRecruitersItem
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Job(UniversalBaseModel):
    """
    # The Job Object

    ### Description

    The `Job` object can be used to track any jobs that are currently or will be open/closed for applications.

    ### Usage Example

    Fetch from the `LIST Jobs` endpoint to show all job postings.
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

    name: typing.Optional[str] = pydantic.Field()
    """
    The job's name.
    """

    description: typing.Optional[str] = pydantic.Field()
    """
    The job's description.
    """

    code: typing.Optional[str] = pydantic.Field()
    """
    The job's code. Typically an additional identifier used to reference the particular job that is displayed on the ATS.
    """

    status: typing.Optional[JobStatus] = pydantic.Field()
    """
    The job's status.
    
    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    - `DRAFT` - DRAFT
    - `ARCHIVED` - ARCHIVED
    - `PENDING` - PENDING
    """

    type: typing.Optional[JobTypeEnum] = pydantic.Field()
    """
    The job's type.
    
    - `POSTING` - POSTING
    - `REQUISITION` - REQUISITION
    - `PROFILE` - PROFILE
    """

    job_postings: typing.Optional[typing.List[typing.Optional[str]]] = pydantic.Field()
    """
    IDs of `JobPosting` objects that serve as job postings for this `Job`.
    """

    job_posting_urls: typing.Optional[typing.List[Url]]
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's job was created.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's job was updated.
    """

    confidential: typing.Optional[bool] = pydantic.Field()
    """
    Whether the job is confidential.
    """

    departments: typing.Optional[typing.List[typing.Optional[JobDepartmentsItem]]] = pydantic.Field()
    """
    IDs of `Department` objects for this `Job`.
    """

    offices: typing.Optional[typing.List[typing.Optional[JobOfficesItem]]] = pydantic.Field()
    """
    IDs of `Office` objects for this `Job`.
    """

    hiring_managers: typing.Optional[typing.List[typing.Optional[JobHiringManagersItem]]] = pydantic.Field()
    """
    IDs of `RemoteUser` objects that serve as hiring managers for this `Job`.
    """

    recruiters: typing.Optional[typing.List[typing.Optional[JobRecruitersItem]]] = pydantic.Field()
    """
    IDs of `RemoteUser` objects that serve as recruiters for this `Job`.
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
