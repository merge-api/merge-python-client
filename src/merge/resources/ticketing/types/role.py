# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .role_ticket_actions_item import RoleTicketActionsItem
from .role_ticket_access import RoleTicketAccess
from .remote_data import RemoteData
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class Role(UniversalBaseModel):
    """
    # The Role Object

    ### Description

    The `Role` object is used to represent the set of actions & access that a user with this role is allowed to perform.

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
    The name of the Role.
    """

    ticket_actions: typing.Optional[typing.List[typing.Optional[RoleTicketActionsItem]]] = pydantic.Field()
    """
    The set of actions that a User with this Role can perform. Possible enum values include: `VIEW`, `CREATE`, `EDIT`, `DELETE`, `CLOSE`, and `ASSIGN`.
    """

    ticket_access: typing.Optional[RoleTicketAccess] = pydantic.Field()
    """
    The level of Ticket access that a User with this Role can perform.
    
    - `ALL` - ALL
    - `ASSIGNED_ONLY` - ASSIGNED_ONLY
    - `TEAM_ONLY` - TEAM_ONLY
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
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
