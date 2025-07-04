# This file was auto-generated by Fern from our API Definition.

import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from .raw_client import AsyncRawDeleteAccountClient, RawDeleteAccountClient


class DeleteAccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeleteAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeleteAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeleteAccountClient
        """
        return self._raw_client

    def delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a linked account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.filestorage.delete_account.delete()
        """
        _response = self._raw_client.delete(request_options=request_options)
        return _response.data


class AsyncDeleteAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeleteAccountClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeleteAccountClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeleteAccountClient
        """
        return self._raw_client

    async def delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a linked account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.filestorage.delete_account.delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(request_options=request_options)
        return _response.data
