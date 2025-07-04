# This file was auto-generated by Fern from our API Definition.

import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ...types.available_actions import AvailableActions
from .raw_client import AsyncRawAvailableActionsClient, RawAvailableActionsClient


class AvailableActionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAvailableActionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAvailableActionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAvailableActionsClient
        """
        return self._raw_client

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
        _response = self._raw_client.retrieve(request_options=request_options)
        return _response.data


class AsyncAvailableActionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAvailableActionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAvailableActionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAvailableActionsClient
        """
        return self._raw_client

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
        _response = await self._raw_client.retrieve(request_options=request_options)
        return _response.data
