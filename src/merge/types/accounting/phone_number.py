# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PhoneNumber"]


class PhoneNumber(BaseModel):
    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    number: Optional[str]
    """The phone number."""

    type: Optional[str]
    """The phone number's type."""
