# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...types import shared
from ..._models import BaseModel

__all__ = ["Application"]


class Application(BaseModel):
    applied_at: Optional[datetime]
    """When the application was submitted."""

    candidate: Optional[str]
    """The candidate applying."""

    credited_to: Optional[str]
    """The user credited for this application."""

    current_stage: Optional[str]
    """The application's current stage."""

    field_mappings: Optional[object]

    id: Optional[str]

    job: Optional[str]
    """The job being applied for."""

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    reject_reason: Optional[str]
    """The application's reason for rejection."""

    rejected_at: Optional[datetime]
    """When the application was rejected."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]

    source: Optional[str]
    """The application's source."""
