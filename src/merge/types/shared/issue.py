# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Issue"]


class Issue(BaseModel):
    error_description: str

    end_user: Optional[str]

    error_details: Optional[List[str]]

    first_incident_time: Optional[datetime]

    id: Optional[str]

    is_muted: Optional[bool]

    last_incident_time: Optional[datetime]

    status: Optional[Literal["ONGOING", "RESOLVED"]]
    """
    - `ONGOING` - ONGOING
    - `RESOLVED` - RESOLVED
    """
