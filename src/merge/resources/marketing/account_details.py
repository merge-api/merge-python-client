# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import shared
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options

__all__ = ["AccountDetails", "AsyncAccountDetails"]


class AccountDetails(SyncAPIResource):
    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.AccountDetail:
        """Get details for a linked account."""
        return self._get(
            "/mktg/v1/account-details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.AccountDetail,
        )


class AsyncAccountDetails(AsyncAPIResource):
    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.AccountDetail:
        """Get details for a linked account."""
        return await self._get(
            "/mktg/v1/account-details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.AccountDetail,
        )
