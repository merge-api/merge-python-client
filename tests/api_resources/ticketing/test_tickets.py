# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.pagination import SyncPage, AsyncPage
from merge.types.ticketing import Ticket, TicketingUser, TicketResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestTickets:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        ticket = client.ticketing.tickets.create(
            model={},
        )
        assert_matches_type(TicketResponse, ticket, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        ticket = client.ticketing.tickets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Ticket, ticket, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        ticket = client.ticketing.tickets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["account", "account", "account"],
            include_remote_data=True,
            include_remote_fields=True,
            remote_fields="priority",
            show_enum_origins="priority",
        )
        assert_matches_type(Ticket, ticket, path=["response"])

    @parametrize
    def test_method_update(self, client: Merge) -> None:
        ticket = client.ticketing.tickets.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model={},
        )
        assert_matches_type(TicketResponse, ticket, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        ticket = client.ticketing.tickets.list()
        assert_matches_type(SyncPage[Ticket], ticket, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        ticket = client.ticketing.tickets.list(
            account_id="string",
            assignee_ids="string",
            collection_ids="string",
            completed_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            completed_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            contact_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            due_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            due_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            expand=["account", "account", "account"],
            include_deleted_data=True,
            include_remote_data=True,
            include_remote_fields=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            parent_ticket_id="string",
            priority="HIGH",
            project_id="string",
            remote_created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            remote_created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            remote_fields="priority",
            remote_id="string",
            remote_updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            remote_updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            show_enum_origins="priority",
            status="CLOSED",
            tags="string",
            ticket_type="string",
        )
        assert_matches_type(SyncPage[Ticket], ticket, path=["response"])

    @parametrize
    def test_method_list_collaborators(self, client: Merge) -> None:
        ticket = client.ticketing.tickets.list_collaborators(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncPage[TicketingUser], ticket, path=["response"])

    @parametrize
    def test_method_list_collaborators_with_all_params(self, client: Merge) -> None:
        ticket = client.ticketing.tickets.list_collaborators(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="string",
            expand=["teams", "teams", "teams"],
            include_deleted_data=True,
            include_remote_data=True,
            page_size=0,
        )
        assert_matches_type(SyncPage[TicketingUser], ticket, path=["response"])

    @parametrize
    def test_method_list_remote_field_classes(self, client: Merge) -> None:
        ticket = client.ticketing.tickets.list_remote_field_classes()
        assert_matches_type(SyncPage[shared.RemoteFieldClass], ticket, path=["response"])

    @parametrize
    def test_method_list_remote_field_classes_with_all_params(self, client: Merge) -> None:
        ticket = client.ticketing.tickets.list_remote_field_classes(
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            page_size=0,
        )
        assert_matches_type(SyncPage[shared.RemoteFieldClass], ticket, path=["response"])


class TestAsyncTickets:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        ticket = await client.ticketing.tickets.create(
            model={},
        )
        assert_matches_type(TicketResponse, ticket, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        ticket = await client.ticketing.tickets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Ticket, ticket, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        ticket = await client.ticketing.tickets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["account", "account", "account"],
            include_remote_data=True,
            include_remote_fields=True,
            remote_fields="priority",
            show_enum_origins="priority",
        )
        assert_matches_type(Ticket, ticket, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncMerge) -> None:
        ticket = await client.ticketing.tickets.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model={},
        )
        assert_matches_type(TicketResponse, ticket, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        ticket = await client.ticketing.tickets.list()
        assert_matches_type(AsyncPage[Ticket], ticket, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        ticket = await client.ticketing.tickets.list(
            account_id="string",
            assignee_ids="string",
            collection_ids="string",
            completed_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            completed_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            contact_id="string",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            due_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            due_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            expand=["account", "account", "account"],
            include_deleted_data=True,
            include_remote_data=True,
            include_remote_fields=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            parent_ticket_id="string",
            priority="HIGH",
            project_id="string",
            remote_created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            remote_created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            remote_fields="priority",
            remote_id="string",
            remote_updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            remote_updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            show_enum_origins="priority",
            status="CLOSED",
            tags="string",
            ticket_type="string",
        )
        assert_matches_type(AsyncPage[Ticket], ticket, path=["response"])

    @parametrize
    async def test_method_list_collaborators(self, client: AsyncMerge) -> None:
        ticket = await client.ticketing.tickets.list_collaborators(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncPage[TicketingUser], ticket, path=["response"])

    @parametrize
    async def test_method_list_collaborators_with_all_params(self, client: AsyncMerge) -> None:
        ticket = await client.ticketing.tickets.list_collaborators(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            cursor="string",
            expand=["teams", "teams", "teams"],
            include_deleted_data=True,
            include_remote_data=True,
            page_size=0,
        )
        assert_matches_type(AsyncPage[TicketingUser], ticket, path=["response"])

    @parametrize
    async def test_method_list_remote_field_classes(self, client: AsyncMerge) -> None:
        ticket = await client.ticketing.tickets.list_remote_field_classes()
        assert_matches_type(AsyncPage[shared.RemoteFieldClass], ticket, path=["response"])

    @parametrize
    async def test_method_list_remote_field_classes_with_all_params(self, client: AsyncMerge) -> None:
        ticket = await client.ticketing.tickets.list_remote_field_classes(
            cursor="string",
            include_deleted_data=True,
            include_remote_data=True,
            page_size=0,
        )
        assert_matches_type(AsyncPage[shared.RemoteFieldClass], ticket, path=["response"])
