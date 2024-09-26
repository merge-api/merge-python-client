# This file was auto-generated by Fern from our API Definition.

from ....core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .opportunity_request_owner import OpportunityRequestOwner
from .opportunity_request_account import OpportunityRequestAccount
from .opportunity_request_stage import OpportunityRequestStage
from .opportunity_request_status import OpportunityRequestStatus
import datetime as dt
from .remote_field_request import RemoteFieldRequest
from ....core.pydantic_utilities import IS_PYDANTIC_V2


class OpportunityRequest(UniversalBaseModel):
    """
    # The Opportunity Object

    ### Description

    The `Opportunity` object is used to represent a deal opportunity in a CRM system.

    ### Usage Example

    TODO
    """

    name: typing.Optional[str] = pydantic.Field()
    """
    The opportunity's name.
    """

    description: typing.Optional[str] = pydantic.Field()
    """
    The opportunity's description.
    """

    amount: typing.Optional[int] = pydantic.Field()
    """
    The opportunity's amount.
    """

    owner: typing.Optional[OpportunityRequestOwner] = pydantic.Field()
    """
    The opportunity's owner.
    """

    account: typing.Optional[OpportunityRequestAccount] = pydantic.Field()
    """
    The account of the opportunity.
    """

    stage: typing.Optional[OpportunityRequestStage] = pydantic.Field()
    """
    The stage of the opportunity.
    """

    status: typing.Optional[OpportunityRequestStatus] = pydantic.Field()
    """
    The opportunity's status.
    
    - `OPEN` - OPEN
    - `WON` - WON
    - `LOST` - LOST
    """

    last_activity_at: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the opportunity's last activity occurred.
    """

    close_date: typing.Optional[dt.datetime] = pydantic.Field()
    """
    When the opportunity was closed.
    """

    integration_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    linked_account_params: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]
    remote_fields: typing.Optional[typing.List[RemoteFieldRequest]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
