# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestIssues:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        issue = client.ticketing.issues.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(shared.Issue, issue, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        issue = client.ticketing.issues.list()
        assert_matches_type(SyncPage[shared.Issue], issue, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        issue = client.ticketing.issues.list(
            account_token="string",
            cursor="string",
            end_date="string",
            end_user_organization_name="string",
            first_incident_time_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_incident_time_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_muted="string",
            integration_name="string",
            last_incident_time_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_incident_time_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            start_date="string",
            status="ONGOING",
        )
        assert_matches_type(SyncPage[shared.Issue], issue, path=["response"])


class TestAsyncIssues:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        issue = await client.ticketing.issues.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(shared.Issue, issue, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        issue = await client.ticketing.issues.list()
        assert_matches_type(AsyncPage[shared.Issue], issue, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        issue = await client.ticketing.issues.list(
            account_token="string",
            cursor="string",
            end_date="string",
            end_user_organization_name="string",
            first_incident_time_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            first_incident_time_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_muted="string",
            integration_name="string",
            last_incident_time_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            last_incident_time_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            start_date="string",
            status="ONGOING",
        )
        assert_matches_type(AsyncPage[shared.Issue], issue, path=["response"])
