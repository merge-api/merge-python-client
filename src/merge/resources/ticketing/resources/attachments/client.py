# This file was auto-generated by Fern from our API Definition.

import typing
from .....core.client_wrapper import SyncClientWrapper
import datetime as dt
from .....core.request_options import RequestOptions
from ...types.paginated_attachment_list import PaginatedAttachmentList
from .....core.datetime_utils import serialize_datetime
from .....core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from .....core.api_error import ApiError
from ...types.attachment_request import AttachmentRequest
from ...types.ticketing_attachment_response import TicketingAttachmentResponse
from ...types.attachment import Attachment
from .....core.jsonable_encoder import jsonable_encoder
from ...types.meta_response import MetaResponse
from .....core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AttachmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["ticket"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_created_after: typing.Optional[dt.datetime] = None,
        remote_id: typing.Optional[str] = None,
        ticket_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedAttachmentList:
        """
        Returns a list of `Attachment` objects.

        Parameters
        ----------
        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[typing.Literal["ticket"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_created_after : typing.Optional[dt.datetime]
            If provided, will only return attachments created in the third party platform after this datetime.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        ticket_id : typing.Optional[str]
            If provided, will only return comments for this ticket.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedAttachmentList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.attachments.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "ticketing/v1/attachments",
            method="GET",
            params={
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "expand": expand,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_shell_data": include_shell_data,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_created_after": serialize_datetime(remote_created_after)
                if remote_created_after is not None
                else None,
                "remote_id": remote_id,
                "ticket_id": ticket_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedAttachmentList,
                    parse_obj_as(
                        type_=PaginatedAttachmentList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        model: AttachmentRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketingAttachmentResponse:
        """
        Creates an `Attachment` object with the given values.

        Parameters
        ----------
        model : AttachmentRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketingAttachmentResponse


        Examples
        --------
        from merge import Merge
        from merge.resources.ticketing import AttachmentRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.attachments.create(
            model=AttachmentRequest(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "ticketing/v1/attachments",
            method="POST",
            params={
                "is_debug_mode": is_debug_mode,
                "run_async": run_async,
            },
            json={
                "model": model,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TicketingAttachmentResponse,
                    parse_obj_as(
                        type_=TicketingAttachmentResponse,  # type: ignore
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
        expand: typing.Optional[typing.Literal["ticket"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Returns an `Attachment` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[typing.Literal["ticket"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attachment


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.attachments.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ticketing/v1/attachments/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Attachment,
                    parse_obj_as(
                        type_=Attachment,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def download_retrieve(
        self,
        id: str,
        *,
        mime_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Returns the `File` content with the given `id` as a stream of bytes.

        Parameters
        ----------
        id : str

        mime_type : typing.Optional[str]
            If provided, specifies the export format of the file to be downloaded. For information on supported export formats, please refer to our <a href='https://help.merge.dev/en/articles/8615316-file-export-and-download-specification' target='_blank'>export format help center article</a>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[bytes]


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.attachments.download_retrieve(
            id="string",
            mime_type="string",
        )
        """
        with self._client_wrapper.httpx_client.stream(
            f"ticketing/v1/attachments/{jsonable_encoder(id)}/download",
            method="GET",
            params={
                "mime_type": mime_type,
            },
            request_options=request_options,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    for _chunk in _response.iter_bytes():
                        yield _chunk
                    return
                _response.read()
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `TicketingAttachment` POSTs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaResponse


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.attachments.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "ticketing/v1/attachments/meta/post",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MetaResponse,
                    parse_obj_as(
                        type_=MetaResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
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
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["ticket"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_created_after: typing.Optional[dt.datetime] = None,
        remote_id: typing.Optional[str] = None,
        ticket_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedAttachmentList:
        """
        Returns a list of `Attachment` objects.

        Parameters
        ----------
        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[typing.Literal["ticket"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_created_after : typing.Optional[dt.datetime]
            If provided, will only return attachments created in the third party platform after this datetime.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        ticket_id : typing.Optional[str]
            If provided, will only return comments for this ticket.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedAttachmentList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.attachments.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ticketing/v1/attachments",
            method="GET",
            params={
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "expand": expand,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_shell_data": include_shell_data,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_created_after": serialize_datetime(remote_created_after)
                if remote_created_after is not None
                else None,
                "remote_id": remote_id,
                "ticket_id": ticket_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedAttachmentList,
                    parse_obj_as(
                        type_=PaginatedAttachmentList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        model: AttachmentRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TicketingAttachmentResponse:
        """
        Creates an `Attachment` object with the given values.

        Parameters
        ----------
        model : AttachmentRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TicketingAttachmentResponse


        Examples
        --------
        import asyncio

        from merge import AsyncMerge
        from merge.resources.ticketing import AttachmentRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.attachments.create(
                model=AttachmentRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ticketing/v1/attachments",
            method="POST",
            params={
                "is_debug_mode": is_debug_mode,
                "run_async": run_async,
            },
            json={
                "model": model,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TicketingAttachmentResponse,
                    parse_obj_as(
                        type_=TicketingAttachmentResponse,  # type: ignore
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
        expand: typing.Optional[typing.Literal["ticket"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Attachment:
        """
        Returns an `Attachment` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[typing.Literal["ticket"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Attachment


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.attachments.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ticketing/v1/attachments/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Attachment,
                    parse_obj_as(
                        type_=Attachment,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def download_retrieve(
        self,
        id: str,
        *,
        mime_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns the `File` content with the given `id` as a stream of bytes.

        Parameters
        ----------
        id : str

        mime_type : typing.Optional[str]
            If provided, specifies the export format of the file to be downloaded. For information on supported export formats, please refer to our <a href='https://help.merge.dev/en/articles/8615316-file-export-and-download-specification' target='_blank'>export format help center article</a>.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[bytes]


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.attachments.download_retrieve(
                id="string",
                mime_type="string",
            )


        asyncio.run(main())
        """
        async with self._client_wrapper.httpx_client.stream(
            f"ticketing/v1/attachments/{jsonable_encoder(id)}/download",
            method="GET",
            params={
                "mime_type": mime_type,
            },
            request_options=request_options,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    async for _chunk in _response.aiter_bytes():
                        yield _chunk
                    return
                await _response.aread()
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `TicketingAttachment` POSTs.

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

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.attachments.meta_post_retrieve()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ticketing/v1/attachments/meta/post",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    MetaResponse,
                    parse_obj_as(
                        type_=MetaResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
