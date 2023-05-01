# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestRemoteKeys:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_generate(self, client: Merge) -> None:
        remote_key = client.marketing.remote_keys.generate(
            name="Remote Deployment Key 1",
        )
        assert_matches_type(shared.RemoteKey, remote_key, path=["response"])

    @parametrize
    def test_method_regenerate(self, client: Merge) -> None:
        remote_key = client.marketing.remote_keys.regenerate(
            name="Remote Deployment Key 1",
        )
        assert_matches_type(shared.RemoteKey, remote_key, path=["response"])


class TestAsyncRemoteKeys:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_generate(self, client: AsyncMerge) -> None:
        remote_key = await client.marketing.remote_keys.generate(
            name="Remote Deployment Key 1",
        )
        assert_matches_type(shared.RemoteKey, remote_key, path=["response"])

    @parametrize
    async def test_method_regenerate(self, client: AsyncMerge) -> None:
        remote_key = await client.marketing.remote_keys.regenerate(
            name="Remote Deployment Key 1",
        )
        assert_matches_type(shared.RemoteKey, remote_key, path=["response"])
