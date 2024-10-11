# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .remote_user_access_role import RemoteUserAccessRole
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class RemoteUser(UniversalBaseModel):
    """
    # The RemoteUser Object

    ### Description

    The `RemoteUser` object is used to represent a user with a login to the ATS system.

    ### Usage Example

    Fetch from the `LIST RemoteUsers` endpoint to show all users for a third party.
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

    first_name: typing.Optional[str] = pydantic.Field()
    """
    The user's first name.
    """

    last_name: typing.Optional[str] = pydantic.Field()
    """
    The user's last name.
    """

    email: typing.Optional[str] = pydantic.Field()
    """
    The user's email.
    """

    disabled: typing.Optional[bool] = pydantic.Field()
    """
    Whether the user's account had been disabled.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the third party's user was created.
    """

    access_role: typing.Optional[RemoteUserAccessRole] = pydantic.Field()
    """
    The user's role.
    
    - `SUPER_ADMIN` - SUPER_ADMIN
    - `ADMIN` - ADMIN
    - `TEAM_MEMBER` - TEAM_MEMBER
    - `LIMITED_TEAM_MEMBER` - LIMITED_TEAM_MEMBER
    - `INTERVIEWER` - INTERVIEWER
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
