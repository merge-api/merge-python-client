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
from ...types.paginated_transaction_list import PaginatedTransactionList
from ...types.transaction import Transaction
from .types.transactions_list_request_expand import TransactionsListRequestExpand
from .types.transactions_retrieve_request_expand import TransactionsRetrieveRequestExpand


class TransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[TransactionsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        transaction_date_after: typing.Optional[dt.datetime] = None,
        transaction_date_before: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTransactionList:
        """
        Returns a list of `Transaction` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return accounting transactions for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[TransactionsListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

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

        transaction_date_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        transaction_date_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedTransactionList


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.transactions.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/transactions",
            method="GET",
            params={
                "company_id": company_id,
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "expand": expand,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_id": remote_id,
                "transaction_date_after": serialize_datetime(transaction_date_after)
                if transaction_date_after is not None
                else None,
                "transaction_date_before": serialize_datetime(transaction_date_before)
                if transaction_date_before is not None
                else None,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PaginatedTransactionList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[TransactionsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Transaction:
        """
        Returns a `Transaction` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[TransactionsRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Transaction


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.transactions.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/v1/transactions/{jsonable_encoder(id)}",
            method="GET",
            params={"expand": expand, "include_remote_data": include_remote_data},
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Transaction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[TransactionsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        transaction_date_after: typing.Optional[dt.datetime] = None,
        transaction_date_before: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTransactionList:
        """
        Returns a list of `Transaction` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return accounting transactions for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[TransactionsListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

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

        transaction_date_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        transaction_date_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedTransactionList


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.accounting.transactions.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/transactions",
            method="GET",
            params={
                "company_id": company_id,
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "expand": expand,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_id": remote_id,
                "transaction_date_after": serialize_datetime(transaction_date_after)
                if transaction_date_after is not None
                else None,
                "transaction_date_before": serialize_datetime(transaction_date_before)
                if transaction_date_before is not None
                else None,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PaginatedTransactionList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[TransactionsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Transaction:
        """
        Returns a `Transaction` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[TransactionsRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Transaction


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.accounting.transactions.retrieve(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/v1/transactions/{jsonable_encoder(id)}",
            method="GET",
            params={"expand": expand, "include_remote_data": include_remote_data},
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Transaction, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
