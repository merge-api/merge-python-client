# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ...types.hris import (
    PayrollRun,
    payroll_run_list_params,
    payroll_run_retrieve_params,
)
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["PayrollRuns", "AsyncPayrollRuns"]


class PayrollRuns(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal["run_state", "run_state,run_type", "run_type"] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["run_state", "run_state,run_type", "run_type"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PayrollRun:
        """
        Returns a `PayrollRun` object with the given `id`.

        Args:
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
            f"/hris/v1/payroll-runs/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_remote_data": include_remote_data,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                    },
                    payroll_run_retrieve_params.PayrollRunRetrieveParams,
                ),
            ),
            cast_to=PayrollRun,
        )

    def list(
        self,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        ended_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        ended_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal["run_state", "run_state,run_type", "run_type"] | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        run_type: Optional[Literal["CORRECTION", "OFF_CYCLE", "REGULAR", "SIGN_ON_BONUS", "TERMINATION"]]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["run_state", "run_state,run_type", "run_type"] | NotGiven = NOT_GIVEN,
        started_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        started_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[PayrollRun]:
        """
        Returns a list of `PayrollRun` objects.

        Args:
          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          ended_after: If provided, will only return payroll runs ended after this datetime.

          ended_before: If provided, will only return payroll runs ended before this datetime.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          run_type:
              If provided, will only return PayrollRun's with this status. Options:
              ('REGULAR', 'OFF_CYCLE', 'CORRECTION', 'TERMINATION', 'SIGN_ON_BONUS')

              - `REGULAR` - REGULAR
              - `OFF_CYCLE` - OFF_CYCLE
              - `CORRECTION` - CORRECTION
              - `TERMINATION` - TERMINATION
              - `SIGN_ON_BONUS` - SIGN_ON_BONUS

          show_enum_origins: Which fields should be returned in non-normalized form.

          started_after: If provided, will only return payroll runs started after this datetime.

          started_before: If provided, will only return payroll runs started before this datetime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/payroll-runs",
            page=SyncPage[PayrollRun],
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
                        "ended_after": ended_after,
                        "ended_before": ended_before,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "run_type": run_type,
                        "show_enum_origins": show_enum_origins,
                        "started_after": started_after,
                        "started_before": started_before,
                    },
                    payroll_run_list_params.PayrollRunListParams,
                ),
            ),
            model=PayrollRun,
        )


class AsyncPayrollRuns(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal["run_state", "run_state,run_type", "run_type"] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["run_state", "run_state,run_type", "run_type"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> PayrollRun:
        """
        Returns a `PayrollRun` object with the given `id`.

        Args:
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
            f"/hris/v1/payroll-runs/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_remote_data": include_remote_data,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                    },
                    payroll_run_retrieve_params.PayrollRunRetrieveParams,
                ),
            ),
            cast_to=PayrollRun,
        )

    def list(
        self,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        ended_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        ended_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal["run_state", "run_state,run_type", "run_type"] | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        run_type: Optional[Literal["CORRECTION", "OFF_CYCLE", "REGULAR", "SIGN_ON_BONUS", "TERMINATION"]]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["run_state", "run_state,run_type", "run_type"] | NotGiven = NOT_GIVEN,
        started_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        started_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PayrollRun, AsyncPage[PayrollRun]]:
        """
        Returns a list of `PayrollRun` objects.

        Args:
          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          ended_after: If provided, will only return payroll runs ended after this datetime.

          ended_before: If provided, will only return payroll runs ended before this datetime.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          run_type:
              If provided, will only return PayrollRun's with this status. Options:
              ('REGULAR', 'OFF_CYCLE', 'CORRECTION', 'TERMINATION', 'SIGN_ON_BONUS')

              - `REGULAR` - REGULAR
              - `OFF_CYCLE` - OFF_CYCLE
              - `CORRECTION` - CORRECTION
              - `TERMINATION` - TERMINATION
              - `SIGN_ON_BONUS` - SIGN_ON_BONUS

          show_enum_origins: Which fields should be returned in non-normalized form.

          started_after: If provided, will only return payroll runs started after this datetime.

          started_before: If provided, will only return payroll runs started before this datetime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/payroll-runs",
            page=AsyncPage[PayrollRun],
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
                        "ended_after": ended_after,
                        "ended_before": ended_before,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "run_type": run_type,
                        "show_enum_origins": show_enum_origins,
                        "started_after": started_after,
                        "started_before": started_before,
                    },
                    payroll_run_list_params.PayrollRunListParams,
                ),
            ),
            model=PayrollRun,
        )
