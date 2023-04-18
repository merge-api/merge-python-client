# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.types.ats import Application, ApplicationResponse
from merge.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestApplications:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        application = client.ats.applications.create(
            model={},
            remote_user_id="string",
        )
        assert_matches_type(ApplicationResponse, application, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        application = client.ats.applications.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Application, application, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        application = client.ats.applications.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand="candidate",
            include_remote_data=True,
        )
        assert_matches_type(Application, application, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        application = client.ats.applications.list()
        assert_matches_type(SyncPage[Application], application, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        application = client.ats.applications.list(
            candidate_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            credited_to_id="string",
            current_stage_id="string",
            cursor="string",
            expand="candidate",
            include_deleted_data=True,
            include_remote_data=True,
            job_id="string",
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            reject_reason_id="string",
            remote_id="string",
            source="string",
        )
        assert_matches_type(SyncPage[Application], application, path=["response"])

    @parametrize
    def test_method_change_stage(self, client: Merge) -> None:
        application = client.ats.applications.change_stage(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApplicationResponse, application, path=["response"])

    @parametrize
    def test_method_change_stage_with_all_params(self, client: Merge) -> None:
        application = client.ats.applications.change_stage(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            job_interview_stage="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remote_user_id="x",
        )
        assert_matches_type(ApplicationResponse, application, path=["response"])


class TestAsyncApplications:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        application = await client.ats.applications.create(
            model={},
            remote_user_id="string",
        )
        assert_matches_type(ApplicationResponse, application, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        application = await client.ats.applications.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Application, application, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        application = await client.ats.applications.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand="candidate",
            include_remote_data=True,
        )
        assert_matches_type(Application, application, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        application = await client.ats.applications.list()
        assert_matches_type(AsyncPage[Application], application, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        application = await client.ats.applications.list(
            candidate_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            credited_to_id="string",
            current_stage_id="string",
            cursor="string",
            expand="candidate",
            include_deleted_data=True,
            include_remote_data=True,
            job_id="string",
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            reject_reason_id="string",
            remote_id="string",
            source="string",
        )
        assert_matches_type(AsyncPage[Application], application, path=["response"])

    @parametrize
    async def test_method_change_stage(self, client: AsyncMerge) -> None:
        application = await client.ats.applications.change_stage(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApplicationResponse, application, path=["response"])

    @parametrize
    async def test_method_change_stage_with_all_params(self, client: AsyncMerge) -> None:
        application = await client.ats.applications.change_stage(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            job_interview_stage="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            remote_user_id="x",
        )
        assert_matches_type(ApplicationResponse, application, path=["response"])
