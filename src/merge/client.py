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
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MergeEnvironment
        The environment to use for requests from the client. from .environment import MergeEnvironment



        Defaults to MergeEnvironment.PRODUCTION



    account_token : typing.Optional[str]
    api_key : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from merge import Merge

    client = Merge(
        account_token="YOUR_ACCOUNT_TOKEN",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MergeEnvironment = MergeEnvironment.PRODUCTION,
        account_token: typing.Optional[str] = None,
        api_key: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            account_token=account_token,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.ats = AtsClient(client_wrapper=self._client_wrapper)
        self.crm = CrmClient(client_wrapper=self._client_wrapper)
        self.filestorage = FilestorageClient(client_wrapper=self._client_wrapper)
        self.hris = HrisClient(client_wrapper=self._client_wrapper)
        self.ticketing = TicketingClient(client_wrapper=self._client_wrapper)
        self.accounting = AccountingClient(client_wrapper=self._client_wrapper)


class AsyncMerge:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MergeEnvironment
        The environment to use for requests from the client. from .environment import MergeEnvironment



        Defaults to MergeEnvironment.PRODUCTION



    account_token : typing.Optional[str]
    api_key : typing.Union[str, typing.Callable[[], str]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from merge import AsyncMerge

    client = AsyncMerge(
        account_token="YOUR_ACCOUNT_TOKEN",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MergeEnvironment = MergeEnvironment.PRODUCTION,
        account_token: typing.Optional[str] = None,
        api_key: typing.Union[str, typing.Callable[[], str]],
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            account_token=account_token,
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.ats = AsyncAtsClient(client_wrapper=self._client_wrapper)
        self.crm = AsyncCrmClient(client_wrapper=self._client_wrapper)
        self.filestorage = AsyncFilestorageClient(client_wrapper=self._client_wrapper)
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
