# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AssociationType", "TargetObjectClass"]


class TargetObjectClass(BaseModel):
    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    origin_type: Optional[str]


class AssociationType(BaseModel):
    cardinality: Optional[Literal["ONE_TO_ONE", "MANY_TO_ONE", "MANY_TO_MANY", "ONE_TO_MANY"]]
    """
    - `ONE_TO_ONE` - ONE_TO_ONE
    - `MANY_TO_ONE` - MANY_TO_ONE
    - `MANY_TO_MANY` - MANY_TO_MANY
    - `ONE_TO_MANY` - ONE_TO_MANY
    """

    display_name: Optional[str]

    id: Optional[str]

    is_required: Optional[bool]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_key_name: Optional[str]

    source_object_class: Optional[object]

    target_object_classes: Optional[List[TargetObjectClass]]
