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
from ...types.accounting_attachment import AccountingAttachment
from ...types.accounting_attachment_request import AccountingAttachmentRequest
from ...types.accounting_attachment_response import AccountingAttachmentResponse
from ...types.meta_response import MetaResponse
from ...types.paginated_accounting_attachment_list import PaginatedAccountingAttachmentList

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AttachmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
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
    ) -> PaginatedAccountingAttachmentList:
        """
        Returns a list of `AccountingAttachment` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return accounting attachments for this company.

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
        PaginatedAccountingAttachmentList


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.attachments.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/attachments",
            method="GET",
            params={
                "company_id": company_id,
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
                return typing.cast(PaginatedAccountingAttachmentList, parse_obj_as(type_=PaginatedAccountingAttachmentList, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        model: AccountingAttachmentRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingAttachmentResponse:
        """
        Creates an `AccountingAttachment` object with the given values.

        Parameters
        ----------
        model : AccountingAttachmentRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingAttachmentResponse


        Examples
        --------
        from merge.client import Merge
        from merge.resources.accounting import AccountingAttachmentRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.attachments.create(
            model=AccountingAttachmentRequest(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/attachments",
            method="POST",
            params={"is_debug_mode": is_debug_mode, "run_async": run_async},
            json={"model": model},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AccountingAttachmentResponse, parse_obj_as(type_=AccountingAttachmentResponse, object_=_response.json()))  # type: ignore
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
    ) -> AccountingAttachment:
        """
        Returns an `AccountingAttachment` object with the given `id`.

        Parameters
        ----------
        id : str

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingAttachment


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.attachments.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/v1/attachments/{jsonable_encoder(id)}",
            method="GET",
            params={"include_remote_data": include_remote_data},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AccountingAttachment, parse_obj_as(type_=AccountingAttachment, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `AccountingAttachment` POSTs.

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
        client.accounting.attachments.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/attachments/meta/post", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MetaResponse, parse_obj_as(type_=MetaResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAttachmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
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
    ) -> PaginatedAccountingAttachmentList:
        """
        Returns a list of `AccountingAttachment` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return accounting attachments for this company.

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
        PaginatedAccountingAttachmentList


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.attachments.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/attachments",
            method="GET",
            params={
                "company_id": company_id,
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
                return typing.cast(PaginatedAccountingAttachmentList, parse_obj_as(type_=PaginatedAccountingAttachmentList, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        model: AccountingAttachmentRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountingAttachmentResponse:
        """
        Creates an `AccountingAttachment` object with the given values.

        Parameters
        ----------
        model : AccountingAttachmentRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingAttachmentResponse


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge
        from merge.resources.accounting import AccountingAttachmentRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.attachments.create(
                model=AccountingAttachmentRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/attachments",
            method="POST",
            params={"is_debug_mode": is_debug_mode, "run_async": run_async},
            json={"model": model},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AccountingAttachmentResponse, parse_obj_as(type_=AccountingAttachmentResponse, object_=_response.json()))  # type: ignore
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
    ) -> AccountingAttachment:
        """
        Returns an `AccountingAttachment` object with the given `id`.

        Parameters
        ----------
        id : str

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountingAttachment


        Examples
        --------
        import asyncio

        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.attachments.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/v1/attachments/{jsonable_encoder(id)}",
            method="GET",
            params={"include_remote_data": include_remote_data},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(AccountingAttachment, parse_obj_as(type_=AccountingAttachment, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `AccountingAttachment` POSTs.

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
            await client.accounting.attachments.meta_post_retrieve()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/attachments/meta/post", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MetaResponse, parse_obj_as(type_=MetaResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
