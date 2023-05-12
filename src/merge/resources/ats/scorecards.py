# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.ats import Scorecard, scorecard_list_params, scorecard_retrieve_params
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["Scorecards", "AsyncScorecards"]


class Scorecards(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["application", "interview", "interviewer"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal["overall_recommendation"] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["overall_recommendation"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Scorecard:
        """
        Returns a `Scorecard` object with the given `id`.

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
            f"/ats/v1/scorecards/{id}",
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
                    scorecard_retrieve_params.ScorecardRetrieveParams,
                ),
            ),
            cast_to=Scorecard,
        )

    def list(
        self,
        *,
        application_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["application", "interview", "interviewer"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        interview_id: str | NotGiven = NOT_GIVEN,
        interviewer_id: str | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal["overall_recommendation"] | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["overall_recommendation"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Scorecard]:
        """
        Returns a list of `Scorecard` objects.

        Args:
          application_id: If provided, will only return scorecards for this application.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          interview_id: If provided, will only return scorecards for this interview.

          interviewer_id: If provided, will only return scorecards for this interviewer.

          modified_after: If provided, only objects synced by Merge after this date time will be returned.

          modified_before: If provided, only objects synced by Merge before this date time will be
              returned.

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
            "/ats/v1/scorecards",
            page=SyncPage[Scorecard],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "application_id": application_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "interview_id": interview_id,
                        "interviewer_id": interviewer_id,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                    },
                    scorecard_list_params.ScorecardListParams,
                ),
            ),
            model=Scorecard,
        )


class AsyncScorecards(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["application", "interview", "interviewer"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal["overall_recommendation"] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["overall_recommendation"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Scorecard:
        """
        Returns a `Scorecard` object with the given `id`.

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
            f"/ats/v1/scorecards/{id}",
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
                    scorecard_retrieve_params.ScorecardRetrieveParams,
                ),
            ),
            cast_to=Scorecard,
        )

    def list(
        self,
        *,
        application_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["application", "interview", "interviewer"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        interview_id: str | NotGiven = NOT_GIVEN,
        interviewer_id: str | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal["overall_recommendation"] | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["overall_recommendation"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Scorecard, AsyncPage[Scorecard]]:
        """
        Returns a list of `Scorecard` objects.

        Args:
          application_id: If provided, will only return scorecards for this application.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          interview_id: If provided, will only return scorecards for this interview.

          interviewer_id: If provided, will only return scorecards for this interviewer.

          modified_after: If provided, only objects synced by Merge after this date time will be returned.

          modified_before: If provided, only objects synced by Merge before this date time will be
              returned.

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
            "/ats/v1/scorecards",
            page=AsyncPage[Scorecard],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "application_id": application_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "interview_id": interview_id,
                        "interviewer_id": interviewer_id,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                    },
                    scorecard_list_params.ScorecardListParams,
                ),
            ),
            model=Scorecard,
        )
