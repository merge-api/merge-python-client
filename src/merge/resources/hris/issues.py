# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ...types import shared
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ...types.hris import issue_list_params
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["Issues", "AsyncIssues"]


class Issues(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.Issue:
        """Get a specific issue."""
        return self._get(
            f"/hris/v1/issues/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.Issue,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        end_user_organization_name: str | NotGiven = NOT_GIVEN,
        first_incident_time_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        first_incident_time_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        include_muted: str | NotGiven = NOT_GIVEN,
        integration_name: str | NotGiven = NOT_GIVEN,
        last_incident_time_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        last_incident_time_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        status: Literal["ONGOING", "RESOLVED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[shared.Issue]:
        """
        Gets issues.

        Args:
          cursor: The pagination cursor value.

          end_date: If included, will only include issues whose most recent action occurred before
              this time

          first_incident_time_after: If provided, will only return issues whose first incident time was after this
              datetime.

          first_incident_time_before: If provided, will only return issues whose first incident time was before this
              datetime.

          include_muted: If True, will include muted issues

          last_incident_time_after: If provided, will only return issues whose first incident time was after this
              datetime.

          last_incident_time_before: If provided, will only return issues whose first incident time was before this
              datetime.

          page_size: Number of results to return per page.

          start_date: If included, will only include issues whose most recent action occurred after
              this time

          status: - `ONGOING` - ONGOING
              - `RESOLVED` - RESOLVED

              - `ONGOING` - ONGOING
              - `RESOLVED` - RESOLVED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/issues",
            page=SyncPage[shared.Issue],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "cursor": cursor,
                        "end_date": end_date,
                        "end_user_organization_name": end_user_organization_name,
                        "first_incident_time_after": first_incident_time_after,
                        "first_incident_time_before": first_incident_time_before,
                        "include_muted": include_muted,
                        "integration_name": integration_name,
                        "last_incident_time_after": last_incident_time_after,
                        "last_incident_time_before": last_incident_time_before,
                        "page_size": page_size,
                        "start_date": start_date,
                        "status": status,
                    },
                    issue_list_params.IssueListParams,
                ),
            ),
            model=shared.Issue,
        )


class AsyncIssues(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.Issue:
        """Get a specific issue."""
        return await self._get(
            f"/hris/v1/issues/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.Issue,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        end_date: str | NotGiven = NOT_GIVEN,
        end_user_organization_name: str | NotGiven = NOT_GIVEN,
        first_incident_time_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        first_incident_time_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        include_muted: str | NotGiven = NOT_GIVEN,
        integration_name: str | NotGiven = NOT_GIVEN,
        last_incident_time_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        last_incident_time_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        start_date: str | NotGiven = NOT_GIVEN,
        status: Literal["ONGOING", "RESOLVED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[shared.Issue, AsyncPage[shared.Issue]]:
        """
        Gets issues.

        Args:
          cursor: The pagination cursor value.

          end_date: If included, will only include issues whose most recent action occurred before
              this time

          first_incident_time_after: If provided, will only return issues whose first incident time was after this
              datetime.

          first_incident_time_before: If provided, will only return issues whose first incident time was before this
              datetime.

          include_muted: If True, will include muted issues

          last_incident_time_after: If provided, will only return issues whose first incident time was after this
              datetime.

          last_incident_time_before: If provided, will only return issues whose first incident time was before this
              datetime.

          page_size: Number of results to return per page.

          start_date: If included, will only include issues whose most recent action occurred after
              this time

          status: - `ONGOING` - ONGOING
              - `RESOLVED` - RESOLVED

              - `ONGOING` - ONGOING
              - `RESOLVED` - RESOLVED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/issues",
            page=AsyncPage[shared.Issue],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "cursor": cursor,
                        "end_date": end_date,
                        "end_user_organization_name": end_user_organization_name,
                        "first_incident_time_after": first_incident_time_after,
                        "first_incident_time_before": first_incident_time_before,
                        "include_muted": include_muted,
                        "integration_name": integration_name,
                        "last_incident_time_after": last_incident_time_after,
                        "last_incident_time_before": last_incident_time_before,
                        "page_size": page_size,
                        "start_date": start_date,
                        "status": status,
                    },
                    issue_list_params.IssueListParams,
                ),
            ),
            model=shared.Issue,
        )
