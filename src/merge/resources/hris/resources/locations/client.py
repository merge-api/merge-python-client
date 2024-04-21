# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from .....core.request_options import RequestOptions
from ...types.location import Location
from ...types.paginated_location_list import PaginatedLocationList
from .types.locations_list_request_location_type import LocationsListRequestLocationType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class LocationsClient:
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
        location_type: typing.Optional[LocationsListRequestLocationType] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing.Literal["location_type"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["location_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedLocationList:
        """
        Returns a list of `Location` objects.

        Parameters:
            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - location_type: typing.Optional[LocationsListRequestLocationType]. If provided, will only return locations with this location_type

                                                                                - `HOME` - HOME
                                                                                - `WORK` - WORK
            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_fields: typing.Optional[typing.Literal["location_type"]]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - show_enum_origins: typing.Optional[typing.Literal["location_type"]]. A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.locations.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "hris/v1/locations"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "created_after": serialize_datetime(created_after) if created_after is not None else None,
                        "created_before": serialize_datetime(created_before) if created_before is not None else None,
                        "cursor": cursor,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "location_type": location_type,
                        "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                        "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedLocationList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["location_type"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["location_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Location:
        """
        Returns a `Location` object with the given `id`.

        Parameters:
            - id: str.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[typing.Literal["location_type"]]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[typing.Literal["location_type"]]. A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.locations.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"hris/v1/locations/{id}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "include_remote_data": include_remote_data,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Location, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncLocationsClient:
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
        location_type: typing.Optional[LocationsListRequestLocationType] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing.Literal["location_type"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["location_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedLocationList:
        """
        Returns a list of `Location` objects.

        Parameters:
            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - location_type: typing.Optional[LocationsListRequestLocationType]. If provided, will only return locations with this location_type

                                                                                - `HOME` - HOME
                                                                                - `WORK` - WORK
            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_fields: typing.Optional[typing.Literal["location_type"]]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - show_enum_origins: typing.Optional[typing.Literal["location_type"]]. A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.locations.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "hris/v1/locations"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "created_after": serialize_datetime(created_after) if created_after is not None else None,
                        "created_before": serialize_datetime(created_before) if created_before is not None else None,
                        "cursor": cursor,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "location_type": location_type,
                        "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                        "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "show_enum_origins": show_enum_origins,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedLocationList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["location_type"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["location_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Location:
        """
        Returns a `Location` object with the given `id`.

        Parameters:
            - id: str.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[typing.Literal["location_type"]]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[typing.Literal["location_type"]]. A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.locations.retrieve(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"hris/v1/locations/{id}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "include_remote_data": include_remote_data,
                        "remote_fields": remote_fields,
                        "show_enum_origins": show_enum_origins,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Location, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
