# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["FileStorageGroup"]


class FileStorageGroup(BaseModel):
    users: List[str]
    """The users that belong in the group.

    If null, this typically means it's either a domain or the third-party platform
    does not surface this information.
    """

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The group's name."""

    remote_data: Optional[List[Optional[object]]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""
