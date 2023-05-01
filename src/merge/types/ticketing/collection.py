# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Collection"]


class Collection(BaseModel):
    collection_type: Optional[Literal["LIST", "PROJECT"]]
    """
    - `LIST` - LIST
    - `PROJECT` - PROJECT
    """

    description: Optional[str]
    """The collection's description."""

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The collection's name."""

    parent_collection: Optional[str]
    """The parent collection for this collection."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""
