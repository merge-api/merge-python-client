# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["RemoteFieldClass", "ItemSchema"]


class ItemSchema(TypedDict, total=False):
    item_choices: List[str]

    item_format: object

    item_type: object


class RemoteFieldClass(TypedDict, total=False):
    description: str

    display_name: str

    field_choices: List[str]

    field_format: Literal["string", "number", "date", "datetime", "bool", "list"]
    """
    - `string` - string
    - `number` - number
    - `date` - date
    - `datetime` - datetime
    - `bool` - bool
    - `list` - list
    """

    field_type: Literal["string", "number", "date", "datetime", "bool", "list"]
    """
    - `string` - string
    - `number` - number
    - `date` - date
    - `datetime` - datetime
    - `bool` - bool
    - `list` - list
    """

    id: str

    is_custom: bool

    is_required: bool

    item_schema: ItemSchema

    remote_key_name: str
