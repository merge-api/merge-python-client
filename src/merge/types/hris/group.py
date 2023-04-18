# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The group name."""

    parent_group: Optional[str]
    """The parent group for this group."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    type: Optional[Literal["TEAM", "DEPARTMENT", "COST_CENTER", "BUSINESS_UNIT"]]
    """
    - `TEAM` - TEAM
    - `DEPARTMENT` - DEPARTMENT
    - `COST_CENTER` - COST_CENTER
    - `BUSINESS_UNIT` - BUSINESS_UNIT
    """
