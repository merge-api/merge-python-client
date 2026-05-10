import typing

import httpx
import pytest

from merge import Merge, MergeEnvironment


def _list_response() -> httpx.Response:
    return httpx.Response(200, json={"next": None, "previous": None, "results": []})


def _client(environment: typing.Optional[MergeEnvironment] = None,
            base_url: typing.Optional[str] = None) -> typing.Tuple[Merge, typing.List[httpx.Request]]:
    captured: typing.List[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return _list_response()

    kwargs: typing.Dict[str, typing.Any] = {
        "account_token": "test-token",
        "api_key": "test-key",
        "httpx_client": httpx.Client(transport=httpx.MockTransport(handler)),
    }
    if environment is not None:
        kwargs["environment"] = environment
    if base_url is not None:
        kwargs["base_url"] = base_url
    return Merge(**kwargs), captured


def test_default_environment_is_production():
    client, reqs = _client()
    client.ticketing.tickets.list(page_size=1)
    assert str(reqs[0].url).startswith("https://api.merge.dev/api")


def test_sandbox_environment_routes_to_sandbox():
    client, reqs = _client(environment=MergeEnvironment.SANDBOX)
    client.ticketing.tickets.list(page_size=1)
    assert str(reqs[0].url).startswith("https://api-sandbox.merge.dev/api")


def test_production_eu_routes_to_eu_endpoint():
    client, reqs = _client(environment=MergeEnvironment.PRODUCTION_EU)
    client.ticketing.tickets.list(page_size=1)
    assert str(reqs[0].url).startswith("https://api-eu.merge.dev/api")


def test_custom_base_url_overrides_environment():
    client, reqs = _client(
        environment=MergeEnvironment.PRODUCTION,
        base_url="https://proxy.example.com/merge",
    )
    client.ticketing.tickets.list(page_size=1)
    assert str(reqs[0].url).startswith("https://proxy.example.com/merge")
