# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ...types import shared
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.marketing import linked_account_list_params

__all__ = ["LinkedAccounts", "AsyncLinkedAccounts"]


class LinkedAccounts(SyncAPIResource):
    def list(
        self,
        *,
        category: Optional[Literal["accounting", "ats", "crm", "filestorage", "hris", "mktg", "ticketing"]]
        | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        end_user_email_address: str | NotGiven = NOT_GIVEN,
        end_user_organization_name: str | NotGiven = NOT_GIVEN,
        end_user_origin_id: str | NotGiven = NOT_GIVEN,
        end_user_origin_ids: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        include_duplicates: bool | NotGiven = NOT_GIVEN,
        integration_name: str | NotGiven = NOT_GIVEN,
        is_test_account: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[shared.AccountDetailsAndActions]:
        """
        List linked accounts for your organization.

        Args:
          category: - `hris` - hris
              - `ats` - ats
              - `accounting` - accounting
              - `ticketing` - ticketing
              - `crm` - crm
              - `mktg` - mktg
              - `filestorage` - filestorage

              - `hris` - hris
              - `ats` - ats
              - `accounting` - accounting
              - `ticketing` - ticketing
              - `crm` - crm
              - `mktg` - mktg
              - `filestorage` - filestorage

          cursor: The pagination cursor value.

          end_user_email_address: If provided, will only return linked accounts associated with the given email
              address.

          end_user_organization_name: If provided, will only return linked accounts associated with the given
              organization name.

          end_user_origin_id: If provided, will only return linked accounts associated with the given origin
              ID.

          end_user_origin_ids: Comma-separated list of EndUser origin IDs, making it possible to specify
              multiple EndUsers at once.

          ids: Comma-separated list of LinkedAccount IDs, making it possible to specify
              multiple LinkedAccounts at once.

          include_duplicates: If `true`, will include complete production duplicates of the account specified
              by the `id` query parameter in the response. `id` must be for a complete
              production linked account.

          integration_name: If provided, will only return linked accounts associated with the given
              integration name.

          is_test_account: If included, will only include test linked accounts. If not included, will only
              include non-test linked accounts.

          page_size: Number of results to return per page.

          status: Filter by status. Options: `COMPLETE`, `INCOMPLETE`, `RELINK_NEEDED`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/mktg/v1/linked-accounts",
            page=SyncPage[shared.AccountDetailsAndActions],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "cursor": cursor,
                        "end_user_email_address": end_user_email_address,
                        "end_user_organization_name": end_user_organization_name,
                        "end_user_origin_id": end_user_origin_id,
                        "end_user_origin_ids": end_user_origin_ids,
                        "id": id,
                        "ids": ids,
                        "include_duplicates": include_duplicates,
                        "integration_name": integration_name,
                        "is_test_account": is_test_account,
                        "page_size": page_size,
                        "status": status,
                    },
                    linked_account_list_params.LinkedAccountListParams,
                ),
            ),
            model=shared.AccountDetailsAndActions,
        )

    def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete a linked account."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/mktg/v1/delete-account",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLinkedAccounts(AsyncAPIResource):
    def list(
        self,
        *,
        category: Optional[Literal["accounting", "ats", "crm", "filestorage", "hris", "mktg", "ticketing"]]
        | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        end_user_email_address: str | NotGiven = NOT_GIVEN,
        end_user_organization_name: str | NotGiven = NOT_GIVEN,
        end_user_origin_id: str | NotGiven = NOT_GIVEN,
        end_user_origin_ids: str | NotGiven = NOT_GIVEN,
        id: str | NotGiven = NOT_GIVEN,
        ids: str | NotGiven = NOT_GIVEN,
        include_duplicates: bool | NotGiven = NOT_GIVEN,
        integration_name: str | NotGiven = NOT_GIVEN,
        is_test_account: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[shared.AccountDetailsAndActions, AsyncPage[shared.AccountDetailsAndActions]]:
        """
        List linked accounts for your organization.

        Args:
          category: - `hris` - hris
              - `ats` - ats
              - `accounting` - accounting
              - `ticketing` - ticketing
              - `crm` - crm
              - `mktg` - mktg
              - `filestorage` - filestorage

              - `hris` - hris
              - `ats` - ats
              - `accounting` - accounting
              - `ticketing` - ticketing
              - `crm` - crm
              - `mktg` - mktg
              - `filestorage` - filestorage

          cursor: The pagination cursor value.

          end_user_email_address: If provided, will only return linked accounts associated with the given email
              address.

          end_user_organization_name: If provided, will only return linked accounts associated with the given
              organization name.

          end_user_origin_id: If provided, will only return linked accounts associated with the given origin
              ID.

          end_user_origin_ids: Comma-separated list of EndUser origin IDs, making it possible to specify
              multiple EndUsers at once.

          ids: Comma-separated list of LinkedAccount IDs, making it possible to specify
              multiple LinkedAccounts at once.

          include_duplicates: If `true`, will include complete production duplicates of the account specified
              by the `id` query parameter in the response. `id` must be for a complete
              production linked account.

          integration_name: If provided, will only return linked accounts associated with the given
              integration name.

          is_test_account: If included, will only include test linked accounts. If not included, will only
              include non-test linked accounts.

          page_size: Number of results to return per page.

          status: Filter by status. Options: `COMPLETE`, `INCOMPLETE`, `RELINK_NEEDED`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/mktg/v1/linked-accounts",
            page=AsyncPage[shared.AccountDetailsAndActions],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "cursor": cursor,
                        "end_user_email_address": end_user_email_address,
                        "end_user_organization_name": end_user_organization_name,
                        "end_user_origin_id": end_user_origin_id,
                        "end_user_origin_ids": end_user_origin_ids,
                        "id": id,
                        "ids": ids,
                        "include_duplicates": include_duplicates,
                        "integration_name": integration_name,
                        "is_test_account": is_test_account,
                        "page_size": page_size,
                        "status": status,
                    },
                    linked_account_list_params.LinkedAccountListParams,
                ),
            ),
            model=shared.AccountDetailsAndActions,
        )

    async def delete(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete a linked account."""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/mktg/v1/delete-account",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
