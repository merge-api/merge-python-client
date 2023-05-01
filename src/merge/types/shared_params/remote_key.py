# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RemoteKey"]


class RemoteKey(TypedDict, total=False):
    key: Required[str]

    name: Required[str]
