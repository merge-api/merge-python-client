# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types.crm import CustomObjectClass
from ...._base_client import make_request_options

__all__ = ["Generators", "AsyncGenerators"]


class Generators(SyncAPIResource):
    def update(
        self,
        generator_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CustomObjectClass:
        """Updates a `CustomObjectClass` object with the given `id`."""
        return self._put(
            f"/crm/v1/custom-object-classes/generator/{generator_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomObjectClass,
        )


class AsyncGenerators(AsyncAPIResource):
    async def update(
        self,
        generator_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CustomObjectClass:
        """Updates a `CustomObjectClass` object with the given `id`."""
        return await self._put(
            f"/crm/v1/custom-object-classes/generator/{generator_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomObjectClass,
        )
