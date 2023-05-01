# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IgnoreCommonModel"]


class IgnoreCommonModel(TypedDict, total=False):
    reason: Required[Literal["GENERAL_CUSTOMER_REQUEST", "GDPR", "OTHER"]]
    """
    - `GENERAL_CUSTOMER_REQUEST` - GENERAL_CUSTOMER_REQUEST
    - `GDPR` - GDPR
    - `OTHER` - OTHER
    """

    message: str
