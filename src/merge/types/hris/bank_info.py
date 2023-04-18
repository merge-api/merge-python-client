# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._models import BaseModel

__all__ = ["BankInfo"]


class BankInfo(BaseModel):
    account_number: Optional[str]
    """The account number."""

    account_type: Optional[Literal["SAVINGS", "CHECKING"]]
    """
    - `SAVINGS` - SAVINGS
    - `CHECKING` - CHECKING
    """

    bank_name: Optional[str]
    """The bank name."""

    employee: Optional[str]
    """The employee with this bank account."""

    field_mappings: Optional[object]

    id: Optional[str]

    remote_created_at: Optional[datetime]
    """When the matching bank object was created in the third party system."""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    routing_number: Optional[str]
    """The routing number."""
