# Merge Python Library

[![pypi](https://img.shields.io/pypi/v/MergePythonClient.svg)](https://pypi.python.org/pypi/MergePythonClient)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://github.com/fern-api/fern)

The Merge Python library provides access to the Merge API from Python.

## Documentation

API reference documentation is available [here](https://docs.merge.dev/).

## Installation

```sh
pip install --upgrade MergePythonClient
```

## Instantiation

```python
import merge
from merge.client import Merge

client = Merge(api_key="YOUR_API_KEY", account_token="YOUR_ACCOUNT_TOKEN")
```

## Categories

This SDK contains both the ATS, HRIS, CRM, Ticketing, and Accounting categories. Even if you do not plan on using more than one Merge API category right now, the SDK provides upgrade-flexibility in case you find new Merge API categories useful in the future.

Each category is namespaced:

```python
client = Merge(api_key="YOUR_API_KEY")

client.ats. # APIs specific to the ATS Category

client.hris. # APIs specific to the HRIS Category
```

## Usage

## Create Link Token

```python
import merge
from merge.client import Merge

merge_client = Merge(
    api_key="<YOUR_API_KEY>", 
    account_token="<YOUR_ACCOUNT_TOKEN>")

link_token_response = merge_client.ats.link_token.create(
    end_user_email_address="john.smith@gmail.com",
    end_user_organization_name="acme",
    end_user_origin_id="1234",
    categories=[CategoriesEnum.ATS],
    link_expiry_mins=30,
)

print("Created link token", link_token_response.link_token)
```

## Get Employee

```python
import merge
from merge.client import Merge

merge_client = Merge(
    api_key="<YOUR_API_KEY>", 
    account_token="<YOUR_ACCOUNT_TOKEN>")

employee = merge_client.hris.employees.retrieve(
    id="0958cbc6-6040-430a-848e-aafacbadf4ae")
```

## Get Candidate

```python
import merge
from merge.client import Merge

merge_client = Merge(
    api_key="<YOUR_API_KEY>", 
    account_token="<YOUR_ACCOUNT_TOKEN>")

candidate = merge_client.ats.candidates.retrieve(
    id="521b18c2-4d01-4297-b451-19858d07c133")
```

## Filter Candidate

```python
import merge
from merge.client import Merge

merge_client = Merge(
    api_key="<YOUR_API_KEY>", 
    account_token="<YOUR_ACCOUNT_TOKEN>")

candidates_response = merge_client.ats.candidates.list(
    created_after="2030-01-01")

print(candidates_response.result)
```

## Get Contact

```python
import merge
from merge.client import Merge

merge_client = Merge(
    api_key="<YOUR_API_KEY>", 
    account_token="<YOUR_ACCOUNT_TOKEN>")

contact = merge_client.accounting.contacts.retrieve(
    id="c640b80b-fac9-409f-aa19-1f9221aec445")
```

## Create Ticket

```python
import merge
from merge.client import Merge

merge_client = Merge(
    api_key="<YOUR_API_KEY>", 
    account_token="<YOUR_ACCOUNT_TOKEN>")

merge_client.ticketing.tickets.create(
    model=merge.ticketing.TicketRequest(
        name="Please add more integrations",
        assignees=[
            "17a54124-287f-494d-965e-3c5b330c9a68"
        ],
        creator="3fa85f64-5717-4562-b3fc-2c963f66afa6",
        due_date="2022-10-11T00:00:00Z",
        status=merge.ticketing.TicketRequestStatus.OPEN,
    ))
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


## Beta status

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning the package version to a specific version in your package.json file. This way, you can install the same version each time without breaking changes unless you are intentionally looking for the latest version.

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
