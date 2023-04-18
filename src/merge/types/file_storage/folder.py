# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Folder"]


class Folder(BaseModel):
    permissions: List[str]
    """
    The Permission object is used to represent a user's or group's access to a File
    or Folder. Permissions are unexpanded by default. Use the query param
    `expand=permissions` to see more details under `GET /folders`.
    """

    description: Optional[str]
    """The folder's description."""

    drive: Optional[str]
    """The drive that the folder belongs to."""

    field_mappings: Optional[object]

    folder_url: Optional[str]
    """The URL to access the folder."""

    id: Optional[str]

    name: Optional[str]
    """The folder's name."""

    parent_folder: Optional[str]
    """The folder that the folder belongs to."""

    remote_created_at: Optional[datetime]
    """When the third party's folder was created."""

    remote_data: Optional[List[Optional[object]]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the third party's folder was updated."""

    size: Optional[int]
    """The folder's size, in bytes."""
