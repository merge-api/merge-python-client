# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Job", "JobPostingURL"]


class JobPostingURL(BaseModel):
    url_type: Optional[Literal["PERSONAL", "COMPANY", "PORTFOLIO", "BLOG", "SOCIAL_MEDIA", "OTHER", "JOB_POSTING"]]
    """
    - `PERSONAL` - PERSONAL
    - `COMPANY` - COMPANY
    - `PORTFOLIO` - PORTFOLIO
    - `BLOG` - BLOG
    - `SOCIAL_MEDIA` - SOCIAL_MEDIA
    - `OTHER` - OTHER
    - `JOB_POSTING` - JOB_POSTING
    """

    value: Optional[str]
    """The site's url."""


class Job(BaseModel):
    code: Optional[str]
    """The job's code.

    Typically an additional identifier used to reference the particular job that is
    displayed on the ATS.
    """

    confidential: Optional[bool]
    """Whether the job is confidential."""

    departments: Optional[List[Optional[str]]]
    """IDs of `Department` objects for this `Job`."""

    description: Optional[str]
    """The job's description."""

    field_mappings: Optional[object]

    hiring_managers: Optional[List[Optional[str]]]
    """IDs of `RemoteUser` objects that serve as hiring managers for this `Job`."""

    id: Optional[str]

    job_posting_urls: Optional[List[JobPostingURL]]

    name: Optional[str]
    """The job's name."""

    offices: Optional[List[Optional[str]]]
    """IDs of `Office` objects for this `Job`."""

    recruiters: Optional[List[Optional[str]]]
    """IDs of `RemoteUser` objects that serve as recruiters for this `Job`."""

    remote_created_at: Optional[datetime]
    """When the third party's job was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the third party's job was updated."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    status: Optional[Literal["OPEN", "CLOSED", "DRAFT", "ARCHIVED", "PENDING"]]
    """
    - `OPEN` - OPEN
    - `CLOSED` - CLOSED
    - `DRAFT` - DRAFT
    - `ARCHIVED` - ARCHIVED
    - `PENDING` - PENDING
    """
