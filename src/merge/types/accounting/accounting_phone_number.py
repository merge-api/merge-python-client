# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AccountingPhoneNumber"]


class AccountingPhoneNumber(BaseModel):
    number: Optional[str]
    """The phone number."""

    type: Optional[str]
    """The phone number's type."""
