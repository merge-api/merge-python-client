# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .meta import Meta, AsyncMeta
from ....types import shared
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types.ats import (
    Candidate,
    CandidateResponse,
    candidate_list_params,
    candidate_create_params,
    candidate_retrieve_params,
    candidate_ignore_row_params,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ...._client import Merge, AsyncMerge

__all__ = ["Candidates", "AsyncCandidates"]


class Candidates(SyncAPIResource):
    meta: Meta

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.meta = Meta(client)

    def create(
        self,
        *,
        model: candidate_create_params.Model,
        remote_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CandidateResponse:
        """
        Creates a `Candidate` object with the given values.

        Args:
          model: # The Candidate Object

              ### Description

              The `Candidate` object is used to represent profile information about a given
              Candidate. Because it is specific to a Candidate, this information stays
              constant across applications.

              ### Usage Example

              Fetch from the `LIST Candidates` endpoint and filter by `ID` to show all
              candidates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ats/v1/candidates",
            body=maybe_transform(
                {
                    "model": model,
                    "remote_user_id": remote_user_id,
                },
                candidate_create_params.CandidateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CandidateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["applications", "attachments"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Candidate:
        """
        Returns a `Candidate` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/ats/v1/candidates/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                    },
                    candidate_retrieve_params.CandidateRetrieveParams,
                ),
            ),
            cast_to=Candidate,
        )

    def list(
        self,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        email_addresses: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["applications", "attachments"]] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Candidate]:
        """
        Returns a list of `Candidate` objects.

        Args:
          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          email_addresses: If provided, will only return candidates with these email addresses; multiple
              addresses can be separated by commas.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          first_name: If provided, will only return candidates with this first name.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          last_name: If provided, will only return candidates with this last name.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          remote_id: The API provider's ID for the given object.

          tags: If provided, will only return candidates with these tags; multiple tags can be
              separated by commas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ats/v1/candidates",
            page=SyncPage[Candidate],
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
                        "email_addresses": email_addresses,
                        "expand": expand,
                        "first_name": first_name,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "last_name": last_name,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_id": remote_id,
                        "tags": tags,
                    },
                    candidate_list_params.CandidateListParams,
                ),
            ),
            model=Candidate,
        )

    def ignore_row(
        self,
        model_id: str,
        *,
        reason: Literal["GENERAL_CUSTOMER_REQUEST", "GDPR", "OTHER"],
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.IgnoreCommonModel:
        """Ignores a specific row based on the `model_id` in the url.

        These records will
        have their properties set to null, and will not be updated in future syncs. The
        "reason" and "message" fields in the request body will be stored for audit
        purposes.

        Args:
          reason: - `GENERAL_CUSTOMER_REQUEST` - GENERAL_CUSTOMER_REQUEST
              - `GDPR` - GDPR
              - `OTHER` - OTHER

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/ats/v1/candidates/ignore/{model_id}",
            body=maybe_transform(
                {
                    "reason": reason,
                    "message": message,
                },
                candidate_ignore_row_params.CandidateIgnoreRowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.IgnoreCommonModel,
        )


class AsyncCandidates(AsyncAPIResource):
    meta: AsyncMeta

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.meta = AsyncMeta(client)

    async def create(
        self,
        *,
        model: candidate_create_params.Model,
        remote_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CandidateResponse:
        """
        Creates a `Candidate` object with the given values.

        Args:
          model: # The Candidate Object

              ### Description

              The `Candidate` object is used to represent profile information about a given
              Candidate. Because it is specific to a Candidate, this information stays
              constant across applications.

              ### Usage Example

              Fetch from the `LIST Candidates` endpoint and filter by `ID` to show all
              candidates.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ats/v1/candidates",
            body=maybe_transform(
                {
                    "model": model,
                    "remote_user_id": remote_user_id,
                },
                candidate_create_params.CandidateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CandidateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["applications", "attachments"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Candidate:
        """
        Returns a `Candidate` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/ats/v1/candidates/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                    },
                    candidate_retrieve_params.CandidateRetrieveParams,
                ),
            ),
            cast_to=Candidate,
        )

    def list(
        self,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        email_addresses: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["applications", "attachments"]] | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Candidate, AsyncPage[Candidate]]:
        """
        Returns a list of `Candidate` objects.

        Args:
          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          email_addresses: If provided, will only return candidates with these email addresses; multiple
              addresses can be separated by commas.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          first_name: If provided, will only return candidates with this first name.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          last_name: If provided, will only return candidates with this last name.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          remote_id: The API provider's ID for the given object.

          tags: If provided, will only return candidates with these tags; multiple tags can be
              separated by commas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ats/v1/candidates",
            page=AsyncPage[Candidate],
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
                        "email_addresses": email_addresses,
                        "expand": expand,
                        "first_name": first_name,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "last_name": last_name,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_id": remote_id,
                        "tags": tags,
                    },
                    candidate_list_params.CandidateListParams,
                ),
            ),
            model=Candidate,
        )

    async def ignore_row(
        self,
        model_id: str,
        *,
        reason: Literal["GENERAL_CUSTOMER_REQUEST", "GDPR", "OTHER"],
        message: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.IgnoreCommonModel:
        """Ignores a specific row based on the `model_id` in the url.

        These records will
        have their properties set to null, and will not be updated in future syncs. The
        "reason" and "message" fields in the request body will be stored for audit
        purposes.

        Args:
          reason: - `GENERAL_CUSTOMER_REQUEST` - GENERAL_CUSTOMER_REQUEST
              - `GDPR` - GDPR
              - `OTHER` - OTHER

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/ats/v1/candidates/ignore/{model_id}",
            body=maybe_transform(
                {
                    "reason": reason,
                    "message": message,
                },
                candidate_ignore_row_params.CandidateIgnoreRowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.IgnoreCommonModel,
        )
