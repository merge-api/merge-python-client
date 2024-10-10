# This file was auto-generated by Fern from our API Definition.

import typing
from .....core.client_wrapper import SyncClientWrapper
from .....core.request_options import RequestOptions
from ...types.common_model_scope_api import CommonModelScopeApi
from .....core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from .....core.api_error import ApiError
from ...types.individual_common_model_scope_deserializer_request import IndividualCommonModelScopeDeserializerRequest
from .....core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ScopesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def default_scopes_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommonModelScopeApi:
        """
        Get the default permissions for Merge Common Models and fields across all Linked Accounts of a given category. [Learn more](https://help.merge.dev/en/articles/5950052-common-model-and-field-scopes).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommonModelScopeApi


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.scopes.default_scopes_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "ats/v1/default-scopes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CommonModelScopeApi,
                    parse_obj_as(
                        type_=CommonModelScopeApi,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def linked_account_scopes_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommonModelScopeApi:
        """
        Get all available permissions for Merge Common Models and fields for a single Linked Account. [Learn more](https://help.merge.dev/en/articles/5950052-common-model-and-field-scopes).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommonModelScopeApi


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.scopes.linked_account_scopes_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "ats/v1/linked-account-scopes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CommonModelScopeApi,
                    parse_obj_as(
                        type_=CommonModelScopeApi,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def linked_account_scopes_create(
        self,
        *,
        common_models: typing.Sequence[IndividualCommonModelScopeDeserializerRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommonModelScopeApi:
        """
        Update permissions for any Common Model or field for a single Linked Account. Any Scopes not set in this POST request will inherit the default Scopes. [Learn more](https://help.merge.dev/en/articles/5950052-common-model-and-field-scopes)

        Parameters
        ----------
        common_models : typing.Sequence[IndividualCommonModelScopeDeserializerRequest]
            The common models you want to update the scopes for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommonModelScopeApi


        Examples
        --------
        from merge import Merge
        from merge.resources.ats import (
            IndividualCommonModelScopeDeserializerRequest,
            ModelPermissionDeserializerRequest,
        )

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.scopes.linked_account_scopes_create(
            common_models=[
                IndividualCommonModelScopeDeserializerRequest(
                    model_name="Employee",
                    model_permissions={
                        "READ": ModelPermissionDeserializerRequest(
                            is_enabled=True,
                        ),
                        "WRITE": ModelPermissionDeserializerRequest(
                            is_enabled=False,
                        ),
                    },
                ),
                IndividualCommonModelScopeDeserializerRequest(
                    model_name="Benefit",
                    model_permissions={
                        "WRITE": ModelPermissionDeserializerRequest(
                            is_enabled=False,
                        )
                    },
                ),
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "ats/v1/linked-account-scopes",
            method="POST",
            json={
                "common_models": common_models,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CommonModelScopeApi,
                    parse_obj_as(
                        type_=CommonModelScopeApi,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncScopesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def default_scopes_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommonModelScopeApi:
        """
        Get the default permissions for Merge Common Models and fields across all Linked Accounts of a given category. [Learn more](https://help.merge.dev/en/articles/5950052-common-model-and-field-scopes).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommonModelScopeApi


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ats.scopes.default_scopes_retrieve()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ats/v1/default-scopes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CommonModelScopeApi,
                    parse_obj_as(
                        type_=CommonModelScopeApi,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def linked_account_scopes_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommonModelScopeApi:
        """
        Get all available permissions for Merge Common Models and fields for a single Linked Account. [Learn more](https://help.merge.dev/en/articles/5950052-common-model-and-field-scopes).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommonModelScopeApi


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ats.scopes.linked_account_scopes_retrieve()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ats/v1/linked-account-scopes",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CommonModelScopeApi,
                    parse_obj_as(
                        type_=CommonModelScopeApi,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def linked_account_scopes_create(
        self,
        *,
        common_models: typing.Sequence[IndividualCommonModelScopeDeserializerRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommonModelScopeApi:
        """
        Update permissions for any Common Model or field for a single Linked Account. Any Scopes not set in this POST request will inherit the default Scopes. [Learn more](https://help.merge.dev/en/articles/5950052-common-model-and-field-scopes)

        Parameters
        ----------
        common_models : typing.Sequence[IndividualCommonModelScopeDeserializerRequest]
            The common models you want to update the scopes for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommonModelScopeApi


        Examples
        --------
        import asyncio

        from merge import AsyncMerge
        from merge.resources.ats import (
            IndividualCommonModelScopeDeserializerRequest,
            ModelPermissionDeserializerRequest,
        )

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ats.scopes.linked_account_scopes_create(
                common_models=[
                    IndividualCommonModelScopeDeserializerRequest(
                        model_name="Employee",
                        model_permissions={
                            "READ": ModelPermissionDeserializerRequest(
                                is_enabled=True,
                            ),
                            "WRITE": ModelPermissionDeserializerRequest(
                                is_enabled=False,
                            ),
                        },
                    ),
                    IndividualCommonModelScopeDeserializerRequest(
                        model_name="Benefit",
                        model_permissions={
                            "WRITE": ModelPermissionDeserializerRequest(
                                is_enabled=False,
                            )
                        },
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ats/v1/linked-account-scopes",
            method="POST",
            json={
                "common_models": common_models,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CommonModelScopeApi,
                    parse_obj_as(
                        type_=CommonModelScopeApi,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
