# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from merge.types import shared
from tests.utils import assert_matches_type

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLinkTokens:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        link_token = client.file_storage.link_tokens.create(
            end_user_email_address="x",
            end_user_organization_name="x",
            end_user_origin_id="x",
            categories=["hris", "hris", "hris"],
        )
        assert_matches_type(shared.LinkToken, link_token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Merge) -> None:
        link_token = client.file_storage.link_tokens.create(
            end_user_email_address="x",
            end_user_organization_name="x",
            end_user_origin_id="x",
            categories=["hris", "hris", "hris"],
            integration="x",
            link_expiry_mins=30,
            should_create_magic_link_url=True,
            common_models=[
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
            ],
        )
        assert_matches_type(shared.LinkToken, link_token, path=["response"])


class TestAsyncLinkTokens:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        link_token = await client.file_storage.link_tokens.create(
            end_user_email_address="x",
            end_user_organization_name="x",
            end_user_origin_id="x",
            categories=["hris", "hris", "hris"],
        )
        assert_matches_type(shared.LinkToken, link_token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncMerge) -> None:
        link_token = await client.file_storage.link_tokens.create(
            end_user_email_address="x",
            end_user_organization_name="x",
            end_user_origin_id="x",
            categories=["hris", "hris", "hris"],
            integration="x",
            link_expiry_mins=30,
            should_create_magic_link_url=True,
            common_models=[
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
                {
                    "model_id": "hris.Employee",
                    "enabled_actions": ["READ", "READ", "READ"],
                    "disabled_fields": ["x", "x", "x"],
                },
            ],
        )
        assert_matches_type(shared.LinkToken, link_token, path=["response"])
