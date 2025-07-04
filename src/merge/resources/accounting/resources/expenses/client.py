# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ...types.expense import Expense
from ...types.expense_request import ExpenseRequest
from ...types.expense_response import ExpenseResponse
from ...types.meta_response import MetaResponse
from ...types.paginated_expense_list import PaginatedExpenseList
from ...types.paginated_remote_field_class_list import PaginatedRemoteFieldClassList
from .raw_client import AsyncRawExpensesClient, RawExpensesClient
from .types.expenses_list_request_expand import ExpensesListRequestExpand
from .types.expenses_retrieve_request_expand import ExpensesRetrieveRequestExpand

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ExpensesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExpensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExpensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExpensesClient
        """
        return self._raw_client

    def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[ExpensesListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        transaction_date_after: typing.Optional[dt.datetime] = None,
        transaction_date_before: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedExpenseList:
        """
        Returns a list of `Expense` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return expenses for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[ExpensesListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

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
        PaginatedExpenseList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.expenses.list()
        """
        _response = self._raw_client.list(
            company_id=company_id,
            created_after=created_after,
            created_before=created_before,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_remote_fields=include_remote_fields,
            include_shell_data=include_shell_data,
            modified_after=modified_after,
            modified_before=modified_before,
            page_size=page_size,
            remote_id=remote_id,
            transaction_date_after=transaction_date_after,
            transaction_date_before=transaction_date_before,
            request_options=request_options,
        )
        return _response.data

    def create(
        self,
        *,
        model: ExpenseRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExpenseResponse:
        """
        Creates an `Expense` object with the given values.

        Parameters
        ----------
        model : ExpenseRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExpenseResponse


        Examples
        --------
        from merge import Merge
        from merge.resources.accounting import ExpenseRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.expenses.create(
            model=ExpenseRequest(),
        )
        """
        _response = self._raw_client.create(
            model=model, is_debug_mode=is_debug_mode, run_async=run_async, request_options=request_options
        )
        return _response.data

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[ExpensesRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Expense:
        """
        Returns an `Expense` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[ExpensesRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Expense


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.expenses.retrieve(
            id="id",
        )
        """
        _response = self._raw_client.retrieve(
            id,
            expand=expand,
            include_remote_data=include_remote_data,
            include_remote_fields=include_remote_fields,
            include_shell_data=include_shell_data,
            request_options=request_options,
        )
        return _response.data

    def lines_remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        is_common_model_field: typing.Optional[bool] = None,
        is_custom: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedRemoteFieldClassList:
        """
        Returns a list of `RemoteFieldClass` objects.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor value.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        is_common_model_field : typing.Optional[bool]
            If provided, will only return remote field classes with this is_common_model_field value

        is_custom : typing.Optional[bool]
            If provided, will only return remote fields classes with this is_custom value

        page_size : typing.Optional[int]
            Number of results to return per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedRemoteFieldClassList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.expenses.lines_remote_field_classes_list()
        """
        _response = self._raw_client.lines_remote_field_classes_list(
            cursor=cursor,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            is_common_model_field=is_common_model_field,
            is_custom=is_custom,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `Expense` POSTs.

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
        client.accounting.expenses.meta_post_retrieve()
        """
        _response = self._raw_client.meta_post_retrieve(request_options=request_options)
        return _response.data

    def remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        is_common_model_field: typing.Optional[bool] = None,
        is_custom: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedRemoteFieldClassList:
        """
        Returns a list of `RemoteFieldClass` objects.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor value.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        is_common_model_field : typing.Optional[bool]
            If provided, will only return remote field classes with this is_common_model_field value

        is_custom : typing.Optional[bool]
            If provided, will only return remote fields classes with this is_custom value

        page_size : typing.Optional[int]
            Number of results to return per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedRemoteFieldClassList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.accounting.expenses.remote_field_classes_list()
        """
        _response = self._raw_client.remote_field_classes_list(
            cursor=cursor,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            is_common_model_field=is_common_model_field,
            is_custom=is_custom,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data


class AsyncExpensesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExpensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExpensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExpensesClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        company_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[ExpensesListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        transaction_date_after: typing.Optional[dt.datetime] = None,
        transaction_date_before: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedExpenseList:
        """
        Returns a list of `Expense` objects.

        Parameters
        ----------
        company_id : typing.Optional[str]
            If provided, will only return expenses for this company.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[ExpensesListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

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
        PaginatedExpenseList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.expenses.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            company_id=company_id,
            created_after=created_after,
            created_before=created_before,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_remote_fields=include_remote_fields,
            include_shell_data=include_shell_data,
            modified_after=modified_after,
            modified_before=modified_before,
            page_size=page_size,
            remote_id=remote_id,
            transaction_date_after=transaction_date_after,
            transaction_date_before=transaction_date_before,
            request_options=request_options,
        )
        return _response.data

    async def create(
        self,
        *,
        model: ExpenseRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExpenseResponse:
        """
        Creates an `Expense` object with the given values.

        Parameters
        ----------
        model : ExpenseRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExpenseResponse


        Examples
        --------
        import asyncio

        from merge import AsyncMerge
        from merge.resources.accounting import ExpenseRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.expenses.create(
                model=ExpenseRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            model=model, is_debug_mode=is_debug_mode, run_async=run_async, request_options=request_options
        )
        return _response.data

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[ExpensesRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Expense:
        """
        Returns an `Expense` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[ExpensesRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Expense


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.expenses.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve(
            id,
            expand=expand,
            include_remote_data=include_remote_data,
            include_remote_fields=include_remote_fields,
            include_shell_data=include_shell_data,
            request_options=request_options,
        )
        return _response.data

    async def lines_remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        is_common_model_field: typing.Optional[bool] = None,
        is_custom: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedRemoteFieldClassList:
        """
        Returns a list of `RemoteFieldClass` objects.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor value.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        is_common_model_field : typing.Optional[bool]
            If provided, will only return remote field classes with this is_common_model_field value

        is_custom : typing.Optional[bool]
            If provided, will only return remote fields classes with this is_custom value

        page_size : typing.Optional[int]
            Number of results to return per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedRemoteFieldClassList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.expenses.lines_remote_field_classes_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.lines_remote_field_classes_list(
            cursor=cursor,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            is_common_model_field=is_common_model_field,
            is_custom=is_custom,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `Expense` POSTs.

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
            await client.accounting.expenses.meta_post_retrieve()


        asyncio.run(main())
        """
        _response = await self._raw_client.meta_post_retrieve(request_options=request_options)
        return _response.data

    async def remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        is_common_model_field: typing.Optional[bool] = None,
        is_custom: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedRemoteFieldClassList:
        """
        Returns a list of `RemoteFieldClass` objects.

        Parameters
        ----------
        cursor : typing.Optional[str]
            The pagination cursor value.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        is_common_model_field : typing.Optional[bool]
            If provided, will only return remote field classes with this is_common_model_field value

        is_custom : typing.Optional[bool]
            If provided, will only return remote fields classes with this is_custom value

        page_size : typing.Optional[int]
            Number of results to return per page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedRemoteFieldClassList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.accounting.expenses.remote_field_classes_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.remote_field_classes_list(
            cursor=cursor,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            is_common_model_field=is_common_model_field,
            is_custom=is_custom,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data
