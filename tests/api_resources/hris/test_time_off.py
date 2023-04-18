# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.pagination import SyncPage, AsyncPage
from merge.types.hris import TimeOff, TimeOffResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestTimeOff:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        time_off = client.hris.time_off.create(
            model={},
        )
        assert_matches_type(TimeOffResponse, time_off, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        time_off = client.hris.time_off.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TimeOff, time_off, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        time_off = client.hris.time_off.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand="approver",
            include_remote_data=True,
            remote_fields="request_type",
            show_enum_origins="request_type",
        )
        assert_matches_type(TimeOff, time_off, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        time_off = client.hris.time_off.list()
        assert_matches_type(SyncPage[TimeOff], time_off, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        time_off = client.hris.time_off.list(
            approver_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            employee_id="string",
            expand="approver",
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_fields="request_type",
            remote_id="string",
            request_type="BEREAVEMENT",
            show_enum_origins="request_type",
            status="APPROVED",
        )
        assert_matches_type(SyncPage[TimeOff], time_off, path=["response"])


class TestAsyncTimeOff:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        time_off = await client.hris.time_off.create(
            model={},
        )
        assert_matches_type(TimeOffResponse, time_off, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        time_off = await client.hris.time_off.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TimeOff, time_off, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        time_off = await client.hris.time_off.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand="approver",
            include_remote_data=True,
            remote_fields="request_type",
            show_enum_origins="request_type",
        )
        assert_matches_type(TimeOff, time_off, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        time_off = await client.hris.time_off.list()
        assert_matches_type(AsyncPage[TimeOff], time_off, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        time_off = await client.hris.time_off.list(
            approver_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            employee_id="string",
            expand="approver",
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_fields="request_type",
            remote_id="string",
            request_type="BEREAVEMENT",
            show_enum_origins="request_type",
            status="APPROVED",
        )
        assert_matches_type(AsyncPage[TimeOff], time_off, path=["response"])
