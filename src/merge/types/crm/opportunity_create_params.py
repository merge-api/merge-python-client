# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OpportunityCreateParams", "Model"]


class Model(TypedDict, total=False):
    account: Optional[str]
    """The account of the opportunity."""

    amount: Optional[int]
    """The opportunity's amount."""

    close_date: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the opportunity was closed."""

    description: Optional[str]
    """The opportunity's description."""

    integration_params: Optional[object]

    last_activity_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """When the opportunity's last activity occurred."""

    linked_account_params: Optional[object]

    name: Optional[str]
    """The opportunity's name."""

    owner: Optional[str]
    """The opportunity's owner."""

    stage: Optional[str]
    """The stage of the opportunity."""

    status: Literal["OPEN", "WON", "LOST"]
    """
    - `OPEN` - OPEN
    - `WON` - WON
    - `LOST` - LOST
    """


class OpportunityCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Opportunity Object

    ### Description

    The `Opportunity` object is used to represent a deal opportunity in a CRM
    system.

    ### Usage Example

    TODO
    """
