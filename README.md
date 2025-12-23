# Merge Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fmerge-api%2Fmerge-python-client)
[![pypi](https://img.shields.io/pypi/v/MergePythonClient)](https://pypi.python.org/pypi/MergePythonClient)

The Merge Python library provides convenient access to the Merge APIs from Python.

## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Instantiation](#instantiation)
- [Categories](#categories)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)
- [File Download](#file-download)
- [Pagination](#pagination)

## Documentation

API reference documentation is available [here](https://docs.merge.dev/).

## Installation

```sh
pip install MergePythonClient
```

## Reference

A full reference for this library is available [here](https://github.com/merge-api/merge-python-client/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from merge import Merge
from merge.resources.ats import ActivityRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.activities.create(
    model=ActivityRequest(),
    remote_user_id="remote_user_id",
)
```

## Instantiation

```python
import merge
from merge.client import Merge

client = Merge(api_key="YOUR_API_KEY", account_token="YOUR_ACCOUNT_TOKEN")
```

## Categories

This SDK contains the ATS, HRIS, CRM, Ticketing, Accounting, and File Storage categories. Even if you do not plan on using more than one Merge API category right now, the SDK provides upgrade-flexibility in case you find new Merge API categories useful in the future.

Each category is namespaced:

```python
client = Merge(api_key="YOUR_API_KEY")

client.ats. # APIs specific to the ATS Category

client.hris. # APIs specific to the HRIS Category
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from merge import AsyncMerge
from merge.resources.ats import ActivityRequest

client = AsyncMerge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)


async def main() -> None:
    await client.ats.activities.create(
        model=ActivityRequest(),
        remote_user_id="remote_user_id",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from merge.core.api_error import ApiError

try:
    client.ats.activities.create(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from merge import Merge

client = Merge(
    ...,
)
response = client.ats.activities.with_raw_response.create(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object
pager = client.ats.activities.list(...)
print(pager.response)  # access the typed response for the first page
for item in pager:
    print(item)  # access the underlying object(s)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)  # access the underlying object(s)
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.ats.activities.create(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from merge import Merge

client = Merge(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.ats.activities.create(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from merge import Merge

client = Merge(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
## File Download

```python
import merge
from merge.client import Merge

merge_client = Merge(
    api_key="<YOUR_API_KEY>", 
    account_token="<YOUR_ACCOUNT_TOKEN>")

files = merge_client.filestorage.files.list(name="<FILE_NAME>").results

id = files[0].id
name = files[0].name
local_filename = f"<LOCAL_FILE_PATH>/{name}"

response = merge_client.filestorage.files.download_retrieve(id=id)
with open(local_filename, "wb") as f:
    for chunk in response:
        f.write(chunk)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.ats.activities.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

```python
# You can also iterate through pages and access the typed response per page
pager = client.ats.activities.list(...)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)
```

