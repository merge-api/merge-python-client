import typing

import httpx
import pytest

from merge import AsyncMerge, Merge
from merge.resources.crm.resources.contacts.types.contacts_list_request_expand_item import (
    ContactsListRequestExpandItem,
)
from merge.resources.ticketing.resources.tickets.types.tickets_list_request_expand_item import (
    TicketsListRequestExpandItem,
)
from merge.resources.ticketing.resources.tickets.types.tickets_list_request_remote_fields import (
    TicketsListRequestRemoteFields,
)
from merge.resources.ticketing.resources.tickets.types.tickets_list_request_show_enum_origins import (
    TicketsListRequestShowEnumOrigins,
)
from merge.resources.ticketing.resources.tickets.types.tickets_retrieve_request_expand_item import (
    TicketsRetrieveRequestExpandItem,
)
from merge.resources.ticketing.resources.tickets.types.tickets_viewers_list_request_expand_item import (
    TicketsViewersListRequestExpandItem,
)


def _list_response() -> httpx.Response:
    return httpx.Response(200, json={"next": None, "previous": None, "results": []})


@pytest.fixture
def client_and_requests():
    captured: typing.List[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return _list_response()

    httpx_client = httpx.Client(transport=httpx.MockTransport(handler))
    client = Merge(
        account_token="test-token",
        api_key="test-key",
        httpx_client=httpx_client,
    )
    return client, captured


@pytest.fixture
def async_client_and_requests():
    captured: typing.List[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return _list_response()

    httpx_client = httpx.AsyncClient(transport=httpx.MockTransport(handler))
    client = AsyncMerge(
        account_token="test-token",
        api_key="test-key",
        httpx_client=httpx_client,
    )
    return client, captured


def expand_param(request: httpx.Request) -> typing.List[str]:
    return request.url.params.get_list("expand")


def test_expand_omitted(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(page_size=1)
    assert expand_param(reqs[0]) == []


def test_expand_single_string(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(expand="account", page_size=1)
    assert expand_param(reqs[0]) == ["account"]


def test_expand_csv_string(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(expand="account,assignees,creator", page_size=1)
    assert expand_param(reqs[0]) == ["account,assignees,creator"]


def test_expand_empty_list(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(expand=[], page_size=1)
    assert expand_param(reqs[0]) == []


def test_expand_single_item_list(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(expand=[TicketsListRequestExpandItem.ACCOUNT], page_size=1)
    assert expand_param(reqs[0]) == ["account"]


def test_expand_tuple_input(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(
        expand=(
            TicketsListRequestExpandItem.ACCOUNT,
            TicketsListRequestExpandItem.ASSIGNEES,
        ),
        page_size=1,
    )
    assert expand_param(reqs[0]) == ["account,assignees"]


def test_expand_combined_enum_single_relation(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(expand=TicketsListRequestExpandItem.ACCOUNT, page_size=1)
    assert expand_param(reqs[0]) == ["account"]


def test_expand_combined_enum_multi_relation(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(
        expand=[
            TicketsListRequestExpandItem.ASSIGNEES,
            TicketsListRequestExpandItem.ACCOUNT,
            TicketsListRequestExpandItem.CREATOR,
        ],
        page_size=1,
    )
    assert expand_param(reqs[0]) == ["assignees,account,creator"]


def test_string_and_enum_produce_same_url(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(
        expand=[
            TicketsListRequestExpandItem.ASSIGNEES,
            TicketsListRequestExpandItem.ACCOUNT,
            TicketsListRequestExpandItem.CREATOR,
        ],
        page_size=1,
    )
    client.ticketing.tickets.list(expand="assignees,account,creator", page_size=1)
    assert expand_param(reqs[0]) == expand_param(reqs[1])


def test_remote_fields_single_value(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(
        remote_fields=TicketsListRequestRemoteFields.PRIORITY, page_size=1
    )
    assert reqs[0].url.params.get_list("remote_fields") == ["priority"]


def test_show_enum_origins_single_value(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(
        show_enum_origins=TicketsListRequestShowEnumOrigins.PRIORITY, page_size=1
    )
    assert reqs[0].url.params.get_list("show_enum_origins") == ["priority"]


def test_expand_coexists_with_other_params(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(
        expand="account,assignees", page_size=50, cursor="cursor-abc"
    )
    params = reqs[0].url.params
    assert params.get_list("expand") == ["account,assignees"]
    assert params["page_size"] == "50"
    assert params["cursor"] == "cursor-abc"


async def test_async_expand_csv_string(async_client_and_requests):
    client, reqs = async_client_and_requests
    await client.ticketing.tickets.list(expand="account,assignees,creator", page_size=1)
    assert expand_param(reqs[0]) == ["account,assignees,creator"]


async def test_async_expand_combined_enum_multi(async_client_and_requests):
    client, reqs = async_client_and_requests
    await client.ticketing.tickets.list(
        expand=[
            TicketsListRequestExpandItem.ASSIGNEES,
            TicketsListRequestExpandItem.ACCOUNT,
            TicketsListRequestExpandItem.CREATOR,
        ],
        page_size=1,
    )
    assert expand_param(reqs[0]) == ["assignees,account,creator"]


async def test_async_expand_list_of_items(async_client_and_requests):
    client, reqs = async_client_and_requests
    await client.ticketing.tickets.list(
        expand=[TicketsListRequestExpandItem.ACCOUNT, TicketsListRequestExpandItem.ASSIGNEES],
        page_size=1,
    )
    assert expand_param(reqs[0]) == ["account,assignees"]


def test_raw_client_expand(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.with_raw_response.list(expand="account,assignees", page_size=1)
    assert expand_param(reqs[0]) == ["account,assignees"]


def test_retrieve_endpoint_expand():
    captured: typing.List[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(200, json={})

    httpx_client = httpx.Client(transport=httpx.MockTransport(handler))
    client = Merge(account_token="t", api_key="k", httpx_client=httpx_client)
    try:
        client.ticketing.tickets.retrieve(
            "some-id",
            expand=[
                TicketsRetrieveRequestExpandItem.ACCOUNT,
                TicketsRetrieveRequestExpandItem.CREATOR,
            ],
        )
    except Exception:
        pass
    assert expand_param(captured[0]) == ["account,creator"]


def test_viewers_list_endpoint_expand(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.viewers_list(
        "some-id",
        expand=[
            TicketsViewersListRequestExpandItem.USER,
            TicketsViewersListRequestExpandItem.TEAM,
        ],
    )
    assert expand_param(reqs[0]) == ["user,team"]


def test_cross_category_expand(client_and_requests):
    client, reqs = client_and_requests
    client.crm.contacts.list(
        expand=[
            ContactsListRequestExpandItem.ACCOUNT,
            ContactsListRequestExpandItem.OWNER,
        ],
    )
    assert expand_param(reqs[0]) == ["account,owner"]


def test_request_method_and_path(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(expand="account", page_size=1)
    assert reqs[0].method == "GET"
    assert "/api/ticketing/v1/tickets" in str(reqs[0].url)
