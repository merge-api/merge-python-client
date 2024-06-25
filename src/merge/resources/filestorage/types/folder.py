# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .folder_drive import FolderDrive
from .folder_permissions import FolderPermissions


class Folder(pydantic_v1.BaseModel):
    """
    # The Folder Object

    ### Description

    The `Folder` object is used to represent a collection of files and/or folders in the workspace. Could be within a drive, if it exists.

    ### Usage Example

    Fetch from the `GET /api/filestorage/v1/folders` endpoint and view their folders.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic_v1.Field()
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    The datetime that this object was modified by Merge.
    """

    name: typing.Optional[str] = pydantic_v1.Field()
    """
    The folder's name.
    """

    folder_url: typing.Optional[str] = pydantic_v1.Field()
    """
    The URL to access the folder.
    """

    size: typing.Optional[int] = pydantic_v1.Field()
    """
    The folder's size, in bytes.
    """

    description: typing.Optional[str] = pydantic_v1.Field()
    """
    The folder's description.
    """

    parent_folder: typing.Optional[FolderParentFolder] = pydantic_v1.Field()
    """
    The folder that the folder belongs to.
    """

    drive: typing.Optional[FolderDrive] = pydantic_v1.Field()
    """
    The drive that the folder belongs to.
    """

    permissions: typing.Optional[FolderPermissions] = pydantic_v1.Field()
    """
    The Permission object is used to represent a user's or group's access to a File or Folder. Permissions are unexpanded by default. Use the query param `expand=permissions` to see more details under `GET /folders`.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the third party's folder was created.
    """

    remote_updated_at: typing.Optional[dt.datetime] = pydantic_v1.Field()
    """
    When the third party's folder was updated.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic_v1.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[typing.Optional[typing.Dict[str, typing.Any]]]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


from .folder_parent_folder import FolderParentFolder  # noqa: E402

Folder.update_forward_refs()
