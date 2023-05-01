# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RemoteResponse"]


class RemoteResponse(TypedDict, total=False):
    method: Required[str]

    path: Required[str]

    response: Required[object]

    status: Required[int]

    headers: object

    response_headers: object

    response_type: Literal["JSON", "BASE64_GZIP"]
    """
    - `JSON` - JSON
    - `BASE64_GZIP` - BASE64_GZIP
    """
