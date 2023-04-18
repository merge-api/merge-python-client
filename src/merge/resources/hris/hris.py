# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .banks import Banks, AsyncBanks
from .teams import Teams, AsyncTeams
from .groups import Groups, AsyncGroups
from .issues import Issues, AsyncIssues
from .benefits import Benefits, AsyncBenefits
from .time_off import TimeOffResource, AsyncTimeOffResource
from .companies import Companies, AsyncCompanies
from .employees import Employees, AsyncEmployees
from .locations import Locations, AsyncLocations
from .pay_groups import PayGroups, AsyncPayGroups
from ..._resource import SyncAPIResource, AsyncAPIResource
from .employments import Employments, AsyncEmployments
from .link_tokens import LinkTokens, AsyncLinkTokens
from .remote_keys import RemoteKeys, AsyncRemoteKeys
from .sync_status import SyncStatus, AsyncSyncStatus
from .payroll_runs import PayrollRuns, AsyncPayrollRuns
from .account_tokens import AccountTokens, AsyncAccountTokens
from .selective_sync import SelectiveSync, AsyncSelectiveSync
from .account_details import AccountDetails, AsyncAccountDetails
from .linked_accounts import LinkedAccounts, AsyncLinkedAccounts
from .available_actions import AvailableActions, AsyncAvailableActions
from .time_off_balances import TimeOffBalances, AsyncTimeOffBalances
from .webhook_receivers import WebhookReceivers, AsyncWebhookReceivers
from .common_model_scopes import CommonModelScopes, AsyncCommonModelScopes
from .passthrough_requests import PassthroughRequests, AsyncPassthroughRequests
from .employee_payroll_runs import EmployeePayrollRuns, AsyncEmployeePayrollRuns

if TYPE_CHECKING:
    from ..._client import Merge, AsyncMerge

__all__ = ["HRIS", "AsyncHRIS"]


class HRIS(SyncAPIResource):
    banks: Banks
    benefits: Benefits
    companies: Companies
    employee_payroll_runs: EmployeePayrollRuns
    employees: Employees
    employments: Employments
    groups: Groups
    locations: Locations
    pay_groups: PayGroups
    payroll_runs: PayrollRuns
    teams: Teams
    time_off: TimeOffResource
    time_off_balances: TimeOffBalances
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
        self.banks = Banks(client)
        self.benefits = Benefits(client)
        self.companies = Companies(client)
        self.employee_payroll_runs = EmployeePayrollRuns(client)
        self.employees = Employees(client)
        self.employments = Employments(client)
        self.groups = Groups(client)
        self.locations = Locations(client)
        self.pay_groups = PayGroups(client)
        self.payroll_runs = PayrollRuns(client)
        self.teams = Teams(client)
        self.time_off = TimeOffResource(client)
        self.time_off_balances = TimeOffBalances(client)
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


class AsyncHRIS(AsyncAPIResource):
    banks: AsyncBanks
    benefits: AsyncBenefits
    companies: AsyncCompanies
    employee_payroll_runs: AsyncEmployeePayrollRuns
    employees: AsyncEmployees
    employments: AsyncEmployments
    groups: AsyncGroups
    locations: AsyncLocations
    pay_groups: AsyncPayGroups
    payroll_runs: AsyncPayrollRuns
    teams: AsyncTeams
    time_off: AsyncTimeOffResource
    time_off_balances: AsyncTimeOffBalances
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
        self.banks = AsyncBanks(client)
        self.benefits = AsyncBenefits(client)
        self.companies = AsyncCompanies(client)
        self.employee_payroll_runs = AsyncEmployeePayrollRuns(client)
        self.employees = AsyncEmployees(client)
        self.employments = AsyncEmployments(client)
        self.groups = AsyncGroups(client)
        self.locations = AsyncLocations(client)
        self.pay_groups = AsyncPayGroups(client)
        self.payroll_runs = AsyncPayrollRuns(client)
        self.teams = AsyncTeams(client)
        self.time_off = AsyncTimeOffResource(client)
        self.time_off_balances = AsyncTimeOffBalances(client)
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
