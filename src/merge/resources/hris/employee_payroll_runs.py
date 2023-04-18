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
    EmployeePayrollRun,
    employee_payroll_run_list_params,
    employee_payroll_run_retrieve_params,
)
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["EmployeePayrollRuns", "AsyncEmployeePayrollRuns"]


class EmployeePayrollRuns(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        expand: Literal["employee", "employee,payroll_run", "payroll_run"] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> EmployeePayrollRun:
        """
        Returns an `EmployeePayrollRun` object with the given `id`.

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
            f"/hris/v1/employee-payroll-runs/{id}",
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
                    employee_payroll_run_retrieve_params.EmployeePayrollRunRetrieveParams,
                ),
            ),
            cast_to=EmployeePayrollRun,
        )

    def list(
        self,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        ended_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        ended_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        expand: Literal["employee", "employee,payroll_run", "payroll_run"] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        payroll_run_id: str | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        started_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        started_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[EmployeePayrollRun]:
        """
        Returns a list of `EmployeePayrollRun` objects.

        Args:
          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          employee_id: If provided, will only return employee payroll runs for this employee.

          ended_after: If provided, will only return employee payroll runs ended after this datetime.

          ended_before: If provided, will only return employee payroll runs ended before this datetime.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          payroll_run_id: If provided, will only return employee payroll runs for this employee.

          remote_id: The API provider's ID for the given object.

          started_after: If provided, will only return employee payroll runs started after this datetime.

          started_before: If provided, will only return employee payroll runs started before this
              datetime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/employee-payroll-runs",
            page=SyncPage[EmployeePayrollRun],
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
                        "employee_id": employee_id,
                        "ended_after": ended_after,
                        "ended_before": ended_before,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "payroll_run_id": payroll_run_id,
                        "remote_id": remote_id,
                        "started_after": started_after,
                        "started_before": started_before,
                    },
                    employee_payroll_run_list_params.EmployeePayrollRunListParams,
                ),
            ),
            model=EmployeePayrollRun,
        )


class AsyncEmployeePayrollRuns(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        expand: Literal["employee", "employee,payroll_run", "payroll_run"] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> EmployeePayrollRun:
        """
        Returns an `EmployeePayrollRun` object with the given `id`.

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
            f"/hris/v1/employee-payroll-runs/{id}",
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
                    employee_payroll_run_retrieve_params.EmployeePayrollRunRetrieveParams,
                ),
            ),
            cast_to=EmployeePayrollRun,
        )

    def list(
        self,
        *,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        ended_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        ended_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        expand: Literal["employee", "employee,payroll_run", "payroll_run"] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        payroll_run_id: str | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        started_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        started_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EmployeePayrollRun, AsyncPage[EmployeePayrollRun]]:
        """
        Returns a list of `EmployeePayrollRun` objects.

        Args:
          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          employee_id: If provided, will only return employee payroll runs for this employee.

          ended_after: If provided, will only return employee payroll runs ended after this datetime.

          ended_before: If provided, will only return employee payroll runs ended before this datetime.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          payroll_run_id: If provided, will only return employee payroll runs for this employee.

          remote_id: The API provider's ID for the given object.

          started_after: If provided, will only return employee payroll runs started after this datetime.

          started_before: If provided, will only return employee payroll runs started before this
              datetime.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/employee-payroll-runs",
            page=AsyncPage[EmployeePayrollRun],
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
                        "employee_id": employee_id,
                        "ended_after": ended_after,
                        "ended_before": ended_before,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "payroll_run_id": payroll_run_id,
                        "remote_id": remote_id,
                        "started_after": started_after,
                        "started_before": started_before,
                    },
                    employee_payroll_run_list_params.EmployeePayrollRunListParams,
                ),
            ),
            model=EmployeePayrollRun,
        )
