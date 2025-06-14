# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ...types.collection import Collection
from ...types.paginated_collection_list import PaginatedCollectionList
from ...types.paginated_viewer_list import PaginatedViewerList
from .raw_client import AsyncRawCollectionsClient, RawCollectionsClient
from .types.collections_viewers_list_request_expand import CollectionsViewersListRequestExpand


class CollectionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCollectionsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        collection_type: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["parent_collection"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        parent_collection_id: typing.Optional[str] = None,
        remote_fields: typing.Optional[typing.Literal["collection_type"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["collection_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedCollectionList:
        """
        Returns a list of `Collection` objects.

        Parameters
        ----------
        collection_type : typing.Optional[str]
            If provided, will only return collections of the given type.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[typing.Literal["parent_collection"]]
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

        parent_collection_id : typing.Optional[str]
            If provided, will only return collections whose parent collection matches the given id.

        remote_fields : typing.Optional[typing.Literal["collection_type"]]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[typing.Literal["collection_type"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedCollectionList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.collections.list()
        """
        _response = self._raw_client.list(
            collection_type=collection_type,
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
            parent_collection_id=parent_collection_id,
            remote_fields=remote_fields,
            remote_id=remote_id,
            show_enum_origins=show_enum_origins,
            request_options=request_options,
        )
        return _response.data

    def viewers_list(
        self,
        collection_id: str,
        *,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[CollectionsViewersListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedViewerList:
        """
        Returns a list of `Viewer` objects that point to a User id or Team id that is either an assignee or viewer on a `Collection` with the given id. [Learn more.](https://help.merge.dev/en/articles/10333658-ticketing-access-control-list-acls)

        Parameters
        ----------
        collection_id : str

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[CollectionsViewersListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        page_size : typing.Optional[int]
            Number of results to return per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedViewerList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.collections.viewers_list(
            collection_id="collection_id",
        )
        """
        _response = self._raw_client.viewers_list(
            collection_id,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing.Literal["parent_collection"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["collection_type"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["collection_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collection:
        """
        Returns a `Collection` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[typing.Literal["parent_collection"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        remote_fields : typing.Optional[typing.Literal["collection_type"]]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[typing.Literal["collection_type"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ticketing.collections.retrieve(
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


class AsyncCollectionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCollectionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCollectionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCollectionsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        collection_type: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["parent_collection"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        parent_collection_id: typing.Optional[str] = None,
        remote_fields: typing.Optional[typing.Literal["collection_type"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["collection_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedCollectionList:
        """
        Returns a list of `Collection` objects.

        Parameters
        ----------
        collection_type : typing.Optional[str]
            If provided, will only return collections of the given type.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[typing.Literal["parent_collection"]]
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

        parent_collection_id : typing.Optional[str]
            If provided, will only return collections whose parent collection matches the given id.

        remote_fields : typing.Optional[typing.Literal["collection_type"]]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[typing.Literal["collection_type"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedCollectionList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.collections.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            collection_type=collection_type,
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
            parent_collection_id=parent_collection_id,
            remote_fields=remote_fields,
            remote_id=remote_id,
            show_enum_origins=show_enum_origins,
            request_options=request_options,
        )
        return _response.data

    async def viewers_list(
        self,
        collection_id: str,
        *,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[CollectionsViewersListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedViewerList:
        """
        Returns a list of `Viewer` objects that point to a User id or Team id that is either an assignee or viewer on a `Collection` with the given id. [Learn more.](https://help.merge.dev/en/articles/10333658-ticketing-access-control-list-acls)

        Parameters
        ----------
        collection_id : str

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[CollectionsViewersListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        page_size : typing.Optional[int]
            Number of results to return per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedViewerList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.collections.viewers_list(
                collection_id="collection_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.viewers_list(
            collection_id,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing.Literal["parent_collection"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["collection_type"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["collection_type"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Collection:
        """
        Returns a `Collection` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[typing.Literal["parent_collection"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        remote_fields : typing.Optional[typing.Literal["collection_type"]]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[typing.Literal["collection_type"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Collection


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ticketing.collections.retrieve(
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
