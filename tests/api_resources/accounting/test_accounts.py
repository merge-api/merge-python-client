# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.pagination import SyncPage, AsyncPage
from merge.types.accounting import AccountResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccounts:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        account = client.accounting.accounts.create(
            model={},
        )
        assert_matches_type(AccountResponse, account, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        account = client.accounting.accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(shared.Account, account, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        account = client.accounting.accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["company", "company", "company"],
            include_remote_data=True,
            remote_fields="classification",
            show_enum_origins="classification",
        )
        assert_matches_type(shared.Account, account, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        account = client.accounting.accounts.list()
        assert_matches_type(SyncPage[shared.Account], account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        account = client.accounting.accounts.list(
            company_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            expand=["company", "company", "company"],
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_fields="classification",
            remote_id="string",
            show_enum_origins="classification",
        )
        assert_matches_type(SyncPage[shared.Account], account, path=["response"])


class TestAsyncAccounts:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        account = await client.accounting.accounts.create(
            model={},
        )
        assert_matches_type(AccountResponse, account, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        account = await client.accounting.accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(shared.Account, account, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        account = await client.accounting.accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["company", "company", "company"],
            include_remote_data=True,
            remote_fields="classification",
            show_enum_origins="classification",
        )
        assert_matches_type(shared.Account, account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        account = await client.accounting.accounts.list()
        assert_matches_type(AsyncPage[shared.Account], account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        account = await client.accounting.accounts.list(
            company_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            expand=["company", "company", "company"],
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_fields="classification",
            remote_id="string",
            show_enum_origins="classification",
        )
        assert_matches_type(AsyncPage[shared.Account], account, path=["response"])
