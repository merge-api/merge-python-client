# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ValidationError", "Source"]


class Source(BaseModel):
    pointer: str


class ValidationError(BaseModel):
    detail: str

    problem_type: str

    title: str

    source: Optional[Source]
