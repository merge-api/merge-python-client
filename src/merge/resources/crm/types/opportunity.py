# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2
from ....core.unchecked_base_model import UncheckedBaseModel
from .opportunity_account import OpportunityAccount
from .opportunity_owner import OpportunityOwner
from .opportunity_stage import OpportunityStage
from .opportunity_status import OpportunityStatus
from .remote_data import RemoteData
from .remote_field import RemoteField


class Opportunity(UncheckedBaseModel):
    """
    # The Opportunity Object
    ### Description
    The `Opportunity` object is used to represent a deal opportunity in a CRM system.
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
    The opportunity's name.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The opportunity's description.
    """

    amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    The opportunity's amount.
    """

    owner: typing.Optional[OpportunityOwner] = pydantic.Field(default=None)
    """
    The opportunity's owner.
    """

    account: typing.Optional[OpportunityAccount] = pydantic.Field(default=None)
    """
    The account of the opportunity.
    """

    stage: typing.Optional[OpportunityStage] = pydantic.Field(default=None)
    """
    The stage of the opportunity.
    """

    status: typing.Optional[OpportunityStatus] = pydantic.Field(default=None)
    """
    The opportunity's status.
    
    * `OPEN` - OPEN
    * `WON` - WON
    * `LOST` - LOST
    """

    last_activity_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the opportunity's last activity occurred.
    """

    close_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the opportunity was closed.
    """

    remote_created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the third party's opportunity was created.
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
