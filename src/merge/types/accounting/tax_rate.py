# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ...types import shared
from ..._models import BaseModel

__all__ = ["TaxRate"]


class TaxRate(BaseModel):
    company: Optional[str]
    """The company the tax rate belongs to."""

    description: Optional[str]
    """The tax rate's description."""

    effective_tax_rate: Optional[float]
    """The tax rate's effective tax rate."""

    field_mappings: Optional[object]

    id: Optional[str]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    remote_data: Optional[List[shared.RemoteData]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""

    remote_was_deleted: Optional[bool]
    """Indicates whether or not this object has been deleted by third party webhooks."""

    total_tax_rate: Optional[float]
    """The tax rate's total tax rate."""
