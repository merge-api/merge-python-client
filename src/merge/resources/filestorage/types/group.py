# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Group(UniversalBaseModel):
    """
    # The Group Object

    ### Description

    The `Group` object is used to represent any subset of `User`s. This can extend to company domains as well.

    ### Usage Example

    Fetch from the `GET /api/filestorage/v1/groups` endpoint and view their groups.
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
    The group's name.
    """

    users: typing.List[str] = pydantic.Field()
    """
    The users that belong in the group. If null, this typically means it's either a domain or the third-party platform does not surface this information.
    """

    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[typing.Optional[typing.Dict[str, typing.Any]]]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
