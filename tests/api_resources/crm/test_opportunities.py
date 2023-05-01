# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.types.crm import Opportunity, OpportunityResponse
from merge.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestOpportunities:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        opportunity = client.crm.opportunities.create(
            model={},
        )
        assert_matches_type(OpportunityResponse, opportunity, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        opportunity = client.crm.opportunities.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Opportunity, opportunity, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        opportunity = client.crm.opportunities.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["account", "account", "account"],
            include_remote_data=True,
            include_remote_fields=True,
            remote_fields="status",
            show_enum_origins="status",
        )
        assert_matches_type(Opportunity, opportunity, path=["response"])

    @parametrize
    def test_method_update(self, client: Merge) -> None:
        opportunity = client.crm.opportunities.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model={},
        )
        assert_matches_type(OpportunityResponse, opportunity, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        opportunity = client.crm.opportunities.list()
        assert_matches_type(SyncPage[Opportunity], opportunity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        opportunity = client.crm.opportunities.list(
            account_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            expand=["account", "account", "account"],
            include_deleted_data=True,
            include_remote_data=True,
            include_remote_fields=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            owner_id="string",
            page_size=0,
            remote_fields="status",
            remote_id="string",
            show_enum_origins="status",
            stage_id="string",
            status="LOST",
        )
        assert_matches_type(SyncPage[Opportunity], opportunity, path=["response"])

    @parametrize
    def test_method_list_remote_field_classes(self, client: Merge) -> None:
        opportunity = client.crm.opportunities.list_remote_field_classes()
        assert_matches_type(SyncPage[shared.RemoteFieldClass], opportunity, path=["response"])

    @parametrize
    def test_method_list_remote_field_classes_with_all_params(self, client: Merge) -> None:
        opportunity = client.crm.opportunities.list_remote_field_classes(
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            include_remote_fields=True,
            page_size=0,
        )
        assert_matches_type(SyncPage[shared.RemoteFieldClass], opportunity, path=["response"])


class TestAsyncOpportunities:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        opportunity = await client.crm.opportunities.create(
            model={},
        )
        assert_matches_type(OpportunityResponse, opportunity, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        opportunity = await client.crm.opportunities.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Opportunity, opportunity, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        opportunity = await client.crm.opportunities.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["account", "account", "account"],
            include_remote_data=True,
            include_remote_fields=True,
            remote_fields="status",
            show_enum_origins="status",
        )
        assert_matches_type(Opportunity, opportunity, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncMerge) -> None:
        opportunity = await client.crm.opportunities.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model={},
        )
        assert_matches_type(OpportunityResponse, opportunity, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        opportunity = await client.crm.opportunities.list()
        assert_matches_type(AsyncPage[Opportunity], opportunity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        opportunity = await client.crm.opportunities.list(
            account_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            expand=["account", "account", "account"],
            include_deleted_data=True,
            include_remote_data=True,
            include_remote_fields=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            owner_id="string",
            page_size=0,
            remote_fields="status",
            remote_id="string",
            show_enum_origins="status",
            stage_id="string",
            status="LOST",
        )
        assert_matches_type(AsyncPage[Opportunity], opportunity, path=["response"])

    @parametrize
    async def test_method_list_remote_field_classes(self, client: AsyncMerge) -> None:
        opportunity = await client.crm.opportunities.list_remote_field_classes()
        assert_matches_type(AsyncPage[shared.RemoteFieldClass], opportunity, path=["response"])

    @parametrize
    async def test_method_list_remote_field_classes_with_all_params(self, client: AsyncMerge) -> None:
        opportunity = await client.crm.opportunities.list_remote_field_classes(
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            include_remote_fields=True,
            page_size=0,
        )
        assert_matches_type(AsyncPage[shared.RemoteFieldClass], opportunity, path=["response"])
