# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .meta import Meta, AsyncMeta
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.accounting import (
    JournalEntry,
    JournalEntryResponse,
    journal_entry_list_params,
    journal_entry_create_params,
    journal_entry_retrieve_params,
)

if TYPE_CHECKING:
    from ...._client import Merge, AsyncMerge

__all__ = ["JournalEntries", "AsyncJournalEntries"]


class JournalEntries(SyncAPIResource):
    meta: Meta

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.meta = Meta(client)

    def create(
        self,
        *,
        model: journal_entry_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> JournalEntryResponse:
        """
        Creates a `JournalEntry` object with the given values.

        Args:
          model: # The JournalEntry Object

              ### Description

              The `JournalEntry` object is used to get a record of all manually created
              entries made in a company’s general ledger. The journal line items for each
              journal entry should sum to zero.

              ### Usage Example

              Fetch from the `GET JournalEntry` endpoint and view a company's journey entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/accounting/v1/journal-entries",
            body=maybe_transform({"model": model}, journal_entry_create_params.JournalEntryCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JournalEntryResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["company", "lines", "payments"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> JournalEntry:
        """
        Returns a `JournalEntry` object with the given `id`.

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
            f"/accounting/v1/journal-entries/{id}",
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
                    journal_entry_retrieve_params.JournalEntryRetrieveParams,
                ),
            ),
            cast_to=JournalEntry,
        )

    def list(
        self,
        *,
        company_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["company", "lines", "payments"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        transaction_date_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        transaction_date_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[JournalEntry]:
        """
        Returns a list of `JournalEntry` objects.

        Args:
          company_id: If provided, will only return journal entries for this company.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          remote_id: The API provider's ID for the given object.

          transaction_date_after: If provided, will only return objects created after this datetime.

          transaction_date_before: If provided, will only return objects created before this datetime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounting/v1/journal-entries",
            page=SyncPage[JournalEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_id": remote_id,
                        "transaction_date_after": transaction_date_after,
                        "transaction_date_before": transaction_date_before,
                    },
                    journal_entry_list_params.JournalEntryListParams,
                ),
            ),
            model=JournalEntry,
        )


class AsyncJournalEntries(AsyncAPIResource):
    meta: AsyncMeta

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.meta = AsyncMeta(client)

    async def create(
        self,
        *,
        model: journal_entry_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> JournalEntryResponse:
        """
        Creates a `JournalEntry` object with the given values.

        Args:
          model: # The JournalEntry Object

              ### Description

              The `JournalEntry` object is used to get a record of all manually created
              entries made in a company’s general ledger. The journal line items for each
              journal entry should sum to zero.

              ### Usage Example

              Fetch from the `GET JournalEntry` endpoint and view a company's journey entry.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/accounting/v1/journal-entries",
            body=maybe_transform({"model": model}, journal_entry_create_params.JournalEntryCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JournalEntryResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["company", "lines", "payments"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> JournalEntry:
        """
        Returns a `JournalEntry` object with the given `id`.

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
            f"/accounting/v1/journal-entries/{id}",
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
                    journal_entry_retrieve_params.JournalEntryRetrieveParams,
                ),
            ),
            cast_to=JournalEntry,
        )

    def list(
        self,
        *,
        company_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["company", "lines", "payments"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        transaction_date_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        transaction_date_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[JournalEntry, AsyncPage[JournalEntry]]:
        """
        Returns a list of `JournalEntry` objects.

        Args:
          company_id: If provided, will only return journal entries for this company.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          remote_id: The API provider's ID for the given object.

          transaction_date_after: If provided, will only return objects created after this datetime.

          transaction_date_before: If provided, will only return objects created before this datetime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounting/v1/journal-entries",
            page=AsyncPage[JournalEntry],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "company_id": company_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_id": remote_id,
                        "transaction_date_after": transaction_date_after,
                        "transaction_date_before": transaction_date_before,
                    },
                    journal_entry_list_params.JournalEntryListParams,
                ),
            ),
            model=JournalEntry,
        )
