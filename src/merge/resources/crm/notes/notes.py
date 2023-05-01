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
    Note,
    NoteResponse,
    note_list_params,
    note_create_params,
    note_retrieve_params,
    note_list_remote_field_classes_params,
)
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ...._client import Merge, AsyncMerge

__all__ = ["Notes", "AsyncNotes"]


class Notes(SyncAPIResource):
    meta: Meta

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.meta = Meta(client)

    def create(
        self,
        *,
        model: note_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> NoteResponse:
        """
        Creates a `Note` object with the given values.

        Args:
          model: # The Note Object

              ### Description

              The `Note` object is used to represent a note on another object.

              ### Usage Example

              TODO

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v1/notes",
            body=maybe_transform({"model": model}, note_create_params.NoteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["account", "contact", "opportunity", "owner"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Note:
        """
        Returns a `Note` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/crm/v1/notes/{id}",
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
                    },
                    note_retrieve_params.NoteRetrieveParams,
                ),
            ),
            cast_to=Note,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        contact_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["account", "contact", "opportunity", "owner"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        opportunity_id: str | NotGiven = NOT_GIVEN,
        owner_id: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Note]:
        """
        Returns a list of `Note` objects.

        Args:
          account_id: If provided, will only return notes with this account.

          contact_id: If provided, will only return notes with this contact.

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

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          opportunity_id: If provided, will only return notes with this opportunity.

          owner_id: If provided, will only return notes with this owner.

          page_size: Number of results to return per page.

          remote_id: The API provider's ID for the given object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v1/notes",
            page=SyncPage[Note],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "contact_id": contact_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "opportunity_id": opportunity_id,
                        "owner_id": owner_id,
                        "page_size": page_size,
                        "remote_id": remote_id,
                    },
                    note_list_params.NoteListParams,
                ),
            ),
            model=Note,
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
            "/crm/v1/notes/remote-field-classes",
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
                    note_list_remote_field_classes_params.NoteListRemoteFieldClassesParams,
                ),
            ),
            model=shared.RemoteFieldClass,
        )


class AsyncNotes(AsyncAPIResource):
    meta: AsyncMeta

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.meta = AsyncMeta(client)

    async def create(
        self,
        *,
        model: note_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> NoteResponse:
        """
        Creates a `Note` object with the given values.

        Args:
          model: # The Note Object

              ### Description

              The `Note` object is used to represent a note on another object.

              ### Usage Example

              TODO

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v1/notes",
            body=maybe_transform({"model": model}, note_create_params.NoteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: List[Literal["account", "contact", "opportunity", "owner"]] | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Note:
        """
        Returns a `Note` object with the given `id`.

        Args:
          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/crm/v1/notes/{id}",
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
                    },
                    note_retrieve_params.NoteRetrieveParams,
                ),
            ),
            cast_to=Note,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        contact_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: List[Literal["account", "contact", "opportunity", "owner"]] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        opportunity_id: str | NotGiven = NOT_GIVEN,
        owner_id: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Note, AsyncPage[Note]]:
        """
        Returns a list of `Note` objects.

        Args:
          account_id: If provided, will only return notes with this account.

          contact_id: If provided, will only return notes with this contact.

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

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          opportunity_id: If provided, will only return notes with this opportunity.

          owner_id: If provided, will only return notes with this owner.

          page_size: Number of results to return per page.

          remote_id: The API provider's ID for the given object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/crm/v1/notes",
            page=AsyncPage[Note],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "contact_id": contact_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "opportunity_id": opportunity_id,
                        "owner_id": owner_id,
                        "page_size": page_size,
                        "remote_id": remote_id,
                    },
                    note_list_params.NoteListParams,
                ),
            ),
            model=Note,
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
            "/crm/v1/notes/remote-field-classes",
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
                    note_list_remote_field_classes_params.NoteListRemoteFieldClassesParams,
                ),
            ),
            model=shared.RemoteFieldClass,
        )
