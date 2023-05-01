# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["LinkedAccountSelectiveSyncConfiguration", "LinkedAccountCondition"]


class LinkedAccountCondition(BaseModel):
    condition_schema_id: str
    """The ID indicating which condition schema to use for a specific condition."""

    field_name: Optional[str]
    """
    The name of the field on the common model that this condition corresponds to, if
    they conceptually match. e.g. "location_type".
    """

    native_name: Optional[str]
    """User-facing _native condition_ name. e.g. "Skip Manager"."""

    operator: str
    """The operator for a specific condition."""

    common_model: Optional[str]
    """The common model for a specific condition."""

    value: Optional[object]
    """The value for a condition."""


class LinkedAccountSelectiveSyncConfiguration(BaseModel):
    linked_account_conditions: Optional[List[LinkedAccountCondition]]
    """The conditions belonging to a selective sync."""
