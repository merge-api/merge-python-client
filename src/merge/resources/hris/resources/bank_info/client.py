# This file was auto-generated by Fern from our API Definition.

from .....core.client_wrapper import SyncClientWrapper
import typing
from .types.bank_info_list_request_account_type import BankInfoListRequestAccountType
import datetime as dt
from .types.bank_info_list_request_order_by import BankInfoListRequestOrderBy
from .....core.request_options import RequestOptions
from ...types.paginated_bank_info_list import PaginatedBankInfoList
from .....core.datetime_utils import serialize_datetime
from .....core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from .....core.api_error import ApiError
from ...types.bank_info import BankInfo
from .....core.jsonable_encoder import jsonable_encoder
from .....core.client_wrapper import AsyncClientWrapper


class BankInfoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        account_type: typing.Optional[BankInfoListRequestAccountType] = None,
        bank_name: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["employee"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[BankInfoListRequestOrderBy] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing.Literal["account_type"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["account_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedBankInfoList:
        """
        Returns a list of `BankInfo` objects.

        Parameters
        ----------
        account_type : typing.Optional[BankInfoListRequestAccountType]
            If provided, will only return BankInfo's with this account type. Options: ('SAVINGS', 'CHECKING')

            - `SAVINGS` - SAVINGS
            - `CHECKING` - CHECKING

        bank_name : typing.Optional[str]
            If provided, will only return BankInfo's with this bank name.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        employee_id : typing.Optional[str]
            If provided, will only return bank accounts for this employee.

        expand : typing.Optional[typing.Literal["employee"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        order_by : typing.Optional[BankInfoListRequestOrderBy]
            Overrides the default ordering for this endpoint. Possible values include: remote_created_at, -remote_created_at.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_fields : typing.Optional[typing.Literal["account_type"]]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[typing.Literal["account_type"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedBankInfoList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.bank_info.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "hris/v1/bank-info",
            method="GET",
            params={
                "account_type": account_type,
                "bank_name": bank_name,
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "employee_id": employee_id,
                "expand": expand,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "order_by": order_by,
                "page_size": page_size,
                "remote_fields": remote_fields,
                "remote_id": remote_id,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedBankInfoList,
                    parse_obj_as(
                        type_=PaginatedBankInfoList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing.Literal["employee"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["account_type"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["account_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankInfo:
        """
        Returns a `BankInfo` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[typing.Literal["employee"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        remote_fields : typing.Optional[typing.Literal["account_type"]]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[typing.Literal["account_type"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankInfo


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.bank_info.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"hris/v1/bank-info/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
                "remote_fields": remote_fields,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BankInfo,
                    parse_obj_as(
                        type_=BankInfo,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncBankInfoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        account_type: typing.Optional[BankInfoListRequestAccountType] = None,
        bank_name: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        employee_id: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["employee"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[BankInfoListRequestOrderBy] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing.Literal["account_type"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["account_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedBankInfoList:
        """
        Returns a list of `BankInfo` objects.

        Parameters
        ----------
        account_type : typing.Optional[BankInfoListRequestAccountType]
            If provided, will only return BankInfo's with this account type. Options: ('SAVINGS', 'CHECKING')

            - `SAVINGS` - SAVINGS
            - `CHECKING` - CHECKING

        bank_name : typing.Optional[str]
            If provided, will only return BankInfo's with this bank name.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        employee_id : typing.Optional[str]
            If provided, will only return bank accounts for this employee.

        expand : typing.Optional[typing.Literal["employee"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        order_by : typing.Optional[BankInfoListRequestOrderBy]
            Overrides the default ordering for this endpoint. Possible values include: remote_created_at, -remote_created_at.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_fields : typing.Optional[typing.Literal["account_type"]]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[typing.Literal["account_type"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedBankInfoList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.hris.bank_info.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "hris/v1/bank-info",
            method="GET",
            params={
                "account_type": account_type,
                "bank_name": bank_name,
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "employee_id": employee_id,
                "expand": expand,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "order_by": order_by,
                "page_size": page_size,
                "remote_fields": remote_fields,
                "remote_id": remote_id,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedBankInfoList,
                    parse_obj_as(
                        type_=PaginatedBankInfoList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing.Literal["employee"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["account_type"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["account_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BankInfo:
        """
        Returns a `BankInfo` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[typing.Literal["employee"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        remote_fields : typing.Optional[typing.Literal["account_type"]]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[typing.Literal["account_type"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BankInfo


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.hris.bank_info.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"hris/v1/bank-info/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
                "remote_fields": remote_fields,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BankInfo,
                    parse_obj_as(
                        type_=BankInfo,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
