# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.ats import EEOC, eeoc_list_params, eeoc_retrieve_params
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["EEOCs", "AsyncEEOCs"]


class EEOCs(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        expand: Literal["candidate"] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "disability_status",
            "disability_status,gender",
            "disability_status,gender,race",
            "disability_status,gender,race,veteran_status",
            "disability_status,gender,veteran_status",
            "disability_status,race",
            "disability_status,race,veteran_status",
            "disability_status,veteran_status",
            "gender",
            "gender,race",
            "gender,race,veteran_status",
            "gender,veteran_status",
            "race",
            "race,veteran_status",
            "veteran_status",
        ]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "disability_status",
            "disability_status,gender",
            "disability_status,gender,race",
            "disability_status,gender,race,veteran_status",
            "disability_status,gender,veteran_status",
            "disability_status,race",
            "disability_status,race,veteran_status",
            "disability_status,veteran_status",
            "gender",
            "gender,race",
            "gender,race,veteran_status",
            "gender,veteran_status",
            "race",
            "race,veteran_status",
            "veteran_status",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> EEOC:
        """
        Returns an `EEOC` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          remote_fields: Deprecated. Use show_enum_origins.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/ats/v1/eeocs/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                    },
                    eeoc_retrieve_params.EEOCRetrieveParams,
                ),
            ),
            cast_to=EEOC,
        )

    def list(
        self,
        *,
        candidate_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: Literal["candidate"] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "disability_status",
            "disability_status,gender",
            "disability_status,gender,race",
            "disability_status,gender,race,veteran_status",
            "disability_status,gender,veteran_status",
            "disability_status,race",
            "disability_status,race,veteran_status",
            "disability_status,veteran_status",
            "gender",
            "gender,race",
            "gender,race,veteran_status",
            "gender,veteran_status",
            "race",
            "race,veteran_status",
            "veteran_status",
        ]
        | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "disability_status",
            "disability_status,gender",
            "disability_status,gender,race",
            "disability_status,gender,race,veteran_status",
            "disability_status,gender,veteran_status",
            "disability_status,race",
            "disability_status,race,veteran_status",
            "disability_status,veteran_status",
            "gender",
            "gender,race",
            "gender,race,veteran_status",
            "gender,veteran_status",
            "race",
            "race,veteran_status",
            "veteran_status",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[EEOC]:
        """
        Returns a list of `EEOC` objects.

        Args:
          candidate_id: If provided, will only return EEOC info for this candidate.

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

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ats/v1/eeocs",
            page=SyncPage[EEOC],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "candidate_id": candidate_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                    },
                    eeoc_list_params.EEOCListParams,
                ),
            ),
            model=EEOC,
        )


class AsyncEEOCs(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        expand: Literal["candidate"] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "disability_status",
            "disability_status,gender",
            "disability_status,gender,race",
            "disability_status,gender,race,veteran_status",
            "disability_status,gender,veteran_status",
            "disability_status,race",
            "disability_status,race,veteran_status",
            "disability_status,veteran_status",
            "gender",
            "gender,race",
            "gender,race,veteran_status",
            "gender,veteran_status",
            "race",
            "race,veteran_status",
            "veteran_status",
        ]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "disability_status",
            "disability_status,gender",
            "disability_status,gender,race",
            "disability_status,gender,race,veteran_status",
            "disability_status,gender,veteran_status",
            "disability_status,race",
            "disability_status,race,veteran_status",
            "disability_status,veteran_status",
            "gender",
            "gender,race",
            "gender,race,veteran_status",
            "gender,veteran_status",
            "race",
            "race,veteran_status",
            "veteran_status",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> EEOC:
        """
        Returns an `EEOC` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          remote_fields: Deprecated. Use show_enum_origins.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/ats/v1/eeocs/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                    },
                    eeoc_retrieve_params.EEOCRetrieveParams,
                ),
            ),
            cast_to=EEOC,
        )

    def list(
        self,
        *,
        candidate_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: Literal["candidate"] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "disability_status",
            "disability_status,gender",
            "disability_status,gender,race",
            "disability_status,gender,race,veteran_status",
            "disability_status,gender,veteran_status",
            "disability_status,race",
            "disability_status,race,veteran_status",
            "disability_status,veteran_status",
            "gender",
            "gender,race",
            "gender,race,veteran_status",
            "gender,veteran_status",
            "race",
            "race,veteran_status",
            "veteran_status",
        ]
        | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "disability_status",
            "disability_status,gender",
            "disability_status,gender,race",
            "disability_status,gender,race,veteran_status",
            "disability_status,gender,veteran_status",
            "disability_status,race",
            "disability_status,race,veteran_status",
            "disability_status,veteran_status",
            "gender",
            "gender,race",
            "gender,race,veteran_status",
            "gender,veteran_status",
            "race",
            "race,veteran_status",
            "veteran_status",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EEOC, AsyncPage[EEOC]]:
        """
        Returns a list of `EEOC` objects.

        Args:
          candidate_id: If provided, will only return EEOC info for this candidate.

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

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ats/v1/eeocs",
            page=AsyncPage[EEOC],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "candidate_id": candidate_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                    },
                    eeoc_list_params.EEOCListParams,
                ),
            ),
            model=EEOC,
        )
