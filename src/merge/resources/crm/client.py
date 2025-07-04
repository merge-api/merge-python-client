# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawCrmClient, RawCrmClient
from .resources.account_details.client import AccountDetailsClient, AsyncAccountDetailsClient
from .resources.account_token.client import AccountTokenClient, AsyncAccountTokenClient
from .resources.accounts.client import AccountsClient, AsyncAccountsClient
from .resources.association_types.client import AssociationTypesClient, AsyncAssociationTypesClient
from .resources.associations.client import AssociationsClient, AsyncAssociationsClient
from .resources.async_passthrough.client import AsyncAsyncPassthroughClient
from .resources.async_passthrough.client import (
    AsyncPassthroughClient as resources_crm_resources_async_passthrough_client_AsyncPassthroughClient,
)
from .resources.audit_trail.client import AsyncAuditTrailClient, AuditTrailClient
from .resources.available_actions.client import AsyncAvailableActionsClient, AvailableActionsClient
from .resources.contacts.client import AsyncContactsClient, ContactsClient
from .resources.custom_object_classes.client import AsyncCustomObjectClassesClient, CustomObjectClassesClient
from .resources.custom_objects.client import AsyncCustomObjectsClient, CustomObjectsClient
from .resources.delete_account.client import AsyncDeleteAccountClient, DeleteAccountClient
from .resources.engagement_types.client import AsyncEngagementTypesClient, EngagementTypesClient
from .resources.engagements.client import AsyncEngagementsClient, EngagementsClient
from .resources.field_mapping.client import AsyncFieldMappingClient, FieldMappingClient
from .resources.force_resync.client import AsyncForceResyncClient, ForceResyncClient
from .resources.generate_key.client import AsyncGenerateKeyClient, GenerateKeyClient
from .resources.issues.client import AsyncIssuesClient, IssuesClient
from .resources.leads.client import AsyncLeadsClient, LeadsClient
from .resources.link_token.client import AsyncLinkTokenClient, LinkTokenClient
from .resources.linked_accounts.client import AsyncLinkedAccountsClient, LinkedAccountsClient
from .resources.notes.client import AsyncNotesClient, NotesClient
from .resources.opportunities.client import AsyncOpportunitiesClient, OpportunitiesClient
from .resources.passthrough.client import (
    AsyncPassthroughClient as resources_crm_resources_passthrough_client_AsyncPassthroughClient,
)
from .resources.passthrough.client import PassthroughClient
from .resources.regenerate_key.client import AsyncRegenerateKeyClient, RegenerateKeyClient
from .resources.scopes.client import AsyncScopesClient, ScopesClient
from .resources.stages.client import AsyncStagesClient, StagesClient
from .resources.sync_status.client import AsyncSyncStatusClient, SyncStatusClient
from .resources.tasks.client import AsyncTasksClient, TasksClient
from .resources.users.client import AsyncUsersClient, UsersClient
from .resources.webhook_receivers.client import AsyncWebhookReceiversClient, WebhookReceiversClient


class CrmClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrmClient(client_wrapper=client_wrapper)
        self.account_details = AccountDetailsClient(client_wrapper=client_wrapper)

        self.account_token = AccountTokenClient(client_wrapper=client_wrapper)

        self.accounts = AccountsClient(client_wrapper=client_wrapper)

        self.async_passthrough = resources_crm_resources_async_passthrough_client_AsyncPassthroughClient(
            client_wrapper=client_wrapper
        )

        self.audit_trail = AuditTrailClient(client_wrapper=client_wrapper)

        self.available_actions = AvailableActionsClient(client_wrapper=client_wrapper)

        self.contacts = ContactsClient(client_wrapper=client_wrapper)

        self.custom_object_classes = CustomObjectClassesClient(client_wrapper=client_wrapper)

        self.association_types = AssociationTypesClient(client_wrapper=client_wrapper)

        self.custom_objects = CustomObjectsClient(client_wrapper=client_wrapper)

        self.associations = AssociationsClient(client_wrapper=client_wrapper)

        self.scopes = ScopesClient(client_wrapper=client_wrapper)

        self.delete_account = DeleteAccountClient(client_wrapper=client_wrapper)

        self.engagement_types = EngagementTypesClient(client_wrapper=client_wrapper)

        self.engagements = EngagementsClient(client_wrapper=client_wrapper)

        self.field_mapping = FieldMappingClient(client_wrapper=client_wrapper)

        self.generate_key = GenerateKeyClient(client_wrapper=client_wrapper)

        self.issues = IssuesClient(client_wrapper=client_wrapper)

        self.leads = LeadsClient(client_wrapper=client_wrapper)

        self.link_token = LinkTokenClient(client_wrapper=client_wrapper)

        self.linked_accounts = LinkedAccountsClient(client_wrapper=client_wrapper)

        self.notes = NotesClient(client_wrapper=client_wrapper)

        self.opportunities = OpportunitiesClient(client_wrapper=client_wrapper)

        self.passthrough = PassthroughClient(client_wrapper=client_wrapper)

        self.regenerate_key = RegenerateKeyClient(client_wrapper=client_wrapper)

        self.stages = StagesClient(client_wrapper=client_wrapper)

        self.sync_status = SyncStatusClient(client_wrapper=client_wrapper)

        self.force_resync = ForceResyncClient(client_wrapper=client_wrapper)

        self.tasks = TasksClient(client_wrapper=client_wrapper)

        self.users = UsersClient(client_wrapper=client_wrapper)

        self.webhook_receivers = WebhookReceiversClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrmClient
        """
        return self._raw_client


class AsyncCrmClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrmClient(client_wrapper=client_wrapper)
        self.account_details = AsyncAccountDetailsClient(client_wrapper=client_wrapper)

        self.account_token = AsyncAccountTokenClient(client_wrapper=client_wrapper)

        self.accounts = AsyncAccountsClient(client_wrapper=client_wrapper)

        self.async_passthrough = AsyncAsyncPassthroughClient(client_wrapper=client_wrapper)

        self.audit_trail = AsyncAuditTrailClient(client_wrapper=client_wrapper)

        self.available_actions = AsyncAvailableActionsClient(client_wrapper=client_wrapper)

        self.contacts = AsyncContactsClient(client_wrapper=client_wrapper)

        self.custom_object_classes = AsyncCustomObjectClassesClient(client_wrapper=client_wrapper)

        self.association_types = AsyncAssociationTypesClient(client_wrapper=client_wrapper)

        self.custom_objects = AsyncCustomObjectsClient(client_wrapper=client_wrapper)

        self.associations = AsyncAssociationsClient(client_wrapper=client_wrapper)

        self.scopes = AsyncScopesClient(client_wrapper=client_wrapper)

        self.delete_account = AsyncDeleteAccountClient(client_wrapper=client_wrapper)

        self.engagement_types = AsyncEngagementTypesClient(client_wrapper=client_wrapper)

        self.engagements = AsyncEngagementsClient(client_wrapper=client_wrapper)

        self.field_mapping = AsyncFieldMappingClient(client_wrapper=client_wrapper)

        self.generate_key = AsyncGenerateKeyClient(client_wrapper=client_wrapper)

        self.issues = AsyncIssuesClient(client_wrapper=client_wrapper)

        self.leads = AsyncLeadsClient(client_wrapper=client_wrapper)

        self.link_token = AsyncLinkTokenClient(client_wrapper=client_wrapper)

        self.linked_accounts = AsyncLinkedAccountsClient(client_wrapper=client_wrapper)

        self.notes = AsyncNotesClient(client_wrapper=client_wrapper)

        self.opportunities = AsyncOpportunitiesClient(client_wrapper=client_wrapper)

        self.passthrough = resources_crm_resources_passthrough_client_AsyncPassthroughClient(
            client_wrapper=client_wrapper
        )

        self.regenerate_key = AsyncRegenerateKeyClient(client_wrapper=client_wrapper)

        self.stages = AsyncStagesClient(client_wrapper=client_wrapper)

        self.sync_status = AsyncSyncStatusClient(client_wrapper=client_wrapper)

        self.force_resync = AsyncForceResyncClient(client_wrapper=client_wrapper)

        self.tasks = AsyncTasksClient(client_wrapper=client_wrapper)

        self.users = AsyncUsersClient(client_wrapper=client_wrapper)

        self.webhook_receivers = AsyncWebhookReceiversClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrmClient
        """
        return self._raw_client
