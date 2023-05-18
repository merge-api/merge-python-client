# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.types.ats import Candidate, CandidateResponse
from merge.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCandidates:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        candidate = client.ats.candidates.create(
            model={},
            remote_user_id="string",
        )
        assert_matches_type(CandidateResponse, candidate, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        candidate = client.ats.candidates.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Candidate, candidate, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        candidate = client.ats.candidates.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["applications", "applications", "applications"],
            include_remote_data=True,
        )
        assert_matches_type(Candidate, candidate, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        candidate = client.ats.candidates.list()
        assert_matches_type(SyncPage[Candidate], candidate, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        candidate = client.ats.candidates.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            email_addresses="string",
            expand=["applications", "applications", "applications"],
            first_name="string",
            include_deleted_data=True,
            include_remote_data=True,
            last_name="string",
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_id="string",
            tags="string",
        )
        assert_matches_type(SyncPage[Candidate], candidate, path=["response"])

    @parametrize
    def test_method_ignore_row(self, client: Merge) -> None:
        candidate = client.ats.candidates.ignore_row(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
        )
        assert candidate is None

    @parametrize
    def test_method_ignore_row_with_all_params(self, client: Merge) -> None:
        candidate = client.ats.candidates.ignore_row(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
            message="deletion request by user id 51903790-7dfe-4053-8d63-5a10cc4ffd39",
        )
        assert candidate is None


class TestAsyncCandidates:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        candidate = await client.ats.candidates.create(
            model={},
            remote_user_id="string",
        )
        assert_matches_type(CandidateResponse, candidate, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        candidate = await client.ats.candidates.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Candidate, candidate, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        candidate = await client.ats.candidates.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["applications", "applications", "applications"],
            include_remote_data=True,
        )
        assert_matches_type(Candidate, candidate, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        candidate = await client.ats.candidates.list()
        assert_matches_type(AsyncPage[Candidate], candidate, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        candidate = await client.ats.candidates.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            email_addresses="string",
            expand=["applications", "applications", "applications"],
            first_name="string",
            include_deleted_data=True,
            include_remote_data=True,
            last_name="string",
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_id="string",
            tags="string",
        )
        assert_matches_type(AsyncPage[Candidate], candidate, path=["response"])

    @parametrize
    async def test_method_ignore_row(self, client: AsyncMerge) -> None:
        candidate = await client.ats.candidates.ignore_row(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
        )
        assert candidate is None

    @parametrize
    async def test_method_ignore_row_with_all_params(self, client: AsyncMerge) -> None:
        candidate = await client.ats.candidates.ignore_row(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
            message="deletion request by user id 51903790-7dfe-4053-8d63-5a10cc4ffd39",
        )
        assert candidate is None
