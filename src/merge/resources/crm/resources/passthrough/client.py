# This file was auto-generated by Fern from our API Definition.

import typing
from .....core.client_wrapper import SyncClientWrapper
from ...types.data_passthrough_request import DataPassthroughRequest
from .....core.request_options import RequestOptions
from ...types.remote_response import RemoteResponse
from .....core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper

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
        from merge import Merge
        from merge.resources.crm import DataPassthroughRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.passthrough.create(
            request=DataPassthroughRequest(
                method="GET",
                path="/scooters",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/v1/passthrough",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RemoteResponse,
                    parse_obj_as(
                        type_=RemoteResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
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
        import asyncio

        from merge import AsyncMerge
        from merge.resources.crm import DataPassthroughRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.crm.passthrough.create(
                request=DataPassthroughRequest(
                    method="GET",
                    path="/scooters",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/v1/passthrough",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RemoteResponse,
                    parse_obj_as(
                        type_=RemoteResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
