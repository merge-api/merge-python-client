# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "CommonModelScope",
    "OrganizationLevelScopes",
    "OrganizationLevelScopesCommonModel",
    "ScopeOverride",
    "ScopeOverrideCommonModel",
]


class OrganizationLevelScopesCommonModel(BaseModel):
    disabled_fields: List[str]

    enabled_actions: List[Literal["ENABLED_ACTION_READ", "ENABLED_ACTION_WRITE"]]

    is_disabled: bool

    model_id: str

    model_name: str


class OrganizationLevelScopes(BaseModel):
    common_models: List[OrganizationLevelScopesCommonModel]

    linked_account_id: Optional[str]


class ScopeOverrideCommonModel(BaseModel):
    disabled_fields: List[str]

    enabled_actions: List[Literal["ENABLED_ACTION_READ", "ENABLED_ACTION_WRITE"]]

    is_disabled: bool

    model_id: str

    model_name: str


class ScopeOverride(BaseModel):
    common_models: List[ScopeOverrideCommonModel]

    linked_account_id: Optional[str]


class CommonModelScope(BaseModel):
    scope_overrides: List[ScopeOverride]

    organization_level_scopes: Optional[OrganizationLevelScopes]
