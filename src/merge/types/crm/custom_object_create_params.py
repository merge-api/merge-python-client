# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CustomObjectCreateParams", "Model"]


class Model(TypedDict, total=False):
    fields: Required[object]


class CustomObjectCreateParams(TypedDict, total=False):
    model: Required[Model]
