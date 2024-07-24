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
from ...types.employee import Employee
from ...types.employee_request import EmployeeRequest
from ...types.employee_response import EmployeeResponse
from ...types.meta_response import MetaResponse
from ...types.paginated_employee_list import PaginatedEmployeeList
from .types.employees_list_request_employment_status import EmployeesListRequestEmploymentStatus
from .types.employees_list_request_expand import EmployeesListRequestExpand
from .types.employees_list_request_remote_fields import EmployeesListRequestRemoteFields
from .types.employees_list_request_show_enum_origins import EmployeesListRequestShowEnumOrigins
from .types.employees_retrieve_request_expand import EmployeesRetrieveRequestExpand
from .types.employees_retrieve_request_remote_fields import EmployeesRetrieveRequestRemoteFields
from .types.employees_retrieve_request_show_enum_origins import EmployeesRetrieveRequestShowEnumOrigins
from .types.ignore_common_model_request_reason import IgnoreCommonModelRequestReason

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EmployeesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        display_full_name: typing.Optional[str] = None,
        employment_status: typing.Optional[EmployeesListRequestEmploymentStatus] = None,
        employment_type: typing.Optional[str] = None,
        expand: typing.Optional[EmployeesListRequestExpand] = None,
        first_name: typing.Optional[str] = None,
        groups: typing.Optional[str] = None,
        home_location_id: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_sensitive_fields: typing.Optional[bool] = None,
        job_title: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        manager_id: typing.Optional[str] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        pay_group_id: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        remote_fields: typing.Optional[EmployeesListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[EmployeesListRequestShowEnumOrigins] = None,
        started_after: typing.Optional[dt.datetime] = None,
        started_before: typing.Optional[dt.datetime] = None,
        team_id: typing.Optional[str] = None,
        terminated_after: typing.Optional[dt.datetime] = None,
        terminated_before: typing.Optional[dt.datetime] = None,
        work_email: typing.Optional[str] = None,
        work_location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedEmployeeList:
        """
        Returns a list of `Employee` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return employees for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        display_full_name : typing.Optional[str]
            If provided, will only return employees with this display name.

        employment_status : typing.Optional[EmployeesListRequestEmploymentStatus]
            If provided, will only return employees with this employment status.

            - `ACTIVE` - ACTIVE
            - `PENDING` - PENDING
            - `INACTIVE` - INACTIVE

        employment_type : typing.Optional[str]
            If provided, will only return employees that have an employment of the specified employment_type.

        expand : typing.Optional[EmployeesListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        first_name : typing.Optional[str]
            If provided, will only return employees with this first name.

        groups : typing.Optional[str]
            If provided, will only return employees matching the group ids; multiple groups can be separated by commas.

        home_location_id : typing.Optional[str]
            If provided, will only return employees for this home location.

        include_deleted_data : typing.Optional[bool]
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_sensitive_fields : typing.Optional[bool]
            Whether to include sensitive fields (such as social security numbers) in the response.

        job_title : typing.Optional[str]
            If provided, will only return employees that have an employment of the specified job_title.

        last_name : typing.Optional[str]
            If provided, will only return employees with this last name.

        manager_id : typing.Optional[str]
            If provided, will only return employees for this manager.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        pay_group_id : typing.Optional[str]
            If provided, will only return employees for this pay group

        personal_email : typing.Optional[str]
            If provided, will only return Employees with this personal email

        remote_fields : typing.Optional[EmployeesListRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[EmployeesListRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        started_after : typing.Optional[dt.datetime]
            If provided, will only return employees that started after this datetime.

        started_before : typing.Optional[dt.datetime]
            If provided, will only return employees that started before this datetime.

        team_id : typing.Optional[str]
            If provided, will only return employees for this team.

        terminated_after : typing.Optional[dt.datetime]
            If provided, will only return employees that were terminated after this datetime.

        terminated_before : typing.Optional[dt.datetime]
            If provided, will only return employees that were terminated before this datetime.

        work_email : typing.Optional[str]
            If provided, will only return Employees with this work email

        work_location_id : typing.Optional[str]
            If provided, will only return employees for this location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedEmployeeList


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.employees.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/v1/employees",
            method="GET",
            params={
                "company_id": company_id,
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "display_full_name": display_full_name,
                "employment_status": employment_status,
                "employment_type": employment_type,
                "expand": expand,
                "first_name": first_name,
                "groups": groups,
                "home_location_id": home_location_id,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_sensitive_fields": include_sensitive_fields,
                "job_title": job_title,
                "last_name": last_name,
                "manager_id": manager_id,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "pay_group_id": pay_group_id,
                "personal_email": personal_email,
                "remote_fields": remote_fields,
                "remote_id": remote_id,
                "show_enum_origins": show_enum_origins,
                "started_after": serialize_datetime(started_after) if started_after is not None else None,
                "started_before": serialize_datetime(started_before) if started_before is not None else None,
                "team_id": team_id,
                "terminated_after": serialize_datetime(terminated_after) if terminated_after is not None else None,
                "terminated_before": serialize_datetime(terminated_before) if terminated_before is not None else None,
                "work_email": work_email,
                "work_location_id": work_location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(PaginatedEmployeeList, parse_obj_as(type_=PaginatedEmployeeList, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        model: EmployeeRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmployeeResponse:
        """
        Creates an `Employee` object with the given values.

        Parameters
        ----------
        model : EmployeeRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmployeeResponse


        Examples
        --------
        from merge.client import Merge
        from merge.resources.hris import EmployeeRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.employees.create(
            model=EmployeeRequest(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/v1/employees",
            method="POST",
            params={"is_debug_mode": is_debug_mode, "run_async": run_async},
            json={"model": model},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(EmployeeResponse, parse_obj_as(type_=EmployeeResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[EmployeesRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_sensitive_fields: typing.Optional[bool] = None,
        remote_fields: typing.Optional[EmployeesRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[EmployeesRetrieveRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Employee:
        """
        Returns an `Employee` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[EmployeesRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_sensitive_fields : typing.Optional[bool]
            Whether to include sensitive fields (such as social security numbers) in the response.

        remote_fields : typing.Optional[EmployeesRetrieveRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[EmployeesRetrieveRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Employee


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.employees.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"hris/v1/employees/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
                "include_sensitive_fields": include_sensitive_fields,
                "remote_fields": remote_fields,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Employee, parse_obj_as(type_=Employee, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def ignore_create(
        self,
        model_id: str,
        *,
        reason: IgnoreCommonModelRequestReason,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.

        Parameters
        ----------
        model_id : str

        reason : IgnoreCommonModelRequestReason

        message : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from merge.client import Merge
        from merge.resources.hris import ReasonEnum

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.employees.ignore_create(
            model_id="model_id",
            reason=ReasonEnum.GENERAL_CUSTOMER_REQUEST,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"hris/v1/employees/ignore/{jsonable_encoder(model_id)}",
            method="POST",
            json={"reason": reason, "message": message},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `Employee` POSTs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaResponse


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.employees.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/v1/employees/meta/post", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MetaResponse, parse_obj_as(type_=MetaResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEmployeesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        display_full_name: typing.Optional[str] = None,
        employment_status: typing.Optional[EmployeesListRequestEmploymentStatus] = None,
        employment_type: typing.Optional[str] = None,
        expand: typing.Optional[EmployeesListRequestExpand] = None,
        first_name: typing.Optional[str] = None,
        groups: typing.Optional[str] = None,
        home_location_id: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_sensitive_fields: typing.Optional[bool] = None,
        job_title: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        manager_id: typing.Optional[str] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        pay_group_id: typing.Optional[str] = None,
        personal_email: typing.Optional[str] = None,
        remote_fields: typing.Optional[EmployeesListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[EmployeesListRequestShowEnumOrigins] = None,
        started_after: typing.Optional[dt.datetime] = None,
        started_before: typing.Optional[dt.datetime] = None,
        team_id: typing.Optional[str] = None,
        terminated_after: typing.Optional[dt.datetime] = None,
        terminated_before: typing.Optional[dt.datetime] = None,
        work_email: typing.Optional[str] = None,
        work_location_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedEmployeeList:
        """
        Returns a list of `Employee` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return employees for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        display_full_name : typing.Optional[str]
            If provided, will only return employees with this display name.

        employment_status : typing.Optional[EmployeesListRequestEmploymentStatus]
            If provided, will only return employees with this employment status.

            - `ACTIVE` - ACTIVE
            - `PENDING` - PENDING
            - `INACTIVE` - INACTIVE

        employment_type : typing.Optional[str]
            If provided, will only return employees that have an employment of the specified employment_type.

        expand : typing.Optional[EmployeesListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        first_name : typing.Optional[str]
            If provided, will only return employees with this first name.

        groups : typing.Optional[str]
            If provided, will only return employees matching the group ids; multiple groups can be separated by commas.

        home_location_id : typing.Optional[str]
            If provided, will only return employees for this home location.

        include_deleted_data : typing.Optional[bool]
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_sensitive_fields : typing.Optional[bool]
            Whether to include sensitive fields (such as social security numbers) in the response.

        job_title : typing.Optional[str]
            If provided, will only return employees that have an employment of the specified job_title.

        last_name : typing.Optional[str]
            If provided, will only return employees with this last name.

        manager_id : typing.Optional[str]
            If provided, will only return employees for this manager.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        pay_group_id : typing.Optional[str]
            If provided, will only return employees for this pay group

        personal_email : typing.Optional[str]
            If provided, will only return Employees with this personal email

        remote_fields : typing.Optional[EmployeesListRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[EmployeesListRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        started_after : typing.Optional[dt.datetime]
            If provided, will only return employees that started after this datetime.

        started_before : typing.Optional[dt.datetime]
            If provided, will only return employees that started before this datetime.

        team_id : typing.Optional[str]
            If provided, will only return employees for this team.

        terminated_after : typing.Optional[dt.datetime]
            If provided, will only return employees that were terminated after this datetime.

        terminated_before : typing.Optional[dt.datetime]
            If provided, will only return employees that were terminated before this datetime.

        work_email : typing.Optional[str]
            If provided, will only return Employees with this work email

        work_location_id : typing.Optional[str]
            If provided, will only return employees for this location.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedEmployeeList


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.hris.employees.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/v1/employees",
            method="GET",
            params={
                "company_id": company_id,
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "display_full_name": display_full_name,
                "employment_status": employment_status,
                "employment_type": employment_type,
                "expand": expand,
                "first_name": first_name,
                "groups": groups,
                "home_location_id": home_location_id,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_sensitive_fields": include_sensitive_fields,
                "job_title": job_title,
                "last_name": last_name,
                "manager_id": manager_id,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "pay_group_id": pay_group_id,
                "personal_email": personal_email,
                "remote_fields": remote_fields,
                "remote_id": remote_id,
                "show_enum_origins": show_enum_origins,
                "started_after": serialize_datetime(started_after) if started_after is not None else None,
                "started_before": serialize_datetime(started_before) if started_before is not None else None,
                "team_id": team_id,
                "terminated_after": serialize_datetime(terminated_after) if terminated_after is not None else None,
                "terminated_before": serialize_datetime(terminated_before) if terminated_before is not None else None,
                "work_email": work_email,
                "work_location_id": work_location_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(PaginatedEmployeeList, parse_obj_as(type_=PaginatedEmployeeList, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        model: EmployeeRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmployeeResponse:
        """
        Creates an `Employee` object with the given values.

        Parameters
        ----------
        model : EmployeeRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmployeeResponse


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge
        from merge.resources.hris import EmployeeRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.hris.employees.create(
                model=EmployeeRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/v1/employees",
            method="POST",
            params={"is_debug_mode": is_debug_mode, "run_async": run_async},
            json={"model": model},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(EmployeeResponse, parse_obj_as(type_=EmployeeResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[EmployeesRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_sensitive_fields: typing.Optional[bool] = None,
        remote_fields: typing.Optional[EmployeesRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[EmployeesRetrieveRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Employee:
        """
        Returns an `Employee` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[EmployeesRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_sensitive_fields : typing.Optional[bool]
            Whether to include sensitive fields (such as social security numbers) in the response.

        remote_fields : typing.Optional[EmployeesRetrieveRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[EmployeesRetrieveRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Employee


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.hris.employees.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"hris/v1/employees/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
                "include_sensitive_fields": include_sensitive_fields,
                "remote_fields": remote_fields,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(Employee, parse_obj_as(type_=Employee, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def ignore_create(
        self,
        model_id: str,
        *,
        reason: IgnoreCommonModelRequestReason,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.

        Parameters
        ----------
        model_id : str

        reason : IgnoreCommonModelRequestReason

        message : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge
        from merge.resources.hris import ReasonEnum

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.hris.employees.ignore_create(
                model_id="model_id",
                reason=ReasonEnum.GENERAL_CUSTOMER_REQUEST,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"hris/v1/employees/ignore/{jsonable_encoder(model_id)}",
            method="POST",
            json={"reason": reason, "message": message},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `Employee` POSTs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaResponse


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.hris.employees.meta_post_retrieve()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/v1/employees/meta/post", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MetaResponse, parse_obj_as(type_=MetaResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
