# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.http_response import AsyncHttpResponse, HttpResponse
from .....core.jsonable_encoder import jsonable_encoder
from .....core.request_options import RequestOptions
from .....core.unchecked_base_model import construct_type
from ...types.async_passthrough_reciept import AsyncPassthroughReciept
from ...types.data_passthrough_request import DataPassthroughRequest
from .types.async_passthrough_retrieve_response import AsyncPassthroughRetrieveResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawAsyncPassthroughClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self, *, request: DataPassthroughRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AsyncPassthroughReciept]:
        """
        Asynchronously pull data from an endpoint not currently supported by Merge.

        Parameters
        ----------
        request : DataPassthroughRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AsyncPassthroughReciept]

        """
        _response = self._client_wrapper.httpx_client.request(
            "filestorage/v1/async-passthrough",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsyncPassthroughReciept,
                    construct_type(
                        type_=AsyncPassthroughReciept,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve(
        self, async_passthrough_receipt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AsyncPassthroughRetrieveResponse]:
        """
        Retrieves data from earlier async-passthrough POST request

        Parameters
        ----------
        async_passthrough_receipt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AsyncPassthroughRetrieveResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"filestorage/v1/async-passthrough/{jsonable_encoder(async_passthrough_receipt_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsyncPassthroughRetrieveResponse,
                    construct_type(
                        type_=AsyncPassthroughRetrieveResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAsyncPassthroughClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self, *, request: DataPassthroughRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AsyncPassthroughReciept]:
        """
        Asynchronously pull data from an endpoint not currently supported by Merge.

        Parameters
        ----------
        request : DataPassthroughRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AsyncPassthroughReciept]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "filestorage/v1/async-passthrough",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsyncPassthroughReciept,
                    construct_type(
                        type_=AsyncPassthroughReciept,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve(
        self, async_passthrough_receipt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AsyncPassthroughRetrieveResponse]:
        """
        Retrieves data from earlier async-passthrough POST request

        Parameters
        ----------
        async_passthrough_receipt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AsyncPassthroughRetrieveResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"filestorage/v1/async-passthrough/{jsonable_encoder(async_passthrough_receipt_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AsyncPassthroughRetrieveResponse,
                    construct_type(
                        type_=AsyncPassthroughRetrieveResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
