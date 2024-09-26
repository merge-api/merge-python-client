# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .folder import Folder
import typing
import pydantic
from .folder_request_parent_folder import FolderRequestParentFolder
from .folder_request_drive import FolderRequestDrive
from .folder_request_permissions import FolderRequestPermissions
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.pydantic_utilities import update_forward_refs


class FolderRequest(UniversalBaseModel):
    """
    # The Folder Object

    ### Description

    The `Folder` object is used to represent a collection of files and/or folders in the workspace. Could be within a drive, if it exists.

    ### Usage Example

    Fetch from the `GET /api/filestorage/v1/folders` endpoint and view their folders.
    """

    name: typing.Optional[str] = pydantic.Field()
    """
    The folder's name.
    """

    folder_url: typing.Optional[str] = pydantic.Field()
    """
    The URL to access the folder.
    """

    size: typing.Optional[int] = pydantic.Field()
    """
    The folder's size, in bytes.
    """

    description: typing.Optional[str] = pydantic.Field()
    """
    The folder's description.
    """

    parent_folder: typing.Optional[FolderRequestParentFolder] = pydantic.Field()
    """
    The folder that the folder belongs to.
    """

    drive: typing.Optional[FolderRequestDrive] = pydantic.Field()
    """
    The drive that the folder belongs to.
    """

    permissions: typing.Optional[FolderRequestPermissions] = pydantic.Field()
    """
    The Permission object is used to represent a user's or group's access to a File or Folder. Permissions are unexpanded by default. Use the query param `expand=permissions` to see more details under `GET /folders`.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Folder, FolderRequest=FolderRequest)
