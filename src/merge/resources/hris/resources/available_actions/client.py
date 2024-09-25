# This file was auto-generated by Fern from our API Definition.

from .....core.client_wrapper import SyncClientWrapper
import typing
from .....core.request_options import RequestOptions
from ...types.available_actions import AvailableActions
from .....core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper


class AvailableActionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> AvailableActions:
        """
        Returns a list of models and actions available for an account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AvailableActions


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.available_actions.retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/v1/available-actions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AvailableActions,
                    parse_obj_as(
                        type_=AvailableActions,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAvailableActionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> AvailableActions:
        """
        Returns a list of models and actions available for an account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AvailableActions


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.hris.available_actions.retrieve()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/v1/available-actions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AvailableActions,
                    parse_obj_as(
                        type_=AvailableActions,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
