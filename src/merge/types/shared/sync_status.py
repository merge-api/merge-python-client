# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SyncStatus"]


class SyncStatus(BaseModel):
    is_initial_sync: bool

    model_id: str

    model_name: str

    status: Literal["SYNCING", "DONE", "FAILED", "DISABLED", "PAUSED"]
    """
    - `SYNCING` - SYNCING
    - `DONE` - DONE
    - `FAILED` - FAILED
    - `DISABLED` - DISABLED
    - `PAUSED` - PAUSED
    """

    last_sync_start: Optional[datetime]

    next_sync_start: Optional[datetime]

    selective_sync_configurations_usage: Optional[Literal["IN_NEXT_SYNC", "IN_LAST_SYNC"]]
    """
    - `IN_NEXT_SYNC` - IN_NEXT_SYNC
    - `IN_LAST_SYNC` - IN_LAST_SYNC
    """
