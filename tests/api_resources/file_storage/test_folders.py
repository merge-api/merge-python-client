# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.pagination import SyncPage, AsyncPage
from merge.types.file_storage import Folder, FolderResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestFolders:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        folder = client.file_storage.folders.create(
            model={
                "permissions": [
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                ]
            },
        )
        assert_matches_type(FolderResponse, folder, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        folder = client.file_storage.folders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        folder = client.file_storage.folders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["drive", "drive", "drive"],
            include_remote_data=True,
        )
        assert_matches_type(Folder, folder, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        folder = client.file_storage.folders.list()
        assert_matches_type(SyncPage[Folder], folder, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        folder = client.file_storage.folders.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            drive_id="string",
            expand=["drive", "drive", "drive"],
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="string",
            page_size=0,
            parent_folder_id="string",
            remote_id="string",
        )
        assert_matches_type(SyncPage[Folder], folder, path=["response"])


class TestAsyncFolders:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        folder = await client.file_storage.folders.create(
            model={
                "permissions": [
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                ]
            },
        )
        assert_matches_type(FolderResponse, folder, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        folder = await client.file_storage.folders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Folder, folder, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        folder = await client.file_storage.folders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["drive", "drive", "drive"],
            include_remote_data=True,
        )
        assert_matches_type(Folder, folder, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        folder = await client.file_storage.folders.list()
        assert_matches_type(AsyncPage[Folder], folder, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        folder = await client.file_storage.folders.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            drive_id="string",
            expand=["drive", "drive", "drive"],
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="string",
            page_size=0,
            parent_folder_id="string",
            remote_id="string",
        )
        assert_matches_type(AsyncPage[Folder], folder, path=["response"])
