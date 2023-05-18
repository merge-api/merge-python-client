# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConditionSchema", "Operator"]


class Operator(BaseModel):
    is_unique: Optional[bool]
    """Whether the operator can be repeated multiple times."""

    operator: Optional[str]
    """The operator for which an operator schema is defined."""


class ConditionSchema(BaseModel):
    condition_type: Literal["BOOLEAN", "DATE", "DATE_TIME", "INTEGER", "FLOAT", "STRING", "LIST_OF_STRINGS"]
    """
    - `BOOLEAN` - BOOLEAN
    - `DATE` - DATE
    - `DATE_TIME` - DATE_TIME
    - `INTEGER` - INTEGER
    - `FLOAT` - FLOAT
    - `STRING` - STRING
    - `LIST_OF_STRINGS` - LIST_OF_STRINGS
    """

    field_name: Optional[str]
    """
    The name of the field on the common model that this condition corresponds to, if
    they conceptually match. e.g. "location_type".
    """

    id: str
    """The ID of the condition schema.

    This ID is used when updating selective syncs for a linked account.
    """

    native_name: Optional[str]
    """User-facing _native condition_ name. e.g. "Skip Manager"."""

    operators: List[Operator]
    """The schemas for the operators that can be used on a condition."""

    common_model: Optional[str]
    """The common model for which a condition schema is defined."""

    is_unique: Optional[bool]
    """Whether this condition can only be applied once.

    If false, the condition can be AND'd together multiple times.
    """
