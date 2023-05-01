# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ...types import shared
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.crm import passthrough_request_send_params
from ..._base_client import make_request_options

__all__ = ["PassthroughRequests", "AsyncPassthroughRequests"]


class PassthroughRequests(SyncAPIResource):
    def send(
        self,
        *,
        method: Literal["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"],
        path: str,
        base_url_override: Optional[str] | NotGiven = NOT_GIVEN,
        data: Optional[str] | NotGiven = NOT_GIVEN,
        headers: Optional[object] | NotGiven = NOT_GIVEN,
        multipart_form_data: List[passthrough_request_send_params.Multipartformdata] | NotGiven = NOT_GIVEN,
        normalize_response: bool | NotGiven = NOT_GIVEN,
        request_format: Literal["JSON", "XML", "MULTIPART"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.RemoteResponse:
        """
        Pull data from an endpoint not currently supported by Merge.

        Args:
          method: - `GET` - GET
              - `OPTIONS` - OPTIONS
              - `HEAD` - HEAD
              - `POST` - POST
              - `PUT` - PUT
              - `PATCH` - PATCH
              - `DELETE` - DELETE

          headers: The headers to use for the request (Merge will handle the account's
              authorization headers). `Content-Type` header is required for passthrough.
              Choose content type corresponding to expected format of receiving server.

          multipart_form_data: Pass an array of `MultipartFormField` objects in here instead of using the
              `data` param if `request_format` is set to `MULTIPART`.

          normalize_response: Optional. If true, the response will always be an object of the form
              `{"type": T, "value": ...}` where `T` will be one of
              `string, boolean, number, null, array, object`.

          request_format: - `JSON` - JSON
              - `XML` - XML
              - `MULTIPART` - MULTIPART

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v1/passthrough",
            body=maybe_transform(
                {
                    "method": method,
                    "path": path,
                    "base_url_override": base_url_override,
                    "data": data,
                    "multipart_form_data": multipart_form_data,
                    "headers": headers,
                    "request_format": request_format,
                    "normalize_response": normalize_response,
                },
                passthrough_request_send_params.PassthroughRequestSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.RemoteResponse,
        )


class AsyncPassthroughRequests(AsyncAPIResource):
    async def send(
        self,
        *,
        method: Literal["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"],
        path: str,
        base_url_override: Optional[str] | NotGiven = NOT_GIVEN,
        data: Optional[str] | NotGiven = NOT_GIVEN,
        headers: Optional[object] | NotGiven = NOT_GIVEN,
        multipart_form_data: List[passthrough_request_send_params.Multipartformdata] | NotGiven = NOT_GIVEN,
        normalize_response: bool | NotGiven = NOT_GIVEN,
        request_format: Literal["JSON", "XML", "MULTIPART"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.RemoteResponse:
        """
        Pull data from an endpoint not currently supported by Merge.

        Args:
          method: - `GET` - GET
              - `OPTIONS` - OPTIONS
              - `HEAD` - HEAD
              - `POST` - POST
              - `PUT` - PUT
              - `PATCH` - PATCH
              - `DELETE` - DELETE

          headers: The headers to use for the request (Merge will handle the account's
              authorization headers). `Content-Type` header is required for passthrough.
              Choose content type corresponding to expected format of receiving server.

          multipart_form_data: Pass an array of `MultipartFormField` objects in here instead of using the
              `data` param if `request_format` is set to `MULTIPART`.

          normalize_response: Optional. If true, the response will always be an object of the form
              `{"type": T, "value": ...}` where `T` will be one of
              `string, boolean, number, null, array, object`.

          request_format: - `JSON` - JSON
              - `XML` - XML
              - `MULTIPART` - MULTIPART

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v1/passthrough",
            body=maybe_transform(
                {
                    "method": method,
                    "path": path,
                    "base_url_override": base_url_override,
                    "data": data,
                    "multipart_form_data": multipart_form_data,
                    "headers": headers,
                    "request_format": request_format,
                    "normalize_response": normalize_response,
                },
                passthrough_request_send_params.PassthroughRequestSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.RemoteResponse,
        )
