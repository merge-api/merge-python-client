# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ...types import shared
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.marketing import link_token_create_params

__all__ = ["LinkTokens", "AsyncLinkTokens"]


class LinkTokens(SyncAPIResource):
    def create(
        self,
        *,
        categories: List[Literal["hris", "ats", "accounting", "ticketing", "crm", "mktg", "filestorage"]],
        end_user_email_address: str,
        end_user_organization_name: str,
        end_user_origin_id: str,
        common_models: List[link_token_create_params.CommonModel] | NotGiven = NOT_GIVEN,
        integration: Optional[str] | NotGiven = NOT_GIVEN,
        link_expiry_mins: int | NotGiven = NOT_GIVEN,
        should_create_magic_link_url: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.LinkToken:
        """
        Creates a link token to be used when linking a new end user.

        Args:
          categories: The integration categories to show in Merge Link.

          end_user_email_address: Your end user's email address. This is purely for identification purposes -
              setting this value will not cause any emails to be sent.

          end_user_organization_name: Your end user's organization.

          end_user_origin_id: This unique identifier typically represents the ID for your end user in your
              product's database. This value must be distinct from other Linked Accounts'
              unique identifiers.

          common_models: An array of objects to specify the models and fields that will be disabled for a
              given Linked Account. Each object uses model_id, enabled_actions, and
              disabled_fields to specify the model, method, and fields that are scoped for a
              given Linked Account.

          integration: The slug of a specific pre-selected integration for this linking flow token. For
              examples of slugs, see https://www.merge.dev/docs/basics/integration-metadata/.

          link_expiry_mins: An integer number of minutes between [30, 720 or 10080 if for a Magic Link URL]
              for how long this token is valid. Defaults to 30.

          should_create_magic_link_url: Whether to generate a Magic Link URL. Defaults to false. For more information on
              Magic Link, see
              https://merge.dev/blog/product/integrations,-fast.-say-hello-to-magic-link/.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/mktg/v1/link-token",
            body=maybe_transform(
                {
                    "end_user_email_address": end_user_email_address,
                    "end_user_organization_name": end_user_organization_name,
                    "end_user_origin_id": end_user_origin_id,
                    "categories": categories,
                    "integration": integration,
                    "link_expiry_mins": link_expiry_mins,
                    "should_create_magic_link_url": should_create_magic_link_url,
                    "common_models": common_models,
                },
                link_token_create_params.LinkTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.LinkToken,
        )


class AsyncLinkTokens(AsyncAPIResource):
    async def create(
        self,
        *,
        categories: List[Literal["hris", "ats", "accounting", "ticketing", "crm", "mktg", "filestorage"]],
        end_user_email_address: str,
        end_user_organization_name: str,
        end_user_origin_id: str,
        common_models: List[link_token_create_params.CommonModel] | NotGiven = NOT_GIVEN,
        integration: Optional[str] | NotGiven = NOT_GIVEN,
        link_expiry_mins: int | NotGiven = NOT_GIVEN,
        should_create_magic_link_url: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> shared.LinkToken:
        """
        Creates a link token to be used when linking a new end user.

        Args:
          categories: The integration categories to show in Merge Link.

          end_user_email_address: Your end user's email address. This is purely for identification purposes -
              setting this value will not cause any emails to be sent.

          end_user_organization_name: Your end user's organization.

          end_user_origin_id: This unique identifier typically represents the ID for your end user in your
              product's database. This value must be distinct from other Linked Accounts'
              unique identifiers.

          common_models: An array of objects to specify the models and fields that will be disabled for a
              given Linked Account. Each object uses model_id, enabled_actions, and
              disabled_fields to specify the model, method, and fields that are scoped for a
              given Linked Account.

          integration: The slug of a specific pre-selected integration for this linking flow token. For
              examples of slugs, see https://www.merge.dev/docs/basics/integration-metadata/.

          link_expiry_mins: An integer number of minutes between [30, 720 or 10080 if for a Magic Link URL]
              for how long this token is valid. Defaults to 30.

          should_create_magic_link_url: Whether to generate a Magic Link URL. Defaults to false. For more information on
              Magic Link, see
              https://merge.dev/blog/product/integrations,-fast.-say-hello-to-magic-link/.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/mktg/v1/link-token",
            body=maybe_transform(
                {
                    "end_user_email_address": end_user_email_address,
                    "end_user_organization_name": end_user_organization_name,
                    "end_user_origin_id": end_user_origin_id,
                    "categories": categories,
                    "integration": integration,
                    "link_expiry_mins": link_expiry_mins,
                    "should_create_magic_link_url": should_create_magic_link_url,
                    "common_models": common_models,
                },
                link_token_create_params.LinkTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=shared.LinkToken,
        )
