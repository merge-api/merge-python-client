# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from merge import Merge, AsyncMerge
from tests.utils import assert_matches_type
from merge._utils import parse_datetime
from merge.pagination import SyncPage, AsyncPage
from merge.types.crm.custom_object_classes import (
    AssociationType,
    CrmAssociationTypeResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAssociationTypes:
    strict_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = Merge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Merge) -> None:
        association_type = client.crm.custom_object_classes.association_types.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model={
                "source_object_class": {
                    "id": "x",
                    "origin_type": "CUSTOM_OBJECT",
                },
                "target_object_classes": [
                    {
                        "id": "x",
                        "origin_type": "CUSTOM_OBJECT",
                    },
                    {
                        "id": "x",
                        "origin_type": "CUSTOM_OBJECT",
                    },
                    {
                        "id": "x",
                        "origin_type": "CUSTOM_OBJECT",
                    },
                ],
                "remote_key_name": "x",
            },
        )
        assert_matches_type(CrmAssociationTypeResponse, association_type, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Merge) -> None:
        association_type = client.crm.custom_object_classes.association_types.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_object_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AssociationType, association_type, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Merge) -> None:
        association_type = client.crm.custom_object_classes.association_types.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_object_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["target_object_classes", "target_object_classes", "target_object_classes"],
            include_remote_data=True,
        )
        assert_matches_type(AssociationType, association_type, path=["response"])

    @parametrize
    def test_method_list(self, client: Merge) -> None:
        association_type = client.crm.custom_object_classes.association_types.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncPage[AssociationType], association_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Merge) -> None:
        association_type = client.crm.custom_object_classes.association_types.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            expand=["target_object_classes", "target_object_classes", "target_object_classes"],
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_id="string",
        )
        assert_matches_type(SyncPage[AssociationType], association_type, path=["response"])


class TestAsyncAssociationTypes:
    strict_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=True, account_token="<account-token>"
    )
    loose_client = AsyncMerge(
        base_url=base_url, api_key=api_key, _strict_response_validation=False, account_token="<account-token>"
    )
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMerge) -> None:
        association_type = await client.crm.custom_object_classes.association_types.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            model={
                "source_object_class": {
                    "id": "x",
                    "origin_type": "CUSTOM_OBJECT",
                },
                "target_object_classes": [
                    {
                        "id": "x",
                        "origin_type": "CUSTOM_OBJECT",
                    },
                    {
                        "id": "x",
                        "origin_type": "CUSTOM_OBJECT",
                    },
                    {
                        "id": "x",
                        "origin_type": "CUSTOM_OBJECT",
                    },
                ],
                "remote_key_name": "x",
            },
        )
        assert_matches_type(CrmAssociationTypeResponse, association_type, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMerge) -> None:
        association_type = await client.crm.custom_object_classes.association_types.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_object_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AssociationType, association_type, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, client: AsyncMerge) -> None:
        association_type = await client.crm.custom_object_classes.association_types.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_object_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expand=["target_object_classes", "target_object_classes", "target_object_classes"],
            include_remote_data=True,
        )
        assert_matches_type(AssociationType, association_type, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMerge) -> None:
        association_type = await client.crm.custom_object_classes.association_types.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncPage[AssociationType], association_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMerge) -> None:
        association_type = await client.crm.custom_object_classes.association_types.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            cursor="string",
            expand=["target_object_classes", "target_object_classes", "target_object_classes"],
            include_deleted_data=True,
            include_remote_data=True,
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_size=0,
            remote_id="string",
        )
        assert_matches_type(AsyncPage[AssociationType], association_type, path=["response"])
