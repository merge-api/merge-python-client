# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

from ...types import shared
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.file_storage import (
    SelectiveSyncListConfigurationsResponse,
    SelectiveSyncReplaceConfigurationsResponse,
    selective_sync_list_metadata_params,
    selective_sync_replace_configurations_params,
)

__all__ = ["SelectiveSync", "AsyncSelectiveSync"]


class SelectiveSync(SyncAPIResource):
    def list_configurations(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SelectiveSyncListConfigurationsResponse:
        """Get a linked account's selective syncs."""
        return self._get(
            "/filestorage/v1/selective-sync/configurations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelectiveSyncListConfigurationsResponse,
        )

    def list_metadata(
        self,
        *,
        common_model: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[shared.ConditionSchema]:
        """
        Get metadata for the conditions available to a linked account.

        Args:
          cursor: The pagination cursor value.

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/filestorage/v1/selective-sync/meta",
            page=SyncPage[shared.ConditionSchema],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "common_model": common_model,
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    selective_sync_list_metadata_params.SelectiveSyncListMetadataParams,
                ),
            ),
            model=shared.ConditionSchema,
        )

    def replace_configurations(
        self,
        *,
        sync_configurations: List[selective_sync_replace_configurations_params.SyncConfiguration],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SelectiveSyncReplaceConfigurationsResponse:
        """
        Replace a linked account's selective syncs.

        Args:
          sync_configurations: The selective syncs associated with a linked account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/filestorage/v1/selective-sync/configurations",
            body=maybe_transform(
                {"sync_configurations": sync_configurations},
                selective_sync_replace_configurations_params.SelectiveSyncReplaceConfigurationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelectiveSyncReplaceConfigurationsResponse,
        )


class AsyncSelectiveSync(AsyncAPIResource):
    async def list_configurations(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SelectiveSyncListConfigurationsResponse:
        """Get a linked account's selective syncs."""
        return await self._get(
            "/filestorage/v1/selective-sync/configurations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelectiveSyncListConfigurationsResponse,
        )

    def list_metadata(
        self,
        *,
        common_model: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[shared.ConditionSchema, AsyncPage[shared.ConditionSchema]]:
        """
        Get metadata for the conditions available to a linked account.

        Args:
          cursor: The pagination cursor value.

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/filestorage/v1/selective-sync/meta",
            page=AsyncPage[shared.ConditionSchema],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "common_model": common_model,
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    selective_sync_list_metadata_params.SelectiveSyncListMetadataParams,
                ),
            ),
            model=shared.ConditionSchema,
        )

    async def replace_configurations(
        self,
        *,
        sync_configurations: List[selective_sync_replace_configurations_params.SyncConfiguration],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SelectiveSyncReplaceConfigurationsResponse:
        """
        Replace a linked account's selective syncs.

        Args:
          sync_configurations: The selective syncs associated with a linked account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/filestorage/v1/selective-sync/configurations",
            body=maybe_transform(
                {"sync_configurations": sync_configurations},
                selective_sync_replace_configurations_params.SelectiveSyncReplaceConfigurationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SelectiveSyncReplaceConfigurationsResponse,
        )
