# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from datetime import datetime

from .meta import Meta, AsyncMeta
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from .generators import Generators, AsyncGenerators
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types.crm import (
    CustomObject,
    CrmCustomObjectResponse,
    custom_object_list_params,
    custom_object_create_params,
    custom_object_update_params,
    custom_object_retrieve_params,
)
from .associations import Associations, AsyncAssociations
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ...._client import Merge, AsyncMerge

__all__ = ["CustomObjects", "AsyncCustomObjects"]


class CustomObjects(SyncAPIResource):
    associations: Associations
    meta: Meta
    generators: Generators

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.associations = Associations(client)
        self.meta = Meta(client)
        self.generators = Generators(client)

    def create(
        self,
        custom_object_class_id: str,
        *,
        model: custom_object_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CrmCustomObjectResponse:
        """
        Creates a `CustomObject` object with the given values.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects",
            body=maybe_transform({"model": model}, custom_object_create_params.CustomObjectCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrmCustomObjectResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        custom_object_class_id: str,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CustomObject:
        """
        Returns a `CustomObject` object with the given `id`.

        Args:
          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                    },
                    custom_object_retrieve_params.CustomObjectRetrieveParams,
                ),
            ),
            cast_to=CustomObject,
        )

    def update(
        self,
        id: str,
        *,
        custom_object_class_id: str,
        model: custom_object_update_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CrmCustomObjectResponse:
        """
        Updates a `CustomObject` object with the given `id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/{id}",
            body=maybe_transform({"model": model}, custom_object_update_params.CustomObjectUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrmCustomObjectResponse,
        )

    def list(
        self,
        custom_object_class_id: str,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[CustomObject]:
        """
        Returns a list of `CustomObject` objects.

        Args:
          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          remote_id: The API provider's ID for the given object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects",
            page=SyncPage[CustomObject],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_id": remote_id,
                    },
                    custom_object_list_params.CustomObjectListParams,
                ),
            ),
            model=CustomObject,
        )


class AsyncCustomObjects(AsyncAPIResource):
    associations: AsyncAssociations
    meta: AsyncMeta
    generators: AsyncGenerators

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.associations = AsyncAssociations(client)
        self.meta = AsyncMeta(client)
        self.generators = AsyncGenerators(client)

    async def create(
        self,
        custom_object_class_id: str,
        *,
        model: custom_object_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CrmCustomObjectResponse:
        """
        Creates a `CustomObject` object with the given values.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects",
            body=maybe_transform({"model": model}, custom_object_create_params.CustomObjectCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrmCustomObjectResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        custom_object_class_id: str,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CustomObject:
        """
        Returns a `CustomObject` object with the given `id`.

        Args:
          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                    },
                    custom_object_retrieve_params.CustomObjectRetrieveParams,
                ),
            ),
            cast_to=CustomObject,
        )

    async def update(
        self,
        id: str,
        *,
        custom_object_class_id: str,
        model: custom_object_update_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CrmCustomObjectResponse:
        """
        Updates a `CustomObject` object with the given `id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/{id}",
            body=maybe_transform({"model": model}, custom_object_update_params.CustomObjectUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CrmCustomObjectResponse,
        )

    def list(
        self,
        custom_object_class_id: str,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CustomObject, AsyncPage[CustomObject]]:
        """
        Returns a list of `CustomObject` objects.

        Args:
          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          remote_id: The API provider's ID for the given object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects",
            page=AsyncPage[CustomObject],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_id": remote_id,
                    },
                    custom_object_list_params.CustomObjectListParams,
                ),
            ),
            model=CustomObject,
        )
