# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge.types.ats import SyncStatusResyncResponse
from merge.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestSyncStatus:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        sync_status = client.ats.sync_status.list()
        assert_matches_type(SyncPage[shared.SyncStatus], sync_status, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        sync_status = client.ats.sync_status.list(
            cursor="string",
            page_size=0,
        )
        assert_matches_type(SyncPage[shared.SyncStatus], sync_status, path=["response"])

    @parametrize
    def test_method_resync(self, client: Merge) -> None:
        sync_status = client.ats.sync_status.resync()
        assert_matches_type(SyncStatusResyncResponse, sync_status, path=["response"])


class TestAsyncSyncStatus:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        sync_status = await client.ats.sync_status.list()
        assert_matches_type(AsyncPage[shared.SyncStatus], sync_status, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        sync_status = await client.ats.sync_status.list(
            cursor="string",
            page_size=0,
        )
        assert_matches_type(AsyncPage[shared.SyncStatus], sync_status, path=["response"])

    @parametrize
    async def test_method_resync(self, client: AsyncMerge) -> None:
        sync_status = await client.ats.sync_status.resync()
        assert_matches_type(SyncStatusResyncResponse, sync_status, path=["response"])
