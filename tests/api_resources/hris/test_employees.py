# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.pagination import SyncPage, AsyncPage
from merge.types.hris import Employee, CreatedEmployeeResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestEmployees:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        employee = client.hris.employees.create(
            model={},
        )
        assert_matches_type(CreatedEmployeeResponse, employee, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        employee = client.hris.employees.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        employee = client.hris.employees.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand="company",
            include_remote_data=True,
            include_sensitive_fields=True,
            remote_fields="employment_status",
            show_enum_origins="employment_status",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        employee = client.hris.employees.list()
        assert_matches_type(SyncPage[Employee], employee, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        employee = client.hris.employees.list(
            company_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            display_full_name="string",
            employment_status="ACTIVE",
            expand="company",
            first_name="string",
            groups="string",
            include_deleted_data=True,
            include_remote_data=True,
            include_sensitive_fields=True,
            last_name="string",
            manager_id="string",
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            pay_group_id="string",
            personal_email="dev@stainlessapi.com",
            remote_fields="employment_status",
            remote_id="string",
            show_enum_origins="employment_status",
            team_id="string",
            work_email="dev@stainlessapi.com",
            work_location_id="string",
        )
        assert_matches_type(SyncPage[Employee], employee, path=["response"])

    @parametrize
    def test_method_ignore(self, client: Merge) -> None:
        employee = client.hris.employees.ignore(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
        )
        assert_matches_type(shared.IgnoreCommonModel, employee, path=["response"])

    @parametrize
    def test_method_ignore_with_all_params(self, client: Merge) -> None:
        employee = client.hris.employees.ignore(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
            message="deletion request by user id 51903790-7dfe-4053-8d63-5a10cc4ffd39",
        )
        assert_matches_type(shared.IgnoreCommonModel, employee, path=["response"])


class TestAsyncEmployees:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        employee = await client.hris.employees.create(
            model={},
        )
        assert_matches_type(CreatedEmployeeResponse, employee, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        employee = await client.hris.employees.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        employee = await client.hris.employees.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand="company",
            include_remote_data=True,
            include_sensitive_fields=True,
            remote_fields="employment_status",
            show_enum_origins="employment_status",
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        employee = await client.hris.employees.list()
        assert_matches_type(AsyncPage[Employee], employee, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        employee = await client.hris.employees.list(
            company_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            display_full_name="string",
            employment_status="ACTIVE",
            expand="company",
            first_name="string",
            groups="string",
            include_deleted_data=True,
            include_remote_data=True,
            include_sensitive_fields=True,
            last_name="string",
            manager_id="string",
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            pay_group_id="string",
            personal_email="dev@stainlessapi.com",
            remote_fields="employment_status",
            remote_id="string",
            show_enum_origins="employment_status",
            team_id="string",
            work_email="dev@stainlessapi.com",
            work_location_id="string",
        )
        assert_matches_type(AsyncPage[Employee], employee, path=["response"])

    @parametrize
    async def test_method_ignore(self, client: AsyncMerge) -> None:
        employee = await client.hris.employees.ignore(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
        )
        assert_matches_type(shared.IgnoreCommonModel, employee, path=["response"])

    @parametrize
    async def test_method_ignore_with_all_params(self, client: AsyncMerge) -> None:
        employee = await client.hris.employees.ignore(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            reason="GENERAL_CUSTOMER_REQUEST",
            message="deletion request by user id 51903790-7dfe-4053-8d63-5a10cc4ffd39",
        )
        assert_matches_type(shared.IgnoreCommonModel, employee, path=["response"])
