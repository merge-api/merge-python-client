# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.pagination import SyncPage, AsyncPage
from merge.types.marketing import ContactList, ContactListCreateResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestContactLists:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        contact_list = client.marketing.contact_lists.create(
            model={},
        )
        assert_matches_type(ContactListCreateResponse, contact_list, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        contact_list = client.marketing.contact_lists.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ContactList, contact_list, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        contact_list = client.marketing.contact_lists.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_remote_data=True,
        )
        assert_matches_type(ContactList, contact_list, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        contact_list = client.marketing.contact_lists.list()
        assert_matches_type(SyncPage[ContactList], contact_list, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        contact_list = client.marketing.contact_lists.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_id="string",
        )
        assert_matches_type(SyncPage[ContactList], contact_list, path=["response"])

    @parametrize
    def test_method_list_subscribers(self, client: Merge) -> None:
        contact_list = client.marketing.contact_lists.list_subscribers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncPage[shared.Contact], contact_list, path=["response"])

    @parametrize
    def test_method_list_subscribers_with_all_params(self, client: Merge) -> None:
        contact_list = client.marketing.contact_lists.list_subscribers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            page_size=0,
        )
        assert_matches_type(SyncPage[shared.Contact], contact_list, path=["response"])


class TestAsyncContactLists:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        contact_list = await client.marketing.contact_lists.create(
            model={},
        )
        assert_matches_type(ContactListCreateResponse, contact_list, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        contact_list = await client.marketing.contact_lists.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ContactList, contact_list, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        contact_list = await client.marketing.contact_lists.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_remote_data=True,
        )
        assert_matches_type(ContactList, contact_list, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        contact_list = await client.marketing.contact_lists.list()
        assert_matches_type(AsyncPage[ContactList], contact_list, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        contact_list = await client.marketing.contact_lists.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_id="string",
        )
        assert_matches_type(AsyncPage[ContactList], contact_list, path=["response"])

    @parametrize
    async def test_method_list_subscribers(self, client: AsyncMerge) -> None:
        contact_list = await client.marketing.contact_lists.list_subscribers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncPage[shared.Contact], contact_list, path=["response"])

    @parametrize
    async def test_method_list_subscribers_with_all_params(self, client: AsyncMerge) -> None:
        contact_list = await client.marketing.contact_lists.list_subscribers(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            page_size=0,
        )
        assert_matches_type(AsyncPage[shared.Contact], contact_list, path=["response"])
