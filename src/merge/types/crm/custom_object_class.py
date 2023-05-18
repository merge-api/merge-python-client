# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CustomObjectClass", "Field", "FieldItemSchema"]


class FieldItemSchema(BaseModel):
    item_choices: Optional[List[Optional[str]]]

    item_format: Optional[str]

    item_type: Optional[str]


class Field(BaseModel):
    description: Optional[str]

    display_name: Optional[str]

    field_choices: Optional[List[Optional[str]]]

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

    is_required: Optional[bool]

    item_schema: Optional[FieldItemSchema]

    modified_at: Optional[datetime]
    """This is the datetime that this object was last updated by Merge"""

    remote_key_name: Optional[str]


class CustomObjectClass(BaseModel):
    association_types: Optional[List[object]]

    description: Optional[str]

    fields: Optional[List[Field]]

    id: Optional[str]

    labels: Optional[Dict[str, Optional[str]]]

    modified_at: Optional[datetime]

    name: Optional[str]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""
