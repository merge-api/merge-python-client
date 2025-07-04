# This file was auto-generated by Fern from our API Definition.

import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ...types.data_passthrough_request import DataPassthroughRequest
from ...types.remote_response import RemoteResponse
from .raw_client import AsyncRawPassthroughClient, RawPassthroughClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PassthroughClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPassthroughClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPassthroughClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPassthroughClient
        """
        return self._raw_client

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
        from merge.resources.filestorage import DataPassthroughRequest, MethodEnum

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.filestorage.passthrough.create(
            request=DataPassthroughRequest(
                method=MethodEnum.GET,
                path="/scooters",
            ),
        )
        """
        _response = self._raw_client.create(request=request, request_options=request_options)
        return _response.data


class AsyncPassthroughClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPassthroughClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPassthroughClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPassthroughClient
        """
        return self._raw_client

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
        from merge.resources.filestorage import DataPassthroughRequest, MethodEnum

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.filestorage.passthrough.create(
                request=DataPassthroughRequest(
                    method=MethodEnum.GET,
                    path="/scooters",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(request=request, request_options=request_options)
        return _response.data
