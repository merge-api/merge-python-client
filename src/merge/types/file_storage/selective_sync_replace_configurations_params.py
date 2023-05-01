# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SelectiveSyncReplaceConfigurationsParams", "SyncConfiguration", "SyncConfigurationLinkedAccountCondition"]


class SyncConfigurationLinkedAccountCondition(TypedDict, total=False):
    condition_schema_id: Required[str]
    """The ID indicating which condition schema to use for a specific condition."""

    operator: Required[str]
    """The operator for a specific condition."""

    value: Required[object]
    """The value for a specific condition."""


class SyncConfiguration(TypedDict, total=False):
    linked_account_conditions: Required[List[SyncConfigurationLinkedAccountCondition]]
    """The conditions belonging to a selective sync."""


class SelectiveSyncReplaceConfigurationsParams(TypedDict, total=False):
    sync_configurations: Required[List[SyncConfiguration]]
    """The selective syncs associated with a linked account."""
