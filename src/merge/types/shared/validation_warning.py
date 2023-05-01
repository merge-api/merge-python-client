# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["ValidationWarning", "Source"]


class Source(BaseModel):
    pointer: str


class ValidationWarning(BaseModel):
    detail: str

    problem_type: str

    title: str

    source: Optional[Source]
