# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
from .resources.account_details.client import AccountDetailsClient
from .resources.account_token.client import AccountTokenClient
from .resources.activities.client import ActivitiesClient
from .resources.applications.client import ApplicationsClient
from .resources.async_passthrough.client import (
    AsyncPassthroughClient as resources_ats_resources_async_passthrough_client_AsyncPassthroughClient,
)
from .resources.attachments.client import AttachmentsClient
from .resources.audit_trail.client import AuditTrailClient
from .resources.available_actions.client import AvailableActionsClient
from .resources.candidates.client import CandidatesClient
from .resources.scopes.client import ScopesClient
from .resources.delete_account.client import DeleteAccountClient
from .resources.departments.client import DepartmentsClient
from .resources.eeocs.client import EeocsClient
from .resources.field_mapping.client import FieldMappingClient
from .resources.generate_key.client import GenerateKeyClient
from .resources.interviews.client import InterviewsClient
from .resources.issues.client import IssuesClient
from .resources.job_interview_stages.client import JobInterviewStagesClient
from .resources.job_postings.client import JobPostingsClient
from .resources.jobs.client import JobsClient
from .resources.link_token.client import LinkTokenClient
from .resources.linked_accounts.client import LinkedAccountsClient
from .resources.offers.client import OffersClient
from .resources.offices.client import OfficesClient
from .resources.passthrough.client import PassthroughClient
from .resources.regenerate_key.client import RegenerateKeyClient
from .resources.reject_reasons.client import RejectReasonsClient
from .resources.scorecards.client import ScorecardsClient
from .resources.sync_status.client import SyncStatusClient
from .resources.force_resync.client import ForceResyncClient
from .resources.tags.client import TagsClient
from .resources.users.client import UsersClient
from .resources.webhook_receivers.client import WebhookReceiversClient
from ...core.client_wrapper import AsyncClientWrapper
from .resources.account_details.client import AsyncAccountDetailsClient
from .resources.account_token.client import AsyncAccountTokenClient
from .resources.activities.client import AsyncActivitiesClient
from .resources.applications.client import AsyncApplicationsClient
from .resources.async_passthrough.client import AsyncAsyncPassthroughClient
from .resources.attachments.client import AsyncAttachmentsClient
from .resources.audit_trail.client import AsyncAuditTrailClient
from .resources.available_actions.client import AsyncAvailableActionsClient
from .resources.candidates.client import AsyncCandidatesClient
from .resources.scopes.client import AsyncScopesClient
from .resources.delete_account.client import AsyncDeleteAccountClient
from .resources.departments.client import AsyncDepartmentsClient
from .resources.eeocs.client import AsyncEeocsClient
from .resources.field_mapping.client import AsyncFieldMappingClient
from .resources.generate_key.client import AsyncGenerateKeyClient
from .resources.interviews.client import AsyncInterviewsClient
from .resources.issues.client import AsyncIssuesClient
from .resources.job_interview_stages.client import AsyncJobInterviewStagesClient
from .resources.job_postings.client import AsyncJobPostingsClient
from .resources.jobs.client import AsyncJobsClient
from .resources.link_token.client import AsyncLinkTokenClient
from .resources.linked_accounts.client import AsyncLinkedAccountsClient
from .resources.offers.client import AsyncOffersClient
from .resources.offices.client import AsyncOfficesClient
from .resources.passthrough.client import (
    AsyncPassthroughClient as resources_ats_resources_passthrough_client_AsyncPassthroughClient,
)
from .resources.regenerate_key.client import AsyncRegenerateKeyClient
from .resources.reject_reasons.client import AsyncRejectReasonsClient
from .resources.scorecards.client import AsyncScorecardsClient
from .resources.sync_status.client import AsyncSyncStatusClient
from .resources.force_resync.client import AsyncForceResyncClient
from .resources.tags.client import AsyncTagsClient
from .resources.users.client import AsyncUsersClient
from .resources.webhook_receivers.client import AsyncWebhookReceiversClient


class AtsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.account_details = AccountDetailsClient(client_wrapper=self._client_wrapper)
        self.account_token = AccountTokenClient(client_wrapper=self._client_wrapper)
        self.activities = ActivitiesClient(client_wrapper=self._client_wrapper)
        self.applications = ApplicationsClient(client_wrapper=self._client_wrapper)
        self.async_passthrough = resources_ats_resources_async_passthrough_client_AsyncPassthroughClient(
            client_wrapper=self._client_wrapper
        )
        self.attachments = AttachmentsClient(client_wrapper=self._client_wrapper)
        self.audit_trail = AuditTrailClient(client_wrapper=self._client_wrapper)
        self.available_actions = AvailableActionsClient(client_wrapper=self._client_wrapper)
        self.candidates = CandidatesClient(client_wrapper=self._client_wrapper)
        self.scopes = ScopesClient(client_wrapper=self._client_wrapper)
        self.delete_account = DeleteAccountClient(client_wrapper=self._client_wrapper)
        self.departments = DepartmentsClient(client_wrapper=self._client_wrapper)
        self.eeocs = EeocsClient(client_wrapper=self._client_wrapper)
        self.field_mapping = FieldMappingClient(client_wrapper=self._client_wrapper)
        self.generate_key = GenerateKeyClient(client_wrapper=self._client_wrapper)
        self.interviews = InterviewsClient(client_wrapper=self._client_wrapper)
        self.issues = IssuesClient(client_wrapper=self._client_wrapper)
        self.job_interview_stages = JobInterviewStagesClient(client_wrapper=self._client_wrapper)
        self.job_postings = JobPostingsClient(client_wrapper=self._client_wrapper)
        self.jobs = JobsClient(client_wrapper=self._client_wrapper)
        self.link_token = LinkTokenClient(client_wrapper=self._client_wrapper)
        self.linked_accounts = LinkedAccountsClient(client_wrapper=self._client_wrapper)
        self.offers = OffersClient(client_wrapper=self._client_wrapper)
        self.offices = OfficesClient(client_wrapper=self._client_wrapper)
        self.passthrough = PassthroughClient(client_wrapper=self._client_wrapper)
        self.regenerate_key = RegenerateKeyClient(client_wrapper=self._client_wrapper)
        self.reject_reasons = RejectReasonsClient(client_wrapper=self._client_wrapper)
        self.scorecards = ScorecardsClient(client_wrapper=self._client_wrapper)
        self.sync_status = SyncStatusClient(client_wrapper=self._client_wrapper)
        self.force_resync = ForceResyncClient(client_wrapper=self._client_wrapper)
        self.tags = TagsClient(client_wrapper=self._client_wrapper)
        self.users = UsersClient(client_wrapper=self._client_wrapper)
        self.webhook_receivers = WebhookReceiversClient(client_wrapper=self._client_wrapper)


class AsyncAtsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.account_details = AsyncAccountDetailsClient(client_wrapper=self._client_wrapper)
        self.account_token = AsyncAccountTokenClient(client_wrapper=self._client_wrapper)
        self.activities = AsyncActivitiesClient(client_wrapper=self._client_wrapper)
        self.applications = AsyncApplicationsClient(client_wrapper=self._client_wrapper)
        self.async_passthrough = AsyncAsyncPassthroughClient(client_wrapper=self._client_wrapper)
        self.attachments = AsyncAttachmentsClient(client_wrapper=self._client_wrapper)
        self.audit_trail = AsyncAuditTrailClient(client_wrapper=self._client_wrapper)
        self.available_actions = AsyncAvailableActionsClient(client_wrapper=self._client_wrapper)
        self.candidates = AsyncCandidatesClient(client_wrapper=self._client_wrapper)
        self.scopes = AsyncScopesClient(client_wrapper=self._client_wrapper)
        self.delete_account = AsyncDeleteAccountClient(client_wrapper=self._client_wrapper)
        self.departments = AsyncDepartmentsClient(client_wrapper=self._client_wrapper)
        self.eeocs = AsyncEeocsClient(client_wrapper=self._client_wrapper)
        self.field_mapping = AsyncFieldMappingClient(client_wrapper=self._client_wrapper)
        self.generate_key = AsyncGenerateKeyClient(client_wrapper=self._client_wrapper)
        self.interviews = AsyncInterviewsClient(client_wrapper=self._client_wrapper)
        self.issues = AsyncIssuesClient(client_wrapper=self._client_wrapper)
        self.job_interview_stages = AsyncJobInterviewStagesClient(client_wrapper=self._client_wrapper)
        self.job_postings = AsyncJobPostingsClient(client_wrapper=self._client_wrapper)
        self.jobs = AsyncJobsClient(client_wrapper=self._client_wrapper)
        self.link_token = AsyncLinkTokenClient(client_wrapper=self._client_wrapper)
        self.linked_accounts = AsyncLinkedAccountsClient(client_wrapper=self._client_wrapper)
        self.offers = AsyncOffersClient(client_wrapper=self._client_wrapper)
        self.offices = AsyncOfficesClient(client_wrapper=self._client_wrapper)
        self.passthrough = resources_ats_resources_passthrough_client_AsyncPassthroughClient(
            client_wrapper=self._client_wrapper
        )
        self.regenerate_key = AsyncRegenerateKeyClient(client_wrapper=self._client_wrapper)
        self.reject_reasons = AsyncRejectReasonsClient(client_wrapper=self._client_wrapper)
        self.scorecards = AsyncScorecardsClient(client_wrapper=self._client_wrapper)
        self.sync_status = AsyncSyncStatusClient(client_wrapper=self._client_wrapper)
        self.force_resync = AsyncForceResyncClient(client_wrapper=self._client_wrapper)
        self.tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        self.webhook_receivers = AsyncWebhookReceiversClient(client_wrapper=self._client_wrapper)
