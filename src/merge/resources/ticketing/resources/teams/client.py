# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import parse_obj_as
from .....core.request_options import RequestOptions
from ...types.paginated_team_list import PaginatedTeamList
from ...types.team import Team


class TeamsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTeamList:
        """
        Returns a list of `Team` objects.

        Parameters
        ----------
        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        include_deleted_data : typing.Optional[bool]
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedTeamList


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.teams.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "ticketing/v1/teams",
            method="GET",
            params={
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_id": remote_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(PaginatedTeamList, parse_obj_as(type_=PaginatedTeamList, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        include_remote_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Returns a `Team` object with the given `id`.

        Parameters
        ----------
        id : str

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.teams.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ticketing/v1/teams/{jsonable_encoder(id)}",
            method="GET",
            params={"include_remote_data": include_remote_data},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Team, parse_obj_as(type_=Team, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTeamsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTeamList:
        """
        Returns a list of `Team` objects.

        Parameters
        ----------
        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        include_deleted_data : typing.Optional[bool]
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedTeamList


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.teams.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ticketing/v1/teams",
            method="GET",
            params={
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_id": remote_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(PaginatedTeamList, parse_obj_as(type_=PaginatedTeamList, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        include_remote_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Team:
        """
        Returns a `Team` object with the given `id`.

        Parameters
        ----------
        id : str

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Team


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.teams.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ticketing/v1/teams/{jsonable_encoder(id)}",
            method="GET",
            params={"include_remote_data": include_remote_data},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Team, parse_obj_as(type_=Team, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
