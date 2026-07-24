import httpx
import pydantic
import pytest

from merge import Merge
from merge.core import ApiError, ParsingError
from merge.core.http_response import HttpResponse
from merge.core.unchecked_base_model import construct_type
from merge.resources.accounting.types.account import Account
from merge.resources.accounting.types.paginated_account_list import PaginatedAccountList


MALFORMED_ACCOUNT = {
    "id": 12345,
    "name": 999,
    "current_balance": "not-a-number",
    "created_at": "definitely-not-a-datetime",
    "status": {"unexpected": "shape"},
    "company": ["wrong", "container"],
    "classification": 3.14,
    "totally_unexpected_key": {"nested": [1, 2, 3]},
}

MALFORMED_PAGE = {
    "next": 42,
    "previous": {"not": "a-string"},
    "results": [MALFORMED_ACCOUNT, "a-bare-string-not-an-object", 777],
}


def _client_with_response(response: httpx.Response) -> Merge:
    def handler(request: httpx.Request) -> httpx.Response:
        return response

    httpx_client = httpx.Client(transport=httpx.MockTransport(handler))
    return Merge(account_token="test-token", api_key="test-key", httpx_client=httpx_client)


def test_malformed_input_is_genuinely_schema_violating():
    with pytest.raises(pydantic.ValidationError):
        Account.model_validate(MALFORMED_ACCOUNT)


def test_parsing_error_is_not_in_the_api_error_hierarchy():
    assert not issubclass(ParsingError, ApiError)
    assert not issubclass(ApiError, ParsingError)


def test_construct_type_does_not_raise_on_malformed_account():
    result = construct_type(type_=Account, object_=MALFORMED_ACCOUNT)
    assert isinstance(result, Account)


def test_construct_type_does_not_raise_on_malformed_paginated_list():
    result = construct_type(type_=PaginatedAccountList, object_=MALFORMED_PAGE)
    assert isinstance(result, PaginatedAccountList)


def test_success_path_with_schema_violating_body_never_raises_parsing_error():
    client = _client_with_response(httpx.Response(200, json=MALFORMED_PAGE))
    result = client.accounting.accounts.list()
    assert isinstance(result, PaginatedAccountList)


def test_raw_success_path_returns_http_response_not_parsing_error():
    client = _client_with_response(httpx.Response(200, json=MALFORMED_PAGE))
    raw = client.accounting.accounts.with_raw_response.list()
    assert isinstance(raw, HttpResponse)


def test_error_path_raises_api_error_not_parsing_error():
    client = _client_with_response(httpx.Response(400, text="<html>gateway error</html>"))
    with pytest.raises(ApiError) as exc_info:
        client.accounting.accounts.list()
    assert not isinstance(exc_info.value, ParsingError)
    assert exc_info.value.status_code == 400
