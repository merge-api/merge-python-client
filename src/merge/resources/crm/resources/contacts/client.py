# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.jsonable_encoder import jsonable_encoder
from .....core.pydantic_utilities import pydantic_v1
from .....core.request_options import RequestOptions
from ...types.contact import Contact
from ...types.contact_request import ContactRequest
from ...types.crm_contact_response import CrmContactResponse
from ...types.ignore_common_model_request import IgnoreCommonModelRequest
from ...types.meta_response import MetaResponse
from ...types.paginated_contact_list import PaginatedContactList
from ...types.paginated_remote_field_class_list import PaginatedRemoteFieldClassList
from ...types.patched_contact_request import PatchedContactRequest
from .types.contacts_list_request_expand import ContactsListRequestExpand
from .types.contacts_retrieve_request_expand import ContactsRetrieveRequestExpand

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ContactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        account_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        email_addresses: typing.Optional[str] = None,
        expand: typing.Optional[ContactsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        phone_numbers: typing.Optional[str] = None,
        remote_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedContactList:
        """
        Returns a list of `Contact` objects.

        Parameters
        ----------
        account_id : typing.Optional[str]
            If provided, will only return contacts with this account.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        email_addresses : typing.Optional[str]
            If provided, will only return contacts matching the email addresses; multiple email_addresses can be separated by commas.

        expand : typing.Optional[ContactsListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        phone_numbers : typing.Optional[str]
            If provided, will only return contacts matching the phone numbers; multiple phone numbers can be separated by commas.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedContactList


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/v1/contacts",
            method="GET",
            params={
                "account_id": account_id,
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "email_addresses": email_addresses,
                "expand": expand,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "phone_numbers": phone_numbers,
                "remote_id": remote_id,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PaginatedContactList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        model: ContactRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmContactResponse:
        """
        Creates a `Contact` object with the given values.

        Parameters
        ----------
        model : ContactRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmContactResponse


        Examples
        --------
        from merge.client import Merge
        from merge.resources.crm import ContactRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.create(
            model=ContactRequest(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/v1/contacts",
            method="POST",
            params={"is_debug_mode": is_debug_mode, "run_async": run_async},
            json={"model": model},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CrmContactResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[ContactsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """
        Returns a `Contact` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[ContactsRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/v1/contacts/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Contact, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def partial_update(
        self,
        id: str,
        *,
        model: PatchedContactRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmContactResponse:
        """
        Updates a `Contact` object with the given `id`.

        Parameters
        ----------
        id : str

        model : PatchedContactRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmContactResponse


        Examples
        --------
        from merge.client import Merge
        from merge.resources.crm import PatchedContactRequest

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.partial_update(
            id="id",
            model=PatchedContactRequest(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/v1/contacts/{jsonable_encoder(id)}",
            method="PATCH",
            params={"is_debug_mode": is_debug_mode, "run_async": run_async},
            json={"model": model},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CrmContactResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def ignore_create(
        self,
        model_id: str,
        *,
        request: IgnoreCommonModelRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.

        Parameters
        ----------
        model_id : str

        request : IgnoreCommonModelRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from merge.client import Merge
        from merge.resources.crm import IgnoreCommonModelRequest, ReasonEnum

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.ignore_create(
            model_id="model_id",
            request=IgnoreCommonModelRequest(
                reason=ReasonEnum.GENERAL_CUSTOMER_REQUEST,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/v1/contacts/ignore/{jsonable_encoder(model_id)}",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_patch_retrieve(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `CRMContact` PATCHs.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaResponse


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.meta_patch_retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"crm/v1/contacts/meta/patch/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `CRMContact` POSTs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaResponse


        Examples
        --------
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.meta_post_retrieve()
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/v1/contacts/meta/post", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
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
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

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
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.crm.contacts.remote_field_classes_list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "crm/v1/contacts/remote-field-classes",
            method="GET",
            params={
                "cursor": cursor,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
                "is_common_model_field": is_common_model_field,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PaginatedRemoteFieldClassList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncContactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        account_id: typing.Optional[str] = None,
        created_after: typing.Optional[dt.datetime] = None,
        created_before: typing.Optional[dt.datetime] = None,
        cursor: typing.Optional[str] = None,
        email_addresses: typing.Optional[str] = None,
        expand: typing.Optional[ContactsListRequestExpand] = None,
        include_deleted_data: typing.Optional[bool] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        modified_after: typing.Optional[dt.datetime] = None,
        modified_before: typing.Optional[dt.datetime] = None,
        page_size: typing.Optional[int] = None,
        phone_numbers: typing.Optional[str] = None,
        remote_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedContactList:
        """
        Returns a list of `Contact` objects.

        Parameters
        ----------
        account_id : typing.Optional[str]
            If provided, will only return contacts with this account.

        created_after : typing.Optional[dt.datetime]
            If provided, will only return objects created after this datetime.

        created_before : typing.Optional[dt.datetime]
            If provided, will only return objects created before this datetime.

        cursor : typing.Optional[str]
            The pagination cursor value.

        email_addresses : typing.Optional[str]
            If provided, will only return contacts matching the email addresses; multiple email_addresses can be separated by commas.

        expand : typing.Optional[ContactsListRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_deleted_data : typing.Optional[bool]
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        modified_after : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge after this date time will be returned.

        modified_before : typing.Optional[dt.datetime]
            If provided, only objects synced by Merge before this date time will be returned.

        page_size : typing.Optional[int]
            Number of results to return per page.

        phone_numbers : typing.Optional[str]
            If provided, will only return contacts matching the phone numbers; multiple phone numbers can be separated by commas.

        remote_id : typing.Optional[str]
            The API provider's ID for the given object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedContactList


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/v1/contacts",
            method="GET",
            params={
                "account_id": account_id,
                "created_after": serialize_datetime(created_after) if created_after is not None else None,
                "created_before": serialize_datetime(created_before) if created_before is not None else None,
                "cursor": cursor,
                "email_addresses": email_addresses,
                "expand": expand,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
                "modified_after": serialize_datetime(modified_after) if modified_after is not None else None,
                "modified_before": serialize_datetime(modified_before) if modified_before is not None else None,
                "page_size": page_size,
                "phone_numbers": phone_numbers,
                "remote_id": remote_id,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PaginatedContactList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        model: ContactRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmContactResponse:
        """
        Creates a `Contact` object with the given values.

        Parameters
        ----------
        model : ContactRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmContactResponse


        Examples
        --------
        from merge.client import AsyncMerge
        from merge.resources.crm import ContactRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.create(
            model=ContactRequest(),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/v1/contacts",
            method="POST",
            params={"is_debug_mode": is_debug_mode, "run_async": run_async},
            json={"model": model},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CrmContactResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(
        self,
        id: str,
        *,
        expand: typing.Optional[ContactsRetrieveRequestExpand] = None,
        include_remote_data: typing.Optional[bool] = None,
        include_remote_fields: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Contact:
        """
        Returns a `Contact` object with the given `id`.

        Parameters
        ----------
        id : str

        expand : typing.Optional[ContactsRetrieveRequestExpand]
            Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Contact


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.retrieve(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/v1/contacts/{jsonable_encoder(id)}",
            method="GET",
            params={
                "expand": expand,
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Contact, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def partial_update(
        self,
        id: str,
        *,
        model: PatchedContactRequest,
        is_debug_mode: typing.Optional[bool] = None,
        run_async: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CrmContactResponse:
        """
        Updates a `Contact` object with the given `id`.

        Parameters
        ----------
        id : str

        model : PatchedContactRequest

        is_debug_mode : typing.Optional[bool]
            Whether to include debug fields (such as log file links) in the response.

        run_async : typing.Optional[bool]
            Whether or not third-party updates should be run asynchronously.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CrmContactResponse


        Examples
        --------
        from merge.client import AsyncMerge
        from merge.resources.crm import PatchedContactRequest

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.partial_update(
            id="id",
            model=PatchedContactRequest(),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/v1/contacts/{jsonable_encoder(id)}",
            method="PATCH",
            params={"is_debug_mode": is_debug_mode, "run_async": run_async},
            json={"model": model},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(CrmContactResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def ignore_create(
        self,
        model_id: str,
        *,
        request: IgnoreCommonModelRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.

        Parameters
        ----------
        model_id : str

        request : IgnoreCommonModelRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from merge.client import AsyncMerge
        from merge.resources.crm import IgnoreCommonModelRequest, ReasonEnum

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.ignore_create(
            model_id="model_id",
            request=IgnoreCommonModelRequest(
                reason=ReasonEnum.GENERAL_CUSTOMER_REQUEST,
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/v1/contacts/ignore/{jsonable_encoder(model_id)}",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_patch_retrieve(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MetaResponse:
        """
        Returns metadata for `CRMContact` PATCHs.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaResponse


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.meta_patch_retrieve(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"crm/v1/contacts/meta/patch/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def meta_post_retrieve(self, *, request_options: typing.Optional[RequestOptions] = None) -> MetaResponse:
        """
        Returns metadata for `CRMContact` POSTs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MetaResponse


        Examples
        --------
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.meta_post_retrieve()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/v1/contacts/meta/post", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MetaResponse, _response.json())  # type: ignore
        try:
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
            Whether to include data that was marked as deleted by third party webhooks.

        include_remote_data : typing.Optional[bool]
            Whether to include the original data Merge fetched from the third-party to produce these models.

        include_remote_fields : typing.Optional[bool]
            Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.

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
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.crm.contacts.remote_field_classes_list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "crm/v1/contacts/remote-field-classes",
            method="GET",
            params={
                "cursor": cursor,
                "include_deleted_data": include_deleted_data,
                "include_remote_data": include_remote_data,
                "include_remote_fields": include_remote_fields,
                "is_common_model_field": is_common_model_field,
                "page_size": page_size,
            },
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(PaginatedRemoteFieldClassList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
