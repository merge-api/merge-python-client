# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SyncStatus"]


class SyncStatus(TypedDict, total=False):
    is_initial_sync: Required[bool]

    model_id: Required[str]

    model_name: Required[str]

    status: Required[Literal["SYNCING", "DONE", "FAILED", "DISABLED", "PAUSED"]]
    """
    - `SYNCING` - SYNCING
    - `DONE` - DONE
    - `FAILED` - FAILED
    - `DISABLED` - DISABLED
    - `PAUSED` - PAUSED
    """

    last_sync_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    next_sync_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    selective_sync_configurations_usage: Literal["IN_NEXT_SYNC", "IN_LAST_SYNC"]
    """
    - `IN_NEXT_SYNC` - IN_NEXT_SYNC
    - `IN_LAST_SYNC` - IN_LAST_SYNC
    """
