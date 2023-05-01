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
    Application,
    ApplicationResponse,
    application_list_params,
    application_create_params,
    application_retrieve_params,
    application_change_stage_params,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ...._client import Merge, AsyncMerge

__all__ = ["Applications", "AsyncApplications"]


class Applications(SyncAPIResource):
    meta: Meta

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.meta = Meta(client)

    def create(
        self,
        *,
        model: application_create_params.Model,
        remote_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationResponse:
        """
        Creates an `Application` object with the given values.

        Args:
          model: # The Application Object

              ### Description

              The Application Object is used to represent a candidate's journey through a
              particular Job's recruiting process. If a Candidate applies for multiple Jobs,
              there will be a separate Application for each Job if the third-party integration
              allows it.

              ### Usage Example

              Fetch from the `LIST Applications` endpoint and filter by `ID` to show all
              applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ats/v1/applications",
            body=maybe_transform(
                {
                    "model": model,
                    "remote_user_id": remote_user_id,
                },
                application_create_params.ApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["candidate", "credited_to", "current_stage", "job", "reject_reason"]]
        | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Application:
        """
        Returns an `Application` object with the given `id`.

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
            f"/ats/v1/applications/{id}",
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
                    application_retrieve_params.ApplicationRetrieveParams,
                ),
            ),
            cast_to=Application,
        )

    def list(
        self,
        *,
        candidate_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        credited_to_id: str | NotGiven = NOT_GIVEN,
        current_stage_id: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["candidate", "credited_to", "current_stage", "job", "reject_reason"]]
        | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        job_id: str | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        reject_reason_id: str | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        source: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Application]:
        """
        Returns a list of `Application` objects.

        Args:
          candidate_id: If provided, will only return applications for this candidate.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          credited_to_id: If provided, will only return applications credited to this user.

          current_stage_id: If provided, will only return applications at this interview stage.

          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          job_id: If provided, will only return applications for this job.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          reject_reason_id: If provided, will only return applications with this reject reason.

          remote_id: The API provider's ID for the given object.

          source: If provided, will only return applications with this source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ats/v1/applications",
            page=SyncPage[Application],
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
                        "credited_to_id": credited_to_id,
                        "current_stage_id": current_stage_id,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "job_id": job_id,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "reject_reason_id": reject_reason_id,
                        "remote_id": remote_id,
                        "source": source,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=Application,
        )

    def change_stage(
        self,
        id: str,
        *,
        job_interview_stage: Optional[str] | NotGiven = NOT_GIVEN,
        remote_user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationResponse:
        """
        Updates the `current_stage` field of an `Application` object

        Args:
          job_interview_stage: The interview stage to move the application to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/ats/v1/applications/{id}/change-stage",
            body=maybe_transform(
                {
                    "job_interview_stage": job_interview_stage,
                    "remote_user_id": remote_user_id,
                },
                application_change_stage_params.ApplicationChangeStageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationResponse,
        )


class AsyncApplications(AsyncAPIResource):
    meta: AsyncMeta

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.meta = AsyncMeta(client)

    async def create(
        self,
        *,
        model: application_create_params.Model,
        remote_user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationResponse:
        """
        Creates an `Application` object with the given values.

        Args:
          model: # The Application Object

              ### Description

              The Application Object is used to represent a candidate's journey through a
              particular Job's recruiting process. If a Candidate applies for multiple Jobs,
              there will be a separate Application for each Job if the third-party integration
              allows it.

              ### Usage Example

              Fetch from the `LIST Applications` endpoint and filter by `ID` to show all
              applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ats/v1/applications",
            body=maybe_transform(
                {
                    "model": model,
                    "remote_user_id": remote_user_id,
                },
                application_create_params.ApplicationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["candidate", "credited_to", "current_stage", "job", "reject_reason"]]
        | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Application:
        """
        Returns an `Application` object with the given `id`.

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
            f"/ats/v1/applications/{id}",
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
                    application_retrieve_params.ApplicationRetrieveParams,
                ),
            ),
            cast_to=Application,
        )

    def list(
        self,
        *,
        candidate_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        credited_to_id: str | NotGiven = NOT_GIVEN,
        current_stage_id: str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["candidate", "credited_to", "current_stage", "job", "reject_reason"]]
        | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        job_id: str | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        reject_reason_id: str | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        source: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Application, AsyncPage[Application]]:
        """
        Returns a list of `Application` objects.

        Args:
          candidate_id: If provided, will only return applications for this candidate.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          credited_to_id: If provided, will only return applications credited to this user.

          current_stage_id: If provided, will only return applications at this interview stage.

          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          job_id: If provided, will only return applications for this job.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          reject_reason_id: If provided, will only return applications with this reject reason.

          remote_id: The API provider's ID for the given object.

          source: If provided, will only return applications with this source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ats/v1/applications",
            page=AsyncPage[Application],
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
                        "credited_to_id": credited_to_id,
                        "current_stage_id": current_stage_id,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "job_id": job_id,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "reject_reason_id": reject_reason_id,
                        "remote_id": remote_id,
                        "source": source,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=Application,
        )

    async def change_stage(
        self,
        id: str,
        *,
        job_interview_stage: Optional[str] | NotGiven = NOT_GIVEN,
        remote_user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationResponse:
        """
        Updates the `current_stage` field of an `Application` object

        Args:
          job_interview_stage: The interview stage to move the application to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/ats/v1/applications/{id}/change-stage",
            body=maybe_transform(
                {
                    "job_interview_stage": job_interview_stage,
                    "remote_user_id": remote_user_id,
                },
                application_change_stage_params.ApplicationChangeStageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationResponse,
        )
