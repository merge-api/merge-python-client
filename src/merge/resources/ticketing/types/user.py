# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .user_teams_item import UserTeamsItem
from .user_roles_item import UserRolesItem
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class User(UniversalBaseModel):
    """
    # The User Object

    ### Description

    The `User` object is used to represent an employee within a company.

    ### Usage Example

    TODO
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
    The user's name.
    """

    email_address: typing.Optional[str] = pydantic.Field()
    """
    The user's email address.
    """

    is_active: typing.Optional[bool] = pydantic.Field()
    """
    Whether or not the user is active.
    """

    teams: typing.Optional[typing.List[typing.Optional[UserTeamsItem]]]
    roles: typing.Optional[typing.List[typing.Optional[UserRolesItem]]]
    avatar: typing.Optional[str] = pydantic.Field()
    """
    The user's avatar picture.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
