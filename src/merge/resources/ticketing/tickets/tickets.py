# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .meta import Meta, AsyncMeta
from ....types import shared
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.ticketing import (
    Ticket,
    TicketResponse,
    ticket_list_params,
    ticket_create_params,
    ticket_update_params,
    ticket_retrieve_params,
    ticket_list_collaborators_params,
    ticket_list_remote_field_classes_params,
)
from ....types.file_storage import FileStorageUser

if TYPE_CHECKING:
    from ...._client import Merge, AsyncMerge

__all__ = ["Tickets", "AsyncTickets"]


class Tickets(SyncAPIResource):
    meta: Meta

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.meta = Meta(client)

    def create(
        self,
        *,
        model: ticket_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> TicketResponse:
        """
        Creates a `Ticket` object with the given values.

        Args:
          model: # The Ticket Object

              ### Description

              The `Ticket` object is used to represent a ticket or a task within a system.

              ### Usage Example

              TODO

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ticketing/v1/tickets",
            body=maybe_transform({"model": model}, ticket_create_params.TicketCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        expand: Literal[
            "account",
            "account,contact",
            "account,contact,creator",
            "account,contact,creator,parent_ticket",
            "account,contact,parent_ticket",
            "account,creator",
            "account,creator,parent_ticket",
            "account,parent_ticket",
            "assignees",
            "assignees,account",
            "assignees,account,contact",
            "assignees,account,contact,creator",
            "assignees,account,contact,creator,parent_ticket",
            "assignees,account,contact,parent_ticket",
            "assignees,account,creator",
            "assignees,account,creator,parent_ticket",
            "assignees,account,parent_ticket",
            "assignees,collections",
            "assignees,collections,account",
            "assignees,collections,account,contact",
            "assignees,collections,account,contact,creator",
            "assignees,collections,account,contact,creator,parent_ticket",
            "assignees,collections,account,contact,parent_ticket",
            "assignees,collections,account,creator",
            "assignees,collections,account,creator,parent_ticket",
            "assignees,collections,account,parent_ticket",
            "assignees,collections,contact",
            "assignees,collections,contact,creator",
            "assignees,collections,contact,creator,parent_ticket",
            "assignees,collections,contact,parent_ticket",
            "assignees,collections,creator",
            "assignees,collections,creator,parent_ticket",
            "assignees,collections,parent_ticket",
            "assignees,collections,project",
            "assignees,collections,project,account",
            "assignees,collections,project,account,contact",
            "assignees,collections,project,account,contact,creator",
            "assignees,collections,project,account,contact,creator,parent_ticket",
            "assignees,collections,project,account,contact,parent_ticket",
            "assignees,collections,project,account,creator",
            "assignees,collections,project,account,creator,parent_ticket",
            "assignees,collections,project,account,parent_ticket",
            "assignees,collections,project,contact",
            "assignees,collections,project,contact,creator",
            "assignees,collections,project,contact,creator,parent_ticket",
            "assignees,collections,project,contact,parent_ticket",
            "assignees,collections,project,creator",
            "assignees,collections,project,creator,parent_ticket",
            "assignees,collections,project,parent_ticket",
            "assignees,contact",
            "assignees,contact,creator",
            "assignees,contact,creator,parent_ticket",
            "assignees,contact,parent_ticket",
            "assignees,creator",
            "assignees,creator,parent_ticket",
            "assignees,parent_ticket",
            "assignees,project",
            "assignees,project,account",
            "assignees,project,account,contact",
            "assignees,project,account,contact,creator",
            "assignees,project,account,contact,creator,parent_ticket",
            "assignees,project,account,contact,parent_ticket",
            "assignees,project,account,creator",
            "assignees,project,account,creator,parent_ticket",
            "assignees,project,account,parent_ticket",
            "assignees,project,contact",
            "assignees,project,contact,creator",
            "assignees,project,contact,creator,parent_ticket",
            "assignees,project,contact,parent_ticket",
            "assignees,project,creator",
            "assignees,project,creator,parent_ticket",
            "assignees,project,parent_ticket",
            "attachments",
            "attachments,account",
            "attachments,account,contact",
            "attachments,account,contact,creator",
            "attachments,account,contact,creator,parent_ticket",
            "attachments,account,contact,parent_ticket",
            "attachments,account,creator",
            "attachments,account,creator,parent_ticket",
            "attachments,account,parent_ticket",
            "attachments,assignees",
            "attachments,assignees,account",
            "attachments,assignees,account,contact",
            "attachments,assignees,account,contact,creator",
            "attachments,assignees,account,contact,creator,parent_ticket",
            "attachments,assignees,account,contact,parent_ticket",
            "attachments,assignees,account,creator",
            "attachments,assignees,account,creator,parent_ticket",
            "attachments,assignees,account,parent_ticket",
            "attachments,assignees,collections",
            "attachments,assignees,collections,account",
            "attachments,assignees,collections,account,contact",
            "attachments,assignees,collections,account,contact,creator",
            "attachments,assignees,collections,account,contact,creator,parent_ticket",
            "attachments,assignees,collections,account,contact,parent_ticket",
            "attachments,assignees,collections,account,creator",
            "attachments,assignees,collections,account,creator,parent_ticket",
            "attachments,assignees,collections,account,parent_ticket",
            "attachments,assignees,collections,contact",
            "attachments,assignees,collections,contact,creator",
            "attachments,assignees,collections,contact,creator,parent_ticket",
            "attachments,assignees,collections,contact,parent_ticket",
            "attachments,assignees,collections,creator",
            "attachments,assignees,collections,creator,parent_ticket",
            "attachments,assignees,collections,parent_ticket",
            "attachments,assignees,collections,project",
            "attachments,assignees,collections,project,account",
            "attachments,assignees,collections,project,account,contact",
            "attachments,assignees,collections,project,account,contact,creator",
            "attachments,assignees,collections,project,account,contact,creator,parent_ticket",
            "attachments,assignees,collections,project,account,contact,parent_ticket",
            "attachments,assignees,collections,project,account,creator",
            "attachments,assignees,collections,project,account,creator,parent_ticket",
            "attachments,assignees,collections,project,account,parent_ticket",
            "attachments,assignees,collections,project,contact",
            "attachments,assignees,collections,project,contact,creator",
            "attachments,assignees,collections,project,contact,creator,parent_ticket",
            "attachments,assignees,collections,project,contact,parent_ticket",
            "attachments,assignees,collections,project,creator",
            "attachments,assignees,collections,project,creator,parent_ticket",
            "attachments,assignees,collections,project,parent_ticket",
            "attachments,assignees,contact",
            "attachments,assignees,contact,creator",
            "attachments,assignees,contact,creator,parent_ticket",
            "attachments,assignees,contact,parent_ticket",
            "attachments,assignees,creator",
            "attachments,assignees,creator,parent_ticket",
            "attachments,assignees,parent_ticket",
            "attachments,assignees,project",
            "attachments,assignees,project,account",
            "attachments,assignees,project,account,contact",
            "attachments,assignees,project,account,contact,creator",
            "attachments,assignees,project,account,contact,creator,parent_ticket",
            "attachments,assignees,project,account,contact,parent_ticket",
            "attachments,assignees,project,account,creator",
            "attachments,assignees,project,account,creator,parent_ticket",
            "attachments,assignees,project,account,parent_ticket",
            "attachments,assignees,project,contact",
            "attachments,assignees,project,contact,creator",
            "attachments,assignees,project,contact,creator,parent_ticket",
            "attachments,assignees,project,contact,parent_ticket",
            "attachments,assignees,project,creator",
            "attachments,assignees,project,creator,parent_ticket",
            "attachments,assignees,project,parent_ticket",
            "attachments,collections",
            "attachments,collections,account",
            "attachments,collections,account,contact",
            "attachments,collections,account,contact,creator",
            "attachments,collections,account,contact,creator,parent_ticket",
            "attachments,collections,account,contact,parent_ticket",
            "attachments,collections,account,creator",
            "attachments,collections,account,creator,parent_ticket",
            "attachments,collections,account,parent_ticket",
            "attachments,collections,contact",
            "attachments,collections,contact,creator",
            "attachments,collections,contact,creator,parent_ticket",
            "attachments,collections,contact,parent_ticket",
            "attachments,collections,creator",
            "attachments,collections,creator,parent_ticket",
            "attachments,collections,parent_ticket",
            "attachments,collections,project",
            "attachments,collections,project,account",
            "attachments,collections,project,account,contact",
            "attachments,collections,project,account,contact,creator",
            "attachments,collections,project,account,contact,creator,parent_ticket",
            "attachments,collections,project,account,contact,parent_ticket",
            "attachments,collections,project,account,creator",
            "attachments,collections,project,account,creator,parent_ticket",
            "attachments,collections,project,account,parent_ticket",
            "attachments,collections,project,contact",
            "attachments,collections,project,contact,creator",
            "attachments,collections,project,contact,creator,parent_ticket",
            "attachments,collections,project,contact,parent_ticket",
            "attachments,collections,project,creator",
            "attachments,collections,project,creator,parent_ticket",
            "attachments,collections,project,parent_ticket",
            "attachments,contact",
            "attachments,contact,creator",
            "attachments,contact,creator,parent_ticket",
            "attachments,contact,parent_ticket",
            "attachments,creator",
            "attachments,creator,parent_ticket",
            "attachments,parent_ticket",
            "attachments,project",
            "attachments,project,account",
            "attachments,project,account,contact",
            "attachments,project,account,contact,creator",
            "attachments,project,account,contact,creator,parent_ticket",
            "attachments,project,account,contact,parent_ticket",
            "attachments,project,account,creator",
            "attachments,project,account,creator,parent_ticket",
            "attachments,project,account,parent_ticket",
            "attachments,project,contact",
            "attachments,project,contact,creator",
            "attachments,project,contact,creator,parent_ticket",
            "attachments,project,contact,parent_ticket",
            "attachments,project,creator",
            "attachments,project,creator,parent_ticket",
            "attachments,project,parent_ticket",
            "collections",
            "collections,account",
            "collections,account,contact",
            "collections,account,contact,creator",
            "collections,account,contact,creator,parent_ticket",
            "collections,account,contact,parent_ticket",
            "collections,account,creator",
            "collections,account,creator,parent_ticket",
            "collections,account,parent_ticket",
            "collections,contact",
            "collections,contact,creator",
            "collections,contact,creator,parent_ticket",
            "collections,contact,parent_ticket",
            "collections,creator",
            "collections,creator,parent_ticket",
            "collections,parent_ticket",
            "collections,project",
            "collections,project,account",
            "collections,project,account,contact",
            "collections,project,account,contact,creator",
            "collections,project,account,contact,creator,parent_ticket",
            "collections,project,account,contact,parent_ticket",
            "collections,project,account,creator",
            "collections,project,account,creator,parent_ticket",
            "collections,project,account,parent_ticket",
            "collections,project,contact",
            "collections,project,contact,creator",
            "collections,project,contact,creator,parent_ticket",
            "collections,project,contact,parent_ticket",
            "collections,project,creator",
            "collections,project,creator,parent_ticket",
            "collections,project,parent_ticket",
            "contact",
            "contact,creator",
            "contact,creator,parent_ticket",
            "contact,parent_ticket",
            "creator",
            "creator,parent_ticket",
            "parent_ticket",
            "project",
            "project,account",
            "project,account,contact",
            "project,account,contact,creator",
            "project,account,contact,creator,parent_ticket",
            "project,account,contact,parent_ticket",
            "project,account,creator",
            "project,account,creator,parent_ticket",
            "project,account,parent_ticket",
            "project,contact",
            "project,contact,creator",
            "project,contact,creator,parent_ticket",
            "project,contact,parent_ticket",
            "project,creator",
            "project,creator,parent_ticket",
            "project,parent_ticket",
        ]
        | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "priority",
            "priority,status",
            "priority,status,ticket_type",
            "priority,ticket_type",
            "status",
            "status,ticket_type",
            "ticket_type",
        ]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "priority",
            "priority,status",
            "priority,status,ticket_type",
            "priority,ticket_type",
            "status",
            "status,ticket_type",
            "ticket_type",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Ticket:
        """
        Returns a `Ticket` object with the given `id`.

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
            f"/ticketing/v1/tickets/{id}",
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
                    ticket_retrieve_params.TicketRetrieveParams,
                ),
            ),
            cast_to=Ticket,
        )

    def update(
        self,
        id: str,
        *,
        model: ticket_update_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> TicketResponse:
        """
        Updates a `Ticket` object with the given `id`.

        Args:
          model: # The Ticket Object

              ### Description

              The `Ticket` object is used to represent a ticket or a task within a system.

              ### Usage Example

              TODO

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/ticketing/v1/tickets/{id}",
            body=maybe_transform({"model": model}, ticket_update_params.TicketUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketResponse,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        assignee_ids: str | NotGiven = NOT_GIVEN,
        collection_ids: str | NotGiven = NOT_GIVEN,
        completed_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        completed_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        contact_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        due_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        due_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        expand: Literal[
            "account",
            "account,contact",
            "account,contact,creator",
            "account,contact,creator,parent_ticket",
            "account,contact,parent_ticket",
            "account,creator",
            "account,creator,parent_ticket",
            "account,parent_ticket",
            "assignees",
            "assignees,account",
            "assignees,account,contact",
            "assignees,account,contact,creator",
            "assignees,account,contact,creator,parent_ticket",
            "assignees,account,contact,parent_ticket",
            "assignees,account,creator",
            "assignees,account,creator,parent_ticket",
            "assignees,account,parent_ticket",
            "assignees,collections",
            "assignees,collections,account",
            "assignees,collections,account,contact",
            "assignees,collections,account,contact,creator",
            "assignees,collections,account,contact,creator,parent_ticket",
            "assignees,collections,account,contact,parent_ticket",
            "assignees,collections,account,creator",
            "assignees,collections,account,creator,parent_ticket",
            "assignees,collections,account,parent_ticket",
            "assignees,collections,contact",
            "assignees,collections,contact,creator",
            "assignees,collections,contact,creator,parent_ticket",
            "assignees,collections,contact,parent_ticket",
            "assignees,collections,creator",
            "assignees,collections,creator,parent_ticket",
            "assignees,collections,parent_ticket",
            "assignees,collections,project",
            "assignees,collections,project,account",
            "assignees,collections,project,account,contact",
            "assignees,collections,project,account,contact,creator",
            "assignees,collections,project,account,contact,creator,parent_ticket",
            "assignees,collections,project,account,contact,parent_ticket",
            "assignees,collections,project,account,creator",
            "assignees,collections,project,account,creator,parent_ticket",
            "assignees,collections,project,account,parent_ticket",
            "assignees,collections,project,contact",
            "assignees,collections,project,contact,creator",
            "assignees,collections,project,contact,creator,parent_ticket",
            "assignees,collections,project,contact,parent_ticket",
            "assignees,collections,project,creator",
            "assignees,collections,project,creator,parent_ticket",
            "assignees,collections,project,parent_ticket",
            "assignees,contact",
            "assignees,contact,creator",
            "assignees,contact,creator,parent_ticket",
            "assignees,contact,parent_ticket",
            "assignees,creator",
            "assignees,creator,parent_ticket",
            "assignees,parent_ticket",
            "assignees,project",
            "assignees,project,account",
            "assignees,project,account,contact",
            "assignees,project,account,contact,creator",
            "assignees,project,account,contact,creator,parent_ticket",
            "assignees,project,account,contact,parent_ticket",
            "assignees,project,account,creator",
            "assignees,project,account,creator,parent_ticket",
            "assignees,project,account,parent_ticket",
            "assignees,project,contact",
            "assignees,project,contact,creator",
            "assignees,project,contact,creator,parent_ticket",
            "assignees,project,contact,parent_ticket",
            "assignees,project,creator",
            "assignees,project,creator,parent_ticket",
            "assignees,project,parent_ticket",
            "attachments",
            "attachments,account",
            "attachments,account,contact",
            "attachments,account,contact,creator",
            "attachments,account,contact,creator,parent_ticket",
            "attachments,account,contact,parent_ticket",
            "attachments,account,creator",
            "attachments,account,creator,parent_ticket",
            "attachments,account,parent_ticket",
            "attachments,assignees",
            "attachments,assignees,account",
            "attachments,assignees,account,contact",
            "attachments,assignees,account,contact,creator",
            "attachments,assignees,account,contact,creator,parent_ticket",
            "attachments,assignees,account,contact,parent_ticket",
            "attachments,assignees,account,creator",
            "attachments,assignees,account,creator,parent_ticket",
            "attachments,assignees,account,parent_ticket",
            "attachments,assignees,collections",
            "attachments,assignees,collections,account",
            "attachments,assignees,collections,account,contact",
            "attachments,assignees,collections,account,contact,creator",
            "attachments,assignees,collections,account,contact,creator,parent_ticket",
            "attachments,assignees,collections,account,contact,parent_ticket",
            "attachments,assignees,collections,account,creator",
            "attachments,assignees,collections,account,creator,parent_ticket",
            "attachments,assignees,collections,account,parent_ticket",
            "attachments,assignees,collections,contact",
            "attachments,assignees,collections,contact,creator",
            "attachments,assignees,collections,contact,creator,parent_ticket",
            "attachments,assignees,collections,contact,parent_ticket",
            "attachments,assignees,collections,creator",
            "attachments,assignees,collections,creator,parent_ticket",
            "attachments,assignees,collections,parent_ticket",
            "attachments,assignees,collections,project",
            "attachments,assignees,collections,project,account",
            "attachments,assignees,collections,project,account,contact",
            "attachments,assignees,collections,project,account,contact,creator",
            "attachments,assignees,collections,project,account,contact,creator,parent_ticket",
            "attachments,assignees,collections,project,account,contact,parent_ticket",
            "attachments,assignees,collections,project,account,creator",
            "attachments,assignees,collections,project,account,creator,parent_ticket",
            "attachments,assignees,collections,project,account,parent_ticket",
            "attachments,assignees,collections,project,contact",
            "attachments,assignees,collections,project,contact,creator",
            "attachments,assignees,collections,project,contact,creator,parent_ticket",
            "attachments,assignees,collections,project,contact,parent_ticket",
            "attachments,assignees,collections,project,creator",
            "attachments,assignees,collections,project,creator,parent_ticket",
            "attachments,assignees,collections,project,parent_ticket",
            "attachments,assignees,contact",
            "attachments,assignees,contact,creator",
            "attachments,assignees,contact,creator,parent_ticket",
            "attachments,assignees,contact,parent_ticket",
            "attachments,assignees,creator",
            "attachments,assignees,creator,parent_ticket",
            "attachments,assignees,parent_ticket",
            "attachments,assignees,project",
            "attachments,assignees,project,account",
            "attachments,assignees,project,account,contact",
            "attachments,assignees,project,account,contact,creator",
            "attachments,assignees,project,account,contact,creator,parent_ticket",
            "attachments,assignees,project,account,contact,parent_ticket",
            "attachments,assignees,project,account,creator",
            "attachments,assignees,project,account,creator,parent_ticket",
            "attachments,assignees,project,account,parent_ticket",
            "attachments,assignees,project,contact",
            "attachments,assignees,project,contact,creator",
            "attachments,assignees,project,contact,creator,parent_ticket",
            "attachments,assignees,project,contact,parent_ticket",
            "attachments,assignees,project,creator",
            "attachments,assignees,project,creator,parent_ticket",
            "attachments,assignees,project,parent_ticket",
            "attachments,collections",
            "attachments,collections,account",
            "attachments,collections,account,contact",
            "attachments,collections,account,contact,creator",
            "attachments,collections,account,contact,creator,parent_ticket",
            "attachments,collections,account,contact,parent_ticket",
            "attachments,collections,account,creator",
            "attachments,collections,account,creator,parent_ticket",
            "attachments,collections,account,parent_ticket",
            "attachments,collections,contact",
            "attachments,collections,contact,creator",
            "attachments,collections,contact,creator,parent_ticket",
            "attachments,collections,contact,parent_ticket",
            "attachments,collections,creator",
            "attachments,collections,creator,parent_ticket",
            "attachments,collections,parent_ticket",
            "attachments,collections,project",
            "attachments,collections,project,account",
            "attachments,collections,project,account,contact",
            "attachments,collections,project,account,contact,creator",
            "attachments,collections,project,account,contact,creator,parent_ticket",
            "attachments,collections,project,account,contact,parent_ticket",
            "attachments,collections,project,account,creator",
            "attachments,collections,project,account,creator,parent_ticket",
            "attachments,collections,project,account,parent_ticket",
            "attachments,collections,project,contact",
            "attachments,collections,project,contact,creator",
            "attachments,collections,project,contact,creator,parent_ticket",
            "attachments,collections,project,contact,parent_ticket",
            "attachments,collections,project,creator",
            "attachments,collections,project,creator,parent_ticket",
            "attachments,collections,project,parent_ticket",
            "attachments,contact",
            "attachments,contact,creator",
            "attachments,contact,creator,parent_ticket",
            "attachments,contact,parent_ticket",
            "attachments,creator",
            "attachments,creator,parent_ticket",
            "attachments,parent_ticket",
            "attachments,project",
            "attachments,project,account",
            "attachments,project,account,contact",
            "attachments,project,account,contact,creator",
            "attachments,project,account,contact,creator,parent_ticket",
            "attachments,project,account,contact,parent_ticket",
            "attachments,project,account,creator",
            "attachments,project,account,creator,parent_ticket",
            "attachments,project,account,parent_ticket",
            "attachments,project,contact",
            "attachments,project,contact,creator",
            "attachments,project,contact,creator,parent_ticket",
            "attachments,project,contact,parent_ticket",
            "attachments,project,creator",
            "attachments,project,creator,parent_ticket",
            "attachments,project,parent_ticket",
            "collections",
            "collections,account",
            "collections,account,contact",
            "collections,account,contact,creator",
            "collections,account,contact,creator,parent_ticket",
            "collections,account,contact,parent_ticket",
            "collections,account,creator",
            "collections,account,creator,parent_ticket",
            "collections,account,parent_ticket",
            "collections,contact",
            "collections,contact,creator",
            "collections,contact,creator,parent_ticket",
            "collections,contact,parent_ticket",
            "collections,creator",
            "collections,creator,parent_ticket",
            "collections,parent_ticket",
            "collections,project",
            "collections,project,account",
            "collections,project,account,contact",
            "collections,project,account,contact,creator",
            "collections,project,account,contact,creator,parent_ticket",
            "collections,project,account,contact,parent_ticket",
            "collections,project,account,creator",
            "collections,project,account,creator,parent_ticket",
            "collections,project,account,parent_ticket",
            "collections,project,contact",
            "collections,project,contact,creator",
            "collections,project,contact,creator,parent_ticket",
            "collections,project,contact,parent_ticket",
            "collections,project,creator",
            "collections,project,creator,parent_ticket",
            "collections,project,parent_ticket",
            "contact",
            "contact,creator",
            "contact,creator,parent_ticket",
            "contact,parent_ticket",
            "creator",
            "creator,parent_ticket",
            "parent_ticket",
            "project",
            "project,account",
            "project,account,contact",
            "project,account,contact,creator",
            "project,account,contact,creator,parent_ticket",
            "project,account,contact,parent_ticket",
            "project,account,creator",
            "project,account,creator,parent_ticket",
            "project,account,parent_ticket",
            "project,contact",
            "project,contact,creator",
            "project,contact,creator,parent_ticket",
            "project,contact,parent_ticket",
            "project,creator",
            "project,creator,parent_ticket",
            "project,parent_ticket",
        ]
        | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        parent_ticket_id: str | NotGiven = NOT_GIVEN,
        priority: Optional[Literal["HIGH", "LOW", "NORMAL", "URGENT"]] | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        remote_created_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        remote_created_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "priority",
            "priority,status",
            "priority,status,ticket_type",
            "priority,ticket_type",
            "status",
            "status,ticket_type",
            "ticket_type",
        ]
        | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        remote_updated_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        remote_updated_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "priority",
            "priority,status",
            "priority,status,ticket_type",
            "priority,ticket_type",
            "status",
            "status,ticket_type",
            "ticket_type",
        ]
        | NotGiven = NOT_GIVEN,
        status: Optional[Literal["CLOSED", "IN_PROGRESS", "ON_HOLD", "OPEN"]] | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        ticket_type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Ticket]:
        """
        Returns a list of `Ticket` objects.

        Args:
          account_id: If provided, will only return tickets for this account.

          assignee_ids: If provided, will only return tickets assigned to the assignee_ids; multiple
              assignee_ids can be separated by commas.

          collection_ids: If provided, will only return tickets assigned to the collection_ids; multiple
              collection_ids can be separated by commas.

          completed_after: If provided, will only return tickets completed after this datetime.

          completed_before: If provided, will only return tickets completed before this datetime.

          contact_id: If provided, will only return tickets for this contact.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          due_after: If provided, will only return tickets due after this datetime.

          due_before: If provided, will only return tickets due before this datetime.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          parent_ticket_id: If provided, will only return sub tickets of the parent_ticket_id.

          priority: If provided, will only return tickets of this priority.

              - `URGENT` - URGENT
              - `HIGH` - HIGH
              - `NORMAL` - NORMAL
              - `LOW` - LOW

          project_id: If provided, will only return tickets for this project.

          remote_created_after: If provided, will only return tickets created in the third party platform after
              this datetime.

          remote_created_before: If provided, will only return tickets created in the third party platform before
              this datetime.

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          remote_updated_after: If provided, will only return tickets updated in the third party platform after
              this datetime.

          remote_updated_before: If provided, will only return tickets updated in the third party platform before
              this datetime.

          show_enum_origins: Which fields should be returned in non-normalized form.

          status: If provided, will only return tickets of this status.

              - `OPEN` - OPEN
              - `CLOSED` - CLOSED
              - `IN_PROGRESS` - IN_PROGRESS
              - `ON_HOLD` - ON_HOLD

          tags: If provided, will only return tickets matching the tags; multiple tags can be
              separated by commas.

          ticket_type: If provided, will only return tickets of this type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ticketing/v1/tickets",
            page=SyncPage[Ticket],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "assignee_ids": assignee_ids,
                        "collection_ids": collection_ids,
                        "completed_after": completed_after,
                        "completed_before": completed_before,
                        "contact_id": contact_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "due_after": due_after,
                        "due_before": due_before,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "parent_ticket_id": parent_ticket_id,
                        "priority": priority,
                        "project_id": project_id,
                        "remote_created_after": remote_created_after,
                        "remote_created_before": remote_created_before,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "remote_updated_after": remote_updated_after,
                        "remote_updated_before": remote_updated_before,
                        "show_enum_origins": show_enum_origins,
                        "status": status,
                        "tags": tags,
                        "ticket_type": ticket_type,
                    },
                    ticket_list_params.TicketListParams,
                ),
            ),
            model=Ticket,
        )

    def list_collaborators(
        self,
        parent_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: Literal["teams"] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[FileStorageUser]:
        """
        Returns a list of `User` objects.

        Args:
          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/ticketing/v1/tickets/{parent_id}/collaborators",
            page=SyncPage[FileStorageUser],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "page_size": page_size,
                    },
                    ticket_list_collaborators_params.TicketListCollaboratorsParams,
                ),
            ),
            model=FileStorageUser,
        )

    def list_remote_field_classes(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
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

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ticketing/v1/tickets/remote-field-classes",
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
                        "page_size": page_size,
                    },
                    ticket_list_remote_field_classes_params.TicketListRemoteFieldClassesParams,
                ),
            ),
            model=shared.RemoteFieldClass,
        )


class AsyncTickets(AsyncAPIResource):
    meta: AsyncMeta

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.meta = AsyncMeta(client)

    async def create(
        self,
        *,
        model: ticket_create_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> TicketResponse:
        """
        Creates a `Ticket` object with the given values.

        Args:
          model: # The Ticket Object

              ### Description

              The `Ticket` object is used to represent a ticket or a task within a system.

              ### Usage Example

              TODO

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ticketing/v1/tickets",
            body=maybe_transform({"model": model}, ticket_create_params.TicketCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        expand: Literal[
            "account",
            "account,contact",
            "account,contact,creator",
            "account,contact,creator,parent_ticket",
            "account,contact,parent_ticket",
            "account,creator",
            "account,creator,parent_ticket",
            "account,parent_ticket",
            "assignees",
            "assignees,account",
            "assignees,account,contact",
            "assignees,account,contact,creator",
            "assignees,account,contact,creator,parent_ticket",
            "assignees,account,contact,parent_ticket",
            "assignees,account,creator",
            "assignees,account,creator,parent_ticket",
            "assignees,account,parent_ticket",
            "assignees,collections",
            "assignees,collections,account",
            "assignees,collections,account,contact",
            "assignees,collections,account,contact,creator",
            "assignees,collections,account,contact,creator,parent_ticket",
            "assignees,collections,account,contact,parent_ticket",
            "assignees,collections,account,creator",
            "assignees,collections,account,creator,parent_ticket",
            "assignees,collections,account,parent_ticket",
            "assignees,collections,contact",
            "assignees,collections,contact,creator",
            "assignees,collections,contact,creator,parent_ticket",
            "assignees,collections,contact,parent_ticket",
            "assignees,collections,creator",
            "assignees,collections,creator,parent_ticket",
            "assignees,collections,parent_ticket",
            "assignees,collections,project",
            "assignees,collections,project,account",
            "assignees,collections,project,account,contact",
            "assignees,collections,project,account,contact,creator",
            "assignees,collections,project,account,contact,creator,parent_ticket",
            "assignees,collections,project,account,contact,parent_ticket",
            "assignees,collections,project,account,creator",
            "assignees,collections,project,account,creator,parent_ticket",
            "assignees,collections,project,account,parent_ticket",
            "assignees,collections,project,contact",
            "assignees,collections,project,contact,creator",
            "assignees,collections,project,contact,creator,parent_ticket",
            "assignees,collections,project,contact,parent_ticket",
            "assignees,collections,project,creator",
            "assignees,collections,project,creator,parent_ticket",
            "assignees,collections,project,parent_ticket",
            "assignees,contact",
            "assignees,contact,creator",
            "assignees,contact,creator,parent_ticket",
            "assignees,contact,parent_ticket",
            "assignees,creator",
            "assignees,creator,parent_ticket",
            "assignees,parent_ticket",
            "assignees,project",
            "assignees,project,account",
            "assignees,project,account,contact",
            "assignees,project,account,contact,creator",
            "assignees,project,account,contact,creator,parent_ticket",
            "assignees,project,account,contact,parent_ticket",
            "assignees,project,account,creator",
            "assignees,project,account,creator,parent_ticket",
            "assignees,project,account,parent_ticket",
            "assignees,project,contact",
            "assignees,project,contact,creator",
            "assignees,project,contact,creator,parent_ticket",
            "assignees,project,contact,parent_ticket",
            "assignees,project,creator",
            "assignees,project,creator,parent_ticket",
            "assignees,project,parent_ticket",
            "attachments",
            "attachments,account",
            "attachments,account,contact",
            "attachments,account,contact,creator",
            "attachments,account,contact,creator,parent_ticket",
            "attachments,account,contact,parent_ticket",
            "attachments,account,creator",
            "attachments,account,creator,parent_ticket",
            "attachments,account,parent_ticket",
            "attachments,assignees",
            "attachments,assignees,account",
            "attachments,assignees,account,contact",
            "attachments,assignees,account,contact,creator",
            "attachments,assignees,account,contact,creator,parent_ticket",
            "attachments,assignees,account,contact,parent_ticket",
            "attachments,assignees,account,creator",
            "attachments,assignees,account,creator,parent_ticket",
            "attachments,assignees,account,parent_ticket",
            "attachments,assignees,collections",
            "attachments,assignees,collections,account",
            "attachments,assignees,collections,account,contact",
            "attachments,assignees,collections,account,contact,creator",
            "attachments,assignees,collections,account,contact,creator,parent_ticket",
            "attachments,assignees,collections,account,contact,parent_ticket",
            "attachments,assignees,collections,account,creator",
            "attachments,assignees,collections,account,creator,parent_ticket",
            "attachments,assignees,collections,account,parent_ticket",
            "attachments,assignees,collections,contact",
            "attachments,assignees,collections,contact,creator",
            "attachments,assignees,collections,contact,creator,parent_ticket",
            "attachments,assignees,collections,contact,parent_ticket",
            "attachments,assignees,collections,creator",
            "attachments,assignees,collections,creator,parent_ticket",
            "attachments,assignees,collections,parent_ticket",
            "attachments,assignees,collections,project",
            "attachments,assignees,collections,project,account",
            "attachments,assignees,collections,project,account,contact",
            "attachments,assignees,collections,project,account,contact,creator",
            "attachments,assignees,collections,project,account,contact,creator,parent_ticket",
            "attachments,assignees,collections,project,account,contact,parent_ticket",
            "attachments,assignees,collections,project,account,creator",
            "attachments,assignees,collections,project,account,creator,parent_ticket",
            "attachments,assignees,collections,project,account,parent_ticket",
            "attachments,assignees,collections,project,contact",
            "attachments,assignees,collections,project,contact,creator",
            "attachments,assignees,collections,project,contact,creator,parent_ticket",
            "attachments,assignees,collections,project,contact,parent_ticket",
            "attachments,assignees,collections,project,creator",
            "attachments,assignees,collections,project,creator,parent_ticket",
            "attachments,assignees,collections,project,parent_ticket",
            "attachments,assignees,contact",
            "attachments,assignees,contact,creator",
            "attachments,assignees,contact,creator,parent_ticket",
            "attachments,assignees,contact,parent_ticket",
            "attachments,assignees,creator",
            "attachments,assignees,creator,parent_ticket",
            "attachments,assignees,parent_ticket",
            "attachments,assignees,project",
            "attachments,assignees,project,account",
            "attachments,assignees,project,account,contact",
            "attachments,assignees,project,account,contact,creator",
            "attachments,assignees,project,account,contact,creator,parent_ticket",
            "attachments,assignees,project,account,contact,parent_ticket",
            "attachments,assignees,project,account,creator",
            "attachments,assignees,project,account,creator,parent_ticket",
            "attachments,assignees,project,account,parent_ticket",
            "attachments,assignees,project,contact",
            "attachments,assignees,project,contact,creator",
            "attachments,assignees,project,contact,creator,parent_ticket",
            "attachments,assignees,project,contact,parent_ticket",
            "attachments,assignees,project,creator",
            "attachments,assignees,project,creator,parent_ticket",
            "attachments,assignees,project,parent_ticket",
            "attachments,collections",
            "attachments,collections,account",
            "attachments,collections,account,contact",
            "attachments,collections,account,contact,creator",
            "attachments,collections,account,contact,creator,parent_ticket",
            "attachments,collections,account,contact,parent_ticket",
            "attachments,collections,account,creator",
            "attachments,collections,account,creator,parent_ticket",
            "attachments,collections,account,parent_ticket",
            "attachments,collections,contact",
            "attachments,collections,contact,creator",
            "attachments,collections,contact,creator,parent_ticket",
            "attachments,collections,contact,parent_ticket",
            "attachments,collections,creator",
            "attachments,collections,creator,parent_ticket",
            "attachments,collections,parent_ticket",
            "attachments,collections,project",
            "attachments,collections,project,account",
            "attachments,collections,project,account,contact",
            "attachments,collections,project,account,contact,creator",
            "attachments,collections,project,account,contact,creator,parent_ticket",
            "attachments,collections,project,account,contact,parent_ticket",
            "attachments,collections,project,account,creator",
            "attachments,collections,project,account,creator,parent_ticket",
            "attachments,collections,project,account,parent_ticket",
            "attachments,collections,project,contact",
            "attachments,collections,project,contact,creator",
            "attachments,collections,project,contact,creator,parent_ticket",
            "attachments,collections,project,contact,parent_ticket",
            "attachments,collections,project,creator",
            "attachments,collections,project,creator,parent_ticket",
            "attachments,collections,project,parent_ticket",
            "attachments,contact",
            "attachments,contact,creator",
            "attachments,contact,creator,parent_ticket",
            "attachments,contact,parent_ticket",
            "attachments,creator",
            "attachments,creator,parent_ticket",
            "attachments,parent_ticket",
            "attachments,project",
            "attachments,project,account",
            "attachments,project,account,contact",
            "attachments,project,account,contact,creator",
            "attachments,project,account,contact,creator,parent_ticket",
            "attachments,project,account,contact,parent_ticket",
            "attachments,project,account,creator",
            "attachments,project,account,creator,parent_ticket",
            "attachments,project,account,parent_ticket",
            "attachments,project,contact",
            "attachments,project,contact,creator",
            "attachments,project,contact,creator,parent_ticket",
            "attachments,project,contact,parent_ticket",
            "attachments,project,creator",
            "attachments,project,creator,parent_ticket",
            "attachments,project,parent_ticket",
            "collections",
            "collections,account",
            "collections,account,contact",
            "collections,account,contact,creator",
            "collections,account,contact,creator,parent_ticket",
            "collections,account,contact,parent_ticket",
            "collections,account,creator",
            "collections,account,creator,parent_ticket",
            "collections,account,parent_ticket",
            "collections,contact",
            "collections,contact,creator",
            "collections,contact,creator,parent_ticket",
            "collections,contact,parent_ticket",
            "collections,creator",
            "collections,creator,parent_ticket",
            "collections,parent_ticket",
            "collections,project",
            "collections,project,account",
            "collections,project,account,contact",
            "collections,project,account,contact,creator",
            "collections,project,account,contact,creator,parent_ticket",
            "collections,project,account,contact,parent_ticket",
            "collections,project,account,creator",
            "collections,project,account,creator,parent_ticket",
            "collections,project,account,parent_ticket",
            "collections,project,contact",
            "collections,project,contact,creator",
            "collections,project,contact,creator,parent_ticket",
            "collections,project,contact,parent_ticket",
            "collections,project,creator",
            "collections,project,creator,parent_ticket",
            "collections,project,parent_ticket",
            "contact",
            "contact,creator",
            "contact,creator,parent_ticket",
            "contact,parent_ticket",
            "creator",
            "creator,parent_ticket",
            "parent_ticket",
            "project",
            "project,account",
            "project,account,contact",
            "project,account,contact,creator",
            "project,account,contact,creator,parent_ticket",
            "project,account,contact,parent_ticket",
            "project,account,creator",
            "project,account,creator,parent_ticket",
            "project,account,parent_ticket",
            "project,contact",
            "project,contact,creator",
            "project,contact,creator,parent_ticket",
            "project,contact,parent_ticket",
            "project,creator",
            "project,creator,parent_ticket",
            "project,parent_ticket",
        ]
        | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "priority",
            "priority,status",
            "priority,status,ticket_type",
            "priority,ticket_type",
            "status",
            "status,ticket_type",
            "ticket_type",
        ]
        | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "priority",
            "priority,status",
            "priority,status,ticket_type",
            "priority,ticket_type",
            "status",
            "status,ticket_type",
            "ticket_type",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Ticket:
        """
        Returns a `Ticket` object with the given `id`.

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
            f"/ticketing/v1/tickets/{id}",
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
                    ticket_retrieve_params.TicketRetrieveParams,
                ),
            ),
            cast_to=Ticket,
        )

    async def update(
        self,
        id: str,
        *,
        model: ticket_update_params.Model,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> TicketResponse:
        """
        Updates a `Ticket` object with the given `id`.

        Args:
          model: # The Ticket Object

              ### Description

              The `Ticket` object is used to represent a ticket or a task within a system.

              ### Usage Example

              TODO

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/ticketing/v1/tickets/{id}",
            body=maybe_transform({"model": model}, ticket_update_params.TicketUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TicketResponse,
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        assignee_ids: str | NotGiven = NOT_GIVEN,
        collection_ids: str | NotGiven = NOT_GIVEN,
        completed_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        completed_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        contact_id: str | NotGiven = NOT_GIVEN,
        created_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        created_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        due_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        due_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        expand: Literal[
            "account",
            "account,contact",
            "account,contact,creator",
            "account,contact,creator,parent_ticket",
            "account,contact,parent_ticket",
            "account,creator",
            "account,creator,parent_ticket",
            "account,parent_ticket",
            "assignees",
            "assignees,account",
            "assignees,account,contact",
            "assignees,account,contact,creator",
            "assignees,account,contact,creator,parent_ticket",
            "assignees,account,contact,parent_ticket",
            "assignees,account,creator",
            "assignees,account,creator,parent_ticket",
            "assignees,account,parent_ticket",
            "assignees,collections",
            "assignees,collections,account",
            "assignees,collections,account,contact",
            "assignees,collections,account,contact,creator",
            "assignees,collections,account,contact,creator,parent_ticket",
            "assignees,collections,account,contact,parent_ticket",
            "assignees,collections,account,creator",
            "assignees,collections,account,creator,parent_ticket",
            "assignees,collections,account,parent_ticket",
            "assignees,collections,contact",
            "assignees,collections,contact,creator",
            "assignees,collections,contact,creator,parent_ticket",
            "assignees,collections,contact,parent_ticket",
            "assignees,collections,creator",
            "assignees,collections,creator,parent_ticket",
            "assignees,collections,parent_ticket",
            "assignees,collections,project",
            "assignees,collections,project,account",
            "assignees,collections,project,account,contact",
            "assignees,collections,project,account,contact,creator",
            "assignees,collections,project,account,contact,creator,parent_ticket",
            "assignees,collections,project,account,contact,parent_ticket",
            "assignees,collections,project,account,creator",
            "assignees,collections,project,account,creator,parent_ticket",
            "assignees,collections,project,account,parent_ticket",
            "assignees,collections,project,contact",
            "assignees,collections,project,contact,creator",
            "assignees,collections,project,contact,creator,parent_ticket",
            "assignees,collections,project,contact,parent_ticket",
            "assignees,collections,project,creator",
            "assignees,collections,project,creator,parent_ticket",
            "assignees,collections,project,parent_ticket",
            "assignees,contact",
            "assignees,contact,creator",
            "assignees,contact,creator,parent_ticket",
            "assignees,contact,parent_ticket",
            "assignees,creator",
            "assignees,creator,parent_ticket",
            "assignees,parent_ticket",
            "assignees,project",
            "assignees,project,account",
            "assignees,project,account,contact",
            "assignees,project,account,contact,creator",
            "assignees,project,account,contact,creator,parent_ticket",
            "assignees,project,account,contact,parent_ticket",
            "assignees,project,account,creator",
            "assignees,project,account,creator,parent_ticket",
            "assignees,project,account,parent_ticket",
            "assignees,project,contact",
            "assignees,project,contact,creator",
            "assignees,project,contact,creator,parent_ticket",
            "assignees,project,contact,parent_ticket",
            "assignees,project,creator",
            "assignees,project,creator,parent_ticket",
            "assignees,project,parent_ticket",
            "attachments",
            "attachments,account",
            "attachments,account,contact",
            "attachments,account,contact,creator",
            "attachments,account,contact,creator,parent_ticket",
            "attachments,account,contact,parent_ticket",
            "attachments,account,creator",
            "attachments,account,creator,parent_ticket",
            "attachments,account,parent_ticket",
            "attachments,assignees",
            "attachments,assignees,account",
            "attachments,assignees,account,contact",
            "attachments,assignees,account,contact,creator",
            "attachments,assignees,account,contact,creator,parent_ticket",
            "attachments,assignees,account,contact,parent_ticket",
            "attachments,assignees,account,creator",
            "attachments,assignees,account,creator,parent_ticket",
            "attachments,assignees,account,parent_ticket",
            "attachments,assignees,collections",
            "attachments,assignees,collections,account",
            "attachments,assignees,collections,account,contact",
            "attachments,assignees,collections,account,contact,creator",
            "attachments,assignees,collections,account,contact,creator,parent_ticket",
            "attachments,assignees,collections,account,contact,parent_ticket",
            "attachments,assignees,collections,account,creator",
            "attachments,assignees,collections,account,creator,parent_ticket",
            "attachments,assignees,collections,account,parent_ticket",
            "attachments,assignees,collections,contact",
            "attachments,assignees,collections,contact,creator",
            "attachments,assignees,collections,contact,creator,parent_ticket",
            "attachments,assignees,collections,contact,parent_ticket",
            "attachments,assignees,collections,creator",
            "attachments,assignees,collections,creator,parent_ticket",
            "attachments,assignees,collections,parent_ticket",
            "attachments,assignees,collections,project",
            "attachments,assignees,collections,project,account",
            "attachments,assignees,collections,project,account,contact",
            "attachments,assignees,collections,project,account,contact,creator",
            "attachments,assignees,collections,project,account,contact,creator,parent_ticket",
            "attachments,assignees,collections,project,account,contact,parent_ticket",
            "attachments,assignees,collections,project,account,creator",
            "attachments,assignees,collections,project,account,creator,parent_ticket",
            "attachments,assignees,collections,project,account,parent_ticket",
            "attachments,assignees,collections,project,contact",
            "attachments,assignees,collections,project,contact,creator",
            "attachments,assignees,collections,project,contact,creator,parent_ticket",
            "attachments,assignees,collections,project,contact,parent_ticket",
            "attachments,assignees,collections,project,creator",
            "attachments,assignees,collections,project,creator,parent_ticket",
            "attachments,assignees,collections,project,parent_ticket",
            "attachments,assignees,contact",
            "attachments,assignees,contact,creator",
            "attachments,assignees,contact,creator,parent_ticket",
            "attachments,assignees,contact,parent_ticket",
            "attachments,assignees,creator",
            "attachments,assignees,creator,parent_ticket",
            "attachments,assignees,parent_ticket",
            "attachments,assignees,project",
            "attachments,assignees,project,account",
            "attachments,assignees,project,account,contact",
            "attachments,assignees,project,account,contact,creator",
            "attachments,assignees,project,account,contact,creator,parent_ticket",
            "attachments,assignees,project,account,contact,parent_ticket",
            "attachments,assignees,project,account,creator",
            "attachments,assignees,project,account,creator,parent_ticket",
            "attachments,assignees,project,account,parent_ticket",
            "attachments,assignees,project,contact",
            "attachments,assignees,project,contact,creator",
            "attachments,assignees,project,contact,creator,parent_ticket",
            "attachments,assignees,project,contact,parent_ticket",
            "attachments,assignees,project,creator",
            "attachments,assignees,project,creator,parent_ticket",
            "attachments,assignees,project,parent_ticket",
            "attachments,collections",
            "attachments,collections,account",
            "attachments,collections,account,contact",
            "attachments,collections,account,contact,creator",
            "attachments,collections,account,contact,creator,parent_ticket",
            "attachments,collections,account,contact,parent_ticket",
            "attachments,collections,account,creator",
            "attachments,collections,account,creator,parent_ticket",
            "attachments,collections,account,parent_ticket",
            "attachments,collections,contact",
            "attachments,collections,contact,creator",
            "attachments,collections,contact,creator,parent_ticket",
            "attachments,collections,contact,parent_ticket",
            "attachments,collections,creator",
            "attachments,collections,creator,parent_ticket",
            "attachments,collections,parent_ticket",
            "attachments,collections,project",
            "attachments,collections,project,account",
            "attachments,collections,project,account,contact",
            "attachments,collections,project,account,contact,creator",
            "attachments,collections,project,account,contact,creator,parent_ticket",
            "attachments,collections,project,account,contact,parent_ticket",
            "attachments,collections,project,account,creator",
            "attachments,collections,project,account,creator,parent_ticket",
            "attachments,collections,project,account,parent_ticket",
            "attachments,collections,project,contact",
            "attachments,collections,project,contact,creator",
            "attachments,collections,project,contact,creator,parent_ticket",
            "attachments,collections,project,contact,parent_ticket",
            "attachments,collections,project,creator",
            "attachments,collections,project,creator,parent_ticket",
            "attachments,collections,project,parent_ticket",
            "attachments,contact",
            "attachments,contact,creator",
            "attachments,contact,creator,parent_ticket",
            "attachments,contact,parent_ticket",
            "attachments,creator",
            "attachments,creator,parent_ticket",
            "attachments,parent_ticket",
            "attachments,project",
            "attachments,project,account",
            "attachments,project,account,contact",
            "attachments,project,account,contact,creator",
            "attachments,project,account,contact,creator,parent_ticket",
            "attachments,project,account,contact,parent_ticket",
            "attachments,project,account,creator",
            "attachments,project,account,creator,parent_ticket",
            "attachments,project,account,parent_ticket",
            "attachments,project,contact",
            "attachments,project,contact,creator",
            "attachments,project,contact,creator,parent_ticket",
            "attachments,project,contact,parent_ticket",
            "attachments,project,creator",
            "attachments,project,creator,parent_ticket",
            "attachments,project,parent_ticket",
            "collections",
            "collections,account",
            "collections,account,contact",
            "collections,account,contact,creator",
            "collections,account,contact,creator,parent_ticket",
            "collections,account,contact,parent_ticket",
            "collections,account,creator",
            "collections,account,creator,parent_ticket",
            "collections,account,parent_ticket",
            "collections,contact",
            "collections,contact,creator",
            "collections,contact,creator,parent_ticket",
            "collections,contact,parent_ticket",
            "collections,creator",
            "collections,creator,parent_ticket",
            "collections,parent_ticket",
            "collections,project",
            "collections,project,account",
            "collections,project,account,contact",
            "collections,project,account,contact,creator",
            "collections,project,account,contact,creator,parent_ticket",
            "collections,project,account,contact,parent_ticket",
            "collections,project,account,creator",
            "collections,project,account,creator,parent_ticket",
            "collections,project,account,parent_ticket",
            "collections,project,contact",
            "collections,project,contact,creator",
            "collections,project,contact,creator,parent_ticket",
            "collections,project,contact,parent_ticket",
            "collections,project,creator",
            "collections,project,creator,parent_ticket",
            "collections,project,parent_ticket",
            "contact",
            "contact,creator",
            "contact,creator,parent_ticket",
            "contact,parent_ticket",
            "creator",
            "creator,parent_ticket",
            "parent_ticket",
            "project",
            "project,account",
            "project,account,contact",
            "project,account,contact,creator",
            "project,account,contact,creator,parent_ticket",
            "project,account,contact,parent_ticket",
            "project,account,creator",
            "project,account,creator,parent_ticket",
            "project,account,parent_ticket",
            "project,contact",
            "project,contact,creator",
            "project,contact,creator,parent_ticket",
            "project,contact,parent_ticket",
            "project,creator",
            "project,creator,parent_ticket",
            "project,parent_ticket",
        ]
        | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        include_remote_fields: bool | NotGiven = NOT_GIVEN,
        modified_after: Union[str, datetime] | NotGiven = NOT_GIVEN,
        modified_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        parent_ticket_id: str | NotGiven = NOT_GIVEN,
        priority: Optional[Literal["HIGH", "LOW", "NORMAL", "URGENT"]] | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        remote_created_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        remote_created_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        remote_fields: Literal[
            "priority",
            "priority,status",
            "priority,status,ticket_type",
            "priority,ticket_type",
            "status",
            "status,ticket_type",
            "ticket_type",
        ]
        | NotGiven = NOT_GIVEN,
        remote_id: Optional[str] | NotGiven = NOT_GIVEN,
        remote_updated_after: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        remote_updated_before: Optional[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        show_enum_origins: Literal[
            "priority",
            "priority,status",
            "priority,status,ticket_type",
            "priority,ticket_type",
            "status",
            "status,ticket_type",
            "ticket_type",
        ]
        | NotGiven = NOT_GIVEN,
        status: Optional[Literal["CLOSED", "IN_PROGRESS", "ON_HOLD", "OPEN"]] | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        ticket_type: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Ticket, AsyncPage[Ticket]]:
        """
        Returns a list of `Ticket` objects.

        Args:
          account_id: If provided, will only return tickets for this account.

          assignee_ids: If provided, will only return tickets assigned to the assignee_ids; multiple
              assignee_ids can be separated by commas.

          collection_ids: If provided, will only return tickets assigned to the collection_ids; multiple
              collection_ids can be separated by commas.

          completed_after: If provided, will only return tickets completed after this datetime.

          completed_before: If provided, will only return tickets completed before this datetime.

          contact_id: If provided, will only return tickets for this contact.

          created_after: If provided, will only return objects created after this datetime.

          created_before: If provided, will only return objects created before this datetime.

          cursor: The pagination cursor value.

          due_after: If provided, will only return tickets due after this datetime.

          due_before: If provided, will only return tickets due before this datetime.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          include_remote_fields: Whether to include all remote fields, including fields that Merge did not map to
              common models, in a normalized format.

          modified_after: If provided, will only return objects modified after this datetime.

          modified_before: If provided, will only return objects modified before this datetime.

          page_size: Number of results to return per page.

          parent_ticket_id: If provided, will only return sub tickets of the parent_ticket_id.

          priority: If provided, will only return tickets of this priority.

              - `URGENT` - URGENT
              - `HIGH` - HIGH
              - `NORMAL` - NORMAL
              - `LOW` - LOW

          project_id: If provided, will only return tickets for this project.

          remote_created_after: If provided, will only return tickets created in the third party platform after
              this datetime.

          remote_created_before: If provided, will only return tickets created in the third party platform before
              this datetime.

          remote_fields: Deprecated. Use show_enum_origins.

          remote_id: The API provider's ID for the given object.

          remote_updated_after: If provided, will only return tickets updated in the third party platform after
              this datetime.

          remote_updated_before: If provided, will only return tickets updated in the third party platform before
              this datetime.

          show_enum_origins: Which fields should be returned in non-normalized form.

          status: If provided, will only return tickets of this status.

              - `OPEN` - OPEN
              - `CLOSED` - CLOSED
              - `IN_PROGRESS` - IN_PROGRESS
              - `ON_HOLD` - ON_HOLD

          tags: If provided, will only return tickets matching the tags; multiple tags can be
              separated by commas.

          ticket_type: If provided, will only return tickets of this type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ticketing/v1/tickets",
            page=AsyncPage[Ticket],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "assignee_ids": assignee_ids,
                        "collection_ids": collection_ids,
                        "completed_after": completed_after,
                        "completed_before": completed_before,
                        "contact_id": contact_id,
                        "created_after": created_after,
                        "created_before": created_before,
                        "cursor": cursor,
                        "due_after": due_after,
                        "due_before": due_before,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "include_remote_fields": include_remote_fields,
                        "modified_after": modified_after,
                        "modified_before": modified_before,
                        "page_size": page_size,
                        "parent_ticket_id": parent_ticket_id,
                        "priority": priority,
                        "project_id": project_id,
                        "remote_created_after": remote_created_after,
                        "remote_created_before": remote_created_before,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "remote_updated_after": remote_updated_after,
                        "remote_updated_before": remote_updated_before,
                        "show_enum_origins": show_enum_origins,
                        "status": status,
                        "tags": tags,
                        "ticket_type": ticket_type,
                    },
                    ticket_list_params.TicketListParams,
                ),
            ),
            model=Ticket,
        )

    def list_collaborators(
        self,
        parent_id: str,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        expand: Literal["teams"] | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[FileStorageUser, AsyncPage[FileStorageUser]]:
        """
        Returns a list of `User` objects.

        Args:
          cursor: The pagination cursor value.

          expand: Which relations should be returned in expanded form. Multiple relation names
              should be comma separated without spaces.

          include_deleted_data: Whether to include data that was marked as deleted by third party webhooks.

          include_remote_data: Whether to include the original data Merge fetched from the third-party to
              produce these models.

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/ticketing/v1/tickets/{parent_id}/collaborators",
            page=AsyncPage[FileStorageUser],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "page_size": page_size,
                    },
                    ticket_list_collaborators_params.TicketListCollaboratorsParams,
                ),
            ),
            model=FileStorageUser,
        )

    def list_remote_field_classes(
        self,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        include_deleted_data: bool | NotGiven = NOT_GIVEN,
        include_remote_data: bool | NotGiven = NOT_GIVEN,
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

          page_size: Number of results to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ticketing/v1/tickets/remote-field-classes",
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
                        "page_size": page_size,
                    },
                    ticket_list_remote_field_classes_params.TicketListRemoteFieldClassesParams,
                ),
            ),
            model=shared.RemoteFieldClass,
        )
