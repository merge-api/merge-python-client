# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.pagination import SyncPage, AsyncPage
from merge.types.ticketing import Collection, TicketingUser

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCollections:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        collection = client.ticketing.collections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        collection = client.ticketing.collections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["parent_collection", "parent_collection", "parent_collection"],
            include_remote_data=True,
            remote_fields="collection_type",
            show_enum_origins="collection_type",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        collection = client.ticketing.collections.list()
        assert_matches_type(SyncPage[Collection], collection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        collection = client.ticketing.collections.list(
            collection_type="LIST",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            expand=["parent_collection", "parent_collection", "parent_collection"],
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            parent_collection_id="string",
            remote_fields="collection_type",
            remote_id="string",
            show_enum_origins="collection_type",
        )
        assert_matches_type(SyncPage[Collection], collection, path=["response"])

    @parametrize
    def test_method_list_users(self, client: Merge) -> None:
        collection = client.ticketing.collections.list_users(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncPage[TicketingUser], collection, path=["response"])

    @parametrize
    def test_method_list_users_with_all_params(self, client: Merge) -> None:
        collection = client.ticketing.collections.list_users(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="string",
            expand=["teams", "teams", "teams"],
            include_deleted_data=True,
            include_remote_data=True,
            page_size=0,
        )
        assert_matches_type(SyncPage[TicketingUser], collection, path=["response"])


class TestAsyncCollections:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        collection = await client.ticketing.collections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        collection = await client.ticketing.collections.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["parent_collection", "parent_collection", "parent_collection"],
            include_remote_data=True,
            remote_fields="collection_type",
            show_enum_origins="collection_type",
        )
        assert_matches_type(Collection, collection, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        collection = await client.ticketing.collections.list()
        assert_matches_type(AsyncPage[Collection], collection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        collection = await client.ticketing.collections.list(
            collection_type="LIST",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            expand=["parent_collection", "parent_collection", "parent_collection"],
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            parent_collection_id="string",
            remote_fields="collection_type",
            remote_id="string",
            show_enum_origins="collection_type",
        )
        assert_matches_type(AsyncPage[Collection], collection, path=["response"])

    @parametrize
    async def test_method_list_users(self, client: AsyncMerge) -> None:
        collection = await client.ticketing.collections.list_users(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncPage[TicketingUser], collection, path=["response"])

    @parametrize
    async def test_method_list_users_with_all_params(self, client: AsyncMerge) -> None:
        collection = await client.ticketing.collections.list_users(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="string",
            expand=["teams", "teams", "teams"],
            include_deleted_data=True,
            include_remote_data=True,
            page_size=0,
        )
        assert_matches_type(AsyncPage[TicketingUser], collection, path=["response"])
