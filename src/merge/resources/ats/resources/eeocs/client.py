# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ...types.eeoc import Eeoc
from ...types.paginated_eeoc_list import PaginatedEeocList
from .raw_client import AsyncRawEeocsClient, RawEeocsClient
from .types.eeocs_list_request_remote_fields import EeocsListRequestRemoteFields
from .types.eeocs_list_request_show_enum_origins import EeocsListRequestShowEnumOrigins
from .types.eeocs_retrieve_request_remote_fields import EeocsRetrieveRequestRemoteFields
from .types.eeocs_retrieve_request_show_enum_origins import EeocsRetrieveRequestShowEnumOrigins


class EeocsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEeocsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEeocsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEeocsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        candidate_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["candidate"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[EeocsListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[EeocsListRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedEeocList:
        """
        Returns a list of `EEOC` objects.

        Parameters
        ----------
        candidate_id : typing.Optional[str]
            If provided, will only return EEOC info for this candidate.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[typing.Literal["candidate"]]
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

        remote_fields : typing.Optional[EeocsListRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[EeocsListRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedEeocList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.eeocs.list()
        """
        _response = self._raw_client.list(
            candidate_id=candidate_id,
            created_after=created_after,
            created_before=created_before,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            modified_after=modified_after,
            modified_before=modified_before,
            page_size=page_size,
            remote_fields=remote_fields,
            remote_id=remote_id,
            show_enum_origins=show_enum_origins,
            request_options=request_options,
        )
        return _response.data

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing.Literal["candidate"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[EeocsRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[EeocsRetrieveRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Eeoc:
        """
        Returns an `EEOC` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[typing.Literal["candidate"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        remote_fields : typing.Optional[EeocsRetrieveRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[EeocsRetrieveRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Eeoc


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.eeocs.retrieve(
            id="id",
        )
        """
        _response = self._raw_client.retrieve(
            id,
            expand=expand,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            remote_fields=remote_fields,
            show_enum_origins=show_enum_origins,
            request_options=request_options,
        )
        return _response.data


class AsyncEeocsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEeocsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEeocsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEeocsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        candidate_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["candidate"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[EeocsListRequestRemoteFields] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[EeocsListRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedEeocList:
        """
        Returns a list of `EEOC` objects.

        Parameters
        ----------
        candidate_id : typing.Optional[str]
            If provided, will only return EEOC info for this candidate.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[typing.Literal["candidate"]]
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

        remote_fields : typing.Optional[EeocsListRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[EeocsListRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedEeocList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ats.eeocs.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            candidate_id=candidate_id,
            created_after=created_after,
            created_before=created_before,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            modified_after=modified_after,
            modified_before=modified_before,
            page_size=page_size,
            remote_fields=remote_fields,
            remote_id=remote_id,
            show_enum_origins=show_enum_origins,
            request_options=request_options,
        )
        return _response.data

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing.Literal["candidate"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[EeocsRetrieveRequestRemoteFields] = None,
        show_enum_origins: typing.Optional[EeocsRetrieveRequestShowEnumOrigins] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Eeoc:
        """
        Returns an `EEOC` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[typing.Literal["candidate"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        remote_fields : typing.Optional[EeocsRetrieveRequestRemoteFields]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[EeocsRetrieveRequestShowEnumOrigins]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Eeoc


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ats.eeocs.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(
            id,
            expand=expand,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            remote_fields=remote_fields,
            show_enum_origins=show_enum_origins,
            request_options=request_options,
        )
        return _response.data
