# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLinkedAccounts:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        linked_account = client.hris.linked_accounts.list()
        assert_matches_type(SyncPage[shared.AccountDetailsAndActions], linked_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        linked_account = client.hris.linked_accounts.list(
            category="accounting",
            cursor="string",
            end_user_email_address="string",
            end_user_organization_name="string",
            end_user_origin_id="string",
            end_user_origin_ids="string",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="string",
            include_duplicates=True,
            integration_name="string",
            is_test_account="string",
            page_size=0,
            status="string",
        )
        assert_matches_type(SyncPage[shared.AccountDetailsAndActions], linked_account, path=["response"])

    @parametrize
    def test_method_delete(self, client: Merge) -> None:
        linked_account = client.hris.linked_accounts.delete()
        assert linked_account is None


class TestAsyncLinkedAccounts:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        linked_account = await client.hris.linked_accounts.list()
        assert_matches_type(AsyncPage[shared.AccountDetailsAndActions], linked_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        linked_account = await client.hris.linked_accounts.list(
            category="accounting",
            cursor="string",
            end_user_email_address="string",
            end_user_organization_name="string",
            end_user_origin_id="string",
            end_user_origin_ids="string",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ids="string",
            include_duplicates=True,
            integration_name="string",
            is_test_account="string",
            page_size=0,
            status="string",
        )
        assert_matches_type(AsyncPage[shared.AccountDetailsAndActions], linked_account, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncMerge) -> None:
        linked_account = await client.hris.linked_accounts.delete()
        assert linked_account is None
