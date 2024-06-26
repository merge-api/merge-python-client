# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from ...types.meta_response import MetaResponse
from ...types.paginated_purchase_order_list import PaginatedPurchaseOrderList
from ...types.purchase_order import PurchaseOrder
from ...types.purchase_order_request import PurchaseOrderRequest
from ...types.purchase_order_response import PurchaseOrderResponse
from .types.purchase_orders_list_request_expand import PurchaseOrdersListRequestExpand
from .types.purchase_orders_retrieve_request_expand import PurchaseOrdersRetrieveRequestExpand

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PurchaseOrdersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[PurchaseOrdersListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        issue_date_after: typing.Optional[dt.datetime] = None,
        issue_date_before: typing.Optional[dt.datetime] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedPurchaseOrderList:
        """
        Returns a list of `PurchaseOrder` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return purchase orders for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[PurchaseOrdersListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        issue_date_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        issue_date_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_fields : typing.Optional[typing.Literal["status"]]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[typing.Literal["status"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedPurchaseOrderList


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.purchase_orders.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/purchase-orders",
            method="GET",
            params={
                "company_id": company_id,
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "expand": expand,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "issue_date_after": serialize_datetime(issue_date_after) if issue_date_after is not None else None,
                "issue_date_before": serialize_datetime(issue_date_before) if issue_date_before is not None else None,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_fields": remote_fields,
                "remote_id": remote_id,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PaginatedPurchaseOrderList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        model: PurchaseOrderRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderResponse:
        """
        Creates a `PurchaseOrder` object with the given values.

        Parameters
        ----------
        model : PurchaseOrderRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderResponse


        Examples
        --------
        from merge.client import Merge
        from merge.resources.accounting import PurchaseOrderRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.purchase_orders.create(
            model=PurchaseOrderRequest(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/purchase-orders",
            method="POST",
            params={"is_debug_mode": is_debug_mode, "run_async": run_async},
            json={"model": model},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PurchaseOrderResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[PurchaseOrdersRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrder:
        """
        Returns a `PurchaseOrder` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[PurchaseOrdersRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        remote_fields : typing.Optional[typing.Literal["status"]]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[typing.Literal["status"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrder


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.purchase_orders.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/v1/purchase-orders/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
                "remote_fields": remote_fields,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PurchaseOrder, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `PurchaseOrder` POSTs.

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
        client.accounting.purchase_orders.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/purchase-orders/meta/post", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPurchaseOrdersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[PurchaseOrdersListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        issue_date_after: typing.Optional[dt.datetime] = None,
        issue_date_before: typing.Optional[dt.datetime] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedPurchaseOrderList:
        """
        Returns a list of `PurchaseOrder` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return purchase orders for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[PurchaseOrdersListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        issue_date_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        issue_date_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_fields : typing.Optional[typing.Literal["status"]]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[typing.Literal["status"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedPurchaseOrderList


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.accounting.purchase_orders.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/purchase-orders",
            method="GET",
            params={
                "company_id": company_id,
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "expand": expand,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "issue_date_after": serialize_datetime(issue_date_after) if issue_date_after is not None else None,
                "issue_date_before": serialize_datetime(issue_date_before) if issue_date_before is not None else None,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_fields": remote_fields,
                "remote_id": remote_id,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PaginatedPurchaseOrderList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        model: PurchaseOrderRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrderResponse:
        """
        Creates a `PurchaseOrder` object with the given values.

        Parameters
        ----------
        model : PurchaseOrderRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrderResponse


        Examples
        --------
        from merge.client import AsyncMerge
        from merge.resources.accounting import PurchaseOrderRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.accounting.purchase_orders.create(
            model=PurchaseOrderRequest(),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/purchase-orders",
            method="POST",
            params={"is_debug_mode": is_debug_mode, "run_async": run_async},
            json={"model": model},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PurchaseOrderResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[PurchaseOrdersRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PurchaseOrder:
        """
        Returns a `PurchaseOrder` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[PurchaseOrdersRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        remote_fields : typing.Optional[typing.Literal["status"]]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[typing.Literal["status"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PurchaseOrder


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.accounting.purchase_orders.retrieve(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/v1/purchase-orders/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
                "remote_fields": remote_fields,
                "show_enum_origins": show_enum_origins,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PurchaseOrder, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `PurchaseOrder` POSTs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaResponse


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.accounting.purchase_orders.meta_post_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/purchase-orders/meta/post", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
