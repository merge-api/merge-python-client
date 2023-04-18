# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CommonModelScopeUpdateParams", "CommonModel"]


class CommonModel(TypedDict, total=False):
    disabled_fields: Required[List[str]]

    enabled_actions: Required[List[Literal["READ", "WRITE"]]]

    model_id: Required[str]


class CommonModelScopeUpdateParams(TypedDict, total=False):
    common_models: Required[List[CommonModel]]
    """The common model scopes to update."""
