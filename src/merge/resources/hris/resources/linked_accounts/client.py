# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.remove_none_from_dict import remove_none_from_dict
from ...types.linked_accounts_list_request_category import LinkedAccountsListRequestCategory
from ...types.paginated_account_details_and_actions_list import PaginatedAccountDetailsAndActionsList

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class LinkedAccountsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        category: typing.Optional[LinkedAccountsListRequestCategory] = None,
        cursor: typing.Optional[str] = None,
        end_user_email_address: typing.Optional[str] = None,
        end_user_organization_name: typing.Optional[str] = None,
        end_user_origin_id: typing.Optional[str] = None,
        end_user_origin_ids: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        include_duplicates: typing.Optional[bool] = None,
        integration_name: typing.Optional[str] = None,
        is_test_account: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
    ) -> PaginatedAccountDetailsAndActionsList:
        """
        List linked accounts for your organization.

        Parameters:
            - category: typing.Optional[LinkedAccountsListRequestCategory]. Options: ('hris', 'ats', 'accounting', 'ticketing', 'crm', 'mktg', 'filestorage')

                                                                            * `hris` - hris
                                                                            * `ats` - ats
                                                                            * `accounting` - accounting
                                                                            * `ticketing` - ticketing
                                                                            * `crm` - crm
                                                                            * `mktg` - mktg
                                                                            * `filestorage` - filestorage
            - cursor: typing.Optional[str]. The pagination cursor value.

            - end_user_email_address: typing.Optional[str]. If provided, will only return linked accounts associated with the given email address.

            - end_user_organization_name: typing.Optional[str]. If provided, will only return linked accounts associated with the given organization name.

            - end_user_origin_id: typing.Optional[str]. If provided, will only return linked accounts associated with the given origin ID.

            - end_user_origin_ids: typing.Optional[str]. Comma-separated list of EndUser origin IDs, making it possible to specify multiple EndUsers at once.

            - id: typing.Optional[str].

            - ids: typing.Optional[str]. Comma-separated list of LinkedAccount IDs, making it possible to specify multiple LinkedAccounts at once.

            - include_duplicates: typing.Optional[bool]. If `true`, will include complete production duplicates of the account specified by the `id` query parameter in the response. `id` must be for a complete production linked account.

            - integration_name: typing.Optional[str]. If provided, will only return linked accounts associated with the given integration name.

            - is_test_account: typing.Optional[str]. If included, will only include test linked accounts. If not included, will only include non-test linked accounts.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - status: typing.Optional[str]. Filter by status. Options: `COMPLETE`, `INCOMPLETE`, `RELINK_NEEDED`
        ---
        from merge import LinkedAccountsListRequestCategory
        from merge.client import Merge

        client = Merge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.hris.list(
            category=LinkedAccountsListRequestCategory.ACCOUNTING,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/linked-accounts"),
            params=remove_none_from_dict(
                {
                    "category": category,
                    "cursor": cursor,
                    "end_user_email_address": end_user_email_address,
                    "end_user_organization_name": end_user_organization_name,
                    "end_user_origin_id": end_user_origin_id,
                    "end_user_origin_ids": end_user_origin_ids,
                    "id": id,
                    "ids": ids,
                    "include_duplicates": include_duplicates,
                    "integration_name": integration_name,
                    "is_test_account": is_test_account,
                    "page_size": page_size,
                    "status": status,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedAccountDetailsAndActionsList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncLinkedAccountsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        category: typing.Optional[LinkedAccountsListRequestCategory] = None,
        cursor: typing.Optional[str] = None,
        end_user_email_address: typing.Optional[str] = None,
        end_user_organization_name: typing.Optional[str] = None,
        end_user_origin_id: typing.Optional[str] = None,
        end_user_origin_ids: typing.Optional[str] = None,
        id: typing.Optional[str] = None,
        ids: typing.Optional[str] = None,
        include_duplicates: typing.Optional[bool] = None,
        integration_name: typing.Optional[str] = None,
        is_test_account: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        status: typing.Optional[str] = None,
    ) -> PaginatedAccountDetailsAndActionsList:
        """
        List linked accounts for your organization.

        Parameters:
            - category: typing.Optional[LinkedAccountsListRequestCategory]. Options: ('hris', 'ats', 'accounting', 'ticketing', 'crm', 'mktg', 'filestorage')

                                                                            * `hris` - hris
                                                                            * `ats` - ats
                                                                            * `accounting` - accounting
                                                                            * `ticketing` - ticketing
                                                                            * `crm` - crm
                                                                            * `mktg` - mktg
                                                                            * `filestorage` - filestorage
            - cursor: typing.Optional[str]. The pagination cursor value.

            - end_user_email_address: typing.Optional[str]. If provided, will only return linked accounts associated with the given email address.

            - end_user_organization_name: typing.Optional[str]. If provided, will only return linked accounts associated with the given organization name.

            - end_user_origin_id: typing.Optional[str]. If provided, will only return linked accounts associated with the given origin ID.

            - end_user_origin_ids: typing.Optional[str]. Comma-separated list of EndUser origin IDs, making it possible to specify multiple EndUsers at once.

            - id: typing.Optional[str].

            - ids: typing.Optional[str]. Comma-separated list of LinkedAccount IDs, making it possible to specify multiple LinkedAccounts at once.

            - include_duplicates: typing.Optional[bool]. If `true`, will include complete production duplicates of the account specified by the `id` query parameter in the response. `id` must be for a complete production linked account.

            - integration_name: typing.Optional[str]. If provided, will only return linked accounts associated with the given integration name.

            - is_test_account: typing.Optional[str]. If included, will only include test linked accounts. If not included, will only include non-test linked accounts.

            - page_size: typing.Optional[int]. Number of results to return per page.

            - status: typing.Optional[str]. Filter by status. Options: `COMPLETE`, `INCOMPLETE`, `RELINK_NEEDED`
        ---
        from merge import LinkedAccountsListRequestCategory
        from merge.client import AsyncMerge

        client = AsyncMerge(
            account_token="YOUR_ACCOUNT_TOKEN",
            api_key="YOUR_API_KEY",
        )
        await client.hris.list(
            category=LinkedAccountsListRequestCategory.ACCOUNTING,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/hris/v1/linked-accounts"),
            params=remove_none_from_dict(
                {
                    "category": category,
                    "cursor": cursor,
                    "end_user_email_address": end_user_email_address,
                    "end_user_organization_name": end_user_organization_name,
                    "end_user_origin_id": end_user_origin_id,
                    "end_user_origin_ids": end_user_origin_ids,
                    "id": id,
                    "ids": ids,
                    "include_duplicates": include_duplicates,
                    "integration_name": integration_name,
                    "is_test_account": is_test_account,
                    "page_size": page_size,
                    "status": status,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedAccountDetailsAndActionsList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
