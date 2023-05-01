# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel

__all__ = ["JobInterviewStage"]


class JobInterviewStage(BaseModel):
    field_mappings: Optional[object]

    id: Optional[str]

    job: Optional[str]
    """This field is populated only if the stage is specific to a particular job.

    If the stage is generic, this field will not be populated.
    """

    name: Optional[str]
    """Standard stage names are offered by ATS systems but can be modified by users."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""
