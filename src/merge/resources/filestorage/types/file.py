# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from .folder import Folder
import typing
import pydantic
import datetime as dt
from .file_folder import FileFolder
from .file_permissions import FilePermissions
from .file_drive import FileDrive
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.pydantic_utilities import update_forward_refs


class File(UniversalBaseModel):
    """
    # The File Object

    ### Description

    The `File` object is used to represent a file in the workspace. The Object typically exists under a folder or drive, if it exists.

    ### Usage Example

    Fetch from the `GET /api/filestorage/v1/files` endpoint and view their files.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The datetime that this object was modified by Merge.
    """

    name: typing.Optional[str] = pydantic.Field()
    """
    The file's name.
    """

    file_url: typing.Optional[str] = pydantic.Field()
    """
    The URL to access the file.
    """

    file_thumbnail_url: typing.Optional[str] = pydantic.Field()
    """
    The URL that produces a thumbnail preview of the file. Typically an image.
    """

    size: typing.Optional[int] = pydantic.Field()
    """
    The file's size, in bytes.
    """

    mime_type: typing.Optional[str] = pydantic.Field()
    """
    The file's mime type.
    """

    description: typing.Optional[str] = pydantic.Field()
    """
    The file's description.
    """

    folder: typing.Optional[FileFolder] = pydantic.Field()
    """
    The folder that the file belongs to.
    """

    permissions: typing.Optional[FilePermissions] = pydantic.Field()
    """
    The Permission object is used to represent a user's or group's access to a File or Folder. Permissions are unexpanded by default. Use the query param `expand=permissions` to see more details under `GET /files`.
    """

    drive: typing.Optional[FileDrive] = pydantic.Field()
    """
    The drive that the file belongs to.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's file was created.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's file was updated.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    remote_data: typing.Optional[typing.List[typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Folder, File=File)
