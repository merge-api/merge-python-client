# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RemoteResponse"]


class RemoteResponse(BaseModel):
    method: str

    path: str

    response: object

    status: int

    headers: Optional[object]

    response_headers: Optional[object]

    response_type: Optional[Literal["JSON", "BASE64_GZIP"]]
    """
    - `JSON` - JSON
    - `BASE64_GZIP` - BASE64_GZIP
    """
