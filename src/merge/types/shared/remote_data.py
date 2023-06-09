# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RemoteData"]


class RemoteData(BaseModel):
    path: str

    data: Optional[object]
