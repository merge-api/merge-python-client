# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.types.crm import CrmUser
from merge.pagination import SyncPage, AsyncPage
from merge.types.file_storage import FileStorageUser

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestUsers:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        user = client.crm.users.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CrmUser, user, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        user = client.crm.users.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_remote_data=True,
            include_remote_fields=True,
        )
        assert_matches_type(CrmUser, user, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        user = client.crm.users.list()
        assert_matches_type(SyncPage[FileStorageUser], user, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        user = client.crm.users.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            include_remote_fields=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_id="string",
        )
        assert_matches_type(SyncPage[FileStorageUser], user, path=["response"])

    @parametrize
    def test_method_ignore_row(self, client: Merge) -> None:
        user = client.crm.users.ignore_row(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
        )
        assert_matches_type(shared.IgnoreCommonModel, user, path=["response"])

    @parametrize
    def test_method_ignore_row_with_all_params(self, client: Merge) -> None:
        user = client.crm.users.ignore_row(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
            message="deletion request by user id 51903790-7dfe-4053-8d63-5a10cc4ffd39",
        )
        assert_matches_type(shared.IgnoreCommonModel, user, path=["response"])

    @parametrize
    def test_method_list_remote_field_classes(self, client: Merge) -> None:
        user = client.crm.users.list_remote_field_classes()
        assert_matches_type(SyncPage[shared.RemoteFieldClass], user, path=["response"])

    @parametrize
    def test_method_list_remote_field_classes_with_all_params(self, client: Merge) -> None:
        user = client.crm.users.list_remote_field_classes(
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            include_remote_fields=True,
            page_size=0,
        )
        assert_matches_type(SyncPage[shared.RemoteFieldClass], user, path=["response"])


class TestAsyncUsers:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        user = await client.crm.users.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CrmUser, user, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        user = await client.crm.users.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_remote_data=True,
            include_remote_fields=True,
        )
        assert_matches_type(CrmUser, user, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        user = await client.crm.users.list()
        assert_matches_type(AsyncPage[FileStorageUser], user, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        user = await client.crm.users.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            include_remote_fields=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_id="string",
        )
        assert_matches_type(AsyncPage[FileStorageUser], user, path=["response"])

    @parametrize
    async def test_method_ignore_row(self, client: AsyncMerge) -> None:
        user = await client.crm.users.ignore_row(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
        )
        assert_matches_type(shared.IgnoreCommonModel, user, path=["response"])

    @parametrize
    async def test_method_ignore_row_with_all_params(self, client: AsyncMerge) -> None:
        user = await client.crm.users.ignore_row(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
            message="deletion request by user id 51903790-7dfe-4053-8d63-5a10cc4ffd39",
        )
        assert_matches_type(shared.IgnoreCommonModel, user, path=["response"])

    @parametrize
    async def test_method_list_remote_field_classes(self, client: AsyncMerge) -> None:
        user = await client.crm.users.list_remote_field_classes()
        assert_matches_type(AsyncPage[shared.RemoteFieldClass], user, path=["response"])

    @parametrize
    async def test_method_list_remote_field_classes_with_all_params(self, client: AsyncMerge) -> None:
        user = await client.crm.users.list_remote_field_classes(
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            include_remote_fields=True,
            page_size=0,
        )
        assert_matches_type(AsyncPage[shared.RemoteFieldClass], user, path=["response"])
