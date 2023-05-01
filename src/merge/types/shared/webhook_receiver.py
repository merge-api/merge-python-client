# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["WebhookReceiver"]


class WebhookReceiver(BaseModel):
    event: str

    is_active: bool

    key: Optional[str]
