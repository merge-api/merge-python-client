# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .jobs import Jobs, AsyncJobs
from .tags import Tags, AsyncTags
from .eeocs import EEOCs, AsyncEEOCs
from .users import Users, AsyncUsers
from .issues import Issues, AsyncIssues
from .offers import Offers, AsyncOffers
from .offices import Offices, AsyncOffices
from .activities import Activities, AsyncActivities
from .candidates import Candidates, AsyncCandidates
from .interviews import Interviews, AsyncInterviews
from .scorecards import Scorecards, AsyncScorecards
from ..._resource import SyncAPIResource, AsyncAPIResource
from .attachments import Attachments, AsyncAttachments
from .departments import Departments, AsyncDepartments
from .link_tokens import LinkTokens, AsyncLinkTokens
from .remote_keys import RemoteKeys, AsyncRemoteKeys
from .sync_status import SyncStatus, AsyncSyncStatus
from .applications import Applications, AsyncApplications
from .account_tokens import AccountTokens, AsyncAccountTokens
from .reject_reasons import RejectReasons, AsyncRejectReasons
from .selective_sync import SelectiveSync, AsyncSelectiveSync
from .account_details import AccountDetails, AsyncAccountDetails
from .linked_accounts import LinkedAccounts, AsyncLinkedAccounts
from .available_actions import AvailableActions, AsyncAvailableActions
from .webhook_receivers import WebhookReceivers, AsyncWebhookReceivers
from .common_model_scopes import CommonModelScopes, AsyncCommonModelScopes
from .job_interview_stages import JobInterviewStages, AsyncJobInterviewStages
from .passthrough_requests import PassthroughRequests, AsyncPassthroughRequests

if TYPE_CHECKING:
    from ..._client import Merge, AsyncMerge

__all__ = ["ATS", "AsyncATS"]


class ATS(SyncAPIResource):
    activities: Activities
    applications: Applications
    attachments: Attachments
    candidates: Candidates
    departments: Departments
    eeocs: EEOCs
    interviews: Interviews
    job_interview_stages: JobInterviewStages
    jobs: Jobs
    offers: Offers
    offices: Offices
    reject_reasons: RejectReasons
    scorecards: Scorecards
    tags: Tags
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
        self.activities = Activities(client)
        self.applications = Applications(client)
        self.attachments = Attachments(client)
        self.candidates = Candidates(client)
        self.departments = Departments(client)
        self.eeocs = EEOCs(client)
        self.interviews = Interviews(client)
        self.job_interview_stages = JobInterviewStages(client)
        self.jobs = Jobs(client)
        self.offers = Offers(client)
        self.offices = Offices(client)
        self.reject_reasons = RejectReasons(client)
        self.scorecards = Scorecards(client)
        self.tags = Tags(client)
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


class AsyncATS(AsyncAPIResource):
    activities: AsyncActivities
    applications: AsyncApplications
    attachments: AsyncAttachments
    candidates: AsyncCandidates
    departments: AsyncDepartments
    eeocs: AsyncEEOCs
    interviews: AsyncInterviews
    job_interview_stages: AsyncJobInterviewStages
    jobs: AsyncJobs
    offers: AsyncOffers
    offices: AsyncOffices
    reject_reasons: AsyncRejectReasons
    scorecards: AsyncScorecards
    tags: AsyncTags
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
        self.activities = AsyncActivities(client)
        self.applications = AsyncApplications(client)
        self.attachments = AsyncAttachments(client)
        self.candidates = AsyncCandidates(client)
        self.departments = AsyncDepartments(client)
        self.eeocs = AsyncEEOCs(client)
        self.interviews = AsyncInterviews(client)
        self.job_interview_stages = AsyncJobInterviewStages(client)
        self.jobs = AsyncJobs(client)
        self.offers = AsyncOffers(client)
        self.offices = AsyncOffices(client)
        self.reject_reasons = AsyncRejectReasons(client)
        self.scorecards = AsyncScorecards(client)
        self.tags = AsyncTags(client)
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
