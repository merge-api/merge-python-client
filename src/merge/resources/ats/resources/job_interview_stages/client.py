# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from .....core.request_options import RequestOptions
from ...types.job_interview_stage import JobInterviewStage
from ...types.paginated_job_interview_stage_list import PaginatedJobInterviewStageList

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class JobInterviewStagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["job"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        job_id: typing.Optional[str] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedJobInterviewStageList:
        """
        Returns a list of `JobInterviewStage` objects.

        Parameters:
            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[typing.Literal["job"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - job_id: typing.Optional[str]. If provided, will only return interview stages for this job.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.job_interview_stages.list(
            expand="job",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/ats/v1/job-interview-stages"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "created_after": serialize_datetime(created_after) if created_after is not None else None,
                        "created_before": serialize_datetime(created_before) if created_before is not None else None,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "job_id": job_id,
                        "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                        "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                        "page_size": page_size,
                        "remote_id": remote_id,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedJobInterviewStageList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing.Literal["job"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobInterviewStage:
        """
        Returns a `JobInterviewStage` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[typing.Literal["job"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.ats.job_interview_stages.retrieve(
            id="string",
            expand="job",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/ats/v1/job-interview-stages/{id}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(JobInterviewStage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncJobInterviewStagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        expand: typing.Optional[typing.Literal["job"]] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        job_id: typing.Optional[str] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedJobInterviewStageList:
        """
        Returns a list of `JobInterviewStage` objects.

        Parameters:
            - created_after: typing.Optional[dt.datetime]. If provided, will only return objects created after this datetime.

            - created_before: typing.Optional[dt.datetime]. If provided, will only return objects created before this datetime.

            - cursor: typing.Optional[str]. The pagination cursor value.

            - expand: typing.Optional[typing.Literal["job"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_deleted_data: typing.Optional[bool]. Whether to include data that was marked as deleted by third party webhooks.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - job_id: typing.Optional[str]. If provided, will only return interview stages for this job.

            - modified_after: typing.Optional[dt.datetime]. If provided, only objects synced by Merge after this date time will be returned.

            - modified_before: typing.Optional[dt.datetime]. If provided, only objects synced by Merge before this date time will be returned.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - remote_id: typing.Optional[str]. The API provider's ID for the given object.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.ats.job_interview_stages.list(
            expand="job",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/ats/v1/job-interview-stages"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "created_after": serialize_datetime(created_after) if created_after is not None else None,
                        "created_before": serialize_datetime(created_before) if created_before is not None else None,
                        "cursor": cursor,
                        "expand": expand,
                        "include_deleted_data": include_deleted_data,
                        "include_remote_data": include_remote_data,
                        "job_id": job_id,
                        "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                        "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                        "page_size": page_size,
                        "remote_id": remote_id,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedJobInterviewStageList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[typing.Literal["job"]] = None,
        include_remote_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobInterviewStage:
        """
        Returns a `JobInterviewStage` object with the given `id`.

        Parameters:
            - id: str.

            - expand: typing.Optional[typing.Literal["job"]]. Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

            - include_remote_data: typing.Optional[bool]. Whether to include the original data Merge fetched from the third-party to produce these models.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.ats.job_interview_stages.retrieve(
            id="string",
            expand="job",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/ats/v1/job-interview-stages/{id}"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "expand": expand,
                        "include_remote_data": include_remote_data,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(JobInterviewStage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
