# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .permission_request_group import PermissionRequestGroup
from .permission_request_roles_item import PermissionRequestRolesItem
from .permission_request_type import PermissionRequestType
from .permission_request_user import PermissionRequestUser

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PermissionRequest(pydantic.BaseModel):
    """
    # The Permission Object
    ### Description
    The Permission object is used to represent a user's or group's access to a File or Folder. Permissions are unexpanded by default.

    ### Usage Example
    Fetch from the `GET Files` or `GET Folders` endpoint. Permissions are unexpanded by default. Use the query param `expand=permissions` to see more details.
    """

    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    user: typing.Optional[PermissionRequestUser] = pydantic.Field(
        description="The user that is granted this permission."
    )
    group: typing.Optional[PermissionRequestGroup] = pydantic.Field(
        description="The group that is granted this permission."
    )
    type: typing.Optional[PermissionRequestType] = pydantic.Field(
        description=(
            "Denotes what type of people have access to the file.\n"
            "\n"
            "* `USER` - USER\n"
            "* `GROUP` - GROUP\n"
            "* `COMPANY` - COMPANY\n"
            "* `ANYONE` - ANYONE\n"
        )
    )
    roles: typing.Optional[typing.List[typing.Optional[PermissionRequestRolesItem]]] = pydantic.Field(
        description="The permissions that the user or group has for the File or Folder. It is possible for a user or group to have multiple roles, such as viewing & uploading. Possible values include: `READ`, `WRITE`, `OWNER`. In cases where there is no clear mapping, the original value passed through will be returned."
    )
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
