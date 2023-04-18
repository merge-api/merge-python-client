# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ValidationError", "Source"]


class Source(TypedDict, total=False):
    pointer: Required[str]


class ValidationError(TypedDict, total=False):
    detail: Required[str]

    problem_type: Required[str]

    title: Required[str]

    source: Source
