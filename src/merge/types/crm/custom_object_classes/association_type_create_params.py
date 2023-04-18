# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AssociationTypeCreateParams", "Model", "ModelSourceObjectClass", "ModelTargetObjectClass"]


class ModelSourceObjectClass(TypedDict, total=False):
    id: Required[str]

    origin_type: Required[Literal["CUSTOM_OBJECT", "COMMON_MODEL", "REMOTE_ONLY_MODEL"]]
    """
    - `CUSTOM_OBJECT` - CUSTOM_OBJECT
    - `COMMON_MODEL` - COMMON_MODEL
    - `REMOTE_ONLY_MODEL` - REMOTE_ONLY_MODEL
    """


class ModelTargetObjectClass(TypedDict, total=False):
    id: Required[str]

    origin_type: Required[Literal["CUSTOM_OBJECT", "COMMON_MODEL", "REMOTE_ONLY_MODEL"]]
    """
    - `CUSTOM_OBJECT` - CUSTOM_OBJECT
    - `COMMON_MODEL` - COMMON_MODEL
    - `REMOTE_ONLY_MODEL` - REMOTE_ONLY_MODEL
    """


class Model(TypedDict, total=False):
    remote_key_name: Required[str]

    source_object_class: Required[ModelSourceObjectClass]

    target_object_classes: Required[List[ModelTargetObjectClass]]

    cardinality: Literal["ONE_TO_ONE", "MANY_TO_ONE", "MANY_TO_MANY", "ONE_TO_MANY"]
    """
    - `ONE_TO_ONE` - ONE_TO_ONE
    - `MANY_TO_ONE` - MANY_TO_ONE
    - `MANY_TO_MANY` - MANY_TO_MANY
    - `ONE_TO_MANY` - ONE_TO_MANY
    """

    display_name: str

    is_required: bool


class AssociationTypeCreateParams(TypedDict, total=False):
    model: Required[Model]
