# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from .remote_data import RemoteData
from .remote_field import RemoteField
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class User(UniversalBaseModel):
    """
    # The User Object

    ### Description

    The `User` object is used to represent a user with a login to the CRM system.

    ### Usage Example

    TODO
    """

    id: typing.Optional[str] = None
    remote_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The third-party API ID of the matching object.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was created by Merge.
    """

    modified_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime that this object was modified by Merge.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's name.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email address.
    """

    is_active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the user is active.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    remote_data: typing.Optional[typing.List[RemoteData]] = None
    remote_fields: typing.Optional[typing.List[RemoteField]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
