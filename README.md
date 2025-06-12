# Merge Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fmerge-api%2Fmerge-python-client)
[![pypi](https://img.shields.io/pypi/v/MergePythonClient)](https://pypi.python.org/pypi/MergePythonClient)

The Merge Python library provides convenient access to the Merge API from Python.

## Documentation

API reference documentation is available [here](https://docs.merge.dev/).

## Installation

```sh
pip install MergePythonClient
```

## Reference

A full reference for this library is available [here](https://github.com/merge-api/merge-python-client/blob/HEAD/./reference.md).

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

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

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

The SDK may return paginated results. Endpoints that return paginated results will 
include a `next` and `prev` property on the response. To get the next page, you can 
pass in the value of `next` to the cursor property on the request. Similarly, to 
get the previous page, you can pass in the value of `prev` to the cursor property on 
the request. 

Below is an example of iterating over all pages:
```python

# response contains the first page
response = merge_client.hris.employees.list(created_after="2030-01-01")

# if there is a next page, load it by passing `next` to the cursor argument
while response.next is not None:
    response = hris_client.employees.list(
        cursor=response.next, 
        created_after="2030-01-01")
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
        proxies="http://my.test.proxy.example.com",
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
