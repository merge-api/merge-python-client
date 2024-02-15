# This file was auto-generated by Fern from our API Definition.

import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import MergeEnvironment
from .resources.accounting.client import AccountingClient, AsyncAccountingClient
from .resources.ats.client import AsyncAtsClient, AtsClient
from .resources.crm.client import AsyncCrmClient, CrmClient
from .resources.filestorage.client import AsyncFilestorageClient, FilestorageClient
from .resources.hris.client import AsyncHrisClient, HrisClient
from .resources.ticketing.client import AsyncTicketingClient, TicketingClient


class Merge:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MergeEnvironment = MergeEnvironment.PRODUCTION,
        account_token: typing.Optional[str] = None,
        api_key: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            account_token=account_token,
            api_key=api_key,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.ats = AtsClient(client_wrapper=self._client_wrapper)
        self.filestorage = FilestorageClient(client_wrapper=self._client_wrapper)
        self.crm = CrmClient(client_wrapper=self._client_wrapper)
        self.hris = HrisClient(client_wrapper=self._client_wrapper)
        self.ticketing = TicketingClient(client_wrapper=self._client_wrapper)
        self.accounting = AccountingClient(client_wrapper=self._client_wrapper)


class AsyncMerge:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MergeEnvironment = MergeEnvironment.PRODUCTION,
        account_token: typing.Optional[str] = None,
        api_key: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            account_token=account_token,
            api_key=api_key,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.ats = AsyncAtsClient(client_wrapper=self._client_wrapper)
        self.filestorage = AsyncFilestorageClient(client_wrapper=self._client_wrapper)
        self.crm = AsyncCrmClient(client_wrapper=self._client_wrapper)
        self.hris = AsyncHrisClient(client_wrapper=self._client_wrapper)
        self.ticketing = AsyncTicketingClient(client_wrapper=self._client_wrapper)
        self.accounting = AsyncAccountingClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: MergeEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
