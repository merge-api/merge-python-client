# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileCreateParams", "Model"]


class Model(TypedDict, total=False):
    permissions: Required[List[str]]
    """
    The Permission object is used to represent a user's or group's access to a File
    or Folder. Permissions are unexpanded by default. Use the query param
    `expand=permissions` to see more details under `GET /files`.
    """

    description: Optional[str]
    """The file's description."""

    drive: Optional[str]
    """The drive that the file belongs to."""

    file_thumbnail_url: Optional[str]
    """The URL that produces a thumbnail preview of the file. Typically an image."""

    file_url: Optional[str]
    """The URL to access the file."""

    folder: Optional[str]
    """The folder that the file belongs to."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    mime_type: Optional[str]
    """The file's mime type."""

    name: Optional[str]
    """The file's name."""

    size: Optional[int]
    """The file's size, in bytes."""


class FileCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The File Object

    ### Description

    The `File` object is used to represent a file in the workspace. The Object
    typically exists under a folder or drive, if it exists.

    ### Usage Example

    Fetch from the `GET /api/filestorage/v1/files` endpoint and view their files.
    """
