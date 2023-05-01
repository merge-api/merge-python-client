# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCommonModelScopes:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        common_model_scope = client.hris.common_model_scopes.retrieve()
        assert_matches_type(shared.CommonModelScope, common_model_scope, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        common_model_scope = client.hris.common_model_scopes.retrieve(
            linked_account_id="string",
        )
        assert_matches_type(shared.CommonModelScope, common_model_scope, path=["response"])

    @parametrize
    def test_method_update(self, client: Merge) -> None:
        common_model_scope = client.hris.common_model_scopes.update(
            common_models=[
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
            ],
        )
        assert_matches_type(shared.CommonModelScope, common_model_scope, path=["response"])


class TestAsyncCommonModelScopes:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        common_model_scope = await client.hris.common_model_scopes.retrieve()
        assert_matches_type(shared.CommonModelScope, common_model_scope, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        common_model_scope = await client.hris.common_model_scopes.retrieve(
            linked_account_id="string",
        )
        assert_matches_type(shared.CommonModelScope, common_model_scope, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncMerge) -> None:
        common_model_scope = await client.hris.common_model_scopes.update(
            common_models=[
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
            ],
        )
        assert_matches_type(shared.CommonModelScope, common_model_scope, path=["response"])
