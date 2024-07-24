# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.pydantic_utilities import parse_obj_as
from .....core.request_options import RequestOptions
from ...types.sync_status import SyncStatus


class ForceResyncClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def sync_status_resync_create(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SyncStatus]:
        """
        Force re-sync of all models. This is available for all organizations via the dashboard. Force re-sync is also available programmatically via API for monthly, quarterly, and highest sync frequency customers on the Launch, Professional, or Enterprise plans. Doing so will consume a sync credit for the relevant linked account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SyncStatus]


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.force_resync.sync_status_resync_create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "ticketing/v1/sync-status/resync", method="POST", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.List[SyncStatus], parse_obj_as(type_=typing.List[SyncStatus], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncForceResyncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def sync_status_resync_create(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SyncStatus]:
        """
        Force re-sync of all models. This is available for all organizations via the dashboard. Force re-sync is also available programmatically via API for monthly, quarterly, and highest sync frequency customers on the Launch, Professional, or Enterprise plans. Doing so will consume a sync credit for the relevant linked account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SyncStatus]


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.force_resync.sync_status_resync_create()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ticketing/v1/sync-status/resync", method="POST", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(typing.List[SyncStatus], parse_obj_as(type_=typing.List[SyncStatus], object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
