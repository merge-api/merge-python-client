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
from ...types.meta_response import MetaResponse
from ...types.paginated_time_off_list import PaginatedTimeOffList
from ...types.time_off import TimeOff
from ...types.time_off_request import TimeOffRequest
from ...types.time_off_response import TimeOffResponse
from .types.time_off_list_request_expand import TimeOffListRequestExpand
from .types.time_off_list_request_remote_fields import TimeOffListRequestRemoteFields
from .types.time_off_list_request_request_type import TimeOffListRequestRequestType
from .types.time_off_list_request_show_enum_origins import TimeOffListRequestShowEnumOrigins
from .types.time_off_list_request_status import TimeOffListRequestStatus
from .types.time_off_retrieve_request_expand import TimeOffRetrieveRequestExpand
from .types.time_off_retrieve_request_remote_fields import TimeOffRetrieveRequestRemoteFields
from .types.time_off_retrieve_request_show_enum_origins import TimeOffRetrieveRequestShowEnumOrigins

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TimeOffClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        approver_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        ended_after: typing.Optional[dt.datetime] = None,
        ended_before: typing.Optional[dt.datetime] = None,
        expand: typing.Optional[TimeOffListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[TimeOffListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        request_type: typing.Optional[TimeOffListRequestRequestType] = None,
        show_enum_origins: typing.Optional[TimeOffListRequestShowEnumOrigins] = None,
        started_after: typing.Optional[dt.datetime] = None,
        started_before: typing.Optional[dt.datetime] = None,
        status: typing.Optional[TimeOffListRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTimeOffList:
        """
        Returns a list of `TimeOff` objects.

        Parameters:
            - approver_id: typing.Optional[str]. If provided, will only return time off for this approver.

            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - employee_id: typing.Optional[str]. If provided, will only return time off for this employee.

            - ended_after: typing.Optional[dt.datetime]. If provided, will only return employees that ended after this datetime.

            - ended_before: typing.Optional[dt.datetime]. If provided, will only return time-offs that ended before this datetime.

            - expand: typing.Optional[TimeOffListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_fields: typing.Optional[TimeOffListRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - request_type: typing.Optional[TimeOffListRequestRequestType]. If provided, will only return TimeOff with this request type. Options: ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER', 'BEREAVEMENT')

                                                                            - `VACATION` - VACATION
                                                                            - `SICK` - SICK
                                                                            - `PERSONAL` - PERSONAL
                                                                            - `JURY_DUTY` - JURY_DUTY
                                                                            - `VOLUNTEER` - VOLUNTEER
                                                                            - `BEREAVEMENT` - BEREAVEMENT
            - show_enum_origins: typing.Optional[TimeOffListRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.

            - started_after: typing.Optional[dt.datetime]. If provided, will only return time-offs that started after this datetime.

            - started_before: typing.Optional[dt.datetime]. If provided, will only return time-offs that started before this datetime.

            - status: typing.Optional[TimeOffListRequestStatus]. If provided, will only return TimeOff with this status. Options: ('REQUESTED', 'APPROVED', 'DECLINED', 'CANCELLED', 'DELETED')

                                                                 - `REQUESTED` - REQUESTED
                                                                 - `APPROVED` - APPROVED
                                                                 - `DECLINED` - DECLINED
                                                                 - `CANCELLED` - CANCELLED
                                                                 - `DELETED` - DELETED
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import Merge
        from merge.resources.hris import (
            TimeOffListRequestExpand,
            TimeOffListRequestRemoteFields,
            TimeOffListRequestRequestType,
            TimeOffListRequestShowEnumOrigins,
            TimeOffListRequestStatus,
        )

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.time_off.list(
            expand=TimeOffListRequestExpand.APPROVER,
            remote_fields=TimeOffListRequestRemoteFields.REQUEST_TYPE,
            request_type=TimeOffListRequestRequestType.BEREAVEMENT,
            show_enum_origins=TimeOffListRequestShowEnumOrigins.REQUEST_TYPE,
            status=TimeOffListRequestStatus.APPROVED,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/time-off"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "approver_id": approver_id,
                        "created_after": serialize_datetime(created_after) if created_after is not None else None,
                        "created_before": serialize_datetime(created_before) if created_before is not None else None,
                        "cursor": cursor,
                        "employee_id": employee_id,
                        "ended_after": serialize_datetime(ended_after) if ended_after is not None else None,
                        "ended_before": serialize_datetime(ended_before) if ended_before is not None else None,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                        "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "request_type": request_type,
                        "show_enum_origins": show_enum_origins,
                        "started_after": serialize_datetime(started_after) if started_after is not None else None,
                        "started_before": serialize_datetime(started_before) if started_before is not None else None,
                        "status": status,
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
            return pydantic.parse_obj_as(PaginatedTimeOffList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: TimeOffRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TimeOffResponse:
        """
        Creates a `TimeOff` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: TimeOffRequest.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        import datetime

        from merge.client import Merge
        from merge.resources.hris import TimeOffRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.time_off.create(
            model=TimeOffRequest(
                employee_note="Moving into the new apartment Kendall Roy gave me!",
                amount=3.0,
                start_time=datetime.datetime.fromisoformat(
                    "2020-11-10 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2020-11-17 00:00:00+00:00",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/time-off"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "is_debug_mode": is_debug_mode,
                        "run_async": run_async,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder({"model": model})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"model": model}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic.parse_obj_as(TimeOffResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[TimeOffRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[TimeOffRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[TimeOffRetrieveRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TimeOff:
        """
        Returns a `TimeOff` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[TimeOffRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[TimeOffRetrieveRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[TimeOffRetrieveRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import Merge
        from merge.resources.hris import (
            TimeOffRetrieveRequestExpand,
            TimeOffRetrieveRequestRemoteFields,
            TimeOffRetrieveRequestShowEnumOrigins,
        )

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.time_off.retrieve(
            id="string",
            expand=TimeOffRetrieveRequestExpand.APPROVER,
            remote_fields=TimeOffRetrieveRequestRemoteFields.REQUEST_TYPE,
            show_enum_origins=TimeOffRetrieveRequestShowEnumOrigins.REQUEST_TYPE,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/hris/v1/time-off/{id}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "expand": expand,
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
            return pydantic.parse_obj_as(TimeOff, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `TimeOff` POSTs.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.time_off.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/time-off/meta/post"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTimeOffClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        approver_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        ended_after: typing.Optional[dt.datetime] = None,
        ended_before: typing.Optional[dt.datetime] = None,
        expand: typing.Optional[TimeOffListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[TimeOffListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        request_type: typing.Optional[TimeOffListRequestRequestType] = None,
        show_enum_origins: typing.Optional[TimeOffListRequestShowEnumOrigins] = None,
        started_after: typing.Optional[dt.datetime] = None,
        started_before: typing.Optional[dt.datetime] = None,
        status: typing.Optional[TimeOffListRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTimeOffList:
        """
        Returns a list of `TimeOff` objects.

        Parameters:
            - approver_id: typing.Optional[str]. If provided, will only return time off for this approver.

            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - employee_id: typing.Optional[str]. If provided, will only return time off for this employee.

            - ended_after: typing.Optional[dt.datetime]. If provided, will only return employees that ended after this datetime.

            - ended_before: typing.Optional[dt.datetime]. If provided, will only return time-offs that ended before this datetime.

            - expand: typing.Optional[TimeOffListRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_fields: typing.Optional[TimeOffListRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - request_type: typing.Optional[TimeOffListRequestRequestType]. If provided, will only return TimeOff with this request type. Options: ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER', 'BEREAVEMENT')

                                                                            - `VACATION` - VACATION
                                                                            - `SICK` - SICK
                                                                            - `PERSONAL` - PERSONAL
                                                                            - `JURY_DUTY` - JURY_DUTY
                                                                            - `VOLUNTEER` - VOLUNTEER
                                                                            - `BEREAVEMENT` - BEREAVEMENT
            - show_enum_origins: typing.Optional[TimeOffListRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.

            - started_after: typing.Optional[dt.datetime]. If provided, will only return time-offs that started after this datetime.

            - started_before: typing.Optional[dt.datetime]. If provided, will only return time-offs that started before this datetime.

            - status: typing.Optional[TimeOffListRequestStatus]. If provided, will only return TimeOff with this status. Options: ('REQUESTED', 'APPROVED', 'DECLINED', 'CANCELLED', 'DELETED')

                                                                 - `REQUESTED` - REQUESTED
                                                                 - `APPROVED` - APPROVED
                                                                 - `DECLINED` - DECLINED
                                                                 - `CANCELLED` - CANCELLED
                                                                 - `DELETED` - DELETED
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import AsyncMerge
        from merge.resources.hris import (
            TimeOffListRequestExpand,
            TimeOffListRequestRemoteFields,
            TimeOffListRequestRequestType,
            TimeOffListRequestShowEnumOrigins,
            TimeOffListRequestStatus,
        )

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.time_off.list(
            expand=TimeOffListRequestExpand.APPROVER,
            remote_fields=TimeOffListRequestRemoteFields.REQUEST_TYPE,
            request_type=TimeOffListRequestRequestType.BEREAVEMENT,
            show_enum_origins=TimeOffListRequestShowEnumOrigins.REQUEST_TYPE,
            status=TimeOffListRequestStatus.APPROVED,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/time-off"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "approver_id": approver_id,
                        "created_after": serialize_datetime(created_after) if created_after is not None else None,
                        "created_before": serialize_datetime(created_before) if created_before is not None else None,
                        "cursor": cursor,
                        "employee_id": employee_id,
                        "ended_after": serialize_datetime(ended_after) if ended_after is not None else None,
                        "ended_before": serialize_datetime(ended_before) if ended_before is not None else None,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                        "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                        "page_size": page_size,
                        "remote_fields": remote_fields,
                        "remote_id": remote_id,
                        "request_type": request_type,
                        "show_enum_origins": show_enum_origins,
                        "started_after": serialize_datetime(started_after) if started_after is not None else None,
                        "started_before": serialize_datetime(started_before) if started_before is not None else None,
                        "status": status,
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
            return pydantic.parse_obj_as(PaginatedTimeOffList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        model: TimeOffRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TimeOffResponse:
        """
        Creates a `TimeOff` object with the given values.

        Parameters:
            - is_debug_mode: typing.Optional[bool]. Whether to include debug fields (such as log file links) in the response.

            - run_async: typing.Optional[bool]. Whether or not third-party updates should be run asynchronously.

            - model: TimeOffRequest.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        import datetime

        from merge.client import AsyncMerge
        from merge.resources.hris import TimeOffRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.time_off.create(
            model=TimeOffRequest(
                employee_note="Moving into the new apartment Kendall Roy gave me!",
                amount=3.0,
                start_time=datetime.datetime.fromisoformat(
                    "2020-11-10 00:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2020-11-17 00:00:00+00:00",
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/time-off"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "is_debug_mode": is_debug_mode,
                        "run_async": run_async,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            json=jsonable_encoder({"model": model})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"model": model}),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic.parse_obj_as(TimeOffResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[TimeOffRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[TimeOffRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[TimeOffRetrieveRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TimeOff:
        """
        Returns a `TimeOff` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[TimeOffRetrieveRequestExpand]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - remote_fields: typing.Optional[TimeOffRetrieveRequestRemoteFields]. Deprecated. Use show_enum_origins.

            - show_enum_origins: typing.Optional[TimeOffRetrieveRequestShowEnumOrigins]. Which fields should be returned in non-normalized form.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import AsyncMerge
        from merge.resources.hris import (
            TimeOffRetrieveRequestExpand,
            TimeOffRetrieveRequestRemoteFields,
            TimeOffRetrieveRequestShowEnumOrigins,
        )

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.time_off.retrieve(
            id="string",
            expand=TimeOffRetrieveRequestExpand.APPROVER,
            remote_fields=TimeOffRetrieveRequestRemoteFields.REQUEST_TYPE,
            show_enum_origins=TimeOffRetrieveRequestShowEnumOrigins.REQUEST_TYPE,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/hris/v1/time-off/{id}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "expand": expand,
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
            return pydantic.parse_obj_as(TimeOff, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `TimeOff` POSTs.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.time_off.meta_post_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/time-off/meta/post"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
            return pydantic.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
