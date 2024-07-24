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
from ...types.issue import Issue
from ...types.paginated_issue_list import PaginatedIssueList
from .types.issues_list_request_status import IssuesListRequestStatus


class IssuesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        account_token: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        end_user_organization_name: typing.Optional[str] = None,
        first_incident_time_after: typing.Optional[dt.datetime] = None,
        first_incident_time_before: typing.Optional[dt.datetime] = None,
        include_muted: typing.Optional[str] = None,
        integration_name: typing.Optional[str] = None,
        last_incident_time_after: typing.Optional[dt.datetime] = None,
        last_incident_time_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        start_date: typing.Optional[str] = None,
        status: typing.Optional[IssuesListRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedIssueList:
        """
        Gets issues.

        Parameters
        ----------
        account_token : typing.Optional[str]

        cursor : typing.Optional[str]
            The pagination cursor value.

        end_date : typing.Optional[str]
            If included, will only include issues whose most recent action occurred before this time

        end_user_organization_name : typing.Optional[str]

        first_incident_time_after : typing.Optional[dt.datetime]
            If provided, will only return issues whose first incident time was after this datetime.

        first_incident_time_before : typing.Optional[dt.datetime]
            If provided, will only return issues whose first incident time was before this datetime.

        include_muted : typing.Optional[str]
            If true, will include muted issues

        integration_name : typing.Optional[str]

        last_incident_time_after : typing.Optional[dt.datetime]
            If provided, will only return issues whose last incident time was after this datetime.

        last_incident_time_before : typing.Optional[dt.datetime]
            If provided, will only return issues whose last incident time was before this datetime.

        page_size : typing.Optional[int]
            Number of results to return per page.

        start_date : typing.Optional[str]
            If included, will only include issues whose most recent action occurred after this time

        status : typing.Optional[IssuesListRequestStatus]
            Status of the issue. Options: ('ONGOING', 'RESOLVED')

            - `ONGOING` - ONGOING
            - `RESOLVED` - RESOLVED

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedIssueList


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.issues.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/issues",
            method="GET",
            params={
                "account_token": account_token,
                "cursor": cursor,
                "end_date": end_date,
                "end_user_organization_name": end_user_organization_name,
                "first_incident_time_after": serialize_datetime(first_incident_time_after)
                if first_incident_time_after is not None
                else None,
                "first_incident_time_before": serialize_datetime(first_incident_time_before)
                if first_incident_time_before is not None
                else None,
                "include_muted": include_muted,
                "integration_name": integration_name,
                "last_incident_time_after": serialize_datetime(last_incident_time_after)
                if last_incident_time_after is not None
                else None,
                "last_incident_time_before": serialize_datetime(last_incident_time_before)
                if last_incident_time_before is not None
                else None,
                "page_size": page_size,
                "start_date": start_date,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(PaginatedIssueList, parse_obj_as(type_=PaginatedIssueList, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Issue:
        """
        Get a specific issue.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Issue


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.issues.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/v1/issues/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Issue, parse_obj_as(type_=Issue, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncIssuesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        account_token: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        end_user_organization_name: typing.Optional[str] = None,
        first_incident_time_after: typing.Optional[dt.datetime] = None,
        first_incident_time_before: typing.Optional[dt.datetime] = None,
        include_muted: typing.Optional[str] = None,
        integration_name: typing.Optional[str] = None,
        last_incident_time_after: typing.Optional[dt.datetime] = None,
        last_incident_time_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        start_date: typing.Optional[str] = None,
        status: typing.Optional[IssuesListRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedIssueList:
        """
        Gets issues.

        Parameters
        ----------
        account_token : typing.Optional[str]

        cursor : typing.Optional[str]
            The pagination cursor value.

        end_date : typing.Optional[str]
            If included, will only include issues whose most recent action occurred before this time

        end_user_organization_name : typing.Optional[str]

        first_incident_time_after : typing.Optional[dt.datetime]
            If provided, will only return issues whose first incident time was after this datetime.

        first_incident_time_before : typing.Optional[dt.datetime]
            If provided, will only return issues whose first incident time was before this datetime.

        include_muted : typing.Optional[str]
            If true, will include muted issues

        integration_name : typing.Optional[str]

        last_incident_time_after : typing.Optional[dt.datetime]
            If provided, will only return issues whose last incident time was after this datetime.

        last_incident_time_before : typing.Optional[dt.datetime]
            If provided, will only return issues whose last incident time was before this datetime.

        page_size : typing.Optional[int]
            Number of results to return per page.

        start_date : typing.Optional[str]
            If included, will only include issues whose most recent action occurred after this time

        status : typing.Optional[IssuesListRequestStatus]
            Status of the issue. Options: ('ONGOING', 'RESOLVED')

            - `ONGOING` - ONGOING
            - `RESOLVED` - RESOLVED

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedIssueList


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.issues.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/issues",
            method="GET",
            params={
                "account_token": account_token,
                "cursor": cursor,
                "end_date": end_date,
                "end_user_organization_name": end_user_organization_name,
                "first_incident_time_after": serialize_datetime(first_incident_time_after)
                if first_incident_time_after is not None
                else None,
                "first_incident_time_before": serialize_datetime(first_incident_time_before)
                if first_incident_time_before is not None
                else None,
                "include_muted": include_muted,
                "integration_name": integration_name,
                "last_incident_time_after": serialize_datetime(last_incident_time_after)
                if last_incident_time_after is not None
                else None,
                "last_incident_time_before": serialize_datetime(last_incident_time_before)
                if last_incident_time_before is not None
                else None,
                "page_size": page_size,
                "start_date": start_date,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(PaginatedIssueList, parse_obj_as(type_=PaginatedIssueList, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Issue:
        """
        Get a specific issue.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Issue


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.issues.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/v1/issues/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Issue, parse_obj_as(type_=Issue, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
