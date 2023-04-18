# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RemoteData"]


class RemoteData(TypedDict, total=False):
    path: Required[str]

    data: object
