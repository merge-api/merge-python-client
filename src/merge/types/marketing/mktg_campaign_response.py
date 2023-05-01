# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel
from ...types.marketing import campaign

__all__ = ["MktgCampaignResponse"]


class MktgCampaignResponse(BaseModel):
    errors: List[shared.ValidationError]

    model: campaign.Campaign
    """# The Campaign Object

    ### Description

    The `Campaign` object is used to represent a marketing campaign in the remote
    system.

    ### Usage Example

    Fetch from the `GET /api/mktg/v1/campaigns` endpoint and view their unique
    opens.
    """

    warnings: List[shared.ValidationWarning]

    logs: Optional[List[shared.DebugLog]]
