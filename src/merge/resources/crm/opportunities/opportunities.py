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
from ....types.crm import (
    Opportunity,
    OpportunityResponse,
    opportunity_list_params,
    opportunity_create_params,
    opportunity_update_params,
    opportunity_retrieve_params,
    opportunity_list_remote_field_classes_params,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ...._client import Merge, AsyncMerge

__all__ = ["Opportunities", "AsyncOpportunities"]


class Opportunities(SyncAPIResource):
    meta: Meta

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.meta = Meta(client)

    def create(
        self,
        *,
        model: opportunity_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> OpportunityResponse:
        """
        Creates an `Opportunity` object with the given values.

        Args:
          model: # The Opportunity Object

              ### Description

              The `Opportunity` object is used to represent a deal opportunity in a CRM
              system.

              ### Usage Example

              TODO

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v1/opportunities",
            body=maybe_transform({"model": model}, opportunity_create_params.OpportunityCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["account", "owner", "stage"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal["status"] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["status"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Opportunity:
        """
        Returns an `Opportunity` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          remote_fields: Deprecated. Use show_enum_origins.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/crm/v1/opportunities/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                    },
                    opportunity_retrieve_params.OpportunityRetrieveParams,
                ),
            ),
            cast_to=Opportunity,
        )

    def update(
        self,
        id: str,
        *,
        model: opportunity_update_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> OpportunityResponse:
        """
        Updates an `Opportunity` object with the given `id`.

        Args:
          model: # The Opportunity Object

              ### Description

              The `Opportunity` object is used to represent a deal opportunity in a CRM
              system.

              ### Usage Example

              TODO

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/crm/v1/opportunities/{id}",
            body=maybe_transform({"model": model}, opportunity_update_params.OpportunityUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityResponse,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["account", "owner", "stage"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        owner_id: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal["status"] | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["status"] | NotGiven = NOT_GIVEN,
        stage_id: str | NotGiven = NOT_GIVEN,
        status: Optional[Literal["LOST", "OPEN", "WON"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Opportunity]:
        """
        Returns a list of `Opportunity` objects.

        Args:
          account_id: If provided, will only return opportunities with this account.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          modified_after: If provided, only objects synced by Merge after this date time will be returned.

          modified_before: If provided, only objects synced by Merge before this date time will be
              returned.

          owner_id: If provided, will only return opportunities with this owner.

          page_size: Number of results to return per page.

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          show_enum_origins: Which fields should be returned in non-normalized form.

          stage_id: If provided, will only return opportunities with this stage.

          status: If provided, will only return opportunities with this status. Options: ('OPEN',
              'WON', 'LOST')

              - `OPEN` - OPEN
              - `WON` - WON
              - `LOST` - LOST

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v1/opportunities",
            page=SyncPage[Opportunity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "owner_id": owner_id,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                        "stage_id": stage_id,
                        "status": status,
                    },
                    opportunity_list_params.OpportunityListParams,
                ),
            ),
            model=Opportunity,
        )

    def list_remote_field_classes(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[shared.RemoteFieldClass]:
        """
        Returns a list of `RemoteFieldClass` objects.

        Args:
          cursor: The pagination cursor value.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v1/opportunities/remote-field-classes",
            page=SyncPage[shared.RemoteFieldClass],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "page_size": page_size,
                    },
                    opportunity_list_remote_field_classes_params.OpportunityListRemoteFieldClassesParams,
                ),
            ),
            model=shared.RemoteFieldClass,
        )


class AsyncOpportunities(AsyncAPIResource):
    meta: AsyncMeta

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.meta = AsyncMeta(client)

    async def create(
        self,
        *,
        model: opportunity_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> OpportunityResponse:
        """
        Creates an `Opportunity` object with the given values.

        Args:
          model: # The Opportunity Object

              ### Description

              The `Opportunity` object is used to represent a deal opportunity in a CRM
              system.

              ### Usage Example

              TODO

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v1/opportunities",
            body=maybe_transform({"model": model}, opportunity_create_params.OpportunityCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["account", "owner", "stage"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal["status"] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["status"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Opportunity:
        """
        Returns an `Opportunity` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          remote_fields: Deprecated. Use show_enum_origins.

          show_enum_origins: Which fields should be returned in non-normalized form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/crm/v1/opportunities/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                    },
                    opportunity_retrieve_params.OpportunityRetrieveParams,
                ),
            ),
            cast_to=Opportunity,
        )

    async def update(
        self,
        id: str,
        *,
        model: opportunity_update_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> OpportunityResponse:
        """
        Updates an `Opportunity` object with the given `id`.

        Args:
          model: # The Opportunity Object

              ### Description

              The `Opportunity` object is used to represent a deal opportunity in a CRM
              system.

              ### Usage Example

              TODO

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/crm/v1/opportunities/{id}",
            body=maybe_transform({"model": model}, opportunity_update_params.OpportunityUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpportunityResponse,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["account", "owner", "stage"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        owner_id: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_fields: Literal["status"] | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal["status"] | NotGiven = NOT_GIVEN,
        stage_id: str | NotGiven = NOT_GIVEN,
        status: Optional[Literal["LOST", "OPEN", "WON"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Opportunity, AsyncPage[Opportunity]]:
        """
        Returns a list of `Opportunity` objects.

        Args:
          account_id: If provided, will only return opportunities with this account.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          modified_after: If provided, only objects synced by Merge after this date time will be returned.

          modified_before: If provided, only objects synced by Merge before this date time will be
              returned.

          owner_id: If provided, will only return opportunities with this owner.

          page_size: Number of results to return per page.

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          show_enum_origins: Which fields should be returned in non-normalized form.

          stage_id: If provided, will only return opportunities with this stage.

          status: If provided, will only return opportunities with this status. Options: ('OPEN',
              'WON', 'LOST')

              - `OPEN` - OPEN
              - `WON` - WON
              - `LOST` - LOST

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v1/opportunities",
            page=AsyncPage[Opportunity],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "owner_id": owner_id,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                        "stage_id": stage_id,
                        "status": status,
                    },
                    opportunity_list_params.OpportunityListParams,
                ),
            ),
            model=Opportunity,
        )

    def list_remote_field_classes(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[shared.RemoteFieldClass, AsyncPage[shared.RemoteFieldClass]]:
        """
        Returns a list of `RemoteFieldClass` objects.

        Args:
          cursor: The pagination cursor value.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v1/opportunities/remote-field-classes",
            page=AsyncPage[shared.RemoteFieldClass],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "page_size": page_size,
                    },
                    opportunity_list_remote_field_classes_params.OpportunityListRemoteFieldClassesParams,
                ),
            ),
            model=shared.RemoteFieldClass,
        )
