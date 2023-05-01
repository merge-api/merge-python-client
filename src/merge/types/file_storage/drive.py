# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Drive"]


class Drive(BaseModel):
    drive_url: Optional[str]
    """The drive's url."""

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The drive's name."""

    remote_created_at: Optional[datetime]
    """When the third party's drive was created."""

    remote_data: Optional[List[Optional[object]]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""
