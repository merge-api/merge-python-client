# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RemoteFieldClass", "ItemSchema"]


class ItemSchema(BaseModel):
    item_choices: Optional[List[str]]

    item_format: Optional[object]

    item_type: Optional[object]


class RemoteFieldClass(BaseModel):
    description: Optional[str]

    display_name: Optional[str]

    field_choices: Optional[List[str]]

    field_format: Optional[Literal["string", "number", "date", "datetime", "bool", "list"]]
    """
    - `string` - string
    - `number` - number
    - `date` - date
    - `datetime` - datetime
    - `bool` - bool
    - `list` - list
    """

    field_type: Optional[Literal["string", "number", "date", "datetime", "bool", "list"]]
    """
    - `string` - string
    - `number` - number
    - `date` - date
    - `datetime` - datetime
    - `bool` - bool
    - `list` - list
    """

    id: Optional[str]

    is_custom: Optional[bool]

    is_required: Optional[bool]

    item_schema: Optional[ItemSchema]

    remote_key_name: Optional[str]
