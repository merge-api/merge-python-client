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
from ....types.hris import (
    TimeOff,
    TimeOffResponse,
    time_off_list_params,
    time_off_create_params,
    time_off_retrieve_params,
)
from ...._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ...._client import Merge, AsyncMerge

__all__ = ["TimeOffResource", "AsyncTimeOffResource"]


class TimeOffResource(SyncAPIResource):
    meta: Meta

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.meta = Meta(client)

    def create(
        self,
        *,
        model: time_off_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> TimeOffResponse:
        """
        Creates a `TimeOff` object with the given values.

        Args:
          model: # The TimeOff Object

              ### Description

              The `TimeOff` object is used to represent all employees' Time Off entries.

              ### Usage Example

              Fetch from the `LIST TimeOffs` endpoint and filter by `ID` to show all time off
              requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/hris/v1/time-off",
            body=maybe_transform({"model": model}, time_off_create_params.TimeOffCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeOffResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["approver", "employee"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "request_type",
            "request_type,status",
            "request_type,status,units",
            "request_type,units",
            "status",
            "status,units",
            "units",
        ]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "request_type",
            "request_type,status",
            "request_type,status,units",
            "request_type,units",
            "status",
            "status,units",
            "units",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> TimeOff:
        """
        Returns a `TimeOff` object with the given `id`.

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
            f"/hris/v1/time-off/{id}",
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
                    time_off_retrieve_params.TimeOffRetrieveParams,
                ),
            ),
            cast_to=TimeOff,
        )

    def list(
        self,
        *,
        approver_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["approver", "employee"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "request_type",
            "request_type,status",
            "request_type,status,units",
            "request_type,units",
            "status",
            "status,units",
            "units",
        ]
        | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        request_type: Optional[Literal["BEREAVEMENT", "JURY_DUTY", "PERSONAL", "SICK", "VACATION", "VOLUNTEER"]]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "request_type",
            "request_type,status",
            "request_type,status,units",
            "request_type,units",
            "status",
            "status,units",
            "units",
        ]
        | NotGiven = NOT_GIVEN,
        status: Optional[Literal["APPROVED", "CANCELLED", "DECLINED", "DELETED", "REQUESTED"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[TimeOff]:
        """
        Returns a list of `TimeOff` objects.

        Args:
          approver_id: If provided, will only return time off for this approver.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          employee_id: If provided, will only return time off for this employee.

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

          request_type:
              If provided, will only return TimeOff with this request type. Options:
              ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER', 'BEREAVEMENT')

              - `VACATION` - VACATION
              - `SICK` - SICK
              - `PERSONAL` - PERSONAL
              - `JURY_DUTY` - JURY_DUTY
              - `VOLUNTEER` - VOLUNTEER
              - `BEREAVEMENT` - BEREAVEMENT

          show_enum_origins: Which fields should be returned in non-normalized form.

          status: If provided, will only return TimeOff with this status. Options: ('REQUESTED',
              'APPROVED', 'DECLINED', 'CANCELLED', 'DELETED')

              - `REQUESTED` - REQUESTED
              - `APPROVED` - APPROVED
              - `DECLINED` - DECLINED
              - `CANCELLED` - CANCELLED
              - `DELETED` - DELETED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/time-off",
            page=SyncPage[TimeOff],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "approver_id": approver_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "employee_id": employee_id,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "request_type": request_type,
                        "show_enum_origins": show_enum_origins,
                        "status": status,
                    },
                    time_off_list_params.TimeOffListParams,
                ),
            ),
            model=TimeOff,
        )


class AsyncTimeOffResource(AsyncAPIResource):
    meta: AsyncMeta

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.meta = AsyncMeta(client)

    async def create(
        self,
        *,
        model: time_off_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> TimeOffResponse:
        """
        Creates a `TimeOff` object with the given values.

        Args:
          model: # The TimeOff Object

              ### Description

              The `TimeOff` object is used to represent all employees' Time Off entries.

              ### Usage Example

              Fetch from the `LIST TimeOffs` endpoint and filter by `ID` to show all time off
              requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/hris/v1/time-off",
            body=maybe_transform({"model": model}, time_off_create_params.TimeOffCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimeOffResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["approver", "employee"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "request_type",
            "request_type,status",
            "request_type,status,units",
            "request_type,units",
            "status",
            "status,units",
            "units",
        ]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "request_type",
            "request_type,status",
            "request_type,status,units",
            "request_type,units",
            "status",
            "status,units",
            "units",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> TimeOff:
        """
        Returns a `TimeOff` object with the given `id`.

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
            f"/hris/v1/time-off/{id}",
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
                    time_off_retrieve_params.TimeOffRetrieveParams,
                ),
            ),
            cast_to=TimeOff,
        )

    def list(
        self,
        *,
        approver_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        employee_id: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["approver", "employee"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "request_type",
            "request_type,status",
            "request_type,status,units",
            "request_type,units",
            "status",
            "status,units",
            "units",
        ]
        | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        request_type: Optional[Literal["BEREAVEMENT", "JURY_DUTY", "PERSONAL", "SICK", "VACATION", "VOLUNTEER"]]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "request_type",
            "request_type,status",
            "request_type,status,units",
            "request_type,units",
            "status",
            "status,units",
            "units",
        ]
        | NotGiven = NOT_GIVEN,
        status: Optional[Literal["APPROVED", "CANCELLED", "DECLINED", "DELETED", "REQUESTED"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[TimeOff, AsyncPage[TimeOff]]:
        """
        Returns a list of `TimeOff` objects.

        Args:
          approver_id: If provided, will only return time off for this approver.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          employee_id: If provided, will only return time off for this employee.

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

          request_type:
              If provided, will only return TimeOff with this request type. Options:
              ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER', 'BEREAVEMENT')

              - `VACATION` - VACATION
              - `SICK` - SICK
              - `PERSONAL` - PERSONAL
              - `JURY_DUTY` - JURY_DUTY
              - `VOLUNTEER` - VOLUNTEER
              - `BEREAVEMENT` - BEREAVEMENT

          show_enum_origins: Which fields should be returned in non-normalized form.

          status: If provided, will only return TimeOff with this status. Options: ('REQUESTED',
              'APPROVED', 'DECLINED', 'CANCELLED', 'DELETED')

              - `REQUESTED` - REQUESTED
              - `APPROVED` - APPROVED
              - `DECLINED` - DECLINED
              - `CANCELLED` - CANCELLED
              - `DELETED` - DELETED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/hris/v1/time-off",
            page=AsyncPage[TimeOff],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "approver_id": approver_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "employee_id": employee_id,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "request_type": request_type,
                        "show_enum_origins": show_enum_origins,
                        "status": status,
                    },
                    time_off_list_params.TimeOffListParams,
                ),
            ),
            model=TimeOff,
        )
