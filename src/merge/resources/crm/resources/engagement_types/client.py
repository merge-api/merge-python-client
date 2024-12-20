# This file was auto-generated by Fern from our API Definition.

from .....core.client_wrapper import SyncClientWrapper
import typing
import datetime as dt
from .....core.request_options import RequestOptions
from ...types.paginated_engagement_type_list import PaginatedEngagementTypeList
from .....core.datetime_utils import serialize_datetime
from .....core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from .....core.api_error import ApiError
from ...types.engagement_type import EngagementType
from .....core.jsonable_encoder import jsonable_encoder
from ...types.paginated_remote_field_class_list import PaginatedRemoteFieldClassList
from .....core.client_wrapper import AsyncClientWrapper


class EngagementTypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedEngagementTypeList:
        """
        Returns a list of `EngagementType` objects.

        Parameters
        ----------
        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedEngagementTypeList


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.engagement_types.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/v1/engagement-types",
            method="GET",
            params={
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
                "include_shell_data": include_shell_data,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_id": remote_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedEngagementTypeList,
                    parse_obj_as(
                        type_=PaginatedEngagementTypeList,  # type: ignore
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
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EngagementType:
        """
        Returns an `EngagementType` object with the given `id`.

        Parameters
        ----------
        id : str

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EngagementType


        Examples
        --------
        from merge import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.engagement_types.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/v1/engagement-types/{jsonable_encoder(id)}",
            method="GET",
            params={
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EngagementType,
                    parse_obj_as(
                        type_=EngagementType,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        is_common_model_field: typing.Optional[bool] = None,
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

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        is_common_model_field : typing.Optional[bool]
            If provided, will only return remote field classes with this is_common_model_field value

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
        client.crm.engagement_types.remote_field_classes_list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/v1/engagement-types/remote-field-classes",
            method="GET",
            params={
                "cursor": cursor,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
                "include_shell_data": include_shell_data,
                "is_common_model_field": is_common_model_field,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedRemoteFieldClassList,
                    parse_obj_as(
                        type_=PaginatedRemoteFieldClassList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEngagementTypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        remote_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedEngagementTypeList:
        """
        Returns a list of `EngagementType` objects.

        Parameters
        ----------
        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

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

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedEngagementTypeList


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.crm.engagement_types.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/v1/engagement-types",
            method="GET",
            params={
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
                "include_shell_data": include_shell_data,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "remote_id": remote_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedEngagementTypeList,
                    parse_obj_as(
                        type_=PaginatedEngagementTypeList,  # type: ignore
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
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EngagementType:
        """
        Returns an `EngagementType` object with the given `id`.

        Parameters
        ----------
        id : str

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EngagementType


        Examples
        --------
        import asyncio

        from merge import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.crm.engagement_types.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/v1/engagement-types/{jsonable_encoder(id)}",
            method="GET",
            params={
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    EngagementType,
                    parse_obj_as(
                        type_=EngagementType,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remote_field_classes_list(
        self,
        *,
        cursor: typing.Optional[str] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        include_shell_data: typing.Optional[bool] = None,
        is_common_model_field: typing.Optional[bool] = None,
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

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        include_shell_data : typing.Optional[bool]
            Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).

        is_common_model_field : typing.Optional[bool]
            If provided, will only return remote field classes with this is_common_model_field value

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
            await client.crm.engagement_types.remote_field_classes_list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/v1/engagement-types/remote-field-classes",
            method="GET",
            params={
                "cursor": cursor,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
                "include_shell_data": include_shell_data,
                "is_common_model_field": is_common_model_field,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedRemoteFieldClassList,
                    parse_obj_as(
                        type_=PaginatedRemoteFieldClassList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
