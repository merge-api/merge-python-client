# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["LinkToken"]


class LinkToken(BaseModel):
    link_token: str

    integration_name: Optional[str]

    magic_link_url: Optional[str]
