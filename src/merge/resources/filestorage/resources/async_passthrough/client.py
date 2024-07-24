# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import parse_obj_as
from .....core.request_options import RequestOptions
from ...types.async_passthrough_reciept import AsyncPassthroughReciept
from ...types.data_passthrough_request import DataPassthroughRequest
from ...types.remote_response import RemoteResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AsyncPassthroughClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self, *, request: DataPassthroughRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPassthroughReciept:
        """
        Asynchronously pull data from an endpoint not currently supported by Merge.

        Parameters
        ----------
        request : DataPassthroughRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPassthroughReciept


        Examples
        --------
        from merge.client import Merge
        from merge.resources.filestorage import DataPassthroughRequest, MethodEnum

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.filestorage.async_passthrough.create(
            request=DataPassthroughRequest(
                method=MethodEnum.GET,
                path="/scooters",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "filestorage/v1/async-passthrough", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AsyncPassthroughReciept, parse_obj_as(type_=AsyncPassthroughReciept, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self, async_passthrough_receipt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteResponse:
        """
        Retrieves data from earlier async-passthrough POST request

        Parameters
        ----------
        async_passthrough_receipt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteResponse


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.filestorage.async_passthrough.retrieve(
            async_passthrough_receipt_id="async_passthrough_receipt_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"filestorage/v1/async-passthrough/{jsonable_encoder(async_passthrough_receipt_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(RemoteResponse, parse_obj_as(type_=RemoteResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAsyncPassthroughClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self, *, request: DataPassthroughRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPassthroughReciept:
        """
        Asynchronously pull data from an endpoint not currently supported by Merge.

        Parameters
        ----------
        request : DataPassthroughRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPassthroughReciept


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge
        from merge.resources.filestorage import DataPassthroughRequest, MethodEnum

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.filestorage.async_passthrough.create(
                request=DataPassthroughRequest(
                    method=MethodEnum.GET,
                    path="/scooters",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "filestorage/v1/async-passthrough", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AsyncPassthroughReciept, parse_obj_as(type_=AsyncPassthroughReciept, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self, async_passthrough_receipt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RemoteResponse:
        """
        Retrieves data from earlier async-passthrough POST request

        Parameters
        ----------
        async_passthrough_receipt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RemoteResponse


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.filestorage.async_passthrough.retrieve(
                async_passthrough_receipt_id="async_passthrough_receipt_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"filestorage/v1/async-passthrough/{jsonable_encoder(async_passthrough_receipt_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(RemoteResponse, parse_obj_as(type_=RemoteResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
