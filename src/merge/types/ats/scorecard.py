# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Scorecard"]


class Scorecard(BaseModel):
    application: Optional[str]
    """The application being scored."""

    field_mappings: Optional[object]

    id: Optional[str]

    interview: Optional[str]
    """The interview being scored."""

    interviewer: Optional[str]
    """The interviewer doing the scoring."""

    overall_recommendation: Optional[Literal["DEFINITELY_NO", "NO", "YES", "STRONG_YES", "NO_DECISION"]]
    """
    - `DEFINITELY_NO` - DEFINITELY_NO
    - `NO` - NO
    - `YES` - YES
    - `STRONG_YES` - STRONG_YES
    - `NO_DECISION` - NO_DECISION
    """

    remote_created_at: Optional[datetime]
    """When the third party's scorecard was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    submitted_at: Optional[datetime]
    """When the scorecard was submitted."""
