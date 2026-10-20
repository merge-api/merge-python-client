import httpx
import pytest

from merge import AsyncMerge, Merge


@pytest.mark.parametrize("milliseconds", ["1", "1500", "3000", "invalid"])
def test_sync_honors_retry_after_milliseconds(monkeypatch, milliseconds):
    delays = []
    requests = []

    def respond(request):
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(429, headers={"retry-after-ms": milliseconds, "retry-after": "9"})
        return httpx.Response(200, json={"results": []})

    monkeypatch.setattr("merge.core.http_client.time.sleep", delays.append)
    with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
        client = Merge(api_key="test-key", account_token="test-account", httpx_client=transport)
        result = client.hris.employees.list(request_options={"max_retries": 1})

    assert result.results == []
    assert len(requests) == 2
    assert delays == [9.0 if milliseconds == "invalid" else int(milliseconds) / 1000]


@pytest.mark.parametrize("milliseconds", ["1", "1500", "3000", "invalid"])
async def test_async_honors_retry_after_milliseconds(monkeypatch, milliseconds):
    delays = []
    requests = []

    def respond(request):
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(429, headers={"retry-after-ms": milliseconds, "retry-after": "9"})
        return httpx.Response(200, json={"results": []})

    async def record_sleep(delay):
        delays.append(delay)

    monkeypatch.setattr("merge.core.http_client.asyncio.sleep", record_sleep)
    async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as transport:
        client = AsyncMerge(api_key="test-key", account_token="test-account", httpx_client=transport)
        result = await client.hris.employees.list(request_options={"max_retries": 1})

    assert result.results == []
    assert len(requests) == 2
    assert delays == [9.0 if milliseconds == "invalid" else int(milliseconds) / 1000]
