import typing

import httpx
import pytest

from merge import Merge
from merge.core import ApiError


def _client_with_response(
    response: httpx.Response,
) -> Merge:
    def handler(request: httpx.Request) -> httpx.Response:
        return response

    httpx_client = httpx.Client(transport=httpx.MockTransport(handler))
    return Merge(
        account_token="test-token",
        api_key="test-key",
        httpx_client=httpx_client,
    )


def test_404_raises_api_error_with_status_code_and_body():
    client = _client_with_response(
        httpx.Response(404, json={"detail": "Not found."})
    )
    with pytest.raises(ApiError) as exc_info:
        client.ticketing.tickets.retrieve("nonexistent-id")
    assert exc_info.value.status_code == 404
    assert exc_info.value.body == {"detail": "Not found."}


def test_429_propagates_retry_after_header():
    client = _client_with_response(
        httpx.Response(
            429,
            json={"detail": "Request was throttled."},
            headers={"Retry-After": "60"},
        )
    )
    with pytest.raises(ApiError) as exc_info:
        client.ticketing.tickets.list()
    assert exc_info.value.status_code == 429
    assert exc_info.value.headers is not None
    assert exc_info.value.headers.get("retry-after") == "60"


def test_non_json_error_body_does_not_crash_handler():
    client = _client_with_response(
        httpx.Response(
            502,
            text="Bad Gateway",
            headers={"Content-Type": "text/html"},
        )
    )
    with pytest.raises(ApiError) as exc_info:
        client.ticketing.tickets.list()
    assert exc_info.value.status_code == 502
    assert exc_info.value.body == "Bad Gateway"
