# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CampaignCreateParams", "Model"]


class Model(TypedDict, total=False):
    emails_sent: Optional[int]
    """The campaign's number of emails sent."""

    integration_params: Optional[object]

    linked_account_params: Optional[object]

    name: Optional[str]
    """The campaign's name."""

    unique_opens: Optional[int]
    """The campaign's unique opens."""


class CampaignCreateParams(TypedDict, total=False):
    model: Required[Model]
    """# The Campaign Object

    ### Description

    The `Campaign` object is used to represent a marketing campaign in the remote
    system.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/campaigns` endpoint and view their unique
    opens.
    """
