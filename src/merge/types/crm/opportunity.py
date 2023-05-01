# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Opportunity", "RemoteField"]


class RemoteField(BaseModel):
    remote_field_class: shared.RemoteFieldClass

    value: Optional[object]


class Opportunity(BaseModel):
    account: Optional[str]
    """The account of the opportunity."""

    amount: Optional[int]
    """The opportunity's amount."""

    close_date: Optional[datetime]
    """When the opportunity was closed."""

    description: Optional[str]
    """The opportunity's description."""

    field_mappings: Optional[object]

    id: Optional[str]

    last_activity_at: Optional[datetime]
    """When the opportunity's last activity occurred."""

    name: Optional[str]
    """The opportunity's name."""

    owner: Optional[str]
    """The opportunity's owner."""

    remote_created_at: Optional[datetime]
    """When the third party's opportunity was created."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_fields: Optional[List[RemoteField]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]

    stage: Optional[str]
    """The stage of the opportunity."""

    status: Optional[Literal["OPEN", "WON", "LOST"]]
    """
    - `OPEN` - OPEN
    - `WON` - WON
    - `LOST` - LOST
    """
