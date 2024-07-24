# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .patched_engagement_request_direction import PatchedEngagementRequestDirection
from .remote_field_request import RemoteFieldRequest


class PatchedEngagementRequest(UniversalBaseModel):
    """
    # The Engagement Object

    ### Description

    The `Engagement` object is used to represent an interaction noted in a CRM system.

    ### Usage Example

    TODO
    """

    owner: typing.Optional[str] = pydantic.Field()
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

    direction: typing.Optional[PatchedEngagementRequestDirection] = pydantic.Field()
    """
    The engagement's direction.
    
    - `INBOUND` - INBOUND
    - `OUTBOUND` - OUTBOUND
    """

    engagement_type: typing.Optional[str] = pydantic.Field()
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

    account: typing.Optional[str] = pydantic.Field()
    """
    The account of the engagement.
    """

    contacts: typing.Optional[typing.List[typing.Optional[str]]]
    integration_params: typing.Optional[typing.Dict[str, typing.Any]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Any]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
