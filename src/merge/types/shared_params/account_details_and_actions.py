# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountDetailsAndActions", "Integration", "IntegrationAvailableModelOperation"]


class IntegrationAvailableModelOperation(TypedDict, total=False):
    available_operations: Required[List[str]]

    model_name: Required[str]

    required_post_parameters: Required[List[str]]

    supported_fields: Required[List[str]]


class Integration(TypedDict, total=False):
    categories: Required[List[Literal["hris", "ats", "accounting", "ticketing", "crm", "mktg", "filestorage"]]]

    color: Required[str]

    name: Required[str]

    passthrough_available: Required[bool]

    slug: Required[str]

    available_model_operations: List[IntegrationAvailableModelOperation]

    image: str

    square_image: str


class AccountDetailsAndActions(TypedDict, total=False):
    end_user_email_address: Required[str]

    end_user_organization_name: Required[str]

    id: Required[str]

    status: Required[Literal["COMPLETE", "INCOMPLETE", "RELINK_NEEDED"]]
    """
    - `COMPLETE` - COMPLETE
    - `INCOMPLETE` - INCOMPLETE
    - `RELINK_NEEDED` - RELINK_NEEDED
    """

    webhook_listener_url: Required[str]

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

    end_user_origin_id: str

    integration: Integration

    is_duplicate: Optional[bool]
    """
    Whether a Production Linked Account's credentials match another existing
    Production Linked Account. This field is `null` for Test Linked Accounts,
    incomplete Production Linked Accounts, and ignored duplicate Production Linked
    Account sets.
    """

    status_detail: str
