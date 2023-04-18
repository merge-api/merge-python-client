# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FolderCreateParams", "Model"]


class Model(TypedDict, total=False):
    permissions: Required[List[str]]
    """
    The Permission object is used to represent a user's or group's access to a File
    or Folder. Permissions are unexpanded by default. Use the query param
    `expand=permissions` to see more details under `GET /folders`.
    """

    description: Optional[str]
    """The folder's description."""

    drive: Optional[str]
    """The drive that the folder belongs to."""

    folder_url: Optional[str]
    """The URL to access the folder."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    name: Optional[str]
    """The folder's name."""

    parent_folder: Optional[str]
    """The folder that the folder belongs to."""

    size: Optional[int]
    """The folder's size, in bytes."""


class FolderCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Folder Object

    ### Description

    The `Folder` object is used to represent a collection of files and/or folders in
    the workspace. Could be within a drive, if it exsts.

    ### Usage Example

    Fetch from the `GET /api/filestorage/v1/folders` endpoint and view their
    folders.
    """
