# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ...types.job import Job
from ...types.paginated_job_list import PaginatedJobList
from ...types.paginated_screening_question_list import PaginatedScreeningQuestionList
from .raw_client import AsyncRawJobsClient, RawJobsClient
from .types.jobs_list_request_expand import JobsListRequestExpand
from .types.jobs_list_request_status import JobsListRequestStatus
from .types.jobs_retrieve_request_expand import JobsRetrieveRequestExpand
from .types.jobs_screening_questions_list_request_expand import JobsScreeningQuestionsListRequestExpand


class JobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        code: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[JobsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        offices: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        status: typing.Optional[JobsListRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedJobList:
        """
        Returns a list of `Job` objects.

        Parameters
        ----------
        code : typing.Optional[str]
            If provided, will only return jobs with this code.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[JobsListRequestExpand]
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

        offices : typing.Optional[str]
            If provided, will only return jobs for this office; multiple offices can be separated by commas.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_fields : typing.Optional[typing.Literal["status"]]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[typing.Literal["status"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        status : typing.Optional[JobsListRequestStatus]
            If provided, will only return jobs with this status. Options: ('OPEN', 'CLOSED', 'DRAFT', 'ARCHIVED', 'PENDING')

            * `OPEN` - OPEN
            * `CLOSED` - CLOSED
            * `DRAFT` - DRAFT
            * `ARCHIVED` - ARCHIVED
            * `PENDING` - PENDING

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedJobList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.jobs.list()
        """
        _response = self._raw_client.list(
            code=code,
            created_after=created_after,
            created_before=created_before,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            modified_after=modified_after,
            modified_before=modified_before,
            offices=offices,
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
        expand: typing.Optional[JobsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Job:
        """
        Returns a `Job` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[JobsRetrieveRequestExpand]
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
        Job


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.jobs.retrieve(
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

    def screening_questions_list(
        self,
        job_id: str,
        *,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[JobsScreeningQuestionsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedScreeningQuestionList:
        """
        Returns a list of `ScreeningQuestion` objects.

        Parameters
        ----------
        job_id : str

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[JobsScreeningQuestionsListRequestExpand]
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
        PaginatedScreeningQuestionList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.jobs.screening_questions_list(
            job_id="job_id",
        )
        """
        _response = self._raw_client.screening_questions_list(
            job_id,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data


class AsyncJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        code: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[JobsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        offices: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        remote_id: typing.Optional[str] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        status: typing.Optional[JobsListRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedJobList:
        """
        Returns a list of `Job` objects.

        Parameters
        ----------
        code : typing.Optional[str]
            If provided, will only return jobs with this code.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[JobsListRequestExpand]
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

        offices : typing.Optional[str]
            If provided, will only return jobs for this office; multiple offices can be separated by commas.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_fields : typing.Optional[typing.Literal["status"]]
            Deprecated. Use show_enum_origins.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        show_enum_origins : typing.Optional[typing.Literal["status"]]
            A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)

        status : typing.Optional[JobsListRequestStatus]
            If provided, will only return jobs with this status. Options: ('OPEN', 'CLOSED', 'DRAFT', 'ARCHIVED', 'PENDING')

            * `OPEN` - OPEN
            * `CLOSED` - CLOSED
            * `DRAFT` - DRAFT
            * `ARCHIVED` - ARCHIVED
            * `PENDING` - PENDING

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedJobList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ats.jobs.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(
            code=code,
            created_after=created_after,
            created_before=created_before,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            modified_after=modified_after,
            modified_before=modified_before,
            offices=offices,
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
        expand: typing.Optional[JobsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        remote_fields: typing.Optional[typing.Literal["status"]] = None,
        show_enum_origins: typing.Optional[typing.Literal["status"]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Job:
        """
        Returns a `Job` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[JobsRetrieveRequestExpand]
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
        Job


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ats.jobs.retrieve(
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

    async def screening_questions_list(
        self,
        job_id: str,
        *,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[JobsScreeningQuestionsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedScreeningQuestionList:
        """
        Returns a list of `ScreeningQuestion` objects.

        Parameters
        ----------
        job_id : str

        cursor : typing.Optional[str]
            The pagination cursor value.

        expand : typing.Optional[JobsScreeningQuestionsListRequestExpand]
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
        PaginatedScreeningQuestionList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ats.jobs.screening_questions_list(
                job_id="job_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.screening_questions_list(
            job_id,
            cursor=cursor,
            expand=expand,
            include_deleted_data=include_deleted_data,
            include_remote_data=include_remote_data,
            include_shell_data=include_shell_data,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data
