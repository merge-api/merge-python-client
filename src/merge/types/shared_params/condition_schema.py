# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConditionSchema", "Operator"]


class Operator(TypedDict, total=False):
    pass


class ConditionSchema(TypedDict, total=False):
    condition_type: Required[Literal["BOOLEAN", "DATE", "DATE_TIME", "INTEGER", "FLOAT", "STRING", "LIST_OF_STRINGS"]]
    """
    - `BOOLEAN` - BOOLEAN
    - `DATE` - DATE
    - `DATE_TIME` - DATE_TIME
    - `INTEGER` - INTEGER
    - `FLOAT` - FLOAT
    - `STRING` - STRING
    - `LIST_OF_STRINGS` - LIST_OF_STRINGS
    """

    field_name: Required[Optional[str]]
    """
    The name of the field on the common model that this condition corresponds to, if
    they conceptually match. e.g. "location_type".
    """

    id: Required[str]
    """The ID of the condition schema.

    This ID is used when updating selective syncs for a linked account.
    """

    native_name: Required[Optional[str]]
    """User-facing _native condition_ name. e.g. "Skip Manager"."""

    operators: Required[List[Operator]]
    """The schemas for the operators that can be used on a condition."""

    is_unique: bool
    """Whether this condition can only be applied once.

    If false, the condition can be AND'd together multiple times.
    """
