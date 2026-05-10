import datetime as dt
import typing

import httpx
import pytest

from merge import Merge


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


def test_created_after_utc_serializes_with_offset(client_and_requests):
    client, reqs = client_and_requests
    when = dt.datetime(2026, 1, 15, 9, 30, tzinfo=dt.timezone.utc)
    client.ticketing.tickets.list(created_after=when)
    assert reqs[0].url.params["created_after"] == "2026-01-15T09:30:00Z"


def test_non_utc_offset_preserved(client_and_requests):
    client, reqs = client_and_requests
    when = dt.datetime(
        2026, 1, 15, 9, 30, tzinfo=dt.timezone(dt.timedelta(hours=-5))
    )
    client.ticketing.tickets.list(created_after=when)
    assert reqs[0].url.params["created_after"] == "2026-01-15T09:30:00-05:00"


def test_remote_updated_filter_pair(client_and_requests):
    client, reqs = client_and_requests
    after = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
    before = dt.datetime(2026, 2, 1, tzinfo=dt.timezone.utc)
    client.ticketing.tickets.list(
        remote_updated_after=after, remote_updated_before=before
    )
    assert reqs[0].url.params["remote_updated_after"] == "2026-01-01T00:00:00Z"
    assert reqs[0].url.params["remote_updated_before"] == "2026-02-01T00:00:00Z"
