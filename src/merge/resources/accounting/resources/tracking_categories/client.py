# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ...types.paginated_tracking_category_list import PaginatedTrackingCategoryList
from ...types.tracking_category import TrackingCategory
from .raw_client import AsyncRawTrackingCategoriesClient, RawTrackingCategoriesClient


class TrackingCategoriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrackingCategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrackingCategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrackingCategoriesClient
        """
        return self._raw_client

    def list(
        self,
        *,
        category_type: typing.Optional[str] = None,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["company"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        name: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTrackingCategoryList:
        """
        Returns a list of `TrackingCategory` objects.

        Parameters
        ----------
        category_type : typing.Optional[str]
            If provided, will only return tracking categories with this type.

        company_id : typing.Optional[str]
            If provided, will only return tracking categories for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[typing.Literal["company"]]
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

        name : typing.Optional[str]
            If provided, will only return tracking categories with this name.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_fields : typing.Optional[typing.Literal["status"]]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[typing.Literal["status"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        status : typing.Optional[str]
            If provided, will only return tracking categories with this status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedTrackingCategoryList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.tracking_categories.list()
        """
        _response = self._raw_client.list(
            category_type=category_type,
            company_id=company_id,
            created_after=created_after,
            created_before=created_before,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            modified_after=modified_after,
            modified_before=modified_before,
            name=name,
            page_size=page_size,
            remote_fields=remote_fields,
            remote_id=remote_id,
            show_enum_origins=show_enum_origins,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing.Literal["company"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrackingCategory:
        """
        Returns a `TrackingCategory` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[typing.Literal["company"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        remote_fields : typing.Optional[typing.Literal["status"]]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[typing.Literal["status"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrackingCategory


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.tracking_categories.retrieve(
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


class AsyncTrackingCategoriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrackingCategoriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrackingCategoriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrackingCategoriesClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        category_type: typing.Optional[str] = None,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["company"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        name: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        status: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedTrackingCategoryList:
        """
        Returns a list of `TrackingCategory` objects.

        Parameters
        ----------
        category_type : typing.Optional[str]
            If provided, will only return tracking categories with this type.

        company_id : typing.Optional[str]
            If provided, will only return tracking categories for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[typing.Literal["company"]]
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

        name : typing.Optional[str]
            If provided, will only return tracking categories with this name.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_fields : typing.Optional[typing.Literal["status"]]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[typing.Literal["status"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        status : typing.Optional[str]
            If provided, will only return tracking categories with this status.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedTrackingCategoryList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.tracking_categories.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            category_type=category_type,
            company_id=company_id,
            created_after=created_after,
            created_before=created_before,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            modified_after=modified_after,
            modified_before=modified_before,
            name=name,
            page_size=page_size,
            remote_fields=remote_fields,
            remote_id=remote_id,
            show_enum_origins=show_enum_origins,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing.Literal["company"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TrackingCategory:
        """
        Returns a `TrackingCategory` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[typing.Literal["company"]]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        remote_fields : typing.Optional[typing.Literal["status"]]
            Deprecated. Use show_enum_origins.

        show_enum_origins : typing.Optional[typing.Literal["status"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrackingCategory


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.tracking_categories.retrieve(
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
