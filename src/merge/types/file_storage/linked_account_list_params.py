# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["LinkedAccountListParams"]


class LinkedAccountListParams(TypedDict, total=False):
    category: Optional[Literal["accounting", "ats", "crm", "filestorage", "hris", "mktg", "ticketing"]]
    """
    - `hris` - hris
    - `ats` - ats
    - `accounting` - accounting
    - `ticketing` - ticketing
    - `crm` - crm
    - `mktg` - mktg
    - `filestorage` - filestorage

    - `hris` - hris
    - `ats` - ats
    - `accounting` - accounting
    - `ticketing` - ticketing
    - `crm` - crm
    - `mktg` - mktg
    - `filestorage` - filestorage
    """

    cursor: str
    """The pagination cursor value."""

    end_user_email_address: str
    """
    If provided, will only return linked accounts associated with the given email
    address.
    """

    end_user_organization_name: str
    """
    If provided, will only return linked accounts associated with the given
    organization name.
    """

    end_user_origin_id: str
    """
    If provided, will only return linked accounts associated with the given origin
    ID.
    """

    end_user_origin_ids: str
    """
    Comma-separated list of EndUser origin IDs, making it possible to specify
    multiple EndUsers at once.
    """

    id: str

    ids: str
    """
    Comma-separated list of LinkedAccount IDs, making it possible to specify
    multiple LinkedAccounts at once.
    """

    include_duplicates: bool
    """
    If `true`, will include complete production duplicates of the account specified
    by the `id` query parameter in the response. `id` must be for a complete
    production linked account.
    """

    integration_name: str
    """
    If provided, will only return linked accounts associated with the given
    integration name.
    """

    is_test_account: str
    """If included, will only include test linked accounts.

    If not included, will only include non-test linked accounts.
    """

    page_size: int
    """Number of results to return per page."""

    status: str
    """Filter by status. Options: `COMPLETE`, `INCOMPLETE`, `RELINK_NEEDED`"""
