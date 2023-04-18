# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    description: Optional[str]
    """The file's description."""

    drive: Optional[str]
    """The drive that the file belongs to."""

    field_mappings: Optional[object]

    file_thumbnail_url: Optional[str]
    """The URL that produces a thumbnail preview of the file. Typically an image."""

    file_url: Optional[str]
    """The URL to access the file."""

    folder: Optional[str]
    """The folder that the file belongs to."""

    id: Optional[str]

    mime_type: Optional[str]
    """The file's mime type."""

    name: Optional[str]
    """The file's name."""

    remote_created_at: Optional[datetime]
    """When the third party's file was created."""

    remote_data: Optional[List[Optional[object]]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the third party's file was updated."""

    size: Optional[int]
    """The file's size, in bytes."""
