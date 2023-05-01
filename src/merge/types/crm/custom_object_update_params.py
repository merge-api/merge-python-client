# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomObjectUpdateParams", "Model"]


class Model(TypedDict, total=False):
    fields: Required[object]


class CustomObjectUpdateParams(TypedDict, total=False):
    model: Required[Model]
