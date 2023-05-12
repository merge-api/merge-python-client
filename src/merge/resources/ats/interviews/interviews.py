# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .meta import Meta, AsyncMeta
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types.ats import (
    ScheduledInterview,
    ScheduledInterviewResponse,
    interview_list_params,
    interview_create_params,
    interview_retrieve_params,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ...._client import Merge, AsyncMerge

__all__ = ["Interviews", "AsyncInterviews"]


class Interviews(SyncAPIResource):
    meta: Meta

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.meta = Meta(client)

    def create(
        self,
        *,
        model: interview_create_params.Model,
        remote_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledInterviewResponse:
        """
        Creates a `ScheduledInterview` object with the given values.

        Args:
          model: # The ScheduledInterview Object

              ### Description

              The `ScheduledInterview` object is used to represent a scheduled interview for a
              given candidate’s application to a job. An `Application` can have multiple
              `ScheduledInterview`s depending on the particular hiring process.

              ### Usage Example

              Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers`
              to show all office locations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ats/v1/interviews",
            body=maybe_transform(
                {
                    "model": model,
                    "remote_user_id": remote_user_id,
                },
                interview_create_params.InterviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledInterviewResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["application", "interviewers", "job_interview_stage", "organizer"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal["status"] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["status"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledInterview:
        """
        Returns a `ScheduledInterview` object with the given `id`.

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
            f"/ats/v1/interviews/{id}",
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
                    interview_retrieve_params.InterviewRetrieveParams,
                ),
            ),
            cast_to=ScheduledInterview,
        )

    def list(
        self,
        *,
        application_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["application", "interviewers", "job_interview_stage", "organizer"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        job_interview_stage_id: str | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        organizer_id: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal["status"] | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["status"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[ScheduledInterview]:
        """
        Returns a list of `ScheduledInterview` objects.

        Args:
          application_id: If provided, will only return interviews for this application.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          job_interview_stage_id: If provided, will only return interviews at this stage.

          modified_after: If provided, only objects synced by Merge after this date time will be returned.

          modified_before: If provided, only objects synced by Merge before this date time will be
              returned.

          organizer_id: If provided, will only return interviews organized by this user.

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
            "/ats/v1/interviews",
            page=SyncPage[ScheduledInterview],
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
                        "job_interview_stage_id": job_interview_stage_id,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "organizer_id": organizer_id,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                    },
                    interview_list_params.InterviewListParams,
                ),
            ),
            model=ScheduledInterview,
        )


class AsyncInterviews(AsyncAPIResource):
    meta: AsyncMeta

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.meta = AsyncMeta(client)

    async def create(
        self,
        *,
        model: interview_create_params.Model,
        remote_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledInterviewResponse:
        """
        Creates a `ScheduledInterview` object with the given values.

        Args:
          model: # The ScheduledInterview Object

              ### Description

              The `ScheduledInterview` object is used to represent a scheduled interview for a
              given candidate’s application to a job. An `Application` can have multiple
              `ScheduledInterview`s depending on the particular hiring process.

              ### Usage Example

              Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers`
              to show all office locations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ats/v1/interviews",
            body=maybe_transform(
                {
                    "model": model,
                    "remote_user_id": remote_user_id,
                },
                interview_create_params.InterviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledInterviewResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["application", "interviewers", "job_interview_stage", "organizer"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal["status"] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["status"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledInterview:
        """
        Returns a `ScheduledInterview` object with the given `id`.

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
            f"/ats/v1/interviews/{id}",
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
                    interview_retrieve_params.InterviewRetrieveParams,
                ),
            ),
            cast_to=ScheduledInterview,
        )

    def list(
        self,
        *,
        application_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["application", "interviewers", "job_interview_stage", "organizer"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        job_interview_stage_id: str | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        organizer_id: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal["status"] | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["status"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ScheduledInterview, AsyncPage[ScheduledInterview]]:
        """
        Returns a list of `ScheduledInterview` objects.

        Args:
          application_id: If provided, will only return interviews for this application.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          job_interview_stage_id: If provided, will only return interviews at this stage.

          modified_after: If provided, only objects synced by Merge after this date time will be returned.

          modified_before: If provided, only objects synced by Merge before this date time will be
              returned.

          organizer_id: If provided, will only return interviews organized by this user.

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
            "/ats/v1/interviews",
            page=AsyncPage[ScheduledInterview],
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
                        "job_interview_stage_id": job_interview_stage_id,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "organizer_id": organizer_id,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                    },
                    interview_list_params.InterviewListParams,
                ),
            ),
            model=ScheduledInterview,
        )
