# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestPassthroughRequests:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_send(self, client: Merge) -> None:
        passthrough_request = client.accounting.passthrough_requests.send(
            method="GET",
            path="/scooters",
        )
        assert_matches_type(shared.RemoteResponse, passthrough_request, path=["response"])

    @parametrize
    def test_method_send_with_all_params(self, client: Merge) -> None:
        passthrough_request = client.accounting.passthrough_requests.send(
            method="GET",
            path="/scooters",
            base_url_override="x",
            data='{"company": "Lime", "model": "Gen 2.5"}',
            multipart_form_data=[
                {
                    "name": "resume",
                    "data": "SW50ZWdyYXRlIGZhc3QKSW50ZWdyYXRlIG9uY2U=",
                    "encoding": "RAW",
                    "file_name": "resume.pdf",
                    "content_type": "application/pdf",
                },
                {
                    "name": "resume",
                    "data": "SW50ZWdyYXRlIGZhc3QKSW50ZWdyYXRlIG9uY2U=",
                    "encoding": "RAW",
                    "file_name": "resume.pdf",
                    "content_type": "application/pdf",
                },
                {
                    "name": "resume",
                    "data": "SW50ZWdyYXRlIGZhc3QKSW50ZWdyYXRlIG9uY2U=",
                    "encoding": "RAW",
                    "file_name": "resume.pdf",
                    "content_type": "application/pdf",
                },
            ],
            headers={"EXTRA-HEADER": "value"},
            request_format="JSON",
            normalize_response=True,
        )
        assert_matches_type(shared.RemoteResponse, passthrough_request, path=["response"])


class TestAsyncPassthroughRequests:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_send(self, client: AsyncMerge) -> None:
        passthrough_request = await client.accounting.passthrough_requests.send(
            method="GET",
            path="/scooters",
        )
        assert_matches_type(shared.RemoteResponse, passthrough_request, path=["response"])

    @parametrize
    async def test_method_send_with_all_params(self, client: AsyncMerge) -> None:
        passthrough_request = await client.accounting.passthrough_requests.send(
            method="GET",
            path="/scooters",
            base_url_override="x",
            data='{"company": "Lime", "model": "Gen 2.5"}',
            multipart_form_data=[
                {
                    "name": "resume",
                    "data": "SW50ZWdyYXRlIGZhc3QKSW50ZWdyYXRlIG9uY2U=",
                    "encoding": "RAW",
                    "file_name": "resume.pdf",
                    "content_type": "application/pdf",
                },
                {
                    "name": "resume",
                    "data": "SW50ZWdyYXRlIGZhc3QKSW50ZWdyYXRlIG9uY2U=",
                    "encoding": "RAW",
                    "file_name": "resume.pdf",
                    "content_type": "application/pdf",
                },
                {
                    "name": "resume",
                    "data": "SW50ZWdyYXRlIGZhc3QKSW50ZWdyYXRlIG9uY2U=",
                    "encoding": "RAW",
                    "file_name": "resume.pdf",
                    "content_type": "application/pdf",
                },
            ],
            headers={"EXTRA-HEADER": "value"},
            request_format="JSON",
            normalize_response=True,
        )
        assert_matches_type(shared.RemoteResponse, passthrough_request, path=["response"])
