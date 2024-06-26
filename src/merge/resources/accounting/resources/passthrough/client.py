# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from ...types.data_passthrough_request import DataPassthroughRequest
from ...types.remote_response import RemoteResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PassthroughClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self, *, request: DataPassthroughRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteResponse:
        """
        Pull data from an endpoint not currently supported by Merge.

        Parameters
        ----------
        request : DataPassthroughRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteResponse


        Examples
        --------
        from merge.client import Merge
        from merge.resources.accounting import DataPassthroughRequest, MethodEnum

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.passthrough.create(
            request=DataPassthroughRequest(
                method=MethodEnum.GET,
                path="/scooters",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/passthrough", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RemoteResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPassthroughClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self, *, request: DataPassthroughRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteResponse:
        """
        Pull data from an endpoint not currently supported by Merge.

        Parameters
        ----------
        request : DataPassthroughRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteResponse


        Examples
        --------
        from merge.client import AsyncMerge
        from merge.resources.accounting import DataPassthroughRequest, MethodEnum

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.accounting.passthrough.create(
            request=DataPassthroughRequest(
                method=MethodEnum.GET,
                path="/scooters",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/passthrough", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RemoteResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
