# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...types import shared
from ..._models import BaseModel

__all__ = ["CustomObject", "RemoteField"]


class RemoteField(BaseModel):
    remote_field_class: shared.RemoteFieldClass

    value: Optional[object]


class CustomObject(BaseModel):
    fields: Optional[object]

    id: Optional[str]

    object_class: Optional[str]

    remote_fields: Optional[List[RemoteField]]

    remote_id: Optional[str]
    """The third-party API ID of the matching object."""
