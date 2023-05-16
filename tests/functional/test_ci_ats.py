from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.types.ats import Candidate
from merge.pagination import SyncPage, AsyncPage

api_key = os.environ.get("API_KEY", "")
ats_account_token = os.environ.get("ACCOUNT_TOKEN_ATS", "")

test_preexisting_candidate_id = "262797e9-bc99-42c4-9c4a-62326ebd2f31"


class TestCandidates:
    strict_client = Merge(api_key=api_key, _strict_response_validation=True, account_token=ats_account_token)
    loose_client = Merge(api_key=api_key, _strict_response_validation=False, account_token=ats_account_token)
    parametrize = pytest.mark.parametrize("client", [loose_client], ids=["loose"])

    @parametrize
    def test_method_retrieve_ci_integration(self, client: Merge) -> None:
        candidate = client.ats.candidates.retrieve(
            test_preexisting_candidate_id,
        )
        assert_matches_type(Candidate, candidate, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params_ci_integration(self, client: Merge) -> None:
        expand = ["applications"] if not client._strict_response_validation else None

        candidate = client.ats.candidates.retrieve(
            test_preexisting_candidate_id,
            expand=expand,  # type: ignore
            include_remote_data=True,
        )
        assert_matches_type(Candidate, candidate, path=["response"])

    @parametrize
    def test_method_list_ci_integration(self, client: Merge) -> None:
        candidate = client.ats.candidates.list()
        assert_matches_type(SyncPage[Candidate], candidate, path=["response"])

    @parametrize
    def test_method_list_with_all_params_ci_integration(self, client: Merge) -> None:
        expand = ["applications", "attachments"] if not client._strict_response_validation else None

        candidate = client.ats.candidates.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            expand=expand,  # type: ignore
            include_remote_data=True,
        )
        assert_matches_type(SyncPage[Candidate], candidate, path=["response"])


class TestAsyncCandidates:
    strict_client = AsyncMerge(api_key=api_key, _strict_response_validation=True, account_token=ats_account_token)
    loose_client = AsyncMerge(api_key=api_key, _strict_response_validation=False, account_token=ats_account_token)
    parametrize = pytest.mark.parametrize("client", [loose_client], ids=["loose"])

    @parametrize
    async def test_method_retrieve_ci_integration(self, client: AsyncMerge) -> None:
        candidate = await client.ats.candidates.retrieve(
            test_preexisting_candidate_id,
        )
        assert_matches_type(Candidate, candidate, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params_ci_integration(self, client: AsyncMerge) -> None:
        expand = ["applications"] if not client._strict_response_validation else None

        candidate = await client.ats.candidates.retrieve(
            test_preexisting_candidate_id,
            expand=expand,  # type: ignore
            include_remote_data=True,
        )
        assert_matches_type(Candidate, candidate, path=["response"])

    @parametrize
    async def test_method_list_ci_integration(self, client: AsyncMerge) -> None:
        candidate = await client.ats.candidates.list()
        assert_matches_type(AsyncPage[Candidate], candidate, path=["response"])

    @parametrize
    async def test_method_list_with_all_params_ci_integration(self, client: AsyncMerge) -> None:
        expand = ["applications", "attachments"] if not client._strict_response_validation else None

        candidate = await client.ats.candidates.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            expand=expand,  # type: ignore
            include_remote_data=True,
        )
        assert_matches_type(AsyncPage[Candidate], candidate, path=["response"])
