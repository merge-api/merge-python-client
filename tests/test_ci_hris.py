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

api_key = os.environ.get("API_KEY", "")
hris_account_token = os.environ.get("ACCOUNT_TOKEN_HRIS", "")

test_preexisting_employee_id = "0c218e36-55ca-47a9-950e-c25bc3a20fb1"


class TestEmployees:
    strict_client = Merge(
        api_key=api_key, _strict_response_validation=True, account_token=hris_account_token
    )
    loose_client = Merge(
        api_key=api_key, _strict_response_validation=False, account_token=hris_account_token
    )
    parametrize = pytest.mark.parametrize("client", [loose_client], ids=["loose"])

    @parametrize
    def test_method_retrieve_ci_integration(self, client: Merge) -> None:
        employee = client.hris.employees.retrieve(
            test_preexisting_employee_id,
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params_ci_integration(self, client: Merge) -> None:
        expand = ["company"] if not client._strict_response_validation else None

        employee = client.hris.employees.retrieve(
            test_preexisting_employee_id,
            expand=expand,
            include_remote_data=True,
            show_enum_origins="employment_status",
        )

        assert employee is not None
        assert employee.id == test_preexisting_employee_id
        assert isinstance(employee.company, dict)

    @parametrize
    def test_method_list_ci_integration(self, client: Merge) -> None:
        employee = client.hris.employees.list()
        assert_matches_type(SyncPage[Employee], employee, path=["response"])

    @parametrize
    def test_method_list_with_all_params_ci_integration(self, client: Merge) -> None:
        employee = client.hris.employees.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_remote_data=True,
            remote_fields="employment_status",
        )
        assert_matches_type(SyncPage[Employee], employee, path=["response"])


class TestAsyncEmployees:
    strict_client = AsyncMerge(
        api_key=api_key, _strict_response_validation=True, account_token=hris_account_token
    )
    loose_client = AsyncMerge(
        api_key=api_key, _strict_response_validation=False, account_token=hris_account_token
    )
    parametrize = pytest.mark.parametrize("client", [loose_client], ids=["loose"])

    @parametrize
    async def test_method_retrieve_ci_integration(self, client: AsyncMerge) -> None:
        employee = await client.hris.employees.retrieve(
            test_preexisting_employee_id,
        )
        assert_matches_type(Employee, employee, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params_ci_integration(self, client: AsyncMerge) -> None:
        expand = ["company"] if not client._strict_response_validation else None

        employee = await client.hris.employees.retrieve(
            test_preexisting_employee_id,
            expand=expand,
            include_remote_data=True,
            show_enum_origins="employment_status",
        )
        
        assert employee is not None
        assert employee.id == test_preexisting_employee_id
        assert isinstance(employee.company, dict)

    @parametrize
    async def test_method_list_ci_integration(self, client: AsyncMerge) -> None:
        employee = await client.hris.employees.list()
        assert_matches_type(AsyncPage[Employee], employee, path=["response"])

    @parametrize
    async def test_method_list_with_params_ci_integration(self, client: AsyncMerge) -> None:
        employee = await client.hris.employees.list(
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_remote_data=True,
            remote_fields="employment_status",
        )
        assert_matches_type(AsyncPage[Employee], employee, path=["response"])
