# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IgnoreCommonModel"]


class IgnoreCommonModel(BaseModel):
    reason: Literal["GENERAL_CUSTOMER_REQUEST", "GDPR", "OTHER"]
    """
    - `GENERAL_CUSTOMER_REQUEST` - GENERAL_CUSTOMER_REQUEST
    - `GDPR` - GDPR
    - `OTHER` - OTHER
    """

    message: Optional[str]
