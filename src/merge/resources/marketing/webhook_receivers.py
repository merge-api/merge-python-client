# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...types import shared
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.marketing import (
    WebhookReceiverListResponse,
    webhook_receiver_create_params,
)

__all__ = ["WebhookReceivers", "AsyncWebhookReceivers"]


class WebhookReceivers(SyncAPIResource):
    def create(
        self,
        *,
        event: str,
        is_active: bool,
        key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.WebhookReceiver:
        """
        Creates a `WebhookReceiver` object with the given values.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/mktg/v1/webhook-receivers",
            body=maybe_transform(
                {
                    "event": event,
                    "is_active": is_active,
                    "key": key,
                },
                webhook_receiver_create_params.WebhookReceiverCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.WebhookReceiver,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> WebhookReceiverListResponse:
        """Returns a list of `WebhookReceiver` objects."""
        return self._get(
            "/mktg/v1/webhook-receivers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookReceiverListResponse,
        )


class AsyncWebhookReceivers(AsyncAPIResource):
    async def create(
        self,
        *,
        event: str,
        is_active: bool,
        key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.WebhookReceiver:
        """
        Creates a `WebhookReceiver` object with the given values.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/mktg/v1/webhook-receivers",
            body=maybe_transform(
                {
                    "event": event,
                    "is_active": is_active,
                    "key": key,
                },
                webhook_receiver_create_params.WebhookReceiverCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.WebhookReceiver,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> WebhookReceiverListResponse:
        """Returns a list of `WebhookReceiver` objects."""
        return await self._get(
            "/mktg/v1/webhook-receivers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebhookReceiverListResponse,
        )
