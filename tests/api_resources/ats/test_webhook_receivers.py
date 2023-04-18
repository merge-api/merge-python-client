# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type
from merge.types.ats import WebhookReceiverListResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestWebhookReceivers:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        webhook_receiver = client.ats.webhook_receivers.create(
            event="x",
            is_active=True,
        )
        assert_matches_type(shared.WebhookReceiver, webhook_receiver, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Merge) -> None:
        webhook_receiver = client.ats.webhook_receivers.create(
            event="x",
            is_active=True,
            key="x",
        )
        assert_matches_type(shared.WebhookReceiver, webhook_receiver, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        webhook_receiver = client.ats.webhook_receivers.list()
        assert_matches_type(WebhookReceiverListResponse, webhook_receiver, path=["response"])


class TestAsyncWebhookReceivers:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        webhook_receiver = await client.ats.webhook_receivers.create(
            event="x",
            is_active=True,
        )
        assert_matches_type(shared.WebhookReceiver, webhook_receiver, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncMerge) -> None:
        webhook_receiver = await client.ats.webhook_receivers.create(
            event="x",
            is_active=True,
            key="x",
        )
        assert_matches_type(shared.WebhookReceiver, webhook_receiver, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        webhook_receiver = await client.ats.webhook_receivers.list()
        assert_matches_type(WebhookReceiverListResponse, webhook_receiver, path=["response"])
