import httpx
import pytest

from merge import Merge
from merge.resources.ticketing.resources.tickets.types.tickets_list_request_expand import (
    TicketsListRequestExpand,
)


@pytest.fixture
def client_and_requests():
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(
            200, json={"next": None, "previous": None, "results": []}
        )

    httpx_client = httpx.Client(transport=httpx.MockTransport(handler))
    client = Merge(
        account_token="test-token",
        api_key="test-key",
        httpx_client=httpx_client,
    )
    return client, captured


def expand_param(request: httpx.Request) -> list[str]:
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


def test_expand_combined_enum_single_relation(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(
        expand=TicketsListRequestExpand.ACCOUNT, page_size=1
    )
    assert expand_param(reqs[0]) == ["account"]


def test_expand_combined_enum_multi_relation(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(
        expand=TicketsListRequestExpand.ASSIGNEES_ACCOUNT_CREATOR, page_size=1
    )
    assert expand_param(reqs[0]) == ["assignees,account,creator"]


def test_string_and_enum_produce_same_url(client_and_requests):
    client, reqs = client_and_requests
    client.ticketing.tickets.list(
        expand=TicketsListRequestExpand.ASSIGNEES_ACCOUNT_CREATOR, page_size=1
    )
    client.ticketing.tickets.list(expand="assignees,account,creator", page_size=1)
    assert expand_param(reqs[0]) == expand_param(reqs[1])
