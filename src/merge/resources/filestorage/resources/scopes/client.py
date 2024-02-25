# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from .....core.request_options import RequestOptions
from ...types.common_model_scope_api import CommonModelScopeApi
from ...types.individual_common_model_scope_deserializer_request import IndividualCommonModelScopeDeserializerRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ScopesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def default_scopes_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommonModelScopeApi:
        """
        Get the default permissions for Merge Common Models and fields across all Linked Accounts of a given category. [Learn More](https://help.merge.dev/en/articles/8828211-common-model-and-field-scopes).

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.filestorage.scopes.default_scopes_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/filestorage/v1/default-scopes"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CommonModelScopeApi, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def linked_account_scopes_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommonModelScopeApi:
        """
        Get all available permissions for Merge Common Models and fields for a single Linked Account. [Learn More](https://help.merge.dev/en/articles/8828211-common-model-and-field-scopes).

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.filestorage.scopes.linked_account_scopes_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/filestorage/v1/linked-account-scopes"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CommonModelScopeApi, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def linked_account_scopes_create(
        self,
        *,
        common_models: typing.List[IndividualCommonModelScopeDeserializerRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommonModelScopeApi:
        """
        Update permissions for any Common Model or field for a single Linked Account. Any Scopes not set in this POST request will inherit the default Scopes. [Learn More](https://help.merge.dev/en/articles/8828211-common-model-and-field-scopes)

        Parameters:
            - common_models: typing.List[IndividualCommonModelScopeDeserializerRequest]. The common models you want to update the scopes for

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.filestorage.scopes.linked_account_scopes_create(
            common_models=[],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/filestorage/v1/linked-account-scopes"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"common_models": common_models})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"common_models": common_models}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CommonModelScopeApi, _response.json())  # type: ignore
        try:
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
        Get the default permissions for Merge Common Models and fields across all Linked Accounts of a given category. [Learn More](https://help.merge.dev/en/articles/8828211-common-model-and-field-scopes).

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.filestorage.scopes.default_scopes_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/filestorage/v1/default-scopes"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CommonModelScopeApi, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def linked_account_scopes_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommonModelScopeApi:
        """
        Get all available permissions for Merge Common Models and fields for a single Linked Account. [Learn More](https://help.merge.dev/en/articles/8828211-common-model-and-field-scopes).

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.filestorage.scopes.linked_account_scopes_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/filestorage/v1/linked-account-scopes"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CommonModelScopeApi, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def linked_account_scopes_create(
        self,
        *,
        common_models: typing.List[IndividualCommonModelScopeDeserializerRequest],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommonModelScopeApi:
        """
        Update permissions for any Common Model or field for a single Linked Account. Any Scopes not set in this POST request will inherit the default Scopes. [Learn More](https://help.merge.dev/en/articles/8828211-common-model-and-field-scopes)

        Parameters:
            - common_models: typing.List[IndividualCommonModelScopeDeserializerRequest]. The common models you want to update the scopes for

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.filestorage.scopes.linked_account_scopes_create(
            common_models=[],
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/filestorage/v1/linked-account-scopes"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"common_models": common_models})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"common_models": common_models}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CommonModelScopeApi, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
