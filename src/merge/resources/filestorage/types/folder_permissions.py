# This file was auto-generated by Fern from our API Definition.

import typing
from .permission_request import PermissionRequest
from .folder_permissions_item import FolderPermissionsItem

FolderPermissions = typing.Union[str, PermissionRequest, typing.List[FolderPermissionsItem]]
