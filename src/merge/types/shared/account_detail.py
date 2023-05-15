# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountDetail"]


class AccountDetail(BaseModel):
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

    end_user_email_address: Optional[str]

    end_user_organization_name: Optional[str]

    end_user_origin_id: Optional[str]

    id: Optional[str]

    integration: Optional[str]

    integration_slug: Optional[str]

    is_duplicate: Optional[bool]
    """
    Whether a Production Linked Account's credentials match another existing
    Production Linked Account. This field is `null` for Test Linked Accounts,
    incomplete Production Linked Accounts, and ignored duplicate Production Linked
    Account sets.
    """

    status: Optional[str]

    webhook_listener_url: Optional[str]
