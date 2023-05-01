# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LinkToken"]


class LinkToken(TypedDict, total=False):
    link_token: Required[str]

    integration_name: str

    magic_link_url: str
