# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .remote_data import RemoteData
from .remote_user_access_role import RemoteUserAccessRole

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RemoteUser(pydantic.BaseModel):
    """
    # The RemoteUser Object
    ### Description
    The `RemoteUser` object is used to represent a user with a login to the ATS system.
    ### Usage Example
    Fetch from the `LIST RemoteUsers` endpoint to show all users for a third party.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    first_name: typing.Optional[str] = pydantic.Field(description="The user's first name.")
    last_name: typing.Optional[str] = pydantic.Field(description="The user's last name.")
    email: typing.Optional[str] = pydantic.Field(description="The user's email.")
    disabled: typing.Optional[bool] = pydantic.Field(description="Whether the user's account had been disabled.")
    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="When the third party's user was created."
    )
    access_role: typing.Optional[RemoteUserAccessRole] = pydantic.Field(
        description=(
            "The user's role.\n"
            "\n"
            "* `SUPER_ADMIN` - SUPER_ADMIN\n"
            "* `ADMIN` - ADMIN\n"
            "* `TEAM_MEMBER` - TEAM_MEMBER\n"
            "* `LIMITED_TEAM_MEMBER` - LIMITED_TEAM_MEMBER\n"
            "* `INTERVIEWER` - INTERVIEWER\n"
        )
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted in the third party platform."
    )
    created_at: typing.Optional[dt.datetime]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

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
