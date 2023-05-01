# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountDetailsAndActions", "Integration", "IntegrationAvailableModelOperation"]


class IntegrationAvailableModelOperation(BaseModel):
    available_operations: List[str]

    model_name: str

    required_post_parameters: List[str]

    supported_fields: List[str]


class Integration(BaseModel):
    categories: List[Literal["hris", "ats", "accounting", "ticketing", "crm", "mktg", "filestorage"]]

    color: str

    name: str

    passthrough_available: bool

    slug: str

    available_model_operations: Optional[List[IntegrationAvailableModelOperation]]

    image: Optional[str]

    square_image: Optional[str]


class AccountDetailsAndActions(BaseModel):
    end_user_email_address: str

    end_user_organization_name: str

    id: str

    status: Literal["COMPLETE", "INCOMPLETE", "RELINK_NEEDED"]
    """
    - `COMPLETE` - COMPLETE
    - `INCOMPLETE` - INCOMPLETE
    - `RELINK_NEEDED` - RELINK_NEEDED
    """

    webhook_listener_url: str

    category: Optional[Literal["hris", "ats", "accounting", "ticketing", "crm", "mktg", "filestorage"]]
    """
    - `hris` - hris
    - `ats` - ats
    - `accounting` - accounting
    - `ticketing` - ticketing
    - `crm` - crm
    - `mktg` - mktg
    - `filestorage` - filestorage
    """

    end_user_origin_id: Optional[str]

    integration: Optional[Integration]

    is_duplicate: Optional[bool]
    """
    Whether a Production Linked Account's credentials match another existing
    Production Linked Account. This field is `null` for Test Linked Accounts,
    incomplete Production Linked Accounts, and ignored duplicate Production Linked
    Account sets.
    """

    status_detail: Optional[str]
