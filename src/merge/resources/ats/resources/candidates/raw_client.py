# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.http_response import AsyncHttpResponse, HttpResponse
from .....core.jsonable_encoder import jsonable_encoder
from .....core.request_options import RequestOptions
from .....core.unchecked_base_model import construct_type
from ...types.candidate import Candidate
from ...types.candidate_request import CandidateRequest
from ...types.candidate_response import CandidateResponse
from ...types.meta_response import MetaResponse
from ...types.paginated_candidate_list import PaginatedCandidateList
from ...types.patched_candidate_request import PatchedCandidateRequest
from .types.candidates_list_request_expand import CandidatesListRequestExpand
from .types.candidates_retrieve_request_expand import CandidatesRetrieveRequestExpand
from .types.ignore_common_model_request_reason import IgnoreCommonModelRequestReason

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawCandidatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        email_addresses: typing.Optional[str] = None,
        expand: typing.Optional[CandidatesListRequestExpand] = None,
        first_name: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        last_name: typing.Optional[str] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedCandidateList]:
        """
        Returns a list of `Candidate` objects.

        Parameters
        ----------
        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        email_addresses : typing.Optional[str]
            If provided, will only return candidates with these email addresses; multiple addresses can be separated by commas.

        expand : typing.Optional[CandidatesListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        first_name : typing.Optional[str]
            If provided, will only return candidates with this first name.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        last_name : typing.Optional[str]
            If provided, will only return candidates with this last name.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        tags : typing.Optional[str]
            If provided, will only return candidates with these tags; multiple tags can be separated by commas.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedCandidateList]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ats/v1/candidates",
            method="GET",
            params={
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "email_addresses": email_addresses,
                "expand": expand,
                "first_name": first_name,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_shell_data": include_shell_data,
                "last_name": last_name,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_id": remote_id,
                "tags": tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedCandidateList,
                    construct_type(
                        type_=PaginatedCandidateList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        model: CandidateRequest,
        remote_user_id: str,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CandidateResponse]:
        """
        Creates a `Candidate` object with the given values.

        Parameters
        ----------
        model : CandidateRequest

        remote_user_id : str

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CandidateResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ats/v1/candidates",
            method="POST",
            params={
                "is_debug_mode": is_debug_mode,
                "run_async": run_async,
            },
            json={
                "model": model,
                "remote_user_id": remote_user_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CandidateResponse,
                    construct_type(
                        type_=CandidateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[CandidatesRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Candidate]:
        """
        Returns a `Candidate` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[CandidatesRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Candidate]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ats/v1/candidates/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
                "include_shell_data": include_shell_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Candidate,
                    construct_type(
                        type_=Candidate,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def partial_update(
        self,
        id: str,
        *,
        model: PatchedCandidateRequest,
        remote_user_id: str,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CandidateResponse]:
        """
        Updates a `Candidate` object with the given `id`.

        Parameters
        ----------
        id : str

        model : PatchedCandidateRequest

        remote_user_id : str

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CandidateResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ats/v1/candidates/{jsonable_encoder(id)}",
            method="PATCH",
            params={
                "is_debug_mode": is_debug_mode,
                "run_async": run_async,
            },
            json={
                "model": model,
                "remote_user_id": remote_user_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CandidateResponse,
                    construct_type(
                        type_=CandidateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ignore_create(
        self,
        model_id: str,
        *,
        reason: IgnoreCommonModelRequestReason,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.

        Parameters
        ----------
        model_id : str

        reason : IgnoreCommonModelRequestReason

        message : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ats/v1/candidates/ignore/{jsonable_encoder(model_id)}",
            method="POST",
            json={
                "reason": reason,
                "message": message,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def meta_patch_retrieve(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MetaResponse]:
        """
        Returns metadata for `Candidate` PATCHs.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MetaResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"ats/v1/candidates/meta/patch/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetaResponse,
                    construct_type(
                        type_=MetaResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def meta_post_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MetaResponse]:
        """
        Returns metadata for `Candidate` POSTs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MetaResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ats/v1/candidates/meta/post",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetaResponse,
                    construct_type(
                        type_=MetaResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCandidatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        email_addresses: typing.Optional[str] = None,
        expand: typing.Optional[CandidatesListRequestExpand] = None,
        first_name: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        last_name: typing.Optional[str] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedCandidateList]:
        """
        Returns a list of `Candidate` objects.

        Parameters
        ----------
        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        email_addresses : typing.Optional[str]
            If provided, will only return candidates with these email addresses; multiple addresses can be separated by commas.

        expand : typing.Optional[CandidatesListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        first_name : typing.Optional[str]
            If provided, will only return candidates with this first name.

        include_deleted_data : typing.Optional[bool]
            Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        last_name : typing.Optional[str]
            If provided, will only return candidates with this last name.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        tags : typing.Optional[str]
            If provided, will only return candidates with these tags; multiple tags can be separated by commas.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedCandidateList]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ats/v1/candidates",
            method="GET",
            params={
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "email_addresses": email_addresses,
                "expand": expand,
                "first_name": first_name,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_shell_data": include_shell_data,
                "last_name": last_name,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_id": remote_id,
                "tags": tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedCandidateList,
                    construct_type(
                        type_=PaginatedCandidateList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        model: CandidateRequest,
        remote_user_id: str,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CandidateResponse]:
        """
        Creates a `Candidate` object with the given values.

        Parameters
        ----------
        model : CandidateRequest

        remote_user_id : str

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CandidateResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ats/v1/candidates",
            method="POST",
            params={
                "is_debug_mode": is_debug_mode,
                "run_async": run_async,
            },
            json={
                "model": model,
                "remote_user_id": remote_user_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CandidateResponse,
                    construct_type(
                        type_=CandidateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[CandidatesRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Candidate]:
        """
        Returns a `Candidate` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[CandidatesRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Candidate]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ats/v1/candidates/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
                "include_shell_data": include_shell_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Candidate,
                    construct_type(
                        type_=Candidate,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def partial_update(
        self,
        id: str,
        *,
        model: PatchedCandidateRequest,
        remote_user_id: str,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CandidateResponse]:
        """
        Updates a `Candidate` object with the given `id`.

        Parameters
        ----------
        id : str

        model : PatchedCandidateRequest

        remote_user_id : str

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CandidateResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ats/v1/candidates/{jsonable_encoder(id)}",
            method="PATCH",
            params={
                "is_debug_mode": is_debug_mode,
                "run_async": run_async,
            },
            json={
                "model": model,
                "remote_user_id": remote_user_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CandidateResponse,
                    construct_type(
                        type_=CandidateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ignore_create(
        self,
        model_id: str,
        *,
        reason: IgnoreCommonModelRequestReason,
        message: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.

        Parameters
        ----------
        model_id : str

        reason : IgnoreCommonModelRequestReason

        message : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ats/v1/candidates/ignore/{jsonable_encoder(model_id)}",
            method="POST",
            json={
                "reason": reason,
                "message": message,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def meta_patch_retrieve(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MetaResponse]:
        """
        Returns metadata for `Candidate` PATCHs.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MetaResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ats/v1/candidates/meta/patch/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetaResponse,
                    construct_type(
                        type_=MetaResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def meta_post_retrieve(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MetaResponse]:
        """
        Returns metadata for `Candidate` POSTs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MetaResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ats/v1/candidates/meta/post",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MetaResponse,
                    construct_type(
                        type_=MetaResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
