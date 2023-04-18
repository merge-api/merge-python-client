# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CommonModelScopeRetrieveParams"]


class CommonModelScopeRetrieveParams(TypedDict, total=False):
    linked_account_id: str
    """ID of specific linked account to fetch"""
