# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["Item"]


class Item(BaseModel):
    company: Optional[str]
    """The company the item belongs to."""

    field_mappings: Optional[object]

    id: Optional[str]

    name: Optional[str]
    """The item's name."""

    purchase_account: Optional[str]
    """References the default account used to record a purchase of the item."""

    purchase_price: Optional[float]
    """The price at which the item is purchased from a vendor."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_updated_at: Optional[datetime]
    """When the third party's item note was updated."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    sales_account: Optional[str]
    """References the default account used to record a sale."""

    status: Optional[Literal["ACTIVE", "ARCHIVED"]]
    """
    - `ACTIVE` - ACTIVE
    - `ARCHIVED` - ARCHIVED
    """

    unit_price: Optional[float]
    """The item's unit price."""
