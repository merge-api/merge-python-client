# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EngagementUpdateParams", "Model"]


class Model(TypedDict, total=False):
    account: Optional[str]
    """The account of the engagement."""

    contacts: List[Optional[str]]

    content: Optional[str]
    """The engagement's content."""

    direction: Literal["INBOUND", "OUTBOUND"]
    """
    - `INBOUND` - INBOUND
    - `OUTBOUND` - OUTBOUND
    """

    end_time: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """The time at which the engagement ended."""

    engagement_type: Optional[str]
    """The engagement type of the engagement."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    owner: Optional[str]
    """The engagement's owner."""

    start_time: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """The time at which the engagement started."""

    subject: Optional[str]
    """The engagement's subject."""


class EngagementUpdateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Engagement Object

    ### Description

    The `Engagement` object is used to represent an interaction noted in a CRM
    system.

    ### Usage Example

    TODO
    """
