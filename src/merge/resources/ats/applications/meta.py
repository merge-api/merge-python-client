# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ....types import shared
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import make_request_options
from ....types.ats.applications import meta_for_create_params

__all__ = ["Meta", "AsyncMeta"]


class Meta(SyncAPIResource):
    def for_create(
        self,
        *,
        application_remote_template_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.MetaResponse:
        """
        Returns metadata for `Application` POSTs.

        Args:
          application_remote_template_id: The template ID associated with the nested application in the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/ats/v1/applications/meta/post",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"application_remote_template_id": application_remote_template_id},
                    meta_for_create_params.MetaForCreateParams,
                ),
            ),
            cast_to=shared.MetaResponse,
        )


class AsyncMeta(AsyncAPIResource):
    async def for_create(
        self,
        *,
        application_remote_template_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.MetaResponse:
        """
        Returns metadata for `Application` POSTs.

        Args:
          application_remote_template_id: The template ID associated with the nested application in the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/ats/v1/applications/meta/post",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"application_remote_template_id": application_remote_template_id},
                    meta_for_create_params.MetaForCreateParams,
                ),
            ),
            cast_to=shared.MetaResponse,
        )
