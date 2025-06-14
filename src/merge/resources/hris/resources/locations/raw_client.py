# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.http_response import AsyncHttpResponse, HttpResponse
from .....core.jsonable_encoder import jsonable_encoder
from .....core.request_options import RequestOptions
from .....core.unchecked_base_model import construct_type
from ...types.location import Location
from ...types.paginated_location_list import PaginatedLocationList
from .types.locations_list_request_location_type import LocationsListRequestLocationType
from .types.locations_list_request_remote_fields import LocationsListRequestRemoteFields
from .types.locations_list_request_show_enum_origins import LocationsListRequestShowEnumOrigins
from .types.locations_retrieve_request_remote_fields import LocationsRetrieveRequestRemoteFields
from .types.locations_retrieve_request_show_enum_origins import LocationsRetrieveRequestShowEnumOrigins


class RawLocationsClient:
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
        include_shell_data: typing.Optional[bool] = None,
        location_type: typing.Optional[LocationsListRequestLocationType] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[LocationsListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[LocationsListRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedLocationList]:
        """
        Returns a list of `Location` objects.

        Parameters
        ----------
        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        location_type : typing.Optional[LocationsListRequestLocationType]
            If provided, will only return locations with this location_type

            * `HOME` - HOME
            * `WORK` - WORK

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_fields : typing.Optional[LocationsListRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[LocationsListRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedLocationList]

        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/v1/locations",
            method="GET",
            params={
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_shell_data": include_shell_data,
                "location_type": location_type,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_fields": remote_fields,
                "remote_id": remote_id,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedLocationList,
                    construct_type(
                        type_=PaginatedLocationList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[LocationsRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[LocationsRetrieveRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Location]:
        """
        Returns a `Location` object with the given `id`.

        Parameters
        ----------
        id : str

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        remote_fields : typing.Optional[LocationsRetrieveRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[LocationsRetrieveRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Location]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"hris/v1/locations/{jsonable_encoder(id)}",
            method="GET",
            params={
                "include_remote_data": include_remote_data,
                "include_shell_data": include_shell_data,
                "remote_fields": remote_fields,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Location,
                    construct_type(
                        type_=Location,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawLocationsClient:
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
        include_shell_data: typing.Optional[bool] = None,
        location_type: typing.Optional[LocationsListRequestLocationType] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[LocationsListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[LocationsListRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedLocationList]:
        """
        Returns a list of `Location` objects.

        Parameters
        ----------
        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        location_type : typing.Optional[LocationsListRequestLocationType]
            If provided, will only return locations with this location_type

            * `HOME` - HOME
            * `WORK` - WORK

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_fields : typing.Optional[LocationsListRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[LocationsListRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedLocationList]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/v1/locations",
            method="GET",
            params={
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_shell_data": include_shell_data,
                "location_type": location_type,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_fields": remote_fields,
                "remote_id": remote_id,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedLocationList,
                    construct_type(
                        type_=PaginatedLocationList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[LocationsRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[LocationsRetrieveRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Location]:
        """
        Returns a `Location` object with the given `id`.

        Parameters
        ----------
        id : str

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        remote_fields : typing.Optional[LocationsRetrieveRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[LocationsRetrieveRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Location]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"hris/v1/locations/{jsonable_encoder(id)}",
            method="GET",
            params={
                "include_remote_data": include_remote_data,
                "include_shell_data": include_shell_data,
                "remote_fields": remote_fields,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Location,
                    construct_type(
                        type_=Location,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
