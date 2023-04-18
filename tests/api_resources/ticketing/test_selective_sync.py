# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge.pagination import SyncPage, AsyncPage
from merge.types.ticketing import (
    SelectiveSyncListConfigurationsResponse,
    SelectiveSyncReplaceConfigurationsResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestSelectiveSync:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list_configurations(self, client: Merge) -> None:
        selective_sync = client.ticketing.selective_sync.list_configurations()
        assert_matches_type(SelectiveSyncListConfigurationsResponse, selective_sync, path=["response"])

    @parametrize
    def test_method_list_metadata(self, client: Merge) -> None:
        selective_sync = client.ticketing.selective_sync.list_metadata()
        assert_matches_type(SyncPage[shared.ConditionSchema], selective_sync, path=["response"])

    @parametrize
    def test_method_list_metadata_with_all_params(self, client: Merge) -> None:
        selective_sync = client.ticketing.selective_sync.list_metadata(
            common_model="string",
            cursor="string",
            page_size=0,
        )
        assert_matches_type(SyncPage[shared.ConditionSchema], selective_sync, path=["response"])

    @parametrize
    def test_method_replace_configurations(self, client: Merge) -> None:
        selective_sync = client.ticketing.selective_sync.replace_configurations(
            sync_configurations=[
                {
                    "linked_account_conditions": [
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                    ]
                },
                {
                    "linked_account_conditions": [
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                    ]
                },
                {
                    "linked_account_conditions": [
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                    ]
                },
            ],
        )
        assert_matches_type(SelectiveSyncReplaceConfigurationsResponse, selective_sync, path=["response"])


class TestAsyncSelectiveSync:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list_configurations(self, client: AsyncMerge) -> None:
        selective_sync = await client.ticketing.selective_sync.list_configurations()
        assert_matches_type(SelectiveSyncListConfigurationsResponse, selective_sync, path=["response"])

    @parametrize
    async def test_method_list_metadata(self, client: AsyncMerge) -> None:
        selective_sync = await client.ticketing.selective_sync.list_metadata()
        assert_matches_type(AsyncPage[shared.ConditionSchema], selective_sync, path=["response"])

    @parametrize
    async def test_method_list_metadata_with_all_params(self, client: AsyncMerge) -> None:
        selective_sync = await client.ticketing.selective_sync.list_metadata(
            common_model="string",
            cursor="string",
            page_size=0,
        )
        assert_matches_type(AsyncPage[shared.ConditionSchema], selective_sync, path=["response"])

    @parametrize
    async def test_method_replace_configurations(self, client: AsyncMerge) -> None:
        selective_sync = await client.ticketing.selective_sync.replace_configurations(
            sync_configurations=[
                {
                    "linked_account_conditions": [
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                    ]
                },
                {
                    "linked_account_conditions": [
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                    ]
                },
                {
                    "linked_account_conditions": [
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                        {
                            "condition_schema_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "operator": "x",
                            "value": {},
                        },
                    ]
                },
            ],
        )
        assert_matches_type(SelectiveSyncReplaceConfigurationsResponse, selective_sync, path=["response"])
