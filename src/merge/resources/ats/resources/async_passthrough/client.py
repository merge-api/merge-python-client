# This file was auto-generated by Fern from our API Definition.

import typing
from .....core.client_wrapper import SyncClientWrapper
from ...types.data_passthrough_request import DataPassthroughRequest
from .....core.request_options import RequestOptions
from ...types.async_passthrough_reciept import AsyncPassthroughReciept
from .....core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from .....core.api_error import ApiError
from .types.async_passthrough_retrieve_response import AsyncPassthroughRetrieveResponse
from .....core.jsonable_encoder import jsonable_encoder
from .....core.client_wrapper import AsyncClientWrapper

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
        from merge import Merge
        from merge.resources.ats import DataPassthroughRequest, MethodEnum

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.async_passthrough.create(
            request=DataPassthroughRequest(
                method=MethodEnum.GET,
                path="/scooters",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "ats/v1/async-passthrough",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AsyncPassthroughReciept,
                    parse_obj_as(
                        type_=AsyncPassthroughReciept,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self, async_passthrough_receipt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPassthroughRetrieveResponse:
        """
        Retrieves data from earlier async-passthrough POST request

        Parameters
        ----------
        async_passthrough_receipt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPassthroughRetrieveResponse


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.async_passthrough.retrieve(
            async_passthrough_receipt_id="async_passthrough_receipt_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ats/v1/async-passthrough/{jsonable_encoder(async_passthrough_receipt_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AsyncPassthroughRetrieveResponse,
                    parse_obj_as(
                        type_=AsyncPassthroughRetrieveResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
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

        from merge import AsyncMerge
        from merge.resources.ats import DataPassthroughRequest, MethodEnum

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ats.async_passthrough.create(
                request=DataPassthroughRequest(
                    method=MethodEnum.GET,
                    path="/scooters",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ats/v1/async-passthrough",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AsyncPassthroughReciept,
                    parse_obj_as(
                        type_=AsyncPassthroughReciept,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self, async_passthrough_receipt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncPassthroughRetrieveResponse:
        """
        Retrieves data from earlier async-passthrough POST request

        Parameters
        ----------
        async_passthrough_receipt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPassthroughRetrieveResponse


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ats.async_passthrough.retrieve(
                async_passthrough_receipt_id="async_passthrough_receipt_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ats/v1/async-passthrough/{jsonable_encoder(async_passthrough_receipt_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AsyncPassthroughRetrieveResponse,
                    parse_obj_as(
                        type_=AsyncPassthroughRetrieveResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
