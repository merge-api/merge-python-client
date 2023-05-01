# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .leads import Leads, AsyncLeads
from .notes import Notes, AsyncNotes
from .tasks import Tasks, AsyncTasks
from .users import Users, AsyncUsers
from .issues import Issues, AsyncIssues
from .stages import Stages, AsyncStages
from .accounts import Accounts, AsyncAccounts
from .contacts import Contacts, AsyncContacts
from ..._resource import SyncAPIResource, AsyncAPIResource
from .engagements import Engagements, AsyncEngagements
from .link_tokens import LinkTokens, AsyncLinkTokens
from .remote_keys import RemoteKeys, AsyncRemoteKeys
from .sync_status import SyncStatus, AsyncSyncStatus
from .opportunities import Opportunities, AsyncOpportunities
from .account_tokens import AccountTokens, AsyncAccountTokens
from .custom_objects import CustomObjects, AsyncCustomObjects
from .selective_sync import SelectiveSync, AsyncSelectiveSync
from .account_details import AccountDetails, AsyncAccountDetails
from .linked_accounts import LinkedAccounts, AsyncLinkedAccounts
from .engagement_types import EngagementTypes, AsyncEngagementTypes
from .available_actions import AvailableActions, AsyncAvailableActions
from .webhook_receivers import WebhookReceivers, AsyncWebhookReceivers
from .common_model_scopes import CommonModelScopes, AsyncCommonModelScopes
from .passthrough_requests import PassthroughRequests, AsyncPassthroughRequests
from .custom_object_classes import CustomObjectClasses, AsyncCustomObjectClasses

if TYPE_CHECKING:
    from ..._client import Merge, AsyncMerge

__all__ = ["Crm", "AsyncCrm"]


class Crm(SyncAPIResource):
    accounts: Accounts
    contacts: Contacts
    custom_object_classes: CustomObjectClasses
    custom_objects: CustomObjects
    engagement_types: EngagementTypes
    engagements: Engagements
    leads: Leads
    notes: Notes
    opportunities: Opportunities
    stages: Stages
    tasks: Tasks
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
        self.contacts = Contacts(client)
        self.custom_object_classes = CustomObjectClasses(client)
        self.custom_objects = CustomObjects(client)
        self.engagement_types = EngagementTypes(client)
        self.engagements = Engagements(client)
        self.leads = Leads(client)
        self.notes = Notes(client)
        self.opportunities = Opportunities(client)
        self.stages = Stages(client)
        self.tasks = Tasks(client)
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


class AsyncCrm(AsyncAPIResource):
    accounts: AsyncAccounts
    contacts: AsyncContacts
    custom_object_classes: AsyncCustomObjectClasses
    custom_objects: AsyncCustomObjects
    engagement_types: AsyncEngagementTypes
    engagements: AsyncEngagements
    leads: AsyncLeads
    notes: AsyncNotes
    opportunities: AsyncOpportunities
    stages: AsyncStages
    tasks: AsyncTasks
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
        self.contacts = AsyncContacts(client)
        self.custom_object_classes = AsyncCustomObjectClasses(client)
        self.custom_objects = AsyncCustomObjects(client)
        self.engagement_types = AsyncEngagementTypes(client)
        self.engagements = AsyncEngagements(client)
        self.leads = AsyncLeads(client)
        self.notes = AsyncNotes(client)
        self.opportunities = AsyncOpportunities(client)
        self.stages = AsyncStages(client)
        self.tasks = AsyncTasks(client)
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
