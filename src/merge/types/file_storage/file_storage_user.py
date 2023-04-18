# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["FileStorageUser"]


class FileStorageUser(BaseModel):
    email_address: Optional[str]
    """The user’s email address.

    This is typically used to identify a user across linked accounts.
    """

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The user's name."""

    remote_data: Optional[List[Optional[object]]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""
