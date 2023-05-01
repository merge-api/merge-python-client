# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["TrackingCategory"]


class TrackingCategory(BaseModel):
    category_type: Optional[Literal["CLASS", "DEPARTMENT"]]
    """
    - `CLASS` - CLASS
    - `DEPARTMENT` - DEPARTMENT
    """

    company: Optional[str]
    """The company the tracking category belongs to."""

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The tracking category's name."""

    parent_category: Optional[str]
    """ID of the parent tracking category."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    status: Optional[Literal["ACTIVE", "ARCHIVED"]]
    """
    - `ACTIVE` - ACTIVE
    - `ARCHIVED` - ARCHIVED
    """
