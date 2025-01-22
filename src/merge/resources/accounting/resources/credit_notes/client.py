# This file was auto-generated by Fern from our API Definition.

import typing
from .....core.client_wrapper import SyncClientWrapper
import datetime as dt
from .types.credit_notes_list_request_expand import CreditNotesListRequestExpand
from .types.credit_notes_list_request_remote_fields import CreditNotesListRequestRemoteFields
from .types.credit_notes_list_request_show_enum_origins import CreditNotesListRequestShowEnumOrigins
from .....core.request_options import RequestOptions
from ...types.paginated_credit_note_list import PaginatedCreditNoteList
from .....core.datetime_utils import serialize_datetime
from .....core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from .....core.api_error import ApiError
from ...types.credit_note_request import CreditNoteRequest
from ...types.credit_note_response import CreditNoteResponse
from .types.credit_notes_retrieve_request_expand import CreditNotesRetrieveRequestExpand
from .types.credit_notes_retrieve_request_remote_fields import CreditNotesRetrieveRequestRemoteFields
from .types.credit_notes_retrieve_request_show_enum_origins import CreditNotesRetrieveRequestShowEnumOrigins
from ...types.credit_note import CreditNote
from .....core.jsonable_encoder import jsonable_encoder
from ...types.meta_response import MetaResponse
from .....core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CreditNotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[CreditNotesListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[CreditNotesListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[CreditNotesListRequestShowEnumOrigins] = None,
        transaction_date_after: typing.Optional[dt.datetime] = None,
        transaction_date_before: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedCreditNoteList:
        """
        Returns a list of `CreditNote` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return credit notes for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[CreditNotesListRequestExpand]
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

        remote_fields : typing.Optional[CreditNotesListRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[CreditNotesListRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        transaction_date_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        transaction_date_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedCreditNoteList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.credit_notes.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/credit-notes",
            method="GET",
            params={
                "company_id": company_id,
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
                "remote_fields": remote_fields,
                "remote_id": remote_id,
                "show_enum_origins": show_enum_origins,
                "transaction_date_after": serialize_datetime(transaction_date_after)
                if transaction_date_after is not None
                else None,
                "transaction_date_before": serialize_datetime(transaction_date_before)
                if transaction_date_before is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedCreditNoteList,
                    parse_obj_as(
                        type_=PaginatedCreditNoteList,  # type: ignore
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
        model: CreditNoteRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditNoteResponse:
        """
        Creates a `CreditNote` object with the given values.

        Parameters
        ----------
        model : CreditNoteRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditNoteResponse


        Examples
        --------
        from merge import Merge
        from merge.resources.accounting import CreditNoteRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.credit_notes.create(
            model=CreditNoteRequest(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/credit-notes",
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
                    CreditNoteResponse,
                    parse_obj_as(
                        type_=CreditNoteResponse,  # type: ignore
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
        expand: typing.Optional[CreditNotesRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[CreditNotesRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[CreditNotesRetrieveRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditNote:
        """
        Returns a `CreditNote` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[CreditNotesRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        remote_fields : typing.Optional[CreditNotesRetrieveRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[CreditNotesRetrieveRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditNote


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.credit_notes.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounting/v1/credit-notes/{jsonable_encoder(id)}",
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
                    CreditNote,
                    parse_obj_as(
                        type_=CreditNote,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `CreditNote` POSTs.

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
        client.accounting.credit_notes.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "accounting/v1/credit-notes/meta/post",
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


class AsyncCreditNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[CreditNotesListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[CreditNotesListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[CreditNotesListRequestShowEnumOrigins] = None,
        transaction_date_after: typing.Optional[dt.datetime] = None,
        transaction_date_before: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedCreditNoteList:
        """
        Returns a list of `CreditNote` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return credit notes for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[CreditNotesListRequestExpand]
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

        remote_fields : typing.Optional[CreditNotesListRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[CreditNotesListRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        transaction_date_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        transaction_date_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedCreditNoteList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.credit_notes.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/credit-notes",
            method="GET",
            params={
                "company_id": company_id,
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
                "remote_fields": remote_fields,
                "remote_id": remote_id,
                "show_enum_origins": show_enum_origins,
                "transaction_date_after": serialize_datetime(transaction_date_after)
                if transaction_date_after is not None
                else None,
                "transaction_date_before": serialize_datetime(transaction_date_before)
                if transaction_date_before is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedCreditNoteList,
                    parse_obj_as(
                        type_=PaginatedCreditNoteList,  # type: ignore
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
        model: CreditNoteRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditNoteResponse:
        """
        Creates a `CreditNote` object with the given values.

        Parameters
        ----------
        model : CreditNoteRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditNoteResponse


        Examples
        --------
        import asyncio

        from merge import AsyncMerge
        from merge.resources.accounting import CreditNoteRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.credit_notes.create(
                model=CreditNoteRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/credit-notes",
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
                    CreditNoteResponse,
                    parse_obj_as(
                        type_=CreditNoteResponse,  # type: ignore
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
        expand: typing.Optional[CreditNotesRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[CreditNotesRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[CreditNotesRetrieveRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreditNote:
        """
        Returns a `CreditNote` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[CreditNotesRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        remote_fields : typing.Optional[CreditNotesRetrieveRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[CreditNotesRetrieveRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreditNote


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.credit_notes.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounting/v1/credit-notes/{jsonable_encoder(id)}",
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
                    CreditNote,
                    parse_obj_as(
                        type_=CreditNote,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `CreditNote` POSTs.

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
            await client.accounting.credit_notes.meta_post_retrieve()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "accounting/v1/credit-notes/meta/post",
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
