# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .tags import Tags, AsyncTags
from .teams import Teams, AsyncTeams
from .users import Users, AsyncUsers
from .issues import Issues, AsyncIssues
from .tickets import Tickets, AsyncTickets
from .accounts import Accounts, AsyncAccounts
from .comments import Comments, AsyncComments
from .contacts import Contacts, AsyncContacts
from .projects import Projects, AsyncProjects
from ..._resource import SyncAPIResource, AsyncAPIResource
from .attachments import Attachments, AsyncAttachments
from .collections import Collections, AsyncCollections
from .link_tokens import LinkTokens, AsyncLinkTokens
from .remote_keys import RemoteKeys, AsyncRemoteKeys
from .sync_status import SyncStatus, AsyncSyncStatus
from .account_tokens import AccountTokens, AsyncAccountTokens
from .selective_sync import SelectiveSync, AsyncSelectiveSync
from .account_details import AccountDetails, AsyncAccountDetails
from .linked_accounts import LinkedAccounts, AsyncLinkedAccounts
from .available_actions import AvailableActions, AsyncAvailableActions
from .webhook_receivers import WebhookReceivers, AsyncWebhookReceivers
from .common_model_scopes import CommonModelScopes, AsyncCommonModelScopes
from .passthrough_requests import PassthroughRequests, AsyncPassthroughRequests

if TYPE_CHECKING:
    from ..._client import Merge, AsyncMerge

__all__ = ["Ticketing", "AsyncTicketing"]


class Ticketing(SyncAPIResource):
    accounts: Accounts
    attachments: Attachments
    collections: Collections
    comments: Comments
    contacts: Contacts
    projects: Projects
    tags: Tags
    teams: Teams
    tickets: Tickets
    users: Users
    account_details: AccountDetails
    account_tokens: AccountTokens
    link_tokens: LinkTokens
    available_actions: AvailableActions
    remote_keys: RemoteKeys
    issues: Issues
    common_model_scopes: CommonModelScopes
    passthrough_requests: PassthroughRequests
    sync_status: SyncStatus
    webhook_receivers: WebhookReceivers
    linked_accounts: LinkedAccounts
    selective_sync: SelectiveSync

    def __init__(self, client: Merge) -> None:
        super().__init__(client)
        self.accounts = Accounts(client)
        self.attachments = Attachments(client)
        self.collections = Collections(client)
        self.comments = Comments(client)
        self.contacts = Contacts(client)
        self.projects = Projects(client)
        self.tags = Tags(client)
        self.teams = Teams(client)
        self.tickets = Tickets(client)
        self.users = Users(client)
        self.account_details = AccountDetails(client)
        self.account_tokens = AccountTokens(client)
        self.link_tokens = LinkTokens(client)
        self.available_actions = AvailableActions(client)
        self.remote_keys = RemoteKeys(client)
        self.issues = Issues(client)
        self.common_model_scopes = CommonModelScopes(client)
        self.passthrough_requests = PassthroughRequests(client)
        self.sync_status = SyncStatus(client)
        self.webhook_receivers = WebhookReceivers(client)
        self.linked_accounts = LinkedAccounts(client)
        self.selective_sync = SelectiveSync(client)


class AsyncTicketing(AsyncAPIResource):
    accounts: AsyncAccounts
    attachments: AsyncAttachments
    collections: AsyncCollections
    comments: AsyncComments
    contacts: AsyncContacts
    projects: AsyncProjects
    tags: AsyncTags
    teams: AsyncTeams
    tickets: AsyncTickets
    users: AsyncUsers
    account_details: AsyncAccountDetails
    account_tokens: AsyncAccountTokens
    link_tokens: AsyncLinkTokens
    available_actions: AsyncAvailableActions
    remote_keys: AsyncRemoteKeys
    issues: AsyncIssues
    common_model_scopes: AsyncCommonModelScopes
    passthrough_requests: AsyncPassthroughRequests
    sync_status: AsyncSyncStatus
    webhook_receivers: AsyncWebhookReceivers
    linked_accounts: AsyncLinkedAccounts
    selective_sync: AsyncSelectiveSync

    def __init__(self, client: AsyncMerge) -> None:
        super().__init__(client)
        self.accounts = AsyncAccounts(client)
        self.attachments = AsyncAttachments(client)
        self.collections = AsyncCollections(client)
        self.comments = AsyncComments(client)
        self.contacts = AsyncContacts(client)
        self.projects = AsyncProjects(client)
        self.tags = AsyncTags(client)
        self.teams = AsyncTeams(client)
        self.tickets = AsyncTickets(client)
        self.users = AsyncUsers(client)
        self.account_details = AsyncAccountDetails(client)
        self.account_tokens = AsyncAccountTokens(client)
        self.link_tokens = AsyncLinkTokens(client)
        self.available_actions = AsyncAvailableActions(client)
        self.remote_keys = AsyncRemoteKeys(client)
        self.issues = AsyncIssues(client)
        self.common_model_scopes = AsyncCommonModelScopes(client)
        self.passthrough_requests = AsyncPassthroughRequests(client)
        self.sync_status = AsyncSyncStatus(client)
        self.webhook_receivers = AsyncWebhookReceivers(client)
        self.linked_accounts = AsyncLinkedAccounts(client)
        self.selective_sync = AsyncSelectiveSync(client)
