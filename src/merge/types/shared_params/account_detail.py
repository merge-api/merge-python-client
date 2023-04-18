# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccountDetail"]


class AccountDetail(TypedDict, total=False):
    category: Literal["hris", "ats", "accounting", "ticketing", "crm", "mktg", "filestorage"]
    """
    - `hris` - hris
    - `ats` - ats
    - `accounting` - accounting
    - `ticketing` - ticketing
    - `crm` - crm
    - `mktg` - mktg
    - `filestorage` - filestorage
    """
