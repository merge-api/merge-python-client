# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .engagement_account import EngagementAccount
from .engagement_contacts_item import EngagementContactsItem
from .engagement_direction import EngagementDirection
from .engagement_engagement_type import EngagementEngagementType
from .engagement_owner import EngagementOwner
from .remote_data import RemoteData
from .remote_field import RemoteField


class Engagement(UniversalBaseModel):
    """
    # The Engagement Object

    ### Description

    The `Engagement` object is used to represent an interaction noted in a CRM system.

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

    owner: typing.Optional[EngagementOwner] = pydantic.Field()
    """
    The engagement's owner.
    """

    content: typing.Optional[str] = pydantic.Field()
    """
    The engagement's content.
    """

    subject: typing.Optional[str] = pydantic.Field()
    """
    The engagement's subject.
    """

    direction: typing.Optional[EngagementDirection] = pydantic.Field()
    """
    The engagement's direction.
    
    - `INBOUND` - INBOUND
    - `OUTBOUND` - OUTBOUND
    """

    engagement_type: typing.Optional[EngagementEngagementType] = pydantic.Field()
    """
    The engagement type of the engagement.
    """

    start_time: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The time at which the engagement started.
    """

    end_time: typing.Optional[dt.datetime] = pydantic.Field()
    """
    The time at which the engagement ended.
    """

    account: typing.Optional[EngagementAccount] = pydantic.Field()
    """
    The account of the engagement.
    """

    contacts: typing.Optional[typing.List[typing.Optional[EngagementContactsItem]]]
    remote_was_deleted: typing.Optional[bool] = pydantic.Field()
    """
    Indicates whether or not this object has been deleted in the third party platform.
    """

    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]
    remote_fields: typing.Optional[typing.List[RemoteField]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
