# Merge Python API Library

[![PyPI version](https://img.shields.io/pypi/v/MergePythonClient.svg)](https://pypi.org/project/MergePythonClient/)

The Merge Python library provides convenient access to the Merge REST API from any Python 3.7+
application. It includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Documentation

The API documentation can be found [here](https://docs.merge.dev).

## Installation

```sh
pip install MergePythonClient
```

## Usage

```python
from merge import Merge

merge = Merge(
    # defaults to os.environ.get("MERGE_API_KEY")
    api_key="my api key",
)

account_detail = merge.hris.account_details.retrieve()
```

While you can provide an `api_key` keyword argument, we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
and adding `MERGE_API_KEY="my api key"` to your `.env` file so that your API Key is not stored in source control.

## Async Usage

Simply import `AsyncMerge` instead of `Merge` and use `await` with each API call:

```python
from merge import AsyncMerge

merge = AsyncMerge(
    # defaults to os.environ.get("MERGE_API_KEY")
    api_key="my api key",
)


async def main():
    account_detail = await merge.hris.account_details.retrieve()
    print(account_detail)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using Types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict), while responses are [Pydantic](https://pydantic-docs.helpmanual.io/) models. This helps provide autocomplete and documentation within your editor.

If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `"basic"`.

## Pagination

List methods in the Merge API are paginated.

This library provides auto-paginating iterators with each list response, so you do not have to request successive pages manually:

```python
import merge

merge = Merge()

all_sync_statuses = []
# Automatically fetches more pages as needed.
for sync_status in merge.hris.sync_status.list():
    # Do something with sync_status here
    all_sync_statuses.append(sync_status)
print(all_sync_statuses)
```

Or, asynchronously:

```python
import asyncio
import merge

merge = AsyncMerge()


async def main() -> None:
    all_sync_statuses = []
    # Iterate through items across all pages, issuing requests as needed.
    async for sync_status in merge.hris.sync_status.list():
        all_sync_statuses.append(sync_status)
    print(all_sync_statuses)


asyncio.run(main())
```

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

```python
first_page = await merge.hris.sync_status.list()
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.results)}")

# Remove `await` for non-async usage.
```

Or just work directly with the returned data:

```python
first_page = await merge.hris.sync_status.list()

print(f"next page cursor: {first_page.next}")  # => "next page cursor: ..."
for sync_status in first_page.results:
    print(sync_status.model_name)

# Remove `await` for non-async usage.
```

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from merge import Merge

merge = Merge()

merge.hris.account_details.retrieve(
    params={},
)
```

## Handling errors

When the library is unable to connect to the API (e.g., due to network connection problems or a timeout), a subclass of `merge.APIConnectionError` is raised.

When the API returns a non-success status code (i.e., 4xx or 5xx
response), a subclass of `merge.APIStatusError` will be raised, containing `status_code` and `response` properties.

All errors inherit from `merge.APIError`.

```python
from merge import Merge

merge = Merge()

try:
    merge.hris.account_details.retrieve()
except merge.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except merge.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except merge.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors will be automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 409 Conflict, 429 Rate Limit,
and >=500 Internal errors will all be retried by default.

You can use the `max_retries` option to configure or disable this:

```python
from merge import Merge

# Configure the default for all requests:
merge = Merge(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
merge.with_options(max_retries=5).hris.account_details.retrieve()
```

### Timeouts

Requests time out after 60 seconds by default. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration):

```python
from merge import Merge

# Configure the default for all requests:
merge = Merge(
    # default is 60s
    timeout=20.0,
)

# More granular control:
merge = Merge(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
merge.with_options(timeout=5 * 1000).hris.account_details.retrieve()
```

On timeout, an `APITimeoutError` is thrown.

Note that requests which time out will be [retried twice by default](#retries).

## Advanced: Configuring custom URLs, proxies, and transports

You can configure the following keyword arguments when instantiating the client:

```python
import httpx
from merge import Merge

merge = Merge(
    # Use a custom base URL
    base_url="http://my.test.server.example.com:8083",
    proxies="http://my.test.proxy.example.com",
    transport=httpx.HTTPTransport(local_address="0.0.0.0"),
)
```

See the httpx documentation for information about the [`proxies`](https://www.python-httpx.org/advanced/#http-proxying) and [`transport`](https://www.python-httpx.org/advanced/#custom-transports) keyword arguments.

## Status

This package is in beta. Its internals and interfaces are not stable and subject to change without a major semver bump;
please reach out if you rely on any undocumented behavior.

We are keen for your feedback; please email us at [hello@merge.dev](mailto:hello@merge.dev) or open an issue with questions,
bugs, or suggestions.

## Requirements

Python 3.7 or higher.