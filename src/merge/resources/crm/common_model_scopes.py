# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

from ...types import shared
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.crm import (
    common_model_scope_update_params,
    common_model_scope_retrieve_params,
)
from ..._base_client import make_request_options

__all__ = ["CommonModelScopes", "AsyncCommonModelScopes"]


class CommonModelScopes(SyncAPIResource):
    def retrieve(
        self,
        *,
        linked_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.CommonModelScope:
        """Fetch the configuration of what data is saved by Merge when syncing.

        Common
        model scopes are set as a default across all linked accounts, but can be updated
        to have greater granularity per account.

        Args:
          linked_account_id: ID of specific linked account to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm/v1/common-model-scopes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"linked_account_id": linked_account_id},
                    common_model_scope_retrieve_params.CommonModelScopeRetrieveParams,
                ),
            ),
            cast_to=shared.CommonModelScope,
        )

    def update(
        self,
        *,
        common_models: List[common_model_scope_update_params.CommonModel],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.CommonModelScope:
        """Update the configuration of what data is saved by Merge when syncing.

        Common
        model scopes are set as a default across all linked accounts, but can be updated
        to have greater granularity per account.

        Args:
          common_models: The common model scopes to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v1/common-model-scopes",
            body=maybe_transform(
                {"common_models": common_models}, common_model_scope_update_params.CommonModelScopeUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.CommonModelScope,
        )


class AsyncCommonModelScopes(AsyncAPIResource):
    async def retrieve(
        self,
        *,
        linked_account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.CommonModelScope:
        """Fetch the configuration of what data is saved by Merge when syncing.

        Common
        model scopes are set as a default across all linked accounts, but can be updated
        to have greater granularity per account.

        Args:
          linked_account_id: ID of specific linked account to fetch

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm/v1/common-model-scopes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"linked_account_id": linked_account_id},
                    common_model_scope_retrieve_params.CommonModelScopeRetrieveParams,
                ),
            ),
            cast_to=shared.CommonModelScope,
        )

    async def update(
        self,
        *,
        common_models: List[common_model_scope_update_params.CommonModel],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.CommonModelScope:
        """Update the configuration of what data is saved by Merge when syncing.

        Common
        model scopes are set as a default across all linked accounts, but can be updated
        to have greater granularity per account.

        Args:
          common_models: The common model scopes to update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v1/common-model-scopes",
            body=maybe_transform(
                {"common_models": common_models}, common_model_scope_update_params.CommonModelScopeUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.CommonModelScope,
        )
