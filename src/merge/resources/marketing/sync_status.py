# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import shared
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.marketing import SyncStatusResyncResponse, sync_status_list_params

__all__ = ["SyncStatus", "AsyncSyncStatus"]


class SyncStatus(SyncAPIResource):
    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[shared.SyncStatus]:
        """Get syncing status.

        Possible values: `DISABLED`, `DONE`, `FAILED`, `PAUSED`,
        `SYNCING`

        Args:
          cursor: The pagination cursor value.

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/mktg/v1/sync-status",
            page=SyncPage[shared.SyncStatus],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    sync_status_list_params.SyncStatusListParams,
                ),
            ),
            model=shared.SyncStatus,
        )

    def resync(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncStatusResyncResponse:
        """Force re-sync of all models.

        This is available for all organizations via the
        dashboard. Force re-sync is also available programmatically via API for monthly,
        quarterly, and highest sync frequency customers on the Core, Professional, or
        Enterprise plans. Doing so will consume a sync credit for the relevant linked
        account.
        """
        return self._post(
            "/mktg/v1/sync-status/resync",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyncStatusResyncResponse,
        )


class AsyncSyncStatus(AsyncAPIResource):
    def list(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[shared.SyncStatus, AsyncPage[shared.SyncStatus]]:
        """Get syncing status.

        Possible values: `DISABLED`, `DONE`, `FAILED`, `PAUSED`,
        `SYNCING`

        Args:
          cursor: The pagination cursor value.

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/mktg/v1/sync-status",
            page=AsyncPage[shared.SyncStatus],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                    },
                    sync_status_list_params.SyncStatusListParams,
                ),
            ),
            model=shared.SyncStatus,
        )

    async def resync(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncStatusResyncResponse:
        """Force re-sync of all models.

        This is available for all organizations via the
        dashboard. Force re-sync is also available programmatically via API for monthly,
        quarterly, and highest sync frequency customers on the Core, Professional, or
        Enterprise plans. Doing so will consume a sync credit for the relevant linked
        account.
        """
        return await self._post(
            "/mktg/v1/sync-status/resync",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyncStatusResyncResponse,
        )
