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
from ....pagination import SyncPage, AsyncPage
from ....types.hris import (
    Employee,
    CreatedEmployeeResponse,
    employee_list_params,
    employee_create_params,
    employee_ignore_params,
    employee_retrieve_params,
)
from ...._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ...._client import Merge, AsyncMerge

__all__ = ["Employees", "AsyncEmployees"]


class Employees(SyncAPIResource):
    meta: Meta

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.meta = Meta(client)

    def create(
        self,
        *,
        model: employee_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CreatedEmployeeResponse:
        """
        Creates an `Employee` object with the given values.

        Args:
          model: # The Employee Object

              ### Description

              The `Employee` object is used to represent any person who has been employed by a
              company.

              ### Usage Example

              Fetch from the `LIST Employee` endpoint and filter by `ID` to show all
              employees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/hris/v1/employees",
            body=maybe_transform({"model": model}, employee_create_params.EmployeeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedEmployeeResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: List[
            Literal[
                "company", "employments", "groups", "home_location", "manager", "pay_group", "team", "work_location"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_sensitive_fields: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "employment_status",
            "employment_status,ethnicity",
            "employment_status,ethnicity,gender",
            "employment_status,ethnicity,gender,marital_status",
            "employment_status,ethnicity,marital_status",
            "employment_status,gender",
            "employment_status,gender,marital_status",
            "employment_status,marital_status",
            "ethnicity",
            "ethnicity,gender",
            "ethnicity,gender,marital_status",
            "ethnicity,marital_status",
            "gender",
            "gender,marital_status",
            "marital_status",
        ]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "employment_status",
            "employment_status,ethnicity",
            "employment_status,ethnicity,gender",
            "employment_status,ethnicity,gender,marital_status",
            "employment_status,ethnicity,marital_status",
            "employment_status,gender",
            "employment_status,gender,marital_status",
            "employment_status,marital_status",
            "ethnicity",
            "ethnicity,gender",
            "ethnicity,gender,marital_status",
            "ethnicity,marital_status",
            "gender",
            "gender,marital_status",
            "marital_status",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Employee:
        """
        Returns an `Employee` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_sensitive_fields: Whether to include sensitive fields (such as social security numbers) in the
              response.

          remote_fields: Deprecated. Use show_enum_origins.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/hris/v1/employees/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                        "include_sensitive_fields": include_sensitive_fields,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                    },
                    employee_retrieve_params.EmployeeRetrieveParams,
                ),
            ),
            cast_to=Employee,
        )

    def list(
        self,
        *,
        company_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        display_full_name: Optional[str] | NotGiven = NOT_GIVEN,
        employment_status: Optional[Literal["ACTIVE", "INACTIVE", "PENDING"]] | NotGiven = NOT_GIVEN,
        expand: List[
            Literal[
                "company", "employments", "groups", "home_location", "manager", "pay_group", "team", "work_location"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        groups: str | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_sensitive_fields: bool | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        manager_id: str | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pay_group_id: str | NotGiven = NOT_GIVEN,
        personal_email: Optional[str] | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "employment_status",
            "employment_status,ethnicity",
            "employment_status,ethnicity,gender",
            "employment_status,ethnicity,gender,marital_status",
            "employment_status,ethnicity,marital_status",
            "employment_status,gender",
            "employment_status,gender,marital_status",
            "employment_status,marital_status",
            "ethnicity",
            "ethnicity,gender",
            "ethnicity,gender,marital_status",
            "ethnicity,marital_status",
            "gender",
            "gender,marital_status",
            "marital_status",
        ]
        | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "employment_status",
            "employment_status,ethnicity",
            "employment_status,ethnicity,gender",
            "employment_status,ethnicity,gender,marital_status",
            "employment_status,ethnicity,marital_status",
            "employment_status,gender",
            "employment_status,gender,marital_status",
            "employment_status,marital_status",
            "ethnicity",
            "ethnicity,gender",
            "ethnicity,gender,marital_status",
            "ethnicity,marital_status",
            "gender",
            "gender,marital_status",
            "marital_status",
        ]
        | NotGiven = NOT_GIVEN,
        team_id: str | NotGiven = NOT_GIVEN,
        work_email: Optional[str] | NotGiven = NOT_GIVEN,
        work_location_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Employee]:
        """
        Returns a list of `Employee` objects.

        Args:
          company_id: If provided, will only return employees for this company.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          display_full_name: If provided, will only return employees with this display name.

          employment_status: If provided, will only return employees with this employment status.

              - `ACTIVE` - ACTIVE
              - `PENDING` - PENDING
              - `INACTIVE` - INACTIVE

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          first_name: If provided, will only return employees with this first name.

          groups: If provided, will only return employees matching the group ids; multiple groups
              can be separated by commas.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_sensitive_fields: Whether to include sensitive fields (such as social security numbers) in the
              response.

          last_name: If provided, will only return employees with this last name.

          manager_id: If provided, will only return employees for this manager.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          pay_group_id: If provided, will only return employees for this pay group

          personal_email: If provided, will only return Employees with this personal email

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          show_enum_origins: Which fields should be returned in non-normalized form.

          team_id: If provided, will only return employees for this team.

          work_email: If provided, will only return Employees with this work email

          work_location_id: If provided, will only return employees for this location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/employees",
            page=SyncPage[Employee],
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
                        "display_full_name": display_full_name,
                        "employment_status": employment_status,
                        "expand": expand,
                        "first_name": first_name,
                        "groups": groups,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_sensitive_fields": include_sensitive_fields,
                        "last_name": last_name,
                        "manager_id": manager_id,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "pay_group_id": pay_group_id,
                        "personal_email": personal_email,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                        "team_id": team_id,
                        "work_email": work_email,
                        "work_location_id": work_location_id,
                    },
                    employee_list_params.EmployeeListParams,
                ),
            ),
            model=Employee,
        )

    def ignore(
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
            f"/hris/v1/employees/ignore/{model_id}",
            body=maybe_transform(
                {
                    "reason": reason,
                    "message": message,
                },
                employee_ignore_params.EmployeeIgnoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.IgnoreCommonModel,
        )


class AsyncEmployees(AsyncAPIResource):
    meta: AsyncMeta

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.meta = AsyncMeta(client)

    async def create(
        self,
        *,
        model: employee_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CreatedEmployeeResponse:
        """
        Creates an `Employee` object with the given values.

        Args:
          model: # The Employee Object

              ### Description

              The `Employee` object is used to represent any person who has been employed by a
              company.

              ### Usage Example

              Fetch from the `LIST Employee` endpoint and filter by `ID` to show all
              employees.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/hris/v1/employees",
            body=maybe_transform({"model": model}, employee_create_params.EmployeeCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedEmployeeResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: List[
            Literal[
                "company", "employments", "groups", "home_location", "manager", "pay_group", "team", "work_location"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_sensitive_fields: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "employment_status",
            "employment_status,ethnicity",
            "employment_status,ethnicity,gender",
            "employment_status,ethnicity,gender,marital_status",
            "employment_status,ethnicity,marital_status",
            "employment_status,gender",
            "employment_status,gender,marital_status",
            "employment_status,marital_status",
            "ethnicity",
            "ethnicity,gender",
            "ethnicity,gender,marital_status",
            "ethnicity,marital_status",
            "gender",
            "gender,marital_status",
            "marital_status",
        ]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "employment_status",
            "employment_status,ethnicity",
            "employment_status,ethnicity,gender",
            "employment_status,ethnicity,gender,marital_status",
            "employment_status,ethnicity,marital_status",
            "employment_status,gender",
            "employment_status,gender,marital_status",
            "employment_status,marital_status",
            "ethnicity",
            "ethnicity,gender",
            "ethnicity,gender,marital_status",
            "ethnicity,marital_status",
            "gender",
            "gender,marital_status",
            "marital_status",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Employee:
        """
        Returns an `Employee` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_sensitive_fields: Whether to include sensitive fields (such as social security numbers) in the
              response.

          remote_fields: Deprecated. Use show_enum_origins.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/hris/v1/employees/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                        "include_sensitive_fields": include_sensitive_fields,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                    },
                    employee_retrieve_params.EmployeeRetrieveParams,
                ),
            ),
            cast_to=Employee,
        )

    def list(
        self,
        *,
        company_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        display_full_name: Optional[str] | NotGiven = NOT_GIVEN,
        employment_status: Optional[Literal["ACTIVE", "INACTIVE", "PENDING"]] | NotGiven = NOT_GIVEN,
        expand: List[
            Literal[
                "company", "employments", "groups", "home_location", "manager", "pay_group", "team", "work_location"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        first_name: Optional[str] | NotGiven = NOT_GIVEN,
        groups: str | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_sensitive_fields: bool | NotGiven = NOT_GIVEN,
        last_name: Optional[str] | NotGiven = NOT_GIVEN,
        manager_id: str | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pay_group_id: str | NotGiven = NOT_GIVEN,
        personal_email: Optional[str] | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "employment_status",
            "employment_status,ethnicity",
            "employment_status,ethnicity,gender",
            "employment_status,ethnicity,gender,marital_status",
            "employment_status,ethnicity,marital_status",
            "employment_status,gender",
            "employment_status,gender,marital_status",
            "employment_status,marital_status",
            "ethnicity",
            "ethnicity,gender",
            "ethnicity,gender,marital_status",
            "ethnicity,marital_status",
            "gender",
            "gender,marital_status",
            "marital_status",
        ]
        | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "employment_status",
            "employment_status,ethnicity",
            "employment_status,ethnicity,gender",
            "employment_status,ethnicity,gender,marital_status",
            "employment_status,ethnicity,marital_status",
            "employment_status,gender",
            "employment_status,gender,marital_status",
            "employment_status,marital_status",
            "ethnicity",
            "ethnicity,gender",
            "ethnicity,gender,marital_status",
            "ethnicity,marital_status",
            "gender",
            "gender,marital_status",
            "marital_status",
        ]
        | NotGiven = NOT_GIVEN,
        team_id: str | NotGiven = NOT_GIVEN,
        work_email: Optional[str] | NotGiven = NOT_GIVEN,
        work_location_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Employee, AsyncPage[Employee]]:
        """
        Returns a list of `Employee` objects.

        Args:
          company_id: If provided, will only return employees for this company.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          display_full_name: If provided, will only return employees with this display name.

          employment_status: If provided, will only return employees with this employment status.

              - `ACTIVE` - ACTIVE
              - `PENDING` - PENDING
              - `INACTIVE` - INACTIVE

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          first_name: If provided, will only return employees with this first name.

          groups: If provided, will only return employees matching the group ids; multiple groups
              can be separated by commas.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_sensitive_fields: Whether to include sensitive fields (such as social security numbers) in the
              response.

          last_name: If provided, will only return employees with this last name.

          manager_id: If provided, will only return employees for this manager.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          pay_group_id: If provided, will only return employees for this pay group

          personal_email: If provided, will only return Employees with this personal email

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          show_enum_origins: Which fields should be returned in non-normalized form.

          team_id: If provided, will only return employees for this team.

          work_email: If provided, will only return Employees with this work email

          work_location_id: If provided, will only return employees for this location.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/employees",
            page=AsyncPage[Employee],
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
                        "display_full_name": display_full_name,
                        "employment_status": employment_status,
                        "expand": expand,
                        "first_name": first_name,
                        "groups": groups,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_sensitive_fields": include_sensitive_fields,
                        "last_name": last_name,
                        "manager_id": manager_id,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "pay_group_id": pay_group_id,
                        "personal_email": personal_email,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                        "team_id": team_id,
                        "work_email": work_email,
                        "work_location_id": work_location_id,
                    },
                    employee_list_params.EmployeeListParams,
                ),
            ),
            model=Employee,
        )

    async def ignore(
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
            f"/hris/v1/employees/ignore/{model_id}",
            body=maybe_transform(
                {
                    "reason": reason,
                    "message": message,
                },
                employee_ignore_params.EmployeeIgnoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.IgnoreCommonModel,
        )
