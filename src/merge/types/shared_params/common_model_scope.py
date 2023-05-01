# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CommonModelScope",
    "ScopeOverride",
    "ScopeOverrideCommonModel",
    "OrganizationLevelScopes",
    "OrganizationLevelScopesCommonModel",
]


class ScopeOverrideCommonModel(TypedDict, total=False):
    disabled_fields: Required[List[str]]

    enabled_actions: Required[List[Literal["ENABLED_ACTION_READ", "ENABLED_ACTION_WRITE"]]]

    is_disabled: Required[bool]

    model_id: Required[str]

    model_name: Required[str]


class ScopeOverride(TypedDict, total=False):
    common_models: Required[List[ScopeOverrideCommonModel]]

    linked_account_id: str


class OrganizationLevelScopesCommonModel(TypedDict, total=False):
    disabled_fields: Required[List[str]]

    enabled_actions: Required[List[Literal["ENABLED_ACTION_READ", "ENABLED_ACTION_WRITE"]]]

    is_disabled: Required[bool]

    model_id: Required[str]

    model_name: Required[str]


class OrganizationLevelScopes(TypedDict, total=False):
    common_models: Required[List[OrganizationLevelScopesCommonModel]]

    linked_account_id: str


class CommonModelScope(TypedDict, total=False):
    scope_overrides: Required[List[ScopeOverride]]

    organization_level_scopes: OrganizationLevelScopes
