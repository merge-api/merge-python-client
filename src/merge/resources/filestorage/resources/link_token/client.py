# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from ...types.categories_enum import CategoriesEnum
from ...types.common_model_scopes_body_request import CommonModelScopesBodyRequest
from ...types.individual_common_model_scope_deserializer_request import IndividualCommonModelScopeDeserializerRequest
from ...types.link_token import LinkToken

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class LinkTokenClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        end_user_email_address: str,
        end_user_organization_name: str,
        end_user_origin_id: str,
        categories: typing.Sequence[CategoriesEnum],
        integration: typing.Optional[str] = OMIT,
        link_expiry_mins: typing.Optional[int] = OMIT,
        should_create_magic_link_url: typing.Optional[bool] = OMIT,
        common_models: typing.Optional[typing.Sequence[CommonModelScopesBodyRequest]] = OMIT,
        category_common_model_scopes: typing.Optional[
            typing.Dict[str, typing.Optional[typing.Sequence[IndividualCommonModelScopeDeserializerRequest]]]
        ] = OMIT,
        language: typing.Optional[str] = OMIT,
        integration_specific_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> LinkToken:
        """
        Creates a link token to be used when linking a new end user.

        Parameters
        ----------
        end_user_email_address : str
            Your end user's email address. This is purely for identification purposes - setting this value will not cause any emails to be sent.

        end_user_organization_name : str
            Your end user's organization.

        end_user_origin_id : str
            This unique identifier typically represents the ID for your end user in your product's database. This value must be distinct from other Linked Accounts' unique identifiers.

        categories : typing.Sequence[CategoriesEnum]
            The integration categories to show in Merge Link.

        integration : typing.Optional[str]
            The slug of a specific pre-selected integration for this linking flow token. For examples of slugs, see https://docs.merge.dev/guides/merge-link/single-integration/.

        link_expiry_mins : typing.Optional[int]
            An integer number of minutes between [30, 720 or 10080 if for a Magic Link URL] for how long this token is valid. Defaults to 30.

        should_create_magic_link_url : typing.Optional[bool]
            Whether to generate a Magic Link URL. Defaults to false. For more information on Magic Link, see https://merge.dev/blog/integrations-fast-say-hello-to-magic-link.

        common_models : typing.Optional[typing.Sequence[CommonModelScopesBodyRequest]]
            An array of objects to specify the models and fields that will be disabled for a given Linked Account. Each object uses model_id, enabled_actions, and disabled_fields to specify the model, method, and fields that are scoped for a given Linked Account.

        category_common_model_scopes : typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[IndividualCommonModelScopeDeserializerRequest]]]]
            When creating a Link Token, you can set permissions for Common Models that will apply to the account that is going to be linked. Any model or field not specified in link token payload will default to existing settings.

        language : typing.Optional[str]
            The language code for the language to localize Merge Link to.

        integration_specific_config : typing.Optional[typing.Dict[str, typing.Any]]
            A JSON object containing integration-specific configuration options.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkToken


        Examples
        --------
        from merge.client import Merge
        from merge.resources.filestorage import CategoriesEnum

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.filestorage.link_token.create(
            end_user_email_address="example@gmail.com",
            end_user_organization_name="Test Organization",
            end_user_origin_id="12345",
            categories=[CategoriesEnum.HRIS, CategoriesEnum.ATS],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "filestorage/v1/link-token",
            method="POST",
            json={
                "end_user_email_address": end_user_email_address,
                "end_user_organization_name": end_user_organization_name,
                "end_user_origin_id": end_user_origin_id,
                "categories": categories,
                "integration": integration,
                "link_expiry_mins": link_expiry_mins,
                "should_create_magic_link_url": should_create_magic_link_url,
                "common_models": common_models,
                "category_common_model_scopes": category_common_model_scopes,
                "language": language,
                "integration_specific_config": integration_specific_config,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(LinkToken, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncLinkTokenClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        end_user_email_address: str,
        end_user_organization_name: str,
        end_user_origin_id: str,
        categories: typing.Sequence[CategoriesEnum],
        integration: typing.Optional[str] = OMIT,
        link_expiry_mins: typing.Optional[int] = OMIT,
        should_create_magic_link_url: typing.Optional[bool] = OMIT,
        common_models: typing.Optional[typing.Sequence[CommonModelScopesBodyRequest]] = OMIT,
        category_common_model_scopes: typing.Optional[
            typing.Dict[str, typing.Optional[typing.Sequence[IndividualCommonModelScopeDeserializerRequest]]]
        ] = OMIT,
        language: typing.Optional[str] = OMIT,
        integration_specific_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> LinkToken:
        """
        Creates a link token to be used when linking a new end user.

        Parameters
        ----------
        end_user_email_address : str
            Your end user's email address. This is purely for identification purposes - setting this value will not cause any emails to be sent.

        end_user_organization_name : str
            Your end user's organization.

        end_user_origin_id : str
            This unique identifier typically represents the ID for your end user in your product's database. This value must be distinct from other Linked Accounts' unique identifiers.

        categories : typing.Sequence[CategoriesEnum]
            The integration categories to show in Merge Link.

        integration : typing.Optional[str]
            The slug of a specific pre-selected integration for this linking flow token. For examples of slugs, see https://docs.merge.dev/guides/merge-link/single-integration/.

        link_expiry_mins : typing.Optional[int]
            An integer number of minutes between [30, 720 or 10080 if for a Magic Link URL] for how long this token is valid. Defaults to 30.

        should_create_magic_link_url : typing.Optional[bool]
            Whether to generate a Magic Link URL. Defaults to false. For more information on Magic Link, see https://merge.dev/blog/integrations-fast-say-hello-to-magic-link.

        common_models : typing.Optional[typing.Sequence[CommonModelScopesBodyRequest]]
            An array of objects to specify the models and fields that will be disabled for a given Linked Account. Each object uses model_id, enabled_actions, and disabled_fields to specify the model, method, and fields that are scoped for a given Linked Account.

        category_common_model_scopes : typing.Optional[typing.Dict[str, typing.Optional[typing.Sequence[IndividualCommonModelScopeDeserializerRequest]]]]
            When creating a Link Token, you can set permissions for Common Models that will apply to the account that is going to be linked. Any model or field not specified in link token payload will default to existing settings.

        language : typing.Optional[str]
            The language code for the language to localize Merge Link to.

        integration_specific_config : typing.Optional[typing.Dict[str, typing.Any]]
            A JSON object containing integration-specific configuration options.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LinkToken


        Examples
        --------
        from merge.client import AsyncMerge
        from merge.resources.filestorage import CategoriesEnum

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.filestorage.link_token.create(
            end_user_email_address="example@gmail.com",
            end_user_organization_name="Test Organization",
            end_user_origin_id="12345",
            categories=[CategoriesEnum.HRIS, CategoriesEnum.ATS],
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "filestorage/v1/link-token",
            method="POST",
            json={
                "end_user_email_address": end_user_email_address,
                "end_user_organization_name": end_user_organization_name,
                "end_user_origin_id": end_user_origin_id,
                "categories": categories,
                "integration": integration,
                "link_expiry_mins": link_expiry_mins,
                "should_create_magic_link_url": should_create_magic_link_url,
                "common_models": common_models,
                "category_common_model_scopes": category_common_model_scopes,
                "language": language,
                "integration_specific_config": integration_specific_config,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(LinkToken, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
