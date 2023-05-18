# Shared Types

```python
from merge.types import (
    Account,
    AccountDetail,
    AccountDetailsAndActions,
    AccountToken,
    Address,
    Attachment,
    AvailableAction,
    CommonModelScope,
    ConditionSchema,
    Contact,
    Country,
    DebugLog,
    Issue,
    LinkToken,
    LinkedAccountSelectiveSyncConfiguration,
    MetaResponse,
    RemoteData,
    RemoteFieldClass,
    RemoteKey,
    RemoteResponse,
    RemoteUser,
    SyncStatus,
    Tag,
    Team,
    ValidationError,
    ValidationWarning,
    WebhookReceiver,
)
```

# HRIS

## Banks

Types:

```python
from merge.types.hris import BankInfo
```

Methods:

- <code title="get /hris/v1/bank-info/{id}">client.hris.banks.<a href="./src/merge/resources/hris/banks.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/bank_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/bank_info.py">BankInfo</a></code>
- <code title="get /hris/v1/bank-info">client.hris.banks.<a href="./src/merge/resources/hris/banks.py">list</a>(\*\*<a href="src/merge/types/hris/bank_list_params.py">params</a>) -> <a href="./src/merge/types/hris/bank_info.py">SyncPage[BankInfo]</a></code>

## Benefits

Types:

```python
from merge.types.hris import Benefit
```

Methods:

- <code title="get /hris/v1/benefits/{id}">client.hris.benefits.<a href="./src/merge/resources/hris/benefits.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/benefit_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/benefit.py">Benefit</a></code>
- <code title="get /hris/v1/benefits">client.hris.benefits.<a href="./src/merge/resources/hris/benefits.py">list</a>(\*\*<a href="src/merge/types/hris/benefit_list_params.py">params</a>) -> <a href="./src/merge/types/hris/benefit.py">SyncPage[Benefit]</a></code>

## Companies

Types:

```python
from merge.types.hris import Company
```

Methods:

- <code title="get /hris/v1/companies/{id}">client.hris.companies.<a href="./src/merge/resources/hris/companies.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/company_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/company.py">Company</a></code>
- <code title="get /hris/v1/companies">client.hris.companies.<a href="./src/merge/resources/hris/companies.py">list</a>(\*\*<a href="src/merge/types/hris/company_list_params.py">params</a>) -> <a href="./src/merge/types/hris/company.py">SyncPage[Company]</a></code>

## EmployeePayrollRuns

Types:

```python
from merge.types.hris import EmployeePayrollRun
```

Methods:

- <code title="get /hris/v1/employee-payroll-runs/{id}">client.hris.employee_payroll_runs.<a href="./src/merge/resources/hris/employee_payroll_runs.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/employee_payroll_run_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/employee_payroll_run.py">EmployeePayrollRun</a></code>
- <code title="get /hris/v1/employee-payroll-runs">client.hris.employee_payroll_runs.<a href="./src/merge/resources/hris/employee_payroll_runs.py">list</a>(\*\*<a href="src/merge/types/hris/employee_payroll_run_list_params.py">params</a>) -> <a href="./src/merge/types/hris/employee_payroll_run.py">SyncPage[EmployeePayrollRun]</a></code>

## Employees

Types:

```python
from merge.types.hris import CreatedEmployeeResponse, Employee
```

Methods:

- <code title="post /hris/v1/employees">client.hris.employees.<a href="./src/merge/resources/hris/employees/employees.py">create</a>(\*\*<a href="src/merge/types/hris/employee_create_params.py">params</a>) -> <a href="./src/merge/types/hris/created_employee_response.py">CreatedEmployeeResponse</a></code>
- <code title="get /hris/v1/employees/{id}">client.hris.employees.<a href="./src/merge/resources/hris/employees/employees.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/employee_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/employee.py">Employee</a></code>
- <code title="get /hris/v1/employees">client.hris.employees.<a href="./src/merge/resources/hris/employees/employees.py">list</a>(\*\*<a href="src/merge/types/hris/employee_list_params.py">params</a>) -> <a href="./src/merge/types/hris/employee.py">SyncPage[Employee]</a></code>
- <code title="post /hris/v1/employees/ignore/{model_id}">client.hris.employees.<a href="./src/merge/resources/hris/employees/employees.py">ignore</a>(model_id, \*\*<a href="src/merge/types/hris/employee_ignore_params.py">params</a>) -> None</code>

### Meta

Methods:

- <code title="get /hris/v1/employees/meta/post">client.hris.employees.meta.<a href="./src/merge/resources/hris/employees/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Employments

Types:

```python
from merge.types.hris import Employment
```

Methods:

- <code title="get /hris/v1/employments/{id}">client.hris.employments.<a href="./src/merge/resources/hris/employments.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/employment_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/employment.py">Employment</a></code>
- <code title="get /hris/v1/employments">client.hris.employments.<a href="./src/merge/resources/hris/employments.py">list</a>(\*\*<a href="src/merge/types/hris/employment_list_params.py">params</a>) -> <a href="./src/merge/types/hris/employment.py">SyncPage[Employment]</a></code>

## Groups

Types:

```python
from merge.types.hris import Group
```

Methods:

- <code title="get /hris/v1/groups/{id}">client.hris.groups.<a href="./src/merge/resources/hris/groups.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/group_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/group.py">Group</a></code>
- <code title="get /hris/v1/groups">client.hris.groups.<a href="./src/merge/resources/hris/groups.py">list</a>(\*\*<a href="src/merge/types/hris/group_list_params.py">params</a>) -> <a href="./src/merge/types/hris/group.py">SyncPage[Group]</a></code>

## Locations

Types:

```python
from merge.types.hris import Location
```

Methods:

- <code title="get /hris/v1/locations/{id}">client.hris.locations.<a href="./src/merge/resources/hris/locations.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/location_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/location.py">Location</a></code>
- <code title="get /hris/v1/locations">client.hris.locations.<a href="./src/merge/resources/hris/locations.py">list</a>(\*\*<a href="src/merge/types/hris/location_list_params.py">params</a>) -> <a href="./src/merge/types/hris/location.py">SyncPage[Location]</a></code>

## PayGroups

Types:

```python
from merge.types.hris import PayGroup
```

Methods:

- <code title="get /hris/v1/pay-groups/{id}">client.hris.pay_groups.<a href="./src/merge/resources/hris/pay_groups.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/pay_group_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/pay_group.py">PayGroup</a></code>
- <code title="get /hris/v1/pay-groups">client.hris.pay_groups.<a href="./src/merge/resources/hris/pay_groups.py">list</a>(\*\*<a href="src/merge/types/hris/pay_group_list_params.py">params</a>) -> <a href="./src/merge/types/hris/pay_group.py">SyncPage[PayGroup]</a></code>

## PayrollRuns

Types:

```python
from merge.types.hris import PayrollRun
```

Methods:

- <code title="get /hris/v1/payroll-runs/{id}">client.hris.payroll_runs.<a href="./src/merge/resources/hris/payroll_runs.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/payroll_run_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/payroll_run.py">PayrollRun</a></code>
- <code title="get /hris/v1/payroll-runs">client.hris.payroll_runs.<a href="./src/merge/resources/hris/payroll_runs.py">list</a>(\*\*<a href="src/merge/types/hris/payroll_run_list_params.py">params</a>) -> <a href="./src/merge/types/hris/payroll_run.py">SyncPage[PayrollRun]</a></code>

## Teams

Methods:

- <code title="get /hris/v1/teams/{id}">client.hris.teams.<a href="./src/merge/resources/hris/teams.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/team_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/team.py">shared.Team</a></code>
- <code title="get /hris/v1/teams">client.hris.teams.<a href="./src/merge/resources/hris/teams.py">list</a>(\*\*<a href="src/merge/types/hris/team_list_params.py">params</a>) -> <a href="./src/merge/types/shared/team.py">SyncPage[shared.Team]</a></code>

## TimeOffResource

Types:

```python
from merge.types.hris import TimeOff, TimeOffResponse
```

Methods:

- <code title="post /hris/v1/time-off">client.hris.time_off.<a href="./src/merge/resources/hris/time_off/time_off.py">create</a>(\*\*<a href="src/merge/types/hris/time_off_create_params.py">params</a>) -> <a href="./src/merge/types/hris/time_off_response.py">TimeOffResponse</a></code>
- <code title="get /hris/v1/time-off/{id}">client.hris.time_off.<a href="./src/merge/resources/hris/time_off/time_off.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/time_off_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/time_off.py">TimeOff</a></code>
- <code title="get /hris/v1/time-off">client.hris.time_off.<a href="./src/merge/resources/hris/time_off/time_off.py">list</a>(\*\*<a href="src/merge/types/hris/time_off_list_params.py">params</a>) -> <a href="./src/merge/types/hris/time_off.py">SyncPage[TimeOff]</a></code>

### Meta

Methods:

- <code title="get /hris/v1/time-off/meta/post">client.hris.time_off.meta.<a href="./src/merge/resources/hris/time_off/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## TimeOffBalances

Types:

```python
from merge.types.hris import TimeOffBalance
```

Methods:

- <code title="get /hris/v1/time-off-balances/{id}">client.hris.time_off_balances.<a href="./src/merge/resources/hris/time_off_balances.py">retrieve</a>(id, \*\*<a href="src/merge/types/hris/time_off_balance_retrieve_params.py">params</a>) -> <a href="./src/merge/types/hris/time_off_balance.py">TimeOffBalance</a></code>
- <code title="get /hris/v1/time-off-balances">client.hris.time_off_balances.<a href="./src/merge/resources/hris/time_off_balances.py">list</a>(\*\*<a href="src/merge/types/hris/time_off_balance_list_params.py">params</a>) -> <a href="./src/merge/types/hris/time_off_balance.py">SyncPage[TimeOffBalance]</a></code>

## AccountDetails

Methods:

- <code title="get /hris/v1/account-details">client.hris.account_details.<a href="./src/merge/resources/hris/account_details.py">retrieve</a>() -> <a href="./src/merge/types/shared/account_detail.py">shared.AccountDetail</a></code>

## AccountTokens

Methods:

- <code title="get /hris/v1/account-token/{public_token}">client.hris.account_tokens.<a href="./src/merge/resources/hris/account_tokens.py">retrieve</a>(public_token) -> <a href="./src/merge/types/shared/account_token.py">shared.AccountToken</a></code>

## LinkTokens

Methods:

- <code title="post /hris/v1/link-token">client.hris.link_tokens.<a href="./src/merge/resources/hris/link_tokens.py">create</a>(\*\*<a href="src/merge/types/hris/link_token_create_params.py">params</a>) -> <a href="./src/merge/types/shared/link_token.py">shared.LinkToken</a></code>

## AvailableActions

Methods:

- <code title="get /hris/v1/available-actions">client.hris.available_actions.<a href="./src/merge/resources/hris/available_actions.py">retrieve</a>() -> <a href="./src/merge/types/shared/available_action.py">shared.AvailableAction</a></code>

## RemoteKeys

Methods:

- <code title="post /hris/v1/generate-key">client.hris.remote_keys.<a href="./src/merge/resources/hris/remote_keys.py">generate</a>(\*\*<a href="src/merge/types/hris/remote_key_generate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>
- <code title="post /hris/v1/regenerate-key">client.hris.remote_keys.<a href="./src/merge/resources/hris/remote_keys.py">regenerate</a>(\*\*<a href="src/merge/types/hris/remote_key_regenerate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>

## Issues

Methods:

- <code title="get /hris/v1/issues/{id}">client.hris.issues.<a href="./src/merge/resources/hris/issues.py">retrieve</a>(id) -> <a href="./src/merge/types/shared/issue.py">shared.Issue</a></code>
- <code title="get /hris/v1/issues">client.hris.issues.<a href="./src/merge/resources/hris/issues.py">list</a>(\*\*<a href="src/merge/types/hris/issue_list_params.py">params</a>) -> <a href="./src/merge/types/shared/issue.py">SyncPage[shared.Issue]</a></code>

## CommonModelScopes

Methods:

- <code title="get /hris/v1/common-model-scopes">client.hris.common_model_scopes.<a href="./src/merge/resources/hris/common_model_scopes.py">retrieve</a>(\*\*<a href="src/merge/types/hris/common_model_scope_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>
- <code title="post /hris/v1/common-model-scopes">client.hris.common_model_scopes.<a href="./src/merge/resources/hris/common_model_scopes.py">update</a>(\*\*<a href="src/merge/types/hris/common_model_scope_update_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>

## PassthroughRequests

Methods:

- <code title="post /hris/v1/passthrough">client.hris.passthrough_requests.<a href="./src/merge/resources/hris/passthrough_requests.py">send</a>(\*\*<a href="src/merge/types/hris/passthrough_request_send_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_response.py">shared.RemoteResponse</a></code>

## SyncStatus

Types:

```python
from merge.types.hris import SyncStatusResyncResponse
```

Methods:

- <code title="get /hris/v1/sync-status">client.hris.sync_status.<a href="./src/merge/resources/hris/sync_status.py">list</a>(\*\*<a href="src/merge/types/hris/sync_status_list_params.py">params</a>) -> <a href="./src/merge/types/shared/sync_status.py">SyncPage[shared.SyncStatus]</a></code>
- <code title="post /hris/v1/sync-status/resync">client.hris.sync_status.<a href="./src/merge/resources/hris/sync_status.py">resync</a>() -> <a href="./src/merge/types/hris/sync_status_resync_response.py">SyncStatusResyncResponse</a></code>

## WebhookReceivers

Types:

```python
from merge.types.hris import WebhookReceiverListResponse
```

Methods:

- <code title="post /hris/v1/webhook-receivers">client.hris.webhook_receivers.<a href="./src/merge/resources/hris/webhook_receivers.py">create</a>(\*\*<a href="src/merge/types/hris/webhook_receiver_create_params.py">params</a>) -> <a href="./src/merge/types/shared/webhook_receiver.py">shared.WebhookReceiver</a></code>
- <code title="get /hris/v1/webhook-receivers">client.hris.webhook_receivers.<a href="./src/merge/resources/hris/webhook_receivers.py">list</a>() -> <a href="./src/merge/types/hris/webhook_receiver_list_response.py">WebhookReceiverListResponse</a></code>

## LinkedAccounts

Methods:

- <code title="get /hris/v1/linked-accounts">client.hris.linked_accounts.<a href="./src/merge/resources/hris/linked_accounts.py">list</a>(\*\*<a href="src/merge/types/hris/linked_account_list_params.py">params</a>) -> <a href="./src/merge/types/shared/account_details_and_actions.py">SyncPage[shared.AccountDetailsAndActions]</a></code>
- <code title="post /hris/v1/delete-account">client.hris.linked_accounts.<a href="./src/merge/resources/hris/linked_accounts.py">delete</a>() -> None</code>

## SelectiveSync

Types:

```python
from merge.types.hris import (
    SelectiveSyncReplaceConfigurationsResponse,
    SelectiveSyncListConfigurationsResponse,
)
```

Methods:

- <code title="get /hris/v1/selective-sync/configurations">client.hris.selective_sync.<a href="./src/merge/resources/hris/selective_sync.py">list_configurations</a>() -> <a href="./src/merge/types/hris/selective_sync_list_configurations_response.py">SelectiveSyncListConfigurationsResponse</a></code>
- <code title="get /hris/v1/selective-sync/meta">client.hris.selective_sync.<a href="./src/merge/resources/hris/selective_sync.py">list_metadata</a>(\*\*<a href="src/merge/types/hris/selective_sync_list_metadata_params.py">params</a>) -> <a href="./src/merge/types/shared/condition_schema.py">SyncPage[shared.ConditionSchema]</a></code>
- <code title="put /hris/v1/selective-sync/configurations">client.hris.selective_sync.<a href="./src/merge/resources/hris/selective_sync.py">replace_configurations</a>(\*\*<a href="src/merge/types/hris/selective_sync_replace_configurations_params.py">params</a>) -> <a href="./src/merge/types/hris/selective_sync_replace_configurations_response.py">SelectiveSyncReplaceConfigurationsResponse</a></code>

# ATS

## Activities

Types:

```python
from merge.types.ats import Activity, ActivityCreateResponse
```

Methods:

- <code title="post /ats/v1/activities">client.ats.activities.<a href="./src/merge/resources/ats/activities/activities.py">create</a>(\*\*<a href="src/merge/types/ats/activity_create_params.py">params</a>) -> <a href="./src/merge/types/ats/activity_create_response.py">ActivityCreateResponse</a></code>
- <code title="get /ats/v1/activities/{id}">client.ats.activities.<a href="./src/merge/resources/ats/activities/activities.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/activity_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/activity.py">Activity</a></code>
- <code title="get /ats/v1/activities">client.ats.activities.<a href="./src/merge/resources/ats/activities/activities.py">list</a>(\*\*<a href="src/merge/types/ats/activity_list_params.py">params</a>) -> <a href="./src/merge/types/ats/activity.py">SyncPage[Activity]</a></code>

### Meta

Methods:

- <code title="get /ats/v1/activities/meta/post">client.ats.activities.meta.<a href="./src/merge/resources/ats/activities/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Applications

Types:

```python
from merge.types.ats import Application, ApplicationResponse
```

Methods:

- <code title="post /ats/v1/applications">client.ats.applications.<a href="./src/merge/resources/ats/applications/applications.py">create</a>(\*\*<a href="src/merge/types/ats/application_create_params.py">params</a>) -> <a href="./src/merge/types/ats/application_response.py">ApplicationResponse</a></code>
- <code title="get /ats/v1/applications/{id}">client.ats.applications.<a href="./src/merge/resources/ats/applications/applications.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/application_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/application.py">Application</a></code>
- <code title="get /ats/v1/applications">client.ats.applications.<a href="./src/merge/resources/ats/applications/applications.py">list</a>(\*\*<a href="src/merge/types/ats/application_list_params.py">params</a>) -> <a href="./src/merge/types/ats/application.py">SyncPage[Application]</a></code>
- <code title="post /ats/v1/applications/{id}/change-stage">client.ats.applications.<a href="./src/merge/resources/ats/applications/applications.py">change_stage</a>(id, \*\*<a href="src/merge/types/ats/application_change_stage_params.py">params</a>) -> <a href="./src/merge/types/ats/application_response.py">ApplicationResponse</a></code>

### Meta

Methods:

- <code title="get /ats/v1/applications/meta/post">client.ats.applications.meta.<a href="./src/merge/resources/ats/applications/meta.py">for_create</a>(\*\*<a href="src/merge/types/ats/applications/meta_for_create_params.py">params</a>) -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Attachments

Types:

```python
from merge.types.ats import AttachmentResponse
```

Methods:

- <code title="post /ats/v1/attachments">client.ats.attachments.<a href="./src/merge/resources/ats/attachments/attachments.py">create</a>(\*\*<a href="src/merge/types/ats/attachment_create_params.py">params</a>) -> <a href="./src/merge/types/ats/attachment_response.py">AttachmentResponse</a></code>
- <code title="get /ats/v1/attachments/{id}">client.ats.attachments.<a href="./src/merge/resources/ats/attachments/attachments.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/attachment_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/attachment.py">shared.Attachment</a></code>
- <code title="get /ats/v1/attachments">client.ats.attachments.<a href="./src/merge/resources/ats/attachments/attachments.py">list</a>(\*\*<a href="src/merge/types/ats/attachment_list_params.py">params</a>) -> <a href="./src/merge/types/shared/attachment.py">SyncPage[shared.Attachment]</a></code>

### Meta

Methods:

- <code title="get /ats/v1/attachments/meta/post">client.ats.attachments.meta.<a href="./src/merge/resources/ats/attachments/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Candidates

Types:

```python
from merge.types.ats import Candidate, CandidateResponse
```

Methods:

- <code title="post /ats/v1/candidates">client.ats.candidates.<a href="./src/merge/resources/ats/candidates/candidates.py">create</a>(\*\*<a href="src/merge/types/ats/candidate_create_params.py">params</a>) -> <a href="./src/merge/types/ats/candidate_response.py">CandidateResponse</a></code>
- <code title="get /ats/v1/candidates/{id}">client.ats.candidates.<a href="./src/merge/resources/ats/candidates/candidates.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/candidate_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/candidate.py">Candidate</a></code>
- <code title="get /ats/v1/candidates">client.ats.candidates.<a href="./src/merge/resources/ats/candidates/candidates.py">list</a>(\*\*<a href="src/merge/types/ats/candidate_list_params.py">params</a>) -> <a href="./src/merge/types/ats/candidate.py">SyncPage[Candidate]</a></code>
- <code title="post /ats/v1/candidates/ignore/{model_id}">client.ats.candidates.<a href="./src/merge/resources/ats/candidates/candidates.py">ignore_row</a>(model_id, \*\*<a href="src/merge/types/ats/candidate_ignore_row_params.py">params</a>) -> None</code>

### Meta

Methods:

- <code title="get /ats/v1/candidates/meta/post">client.ats.candidates.meta.<a href="./src/merge/resources/ats/candidates/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Departments

Types:

```python
from merge.types.ats import Department
```

Methods:

- <code title="get /ats/v1/departments/{id}">client.ats.departments.<a href="./src/merge/resources/ats/departments.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/department_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/department.py">Department</a></code>
- <code title="get /ats/v1/departments">client.ats.departments.<a href="./src/merge/resources/ats/departments.py">list</a>(\*\*<a href="src/merge/types/ats/department_list_params.py">params</a>) -> <a href="./src/merge/types/ats/department.py">SyncPage[Department]</a></code>

## EEOCs

Types:

```python
from merge.types.ats import EEOC
```

Methods:

- <code title="get /ats/v1/eeocs/{id}">client.ats.eeocs.<a href="./src/merge/resources/ats/eeocs.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/eeoc_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/eeoc.py">EEOC</a></code>
- <code title="get /ats/v1/eeocs">client.ats.eeocs.<a href="./src/merge/resources/ats/eeocs.py">list</a>(\*\*<a href="src/merge/types/ats/eeoc_list_params.py">params</a>) -> <a href="./src/merge/types/ats/eeoc.py">SyncPage[EEOC]</a></code>

## Interviews

Types:

```python
from merge.types.ats import ScheduledInterview, ScheduledInterviewResponse
```

Methods:

- <code title="post /ats/v1/interviews">client.ats.interviews.<a href="./src/merge/resources/ats/interviews/interviews.py">create</a>(\*\*<a href="src/merge/types/ats/interview_create_params.py">params</a>) -> <a href="./src/merge/types/ats/scheduled_interview_response.py">ScheduledInterviewResponse</a></code>
- <code title="get /ats/v1/interviews/{id}">client.ats.interviews.<a href="./src/merge/resources/ats/interviews/interviews.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/interview_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/scheduled_interview.py">ScheduledInterview</a></code>
- <code title="get /ats/v1/interviews">client.ats.interviews.<a href="./src/merge/resources/ats/interviews/interviews.py">list</a>(\*\*<a href="src/merge/types/ats/interview_list_params.py">params</a>) -> <a href="./src/merge/types/ats/scheduled_interview.py">SyncPage[ScheduledInterview]</a></code>

### Meta

Methods:

- <code title="get /ats/v1/interviews/meta/post">client.ats.interviews.meta.<a href="./src/merge/resources/ats/interviews/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## JobInterviewStages

Types:

```python
from merge.types.ats import JobInterviewStage
```

Methods:

- <code title="get /ats/v1/job-interview-stages/{id}">client.ats.job_interview_stages.<a href="./src/merge/resources/ats/job_interview_stages.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/job_interview_stage_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/job_interview_stage.py">JobInterviewStage</a></code>
- <code title="get /ats/v1/job-interview-stages">client.ats.job_interview_stages.<a href="./src/merge/resources/ats/job_interview_stages.py">list</a>(\*\*<a href="src/merge/types/ats/job_interview_stage_list_params.py">params</a>) -> <a href="./src/merge/types/ats/job_interview_stage.py">SyncPage[JobInterviewStage]</a></code>

## Jobs

Types:

```python
from merge.types.ats import Job
```

Methods:

- <code title="get /ats/v1/jobs/{id}">client.ats.jobs.<a href="./src/merge/resources/ats/jobs.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/job_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/job.py">Job</a></code>
- <code title="get /ats/v1/jobs">client.ats.jobs.<a href="./src/merge/resources/ats/jobs.py">list</a>(\*\*<a href="src/merge/types/ats/job_list_params.py">params</a>) -> <a href="./src/merge/types/ats/job.py">SyncPage[Job]</a></code>

## Offers

Types:

```python
from merge.types.ats import Offer
```

Methods:

- <code title="get /ats/v1/offers/{id}">client.ats.offers.<a href="./src/merge/resources/ats/offers.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/offer_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/offer.py">Offer</a></code>
- <code title="get /ats/v1/offers">client.ats.offers.<a href="./src/merge/resources/ats/offers.py">list</a>(\*\*<a href="src/merge/types/ats/offer_list_params.py">params</a>) -> <a href="./src/merge/types/ats/offer.py">SyncPage[Offer]</a></code>

## Offices

Types:

```python
from merge.types.ats import Office
```

Methods:

- <code title="get /ats/v1/offices/{id}">client.ats.offices.<a href="./src/merge/resources/ats/offices.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/office_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/office.py">Office</a></code>
- <code title="get /ats/v1/offices">client.ats.offices.<a href="./src/merge/resources/ats/offices.py">list</a>(\*\*<a href="src/merge/types/ats/office_list_params.py">params</a>) -> <a href="./src/merge/types/ats/office.py">SyncPage[Office]</a></code>

## RejectReasons

Types:

```python
from merge.types.ats import RejectReason
```

Methods:

- <code title="get /ats/v1/reject-reasons/{id}">client.ats.reject_reasons.<a href="./src/merge/resources/ats/reject_reasons.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/reject_reason_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/reject_reason.py">RejectReason</a></code>
- <code title="get /ats/v1/reject-reasons">client.ats.reject_reasons.<a href="./src/merge/resources/ats/reject_reasons.py">list</a>(\*\*<a href="src/merge/types/ats/reject_reason_list_params.py">params</a>) -> <a href="./src/merge/types/ats/reject_reason.py">SyncPage[RejectReason]</a></code>

## Scorecards

Types:

```python
from merge.types.ats import Scorecard
```

Methods:

- <code title="get /ats/v1/scorecards/{id}">client.ats.scorecards.<a href="./src/merge/resources/ats/scorecards.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/scorecard_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ats/scorecard.py">Scorecard</a></code>
- <code title="get /ats/v1/scorecards">client.ats.scorecards.<a href="./src/merge/resources/ats/scorecards.py">list</a>(\*\*<a href="src/merge/types/ats/scorecard_list_params.py">params</a>) -> <a href="./src/merge/types/ats/scorecard.py">SyncPage[Scorecard]</a></code>

## Tags

Methods:

- <code title="get /ats/v1/tags">client.ats.tags.<a href="./src/merge/resources/ats/tags.py">list</a>(\*\*<a href="src/merge/types/ats/tag_list_params.py">params</a>) -> <a href="./src/merge/types/shared/tag.py">SyncPage[shared.Tag]</a></code>

## Users

Methods:

- <code title="get /ats/v1/users/{id}">client.ats.users.<a href="./src/merge/resources/ats/users.py">retrieve</a>(id, \*\*<a href="src/merge/types/ats/user_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_user.py">shared.RemoteUser</a></code>
- <code title="get /ats/v1/users">client.ats.users.<a href="./src/merge/resources/ats/users.py">list</a>(\*\*<a href="src/merge/types/ats/user_list_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_user.py">SyncPage[shared.RemoteUser]</a></code>

## AccountDetails

Methods:

- <code title="get /ats/v1/account-details">client.ats.account_details.<a href="./src/merge/resources/ats/account_details.py">retrieve</a>() -> <a href="./src/merge/types/shared/account_detail.py">shared.AccountDetail</a></code>

## AccountTokens

Methods:

- <code title="get /ats/v1/account-token/{public_token}">client.ats.account_tokens.<a href="./src/merge/resources/ats/account_tokens.py">retrieve</a>(public_token) -> <a href="./src/merge/types/shared/account_token.py">shared.AccountToken</a></code>

## LinkTokens

Methods:

- <code title="post /ats/v1/link-token">client.ats.link_tokens.<a href="./src/merge/resources/ats/link_tokens.py">create</a>(\*\*<a href="src/merge/types/ats/link_token_create_params.py">params</a>) -> <a href="./src/merge/types/shared/link_token.py">shared.LinkToken</a></code>

## AvailableActions

Methods:

- <code title="get /ats/v1/available-actions">client.ats.available_actions.<a href="./src/merge/resources/ats/available_actions.py">retrieve</a>() -> <a href="./src/merge/types/shared/available_action.py">shared.AvailableAction</a></code>

## RemoteKeys

Methods:

- <code title="post /ats/v1/generate-key">client.ats.remote_keys.<a href="./src/merge/resources/ats/remote_keys.py">generate</a>(\*\*<a href="src/merge/types/ats/remote_key_generate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>
- <code title="post /ats/v1/regenerate-key">client.ats.remote_keys.<a href="./src/merge/resources/ats/remote_keys.py">regenerate</a>(\*\*<a href="src/merge/types/ats/remote_key_regenerate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>

## Issues

Methods:

- <code title="get /ats/v1/issues/{id}">client.ats.issues.<a href="./src/merge/resources/ats/issues.py">retrieve</a>(id) -> <a href="./src/merge/types/shared/issue.py">shared.Issue</a></code>
- <code title="get /ats/v1/issues">client.ats.issues.<a href="./src/merge/resources/ats/issues.py">list</a>(\*\*<a href="src/merge/types/ats/issue_list_params.py">params</a>) -> <a href="./src/merge/types/shared/issue.py">SyncPage[shared.Issue]</a></code>

## CommonModelScopes

Methods:

- <code title="get /ats/v1/common-model-scopes">client.ats.common_model_scopes.<a href="./src/merge/resources/ats/common_model_scopes.py">retrieve</a>(\*\*<a href="src/merge/types/ats/common_model_scope_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>
- <code title="post /ats/v1/common-model-scopes">client.ats.common_model_scopes.<a href="./src/merge/resources/ats/common_model_scopes.py">update</a>(\*\*<a href="src/merge/types/ats/common_model_scope_update_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>

## PassthroughRequests

Methods:

- <code title="post /ats/v1/passthrough">client.ats.passthrough_requests.<a href="./src/merge/resources/ats/passthrough_requests.py">send</a>(\*\*<a href="src/merge/types/ats/passthrough_request_send_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_response.py">shared.RemoteResponse</a></code>

## SyncStatus

Types:

```python
from merge.types.ats import SyncStatusResyncResponse
```

Methods:

- <code title="get /ats/v1/sync-status">client.ats.sync_status.<a href="./src/merge/resources/ats/sync_status.py">list</a>(\*\*<a href="src/merge/types/ats/sync_status_list_params.py">params</a>) -> <a href="./src/merge/types/shared/sync_status.py">SyncPage[shared.SyncStatus]</a></code>
- <code title="post /ats/v1/sync-status/resync">client.ats.sync_status.<a href="./src/merge/resources/ats/sync_status.py">resync</a>() -> <a href="./src/merge/types/ats/sync_status_resync_response.py">SyncStatusResyncResponse</a></code>

## WebhookReceivers

Types:

```python
from merge.types.ats import WebhookReceiverListResponse
```

Methods:

- <code title="post /ats/v1/webhook-receivers">client.ats.webhook_receivers.<a href="./src/merge/resources/ats/webhook_receivers.py">create</a>(\*\*<a href="src/merge/types/ats/webhook_receiver_create_params.py">params</a>) -> <a href="./src/merge/types/shared/webhook_receiver.py">shared.WebhookReceiver</a></code>
- <code title="get /ats/v1/webhook-receivers">client.ats.webhook_receivers.<a href="./src/merge/resources/ats/webhook_receivers.py">list</a>() -> <a href="./src/merge/types/ats/webhook_receiver_list_response.py">WebhookReceiverListResponse</a></code>

## LinkedAccounts

Methods:

- <code title="get /ats/v1/linked-accounts">client.ats.linked_accounts.<a href="./src/merge/resources/ats/linked_accounts.py">list</a>(\*\*<a href="src/merge/types/ats/linked_account_list_params.py">params</a>) -> <a href="./src/merge/types/shared/account_details_and_actions.py">SyncPage[shared.AccountDetailsAndActions]</a></code>
- <code title="post /ats/v1/delete-account">client.ats.linked_accounts.<a href="./src/merge/resources/ats/linked_accounts.py">delete</a>() -> None</code>

## SelectiveSync

Types:

```python
from merge.types.ats import (
    SelectiveSyncReplaceConfigurationsResponse,
    SelectiveSyncListConfigurationsResponse,
)
```

Methods:

- <code title="get /ats/v1/selective-sync/configurations">client.ats.selective_sync.<a href="./src/merge/resources/ats/selective_sync.py">list_configurations</a>() -> <a href="./src/merge/types/ats/selective_sync_list_configurations_response.py">SelectiveSyncListConfigurationsResponse</a></code>
- <code title="get /ats/v1/selective-sync/meta">client.ats.selective_sync.<a href="./src/merge/resources/ats/selective_sync.py">list_metadata</a>(\*\*<a href="src/merge/types/ats/selective_sync_list_metadata_params.py">params</a>) -> <a href="./src/merge/types/shared/condition_schema.py">SyncPage[shared.ConditionSchema]</a></code>
- <code title="put /ats/v1/selective-sync/configurations">client.ats.selective_sync.<a href="./src/merge/resources/ats/selective_sync.py">replace_configurations</a>(\*\*<a href="src/merge/types/ats/selective_sync_replace_configurations_params.py">params</a>) -> <a href="./src/merge/types/ats/selective_sync_replace_configurations_response.py">SelectiveSyncReplaceConfigurationsResponse</a></code>

# Accounting

## Accounts

Types:

```python
from merge.types.accounting import AccountResponse
```

Methods:

- <code title="post /accounting/v1/accounts">client.accounting.accounts.<a href="./src/merge/resources/accounting/accounts/accounts.py">create</a>(\*\*<a href="src/merge/types/accounting/account_create_params.py">params</a>) -> <a href="./src/merge/types/accounting/account_response.py">AccountResponse</a></code>
- <code title="get /accounting/v1/accounts/{id}">client.accounting.accounts.<a href="./src/merge/resources/accounting/accounts/accounts.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/account_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/account.py">shared.Account</a></code>
- <code title="get /accounting/v1/accounts">client.accounting.accounts.<a href="./src/merge/resources/accounting/accounts/accounts.py">list</a>(\*\*<a href="src/merge/types/accounting/account_list_params.py">params</a>) -> <a href="./src/merge/types/shared/account.py">SyncPage[shared.Account]</a></code>

### Meta

Methods:

- <code title="get /accounting/v1/accounts/meta/post">client.accounting.accounts.meta.<a href="./src/merge/resources/accounting/accounts/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Addresses

Methods:

- <code title="get /accounting/v1/addresses/{id}">client.accounting.addresses.<a href="./src/merge/resources/accounting/addresses.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/address_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/address.py">shared.Address</a></code>

## Attachments

Types:

```python
from merge.types.accounting import AccountingAttachment, AccountingAttachmentResponse
```

Methods:

- <code title="post /accounting/v1/attachments">client.accounting.attachments.<a href="./src/merge/resources/accounting/attachments/attachments.py">create</a>(\*\*<a href="src/merge/types/accounting/attachment_create_params.py">params</a>) -> <a href="./src/merge/types/accounting/accounting_attachment_response.py">AccountingAttachmentResponse</a></code>
- <code title="get /accounting/v1/attachments/{id}">client.accounting.attachments.<a href="./src/merge/resources/accounting/attachments/attachments.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/attachment_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/accounting_attachment.py">AccountingAttachment</a></code>
- <code title="get /accounting/v1/attachments">client.accounting.attachments.<a href="./src/merge/resources/accounting/attachments/attachments.py">list</a>(\*\*<a href="src/merge/types/accounting/attachment_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/accounting_attachment.py">SyncPage[AccountingAttachment]</a></code>

### Meta

Methods:

- <code title="get /accounting/v1/attachments/meta/post">client.accounting.attachments.meta.<a href="./src/merge/resources/accounting/attachments/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## BalanceSheets

Types:

```python
from merge.types.accounting import BalanceSheet
```

Methods:

- <code title="get /accounting/v1/balance-sheets/{id}">client.accounting.balance_sheets.<a href="./src/merge/resources/accounting/balance_sheets.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/balance_sheet_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/balance_sheet.py">BalanceSheet</a></code>
- <code title="get /accounting/v1/balance-sheets">client.accounting.balance_sheets.<a href="./src/merge/resources/accounting/balance_sheets.py">list</a>(\*\*<a href="src/merge/types/accounting/balance_sheet_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/balance_sheet.py">SyncPage[BalanceSheet]</a></code>

## CashFlowStatements

Types:

```python
from merge.types.accounting import CashFlowStatement
```

Methods:

- <code title="get /accounting/v1/cash-flow-statements/{id}">client.accounting.cash_flow_statements.<a href="./src/merge/resources/accounting/cash_flow_statements.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/cash_flow_statement_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/cash_flow_statement.py">CashFlowStatement</a></code>
- <code title="get /accounting/v1/cash-flow-statements">client.accounting.cash_flow_statements.<a href="./src/merge/resources/accounting/cash_flow_statements.py">list</a>(\*\*<a href="src/merge/types/accounting/cash_flow_statement_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/cash_flow_statement.py">SyncPage[CashFlowStatement]</a></code>

## CompanyInfoResource

Types:

```python
from merge.types.accounting import CompanyInfo
```

Methods:

- <code title="get /accounting/v1/company-info/{id}">client.accounting.company_info.<a href="./src/merge/resources/accounting/company_info.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/company_info_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/company_info.py">CompanyInfo</a></code>
- <code title="get /accounting/v1/company-info">client.accounting.company_info.<a href="./src/merge/resources/accounting/company_info.py">list</a>(\*\*<a href="src/merge/types/accounting/company_info_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/company_info.py">SyncPage[CompanyInfo]</a></code>

## Contacts

Types:

```python
from merge.types.accounting import ContactResponse
```

Methods:

- <code title="post /accounting/v1/contacts">client.accounting.contacts.<a href="./src/merge/resources/accounting/contacts/contacts.py">create</a>(\*\*<a href="src/merge/types/accounting/contact_create_params.py">params</a>) -> <a href="./src/merge/types/accounting/contact_response.py">ContactResponse</a></code>
- <code title="get /accounting/v1/contacts/{id}">client.accounting.contacts.<a href="./src/merge/resources/accounting/contacts/contacts.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/contact_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">shared.Contact</a></code>
- <code title="get /accounting/v1/contacts">client.accounting.contacts.<a href="./src/merge/resources/accounting/contacts/contacts.py">list</a>(\*\*<a href="src/merge/types/accounting/contact_list_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">SyncPage[shared.Contact]</a></code>

### Meta

Methods:

- <code title="get /accounting/v1/contacts/meta/post">client.accounting.contacts.meta.<a href="./src/merge/resources/accounting/contacts/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## CreditNotes

Types:

```python
from merge.types.accounting import CreditNote
```

Methods:

- <code title="get /accounting/v1/credit-notes/{id}">client.accounting.credit_notes.<a href="./src/merge/resources/accounting/credit_notes.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/credit_note_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/credit_note.py">CreditNote</a></code>
- <code title="get /accounting/v1/credit-notes">client.accounting.credit_notes.<a href="./src/merge/resources/accounting/credit_notes.py">list</a>(\*\*<a href="src/merge/types/accounting/credit_note_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/credit_note.py">SyncPage[CreditNote]</a></code>

## Expenses

Types:

```python
from merge.types.accounting import Expense, ExpenseResponse
```

Methods:

- <code title="post /accounting/v1/expenses">client.accounting.expenses.<a href="./src/merge/resources/accounting/expenses/expenses.py">create</a>(\*\*<a href="src/merge/types/accounting/expense_create_params.py">params</a>) -> <a href="./src/merge/types/accounting/expense_response.py">ExpenseResponse</a></code>
- <code title="get /accounting/v1/expenses/{id}">client.accounting.expenses.<a href="./src/merge/resources/accounting/expenses/expenses.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/expense_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/expense.py">Expense</a></code>
- <code title="get /accounting/v1/expenses">client.accounting.expenses.<a href="./src/merge/resources/accounting/expenses/expenses.py">list</a>(\*\*<a href="src/merge/types/accounting/expense_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/expense.py">SyncPage[Expense]</a></code>

### Meta

Methods:

- <code title="get /accounting/v1/expenses/meta/post">client.accounting.expenses.meta.<a href="./src/merge/resources/accounting/expenses/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## IncomeStatements

Types:

```python
from merge.types.accounting import IncomeStatement
```

Methods:

- <code title="get /accounting/v1/income-statements/{id}">client.accounting.income_statements.<a href="./src/merge/resources/accounting/income_statements.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/income_statement_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/income_statement.py">IncomeStatement</a></code>
- <code title="get /accounting/v1/income-statements">client.accounting.income_statements.<a href="./src/merge/resources/accounting/income_statements.py">list</a>(\*\*<a href="src/merge/types/accounting/income_statement_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/income_statement.py">SyncPage[IncomeStatement]</a></code>

## Invoices

Types:

```python
from merge.types.accounting import Invoice, InvoiceResponse
```

Methods:

- <code title="post /accounting/v1/invoices">client.accounting.invoices.<a href="./src/merge/resources/accounting/invoices/invoices.py">create</a>(\*\*<a href="src/merge/types/accounting/invoice_create_params.py">params</a>) -> <a href="./src/merge/types/accounting/invoice_response.py">InvoiceResponse</a></code>
- <code title="get /accounting/v1/invoices/{id}">client.accounting.invoices.<a href="./src/merge/resources/accounting/invoices/invoices.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/invoice_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/invoice.py">Invoice</a></code>
- <code title="get /accounting/v1/invoices">client.accounting.invoices.<a href="./src/merge/resources/accounting/invoices/invoices.py">list</a>(\*\*<a href="src/merge/types/accounting/invoice_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/invoice.py">SyncPage[Invoice]</a></code>

### Meta

Methods:

- <code title="get /accounting/v1/invoices/meta/post">client.accounting.invoices.meta.<a href="./src/merge/resources/accounting/invoices/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Items

Types:

```python
from merge.types.accounting import Item
```

Methods:

- <code title="get /accounting/v1/items/{id}">client.accounting.items.<a href="./src/merge/resources/accounting/items.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/item_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/item.py">Item</a></code>
- <code title="get /accounting/v1/items">client.accounting.items.<a href="./src/merge/resources/accounting/items.py">list</a>(\*\*<a href="src/merge/types/accounting/item_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/item.py">SyncPage[Item]</a></code>

## JournalEntries

Types:

```python
from merge.types.accounting import JournalEntry, JournalEntryResponse
```

Methods:

- <code title="post /accounting/v1/journal-entries">client.accounting.journal_entries.<a href="./src/merge/resources/accounting/journal_entries/journal_entries.py">create</a>(\*\*<a href="src/merge/types/accounting/journal_entry_create_params.py">params</a>) -> <a href="./src/merge/types/accounting/journal_entry_response.py">JournalEntryResponse</a></code>
- <code title="get /accounting/v1/journal-entries/{id}">client.accounting.journal_entries.<a href="./src/merge/resources/accounting/journal_entries/journal_entries.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/journal_entry_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/journal_entry.py">JournalEntry</a></code>
- <code title="get /accounting/v1/journal-entries">client.accounting.journal_entries.<a href="./src/merge/resources/accounting/journal_entries/journal_entries.py">list</a>(\*\*<a href="src/merge/types/accounting/journal_entry_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/journal_entry.py">SyncPage[JournalEntry]</a></code>

### Meta

Methods:

- <code title="get /accounting/v1/journal-entries/meta/post">client.accounting.journal_entries.meta.<a href="./src/merge/resources/accounting/journal_entries/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Payments

Types:

```python
from merge.types.accounting import Payment, PaymentResponse
```

Methods:

- <code title="post /accounting/v1/payments">client.accounting.payments.<a href="./src/merge/resources/accounting/payments/payments.py">create</a>(\*\*<a href="src/merge/types/accounting/payment_create_params.py">params</a>) -> <a href="./src/merge/types/accounting/payment_response.py">PaymentResponse</a></code>
- <code title="get /accounting/v1/payments/{id}">client.accounting.payments.<a href="./src/merge/resources/accounting/payments/payments.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/payment_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/payment.py">Payment</a></code>
- <code title="get /accounting/v1/payments">client.accounting.payments.<a href="./src/merge/resources/accounting/payments/payments.py">list</a>(\*\*<a href="src/merge/types/accounting/payment_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/payment.py">SyncPage[Payment]</a></code>

### Meta

Methods:

- <code title="get /accounting/v1/payments/meta/post">client.accounting.payments.meta.<a href="./src/merge/resources/accounting/payments/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## PhoneNumbers

Types:

```python
from merge.types.accounting import PhoneNumber
```

Methods:

- <code title="get /accounting/v1/phone-numbers/{id}">client.accounting.phone_numbers.<a href="./src/merge/resources/accounting/phone_numbers.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/phone_number_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/phone_number.py">PhoneNumber</a></code>

## PurchaseOrders

Types:

```python
from merge.types.accounting import PurchaseOrder, PurchaseOrderResponse
```

Methods:

- <code title="post /accounting/v1/purchase-orders">client.accounting.purchase_orders.<a href="./src/merge/resources/accounting/purchase_orders/purchase_orders.py">create</a>(\*\*<a href="src/merge/types/accounting/purchase_order_create_params.py">params</a>) -> <a href="./src/merge/types/accounting/purchase_order_response.py">PurchaseOrderResponse</a></code>
- <code title="get /accounting/v1/purchase-orders/{id}">client.accounting.purchase_orders.<a href="./src/merge/resources/accounting/purchase_orders/purchase_orders.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/purchase_order_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/purchase_order.py">PurchaseOrder</a></code>
- <code title="get /accounting/v1/purchase-orders">client.accounting.purchase_orders.<a href="./src/merge/resources/accounting/purchase_orders/purchase_orders.py">list</a>(\*\*<a href="src/merge/types/accounting/purchase_order_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/purchase_order.py">SyncPage[PurchaseOrder]</a></code>

### Meta

Methods:

- <code title="get /accounting/v1/purchase-orders/meta/post">client.accounting.purchase_orders.meta.<a href="./src/merge/resources/accounting/purchase_orders/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## TaxRates

Types:

```python
from merge.types.accounting import TaxRate
```

Methods:

- <code title="get /accounting/v1/tax-rates/{id}">client.accounting.tax_rates.<a href="./src/merge/resources/accounting/tax_rates.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/tax_rate_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/tax_rate.py">TaxRate</a></code>
- <code title="get /accounting/v1/tax-rates">client.accounting.tax_rates.<a href="./src/merge/resources/accounting/tax_rates.py">list</a>(\*\*<a href="src/merge/types/accounting/tax_rate_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/tax_rate.py">SyncPage[TaxRate]</a></code>

## TrackingCategories

Types:

```python
from merge.types.accounting import TrackingCategory
```

Methods:

- <code title="get /accounting/v1/tracking-categories/{id}">client.accounting.tracking_categories.<a href="./src/merge/resources/accounting/tracking_categories.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/tracking_category_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/tracking_category.py">TrackingCategory</a></code>
- <code title="get /accounting/v1/tracking-categories">client.accounting.tracking_categories.<a href="./src/merge/resources/accounting/tracking_categories.py">list</a>(\*\*<a href="src/merge/types/accounting/tracking_category_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/tracking_category.py">SyncPage[TrackingCategory]</a></code>

## Transactions

Types:

```python
from merge.types.accounting import Transaction
```

Methods:

- <code title="get /accounting/v1/transactions/{id}">client.accounting.transactions.<a href="./src/merge/resources/accounting/transactions.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/transaction_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/transaction.py">Transaction</a></code>
- <code title="get /accounting/v1/transactions">client.accounting.transactions.<a href="./src/merge/resources/accounting/transactions.py">list</a>(\*\*<a href="src/merge/types/accounting/transaction_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/transaction.py">SyncPage[Transaction]</a></code>

## VendorCredits

Types:

```python
from merge.types.accounting import VendorCredit
```

Methods:

- <code title="get /accounting/v1/vendor-credits/{id}">client.accounting.vendor_credits.<a href="./src/merge/resources/accounting/vendor_credits.py">retrieve</a>(id, \*\*<a href="src/merge/types/accounting/vendor_credit_retrieve_params.py">params</a>) -> <a href="./src/merge/types/accounting/vendor_credit.py">VendorCredit</a></code>
- <code title="get /accounting/v1/vendor-credits">client.accounting.vendor_credits.<a href="./src/merge/resources/accounting/vendor_credits.py">list</a>(\*\*<a href="src/merge/types/accounting/vendor_credit_list_params.py">params</a>) -> <a href="./src/merge/types/accounting/vendor_credit.py">SyncPage[VendorCredit]</a></code>

## AccountDetails

Methods:

- <code title="get /accounting/v1/account-details">client.accounting.account_details.<a href="./src/merge/resources/accounting/account_details.py">retrieve</a>() -> <a href="./src/merge/types/shared/account_detail.py">shared.AccountDetail</a></code>

## AccountTokens

Methods:

- <code title="get /accounting/v1/account-token/{public_token}">client.accounting.account_tokens.<a href="./src/merge/resources/accounting/account_tokens.py">retrieve</a>(public_token) -> <a href="./src/merge/types/shared/account_token.py">shared.AccountToken</a></code>

## LinkTokens

Methods:

- <code title="post /accounting/v1/link-token">client.accounting.link_tokens.<a href="./src/merge/resources/accounting/link_tokens.py">create</a>(\*\*<a href="src/merge/types/accounting/link_token_create_params.py">params</a>) -> <a href="./src/merge/types/shared/link_token.py">shared.LinkToken</a></code>

## AvailableActions

Methods:

- <code title="get /accounting/v1/available-actions">client.accounting.available_actions.<a href="./src/merge/resources/accounting/available_actions.py">retrieve</a>() -> <a href="./src/merge/types/shared/available_action.py">shared.AvailableAction</a></code>

## RemoteKeys

Methods:

- <code title="post /accounting/v1/generate-key">client.accounting.remote_keys.<a href="./src/merge/resources/accounting/remote_keys.py">generate</a>(\*\*<a href="src/merge/types/accounting/remote_key_generate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>
- <code title="post /accounting/v1/regenerate-key">client.accounting.remote_keys.<a href="./src/merge/resources/accounting/remote_keys.py">regenerate</a>(\*\*<a href="src/merge/types/accounting/remote_key_regenerate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>

## Issues

Methods:

- <code title="get /accounting/v1/issues/{id}">client.accounting.issues.<a href="./src/merge/resources/accounting/issues.py">retrieve</a>(id) -> <a href="./src/merge/types/shared/issue.py">shared.Issue</a></code>
- <code title="get /accounting/v1/issues">client.accounting.issues.<a href="./src/merge/resources/accounting/issues.py">list</a>(\*\*<a href="src/merge/types/accounting/issue_list_params.py">params</a>) -> <a href="./src/merge/types/shared/issue.py">SyncPage[shared.Issue]</a></code>

## CommonModelScopes

Methods:

- <code title="get /accounting/v1/common-model-scopes">client.accounting.common_model_scopes.<a href="./src/merge/resources/accounting/common_model_scopes.py">retrieve</a>(\*\*<a href="src/merge/types/accounting/common_model_scope_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>
- <code title="post /accounting/v1/common-model-scopes">client.accounting.common_model_scopes.<a href="./src/merge/resources/accounting/common_model_scopes.py">update</a>(\*\*<a href="src/merge/types/accounting/common_model_scope_update_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>

## PassthroughRequests

Methods:

- <code title="post /accounting/v1/passthrough">client.accounting.passthrough_requests.<a href="./src/merge/resources/accounting/passthrough_requests.py">send</a>(\*\*<a href="src/merge/types/accounting/passthrough_request_send_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_response.py">shared.RemoteResponse</a></code>

## SyncStatus

Types:

```python
from merge.types.accounting import SyncStatusResyncResponse
```

Methods:

- <code title="get /accounting/v1/sync-status">client.accounting.sync_status.<a href="./src/merge/resources/accounting/sync_status.py">list</a>(\*\*<a href="src/merge/types/accounting/sync_status_list_params.py">params</a>) -> <a href="./src/merge/types/shared/sync_status.py">SyncPage[shared.SyncStatus]</a></code>
- <code title="post /accounting/v1/sync-status/resync">client.accounting.sync_status.<a href="./src/merge/resources/accounting/sync_status.py">resync</a>() -> <a href="./src/merge/types/accounting/sync_status_resync_response.py">SyncStatusResyncResponse</a></code>

## WebhookReceivers

Types:

```python
from merge.types.accounting import WebhookReceiverListResponse
```

Methods:

- <code title="post /accounting/v1/webhook-receivers">client.accounting.webhook_receivers.<a href="./src/merge/resources/accounting/webhook_receivers.py">create</a>(\*\*<a href="src/merge/types/accounting/webhook_receiver_create_params.py">params</a>) -> <a href="./src/merge/types/shared/webhook_receiver.py">shared.WebhookReceiver</a></code>
- <code title="get /accounting/v1/webhook-receivers">client.accounting.webhook_receivers.<a href="./src/merge/resources/accounting/webhook_receivers.py">list</a>() -> <a href="./src/merge/types/accounting/webhook_receiver_list_response.py">WebhookReceiverListResponse</a></code>

## LinkedAccounts

Methods:

- <code title="get /accounting/v1/linked-accounts">client.accounting.linked_accounts.<a href="./src/merge/resources/accounting/linked_accounts.py">list</a>(\*\*<a href="src/merge/types/accounting/linked_account_list_params.py">params</a>) -> <a href="./src/merge/types/shared/account_details_and_actions.py">SyncPage[shared.AccountDetailsAndActions]</a></code>
- <code title="post /accounting/v1/delete-account">client.accounting.linked_accounts.<a href="./src/merge/resources/accounting/linked_accounts.py">delete</a>() -> None</code>

## SelectiveSync

Types:

```python
from merge.types.accounting import (
    SelectiveSyncReplaceConfigurationsResponse,
    SelectiveSyncListConfigurationsResponse,
)
```

Methods:

- <code title="get /accounting/v1/selective-sync/configurations">client.accounting.selective_sync.<a href="./src/merge/resources/accounting/selective_sync.py">list_configurations</a>() -> <a href="./src/merge/types/accounting/selective_sync_list_configurations_response.py">SelectiveSyncListConfigurationsResponse</a></code>
- <code title="get /accounting/v1/selective-sync/meta">client.accounting.selective_sync.<a href="./src/merge/resources/accounting/selective_sync.py">list_metadata</a>(\*\*<a href="src/merge/types/accounting/selective_sync_list_metadata_params.py">params</a>) -> <a href="./src/merge/types/shared/condition_schema.py">SyncPage[shared.ConditionSchema]</a></code>
- <code title="put /accounting/v1/selective-sync/configurations">client.accounting.selective_sync.<a href="./src/merge/resources/accounting/selective_sync.py">replace_configurations</a>(\*\*<a href="src/merge/types/accounting/selective_sync_replace_configurations_params.py">params</a>) -> <a href="./src/merge/types/accounting/selective_sync_replace_configurations_response.py">SelectiveSyncReplaceConfigurationsResponse</a></code>

# Ticketing

## Accounts

Methods:

- <code title="get /ticketing/v1/accounts/{id}">client.ticketing.accounts.<a href="./src/merge/resources/ticketing/accounts.py">retrieve</a>(id, \*\*<a href="src/merge/types/ticketing/account_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/account.py">shared.Account</a></code>
- <code title="get /ticketing/v1/accounts">client.ticketing.accounts.<a href="./src/merge/resources/ticketing/accounts.py">list</a>(\*\*<a href="src/merge/types/ticketing/account_list_params.py">params</a>) -> <a href="./src/merge/types/shared/account.py">SyncPage[shared.Account]</a></code>

## Attachments

Types:

```python
from merge.types.ticketing import AttachmentCreateResponse
```

Methods:

- <code title="post /ticketing/v1/attachments">client.ticketing.attachments.<a href="./src/merge/resources/ticketing/attachments/attachments.py">create</a>(\*\*<a href="src/merge/types/ticketing/attachment_create_params.py">params</a>) -> <a href="./src/merge/types/ticketing/attachment_create_response.py">AttachmentCreateResponse</a></code>
- <code title="get /ticketing/v1/attachments/{id}">client.ticketing.attachments.<a href="./src/merge/resources/ticketing/attachments/attachments.py">retrieve</a>(id, \*\*<a href="src/merge/types/ticketing/attachment_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/attachment.py">shared.Attachment</a></code>
- <code title="get /ticketing/v1/attachments">client.ticketing.attachments.<a href="./src/merge/resources/ticketing/attachments/attachments.py">list</a>(\*\*<a href="src/merge/types/ticketing/attachment_list_params.py">params</a>) -> <a href="./src/merge/types/shared/attachment.py">SyncPage[shared.Attachment]</a></code>

### Meta

Methods:

- <code title="get /ticketing/v1/attachments/meta/post">client.ticketing.attachments.meta.<a href="./src/merge/resources/ticketing/attachments/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Collections

Types:

```python
from merge.types.ticketing import Collection
```

Methods:

- <code title="get /ticketing/v1/collections/{id}">client.ticketing.collections.<a href="./src/merge/resources/ticketing/collections.py">retrieve</a>(id, \*\*<a href="src/merge/types/ticketing/collection_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ticketing/collection.py">Collection</a></code>
- <code title="get /ticketing/v1/collections">client.ticketing.collections.<a href="./src/merge/resources/ticketing/collections.py">list</a>(\*\*<a href="src/merge/types/ticketing/collection_list_params.py">params</a>) -> <a href="./src/merge/types/ticketing/collection.py">SyncPage[Collection]</a></code>
- <code title="get /ticketing/v1/collections/{parent_id}/users">client.ticketing.collections.<a href="./src/merge/resources/ticketing/collections.py">list_users</a>(parent_id, \*\*<a href="src/merge/types/ticketing/collection_list_users_params.py">params</a>) -> <a href="./src/merge/types/ticketing/user.py">SyncPage[User]</a></code>

## Comments

Types:

```python
from merge.types.ticketing import Comment, CommentResponse
```

Methods:

- <code title="post /ticketing/v1/comments">client.ticketing.comments.<a href="./src/merge/resources/ticketing/comments/comments.py">create</a>(\*\*<a href="src/merge/types/ticketing/comment_create_params.py">params</a>) -> <a href="./src/merge/types/ticketing/comment_response.py">CommentResponse</a></code>
- <code title="get /ticketing/v1/comments/{id}">client.ticketing.comments.<a href="./src/merge/resources/ticketing/comments/comments.py">retrieve</a>(id, \*\*<a href="src/merge/types/ticketing/comment_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ticketing/comment.py">Comment</a></code>
- <code title="get /ticketing/v1/comments">client.ticketing.comments.<a href="./src/merge/resources/ticketing/comments/comments.py">list</a>(\*\*<a href="src/merge/types/ticketing/comment_list_params.py">params</a>) -> <a href="./src/merge/types/ticketing/comment.py">SyncPage[Comment]</a></code>

### Meta

Methods:

- <code title="get /ticketing/v1/comments/meta/post">client.ticketing.comments.meta.<a href="./src/merge/resources/ticketing/comments/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Contacts

Methods:

- <code title="get /ticketing/v1/contacts/{id}">client.ticketing.contacts.<a href="./src/merge/resources/ticketing/contacts.py">retrieve</a>(id, \*\*<a href="src/merge/types/ticketing/contact_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">shared.Contact</a></code>
- <code title="get /ticketing/v1/contacts">client.ticketing.contacts.<a href="./src/merge/resources/ticketing/contacts.py">list</a>(\*\*<a href="src/merge/types/ticketing/contact_list_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">SyncPage[shared.Contact]</a></code>

## Projects

Types:

```python
from merge.types.ticketing import Project
```

Methods:

- <code title="get /ticketing/v1/projects/{id}">client.ticketing.projects.<a href="./src/merge/resources/ticketing/projects.py">retrieve</a>(id, \*\*<a href="src/merge/types/ticketing/project_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ticketing/project.py">Project</a></code>
- <code title="get /ticketing/v1/projects">client.ticketing.projects.<a href="./src/merge/resources/ticketing/projects.py">list</a>(\*\*<a href="src/merge/types/ticketing/project_list_params.py">params</a>) -> <a href="./src/merge/types/ticketing/project.py">SyncPage[Project]</a></code>
- <code title="get /ticketing/v1/projects/{parent_id}/users">client.ticketing.projects.<a href="./src/merge/resources/ticketing/projects.py">list_users</a>(parent_id, \*\*<a href="src/merge/types/ticketing/project_list_users_params.py">params</a>) -> <a href="./src/merge/types/ticketing/user.py">SyncPage[User]</a></code>

## Tags

Methods:

- <code title="get /ticketing/v1/tags/{id}">client.ticketing.tags.<a href="./src/merge/resources/ticketing/tags.py">retrieve</a>(id, \*\*<a href="src/merge/types/ticketing/tag_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/tag.py">shared.Tag</a></code>
- <code title="get /ticketing/v1/tags">client.ticketing.tags.<a href="./src/merge/resources/ticketing/tags.py">list</a>(\*\*<a href="src/merge/types/ticketing/tag_list_params.py">params</a>) -> <a href="./src/merge/types/shared/tag.py">SyncPage[shared.Tag]</a></code>

## Teams

Methods:

- <code title="get /ticketing/v1/teams/{id}">client.ticketing.teams.<a href="./src/merge/resources/ticketing/teams.py">retrieve</a>(id, \*\*<a href="src/merge/types/ticketing/team_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/team.py">shared.Team</a></code>
- <code title="get /ticketing/v1/teams">client.ticketing.teams.<a href="./src/merge/resources/ticketing/teams.py">list</a>(\*\*<a href="src/merge/types/ticketing/team_list_params.py">params</a>) -> <a href="./src/merge/types/shared/team.py">SyncPage[shared.Team]</a></code>

## Tickets

Types:

```python
from merge.types.ticketing import Ticket, TicketResponse
```

Methods:

- <code title="post /ticketing/v1/tickets">client.ticketing.tickets.<a href="./src/merge/resources/ticketing/tickets/tickets.py">create</a>(\*\*<a href="src/merge/types/ticketing/ticket_create_params.py">params</a>) -> <a href="./src/merge/types/ticketing/ticket_response.py">TicketResponse</a></code>
- <code title="get /ticketing/v1/tickets/{id}">client.ticketing.tickets.<a href="./src/merge/resources/ticketing/tickets/tickets.py">retrieve</a>(id, \*\*<a href="src/merge/types/ticketing/ticket_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ticketing/ticket.py">Ticket</a></code>
- <code title="patch /ticketing/v1/tickets/{id}">client.ticketing.tickets.<a href="./src/merge/resources/ticketing/tickets/tickets.py">update</a>(id, \*\*<a href="src/merge/types/ticketing/ticket_update_params.py">params</a>) -> <a href="./src/merge/types/ticketing/ticket_response.py">TicketResponse</a></code>
- <code title="get /ticketing/v1/tickets">client.ticketing.tickets.<a href="./src/merge/resources/ticketing/tickets/tickets.py">list</a>(\*\*<a href="src/merge/types/ticketing/ticket_list_params.py">params</a>) -> <a href="./src/merge/types/ticketing/ticket.py">SyncPage[Ticket]</a></code>
- <code title="get /ticketing/v1/tickets/{parent_id}/collaborators">client.ticketing.tickets.<a href="./src/merge/resources/ticketing/tickets/tickets.py">list_collaborators</a>(parent_id, \*\*<a href="src/merge/types/ticketing/ticket_list_collaborators_params.py">params</a>) -> <a href="./src/merge/types/ticketing/user.py">SyncPage[User]</a></code>
- <code title="get /ticketing/v1/tickets/remote-field-classes">client.ticketing.tickets.<a href="./src/merge/resources/ticketing/tickets/tickets.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/ticketing/ticket_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

### Meta

Methods:

- <code title="get /ticketing/v1/tickets/meta/post">client.ticketing.tickets.meta.<a href="./src/merge/resources/ticketing/tickets/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>
- <code title="get /ticketing/v1/tickets/meta/patch/{id}">client.ticketing.tickets.meta.<a href="./src/merge/resources/ticketing/tickets/meta.py">for_update</a>(id) -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Users

Types:

```python
from merge.types.ticketing import User
```

Methods:

- <code title="get /ticketing/v1/users/{id}">client.ticketing.users.<a href="./src/merge/resources/ticketing/users.py">retrieve</a>(id, \*\*<a href="src/merge/types/ticketing/user_retrieve_params.py">params</a>) -> <a href="./src/merge/types/ticketing/user.py">User</a></code>
- <code title="get /ticketing/v1/users">client.ticketing.users.<a href="./src/merge/resources/ticketing/users.py">list</a>(\*\*<a href="src/merge/types/ticketing/user_list_params.py">params</a>) -> <a href="./src/merge/types/ticketing/user.py">SyncPage[User]</a></code>

## AccountDetails

Methods:

- <code title="get /ticketing/v1/account-details">client.ticketing.account_details.<a href="./src/merge/resources/ticketing/account_details.py">retrieve</a>() -> <a href="./src/merge/types/shared/account_detail.py">shared.AccountDetail</a></code>

## AccountTokens

Methods:

- <code title="get /ticketing/v1/account-token/{public_token}">client.ticketing.account_tokens.<a href="./src/merge/resources/ticketing/account_tokens.py">retrieve</a>(public_token) -> <a href="./src/merge/types/shared/account_token.py">shared.AccountToken</a></code>

## LinkTokens

Methods:

- <code title="post /ticketing/v1/link-token">client.ticketing.link_tokens.<a href="./src/merge/resources/ticketing/link_tokens.py">create</a>(\*\*<a href="src/merge/types/ticketing/link_token_create_params.py">params</a>) -> <a href="./src/merge/types/shared/link_token.py">shared.LinkToken</a></code>

## AvailableActions

Methods:

- <code title="get /ticketing/v1/available-actions">client.ticketing.available_actions.<a href="./src/merge/resources/ticketing/available_actions.py">retrieve</a>() -> <a href="./src/merge/types/shared/available_action.py">shared.AvailableAction</a></code>

## RemoteKeys

Methods:

- <code title="post /ticketing/v1/generate-key">client.ticketing.remote_keys.<a href="./src/merge/resources/ticketing/remote_keys.py">generate</a>(\*\*<a href="src/merge/types/ticketing/remote_key_generate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>
- <code title="post /ticketing/v1/regenerate-key">client.ticketing.remote_keys.<a href="./src/merge/resources/ticketing/remote_keys.py">regenerate</a>(\*\*<a href="src/merge/types/ticketing/remote_key_regenerate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>

## Issues

Methods:

- <code title="get /ticketing/v1/issues/{id}">client.ticketing.issues.<a href="./src/merge/resources/ticketing/issues.py">retrieve</a>(id) -> <a href="./src/merge/types/shared/issue.py">shared.Issue</a></code>
- <code title="get /ticketing/v1/issues">client.ticketing.issues.<a href="./src/merge/resources/ticketing/issues.py">list</a>(\*\*<a href="src/merge/types/ticketing/issue_list_params.py">params</a>) -> <a href="./src/merge/types/shared/issue.py">SyncPage[shared.Issue]</a></code>

## CommonModelScopes

Methods:

- <code title="get /ticketing/v1/common-model-scopes">client.ticketing.common_model_scopes.<a href="./src/merge/resources/ticketing/common_model_scopes.py">retrieve</a>(\*\*<a href="src/merge/types/ticketing/common_model_scope_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>
- <code title="post /ticketing/v1/common-model-scopes">client.ticketing.common_model_scopes.<a href="./src/merge/resources/ticketing/common_model_scopes.py">update</a>(\*\*<a href="src/merge/types/ticketing/common_model_scope_update_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>

## PassthroughRequests

Methods:

- <code title="post /ticketing/v1/passthrough">client.ticketing.passthrough_requests.<a href="./src/merge/resources/ticketing/passthrough_requests.py">send</a>(\*\*<a href="src/merge/types/ticketing/passthrough_request_send_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_response.py">shared.RemoteResponse</a></code>

## SyncStatus

Types:

```python
from merge.types.ticketing import SyncStatusResyncResponse
```

Methods:

- <code title="get /ticketing/v1/sync-status">client.ticketing.sync_status.<a href="./src/merge/resources/ticketing/sync_status.py">list</a>(\*\*<a href="src/merge/types/ticketing/sync_status_list_params.py">params</a>) -> <a href="./src/merge/types/shared/sync_status.py">SyncPage[shared.SyncStatus]</a></code>
- <code title="post /ticketing/v1/sync-status/resync">client.ticketing.sync_status.<a href="./src/merge/resources/ticketing/sync_status.py">resync</a>() -> <a href="./src/merge/types/ticketing/sync_status_resync_response.py">SyncStatusResyncResponse</a></code>

## WebhookReceivers

Types:

```python
from merge.types.ticketing import WebhookReceiverListResponse
```

Methods:

- <code title="post /ticketing/v1/webhook-receivers">client.ticketing.webhook_receivers.<a href="./src/merge/resources/ticketing/webhook_receivers.py">create</a>(\*\*<a href="src/merge/types/ticketing/webhook_receiver_create_params.py">params</a>) -> <a href="./src/merge/types/shared/webhook_receiver.py">shared.WebhookReceiver</a></code>
- <code title="get /ticketing/v1/webhook-receivers">client.ticketing.webhook_receivers.<a href="./src/merge/resources/ticketing/webhook_receivers.py">list</a>() -> <a href="./src/merge/types/ticketing/webhook_receiver_list_response.py">WebhookReceiverListResponse</a></code>

## LinkedAccounts

Methods:

- <code title="get /ticketing/v1/linked-accounts">client.ticketing.linked_accounts.<a href="./src/merge/resources/ticketing/linked_accounts.py">list</a>(\*\*<a href="src/merge/types/ticketing/linked_account_list_params.py">params</a>) -> <a href="./src/merge/types/shared/account_details_and_actions.py">SyncPage[shared.AccountDetailsAndActions]</a></code>
- <code title="post /ticketing/v1/delete-account">client.ticketing.linked_accounts.<a href="./src/merge/resources/ticketing/linked_accounts.py">delete</a>() -> None</code>

## SelectiveSync

Types:

```python
from merge.types.ticketing import (
    SelectiveSyncReplaceConfigurationsResponse,
    SelectiveSyncListConfigurationsResponse,
)
```

Methods:

- <code title="get /ticketing/v1/selective-sync/configurations">client.ticketing.selective_sync.<a href="./src/merge/resources/ticketing/selective_sync.py">list_configurations</a>() -> <a href="./src/merge/types/ticketing/selective_sync_list_configurations_response.py">SelectiveSyncListConfigurationsResponse</a></code>
- <code title="get /ticketing/v1/selective-sync/meta">client.ticketing.selective_sync.<a href="./src/merge/resources/ticketing/selective_sync.py">list_metadata</a>(\*\*<a href="src/merge/types/ticketing/selective_sync_list_metadata_params.py">params</a>) -> <a href="./src/merge/types/shared/condition_schema.py">SyncPage[shared.ConditionSchema]</a></code>
- <code title="put /ticketing/v1/selective-sync/configurations">client.ticketing.selective_sync.<a href="./src/merge/resources/ticketing/selective_sync.py">replace_configurations</a>(\*\*<a href="src/merge/types/ticketing/selective_sync_replace_configurations_params.py">params</a>) -> <a href="./src/merge/types/ticketing/selective_sync_replace_configurations_response.py">SelectiveSyncReplaceConfigurationsResponse</a></code>

# CRM

## Accounts

Types:

```python
from merge.types.crm import AccountResponse
```

Methods:

- <code title="post /crm/v1/accounts">client.crm.accounts.<a href="./src/merge/resources/crm/accounts/accounts.py">create</a>(\*\*<a href="src/merge/types/crm/account_create_params.py">params</a>) -> <a href="./src/merge/types/crm/account_response.py">AccountResponse</a></code>
- <code title="get /crm/v1/accounts/{id}">client.crm.accounts.<a href="./src/merge/resources/crm/accounts/accounts.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/account_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/account.py">shared.Account</a></code>
- <code title="patch /crm/v1/accounts/{id}">client.crm.accounts.<a href="./src/merge/resources/crm/accounts/accounts.py">update</a>(id, \*\*<a href="src/merge/types/crm/account_update_params.py">params</a>) -> <a href="./src/merge/types/crm/account_response.py">AccountResponse</a></code>
- <code title="get /crm/v1/accounts">client.crm.accounts.<a href="./src/merge/resources/crm/accounts/accounts.py">list</a>(\*\*<a href="src/merge/types/crm/account_list_params.py">params</a>) -> <a href="./src/merge/types/shared/account.py">SyncPage[shared.Account]</a></code>
- <code title="get /crm/v1/accounts/remote-field-classes">client.crm.accounts.<a href="./src/merge/resources/crm/accounts/accounts.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/crm/account_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

### Meta

Methods:

- <code title="get /crm/v1/accounts/meta/post">client.crm.accounts.meta.<a href="./src/merge/resources/crm/accounts/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>
- <code title="get /crm/v1/accounts/meta/patch/{id}">client.crm.accounts.meta.<a href="./src/merge/resources/crm/accounts/meta.py">for_update</a>(id) -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Contacts

Types:

```python
from merge.types.crm import ContactResponse
```

Methods:

- <code title="post /crm/v1/contacts">client.crm.contacts.<a href="./src/merge/resources/crm/contacts/contacts.py">create</a>(\*\*<a href="src/merge/types/crm/contact_create_params.py">params</a>) -> <a href="./src/merge/types/crm/contact_response.py">ContactResponse</a></code>
- <code title="get /crm/v1/contacts/{id}">client.crm.contacts.<a href="./src/merge/resources/crm/contacts/contacts.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/contact_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">shared.Contact</a></code>
- <code title="patch /crm/v1/contacts/{id}">client.crm.contacts.<a href="./src/merge/resources/crm/contacts/contacts.py">update</a>(id, \*\*<a href="src/merge/types/crm/contact_update_params.py">params</a>) -> <a href="./src/merge/types/crm/contact_response.py">ContactResponse</a></code>
- <code title="get /crm/v1/contacts">client.crm.contacts.<a href="./src/merge/resources/crm/contacts/contacts.py">list</a>(\*\*<a href="src/merge/types/crm/contact_list_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">SyncPage[shared.Contact]</a></code>
- <code title="post /crm/v1/contacts/ignore/{model_id}">client.crm.contacts.<a href="./src/merge/resources/crm/contacts/contacts.py">ignore_row</a>(model_id, \*\*<a href="src/merge/types/crm/contact_ignore_row_params.py">params</a>) -> None</code>
- <code title="get /crm/v1/contacts/remote-field-classes">client.crm.contacts.<a href="./src/merge/resources/crm/contacts/contacts.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/crm/contact_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

### Meta

Methods:

- <code title="get /crm/v1/contacts/meta/post">client.crm.contacts.meta.<a href="./src/merge/resources/crm/contacts/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>
- <code title="get /crm/v1/contacts/meta/patch/{id}">client.crm.contacts.meta.<a href="./src/merge/resources/crm/contacts/meta.py">for_update</a>(id) -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## CustomObjectClasses

Types:

```python
from merge.types.crm import CustomObjectClass
```

Methods:

- <code title="get /crm/v1/custom-object-classes/{id}">client.crm.custom_object_classes.<a href="./src/merge/resources/crm/custom_object_classes/custom_object_classes.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/custom_object_class_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/custom_object_class.py">CustomObjectClass</a></code>
- <code title="get /crm/v1/custom-object-classes">client.crm.custom_object_classes.<a href="./src/merge/resources/crm/custom_object_classes/custom_object_classes.py">list</a>(\*\*<a href="src/merge/types/crm/custom_object_class_list_params.py">params</a>) -> <a href="./src/merge/types/crm/custom_object_class.py">SyncPage[CustomObjectClass]</a></code>

### AssociationTypes

Types:

```python
from merge.types.crm.custom_object_classes import (
    AssociationType,
    AssociationTypeResponse,
)
```

Methods:

- <code title="post /crm/v1/custom-object-classes/{custom_object_class_id}/association-types">client.crm.custom_object_classes.association_types.<a href="./src/merge/resources/crm/custom_object_classes/association_types/association_types.py">create</a>(custom_object_class_id, \*\*<a href="src/merge/types/crm/custom_object_classes/association_type_create_params.py">params</a>) -> <a href="./src/merge/types/crm/custom_object_classes/association_type_response.py">AssociationTypeResponse</a></code>
- <code title="get /crm/v1/custom-object-classes/{custom_object_class_id}/association-types/{id}">client.crm.custom_object_classes.association_types.<a href="./src/merge/resources/crm/custom_object_classes/association_types/association_types.py">retrieve</a>(id, custom_object_class_id, \*\*<a href="src/merge/types/crm/custom_object_classes/association_type_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/custom_object_classes/association_type.py">AssociationType</a></code>
- <code title="get /crm/v1/custom-object-classes/{custom_object_class_id}/association-types">client.crm.custom_object_classes.association_types.<a href="./src/merge/resources/crm/custom_object_classes/association_types/association_types.py">list</a>(custom_object_class_id, \*\*<a href="src/merge/types/crm/custom_object_classes/association_type_list_params.py">params</a>) -> <a href="./src/merge/types/crm/custom_object_classes/association_type.py">SyncPage[AssociationType]</a></code>

#### Meta

Methods:

- <code title="get /crm/v1/custom-object-classes/{custom_object_class_id}/association-types/meta/post">client.crm.custom_object_classes.association_types.meta.<a href="./src/merge/resources/crm/custom_object_classes/association_types/meta.py">for_create</a>(custom_object_class_id) -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## CustomObjects

Types:

```python
from merge.types.crm import CustomObject, CustomObjectResponse
```

Methods:

- <code title="post /crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects">client.crm.custom_objects.<a href="./src/merge/resources/crm/custom_objects/custom_objects.py">create</a>(custom_object_class_id, \*\*<a href="src/merge/types/crm/custom_object_create_params.py">params</a>) -> <a href="./src/merge/types/crm/custom_object_response.py">CustomObjectResponse</a></code>
- <code title="get /crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/{id}">client.crm.custom_objects.<a href="./src/merge/resources/crm/custom_objects/custom_objects.py">retrieve</a>(id, custom_object_class_id, \*\*<a href="src/merge/types/crm/custom_object_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/custom_object.py">CustomObject</a></code>
- <code title="patch /crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/{id}">client.crm.custom_objects.<a href="./src/merge/resources/crm/custom_objects/custom_objects.py">update</a>(id, custom_object_class_id, \*\*<a href="src/merge/types/crm/custom_object_update_params.py">params</a>) -> <a href="./src/merge/types/crm/custom_object_response.py">CustomObjectResponse</a></code>
- <code title="get /crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects">client.crm.custom_objects.<a href="./src/merge/resources/crm/custom_objects/custom_objects.py">list</a>(custom_object_class_id, \*\*<a href="src/merge/types/crm/custom_object_list_params.py">params</a>) -> <a href="./src/merge/types/crm/custom_object.py">SyncPage[CustomObject]</a></code>

### Associations

Types:

```python
from merge.types.crm.custom_objects import Association
```

Methods:

- <code title="put /crm/v1/custom-object-classes/{source_class_id}/custom-objects/{source_object_id}/associations/{target_class_id}/{target_object_id}/{association_type_id}">client.crm.custom_objects.associations.<a href="./src/merge/resources/crm/custom_objects/associations.py">update</a>(association_type_id, source_class_id, source_object_id, target_class_id, target_object_id) -> <a href="./src/merge/types/crm/custom_objects/association.py">Association</a></code>
- <code title="get /crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/{object_id}/associations">client.crm.custom_objects.associations.<a href="./src/merge/resources/crm/custom_objects/associations.py">list</a>(object_id, custom_object_class_id, \*\*<a href="src/merge/types/crm/custom_objects/association_list_params.py">params</a>) -> <a href="./src/merge/types/crm/custom_objects/association.py">SyncPage[Association]</a></code>

### Meta

Methods:

- <code title="get /crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/meta/post">client.crm.custom_objects.meta.<a href="./src/merge/resources/crm/custom_objects/meta.py">for_create</a>(custom_object_class_id) -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>
- <code title="get /crm/v1/custom-object-classes/{custom_object_class_id}/custom-objects/meta/patch/{id}">client.crm.custom_objects.meta.<a href="./src/merge/resources/crm/custom_objects/meta.py">for_update</a>(id, custom_object_class_id) -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

### Generators

Methods:

- <code title="put /crm/v1/custom-object-classes/generator/{generator_id}">client.crm.custom_objects.generators.<a href="./src/merge/resources/crm/custom_objects/generators.py">update</a>(generator_id) -> <a href="./src/merge/types/crm/custom_object_class.py">CustomObjectClass</a></code>

## EngagementTypes

Types:

```python
from merge.types.crm import EngagementType
```

Methods:

- <code title="get /crm/v1/engagement-types/{id}">client.crm.engagement_types.<a href="./src/merge/resources/crm/engagement_types.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/engagement_type_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/engagement_type.py">EngagementType</a></code>
- <code title="get /crm/v1/engagement-types">client.crm.engagement_types.<a href="./src/merge/resources/crm/engagement_types.py">list</a>(\*\*<a href="src/merge/types/crm/engagement_type_list_params.py">params</a>) -> <a href="./src/merge/types/crm/engagement_type.py">SyncPage[EngagementType]</a></code>
- <code title="get /crm/v1/engagement-types/remote-field-classes">client.crm.engagement_types.<a href="./src/merge/resources/crm/engagement_types.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/crm/engagement_type_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

## Engagements

Types:

```python
from merge.types.crm import Engagement, EngagementResponse
```

Methods:

- <code title="post /crm/v1/engagements">client.crm.engagements.<a href="./src/merge/resources/crm/engagements/engagements.py">create</a>(\*\*<a href="src/merge/types/crm/engagement_create_params.py">params</a>) -> <a href="./src/merge/types/crm/engagement_response.py">EngagementResponse</a></code>
- <code title="get /crm/v1/engagements/{id}">client.crm.engagements.<a href="./src/merge/resources/crm/engagements/engagements.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/engagement_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/engagement.py">Engagement</a></code>
- <code title="patch /crm/v1/engagements/{id}">client.crm.engagements.<a href="./src/merge/resources/crm/engagements/engagements.py">update</a>(id, \*\*<a href="src/merge/types/crm/engagement_update_params.py">params</a>) -> <a href="./src/merge/types/crm/engagement_response.py">EngagementResponse</a></code>
- <code title="get /crm/v1/engagements">client.crm.engagements.<a href="./src/merge/resources/crm/engagements/engagements.py">list</a>(\*\*<a href="src/merge/types/crm/engagement_list_params.py">params</a>) -> <a href="./src/merge/types/crm/engagement.py">SyncPage[Engagement]</a></code>
- <code title="get /crm/v1/engagements/remote-field-classes">client.crm.engagements.<a href="./src/merge/resources/crm/engagements/engagements.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/crm/engagement_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

### Meta

Methods:

- <code title="get /crm/v1/engagements/meta/post">client.crm.engagements.meta.<a href="./src/merge/resources/crm/engagements/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>
- <code title="get /crm/v1/engagements/meta/patch/{id}">client.crm.engagements.meta.<a href="./src/merge/resources/crm/engagements/meta.py">for_update</a>(id) -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Leads

Types:

```python
from merge.types.crm import Lead, LeadResponse
```

Methods:

- <code title="post /crm/v1/leads">client.crm.leads.<a href="./src/merge/resources/crm/leads/leads.py">create</a>(\*\*<a href="src/merge/types/crm/lead_create_params.py">params</a>) -> <a href="./src/merge/types/crm/lead_response.py">LeadResponse</a></code>
- <code title="get /crm/v1/leads/{id}">client.crm.leads.<a href="./src/merge/resources/crm/leads/leads.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/lead_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/lead.py">Lead</a></code>
- <code title="get /crm/v1/leads">client.crm.leads.<a href="./src/merge/resources/crm/leads/leads.py">list</a>(\*\*<a href="src/merge/types/crm/lead_list_params.py">params</a>) -> <a href="./src/merge/types/crm/lead.py">SyncPage[Lead]</a></code>
- <code title="get /crm/v1/leads/remote-field-classes">client.crm.leads.<a href="./src/merge/resources/crm/leads/leads.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/crm/lead_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

### Meta

Methods:

- <code title="get /crm/v1/leads/meta/post">client.crm.leads.meta.<a href="./src/merge/resources/crm/leads/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Notes

Types:

```python
from merge.types.crm import Note, NoteResponse
```

Methods:

- <code title="post /crm/v1/notes">client.crm.notes.<a href="./src/merge/resources/crm/notes/notes.py">create</a>(\*\*<a href="src/merge/types/crm/note_create_params.py">params</a>) -> <a href="./src/merge/types/crm/note_response.py">NoteResponse</a></code>
- <code title="get /crm/v1/notes/{id}">client.crm.notes.<a href="./src/merge/resources/crm/notes/notes.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/note_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/note.py">Note</a></code>
- <code title="get /crm/v1/notes">client.crm.notes.<a href="./src/merge/resources/crm/notes/notes.py">list</a>(\*\*<a href="src/merge/types/crm/note_list_params.py">params</a>) -> <a href="./src/merge/types/crm/note.py">SyncPage[Note]</a></code>
- <code title="get /crm/v1/notes/remote-field-classes">client.crm.notes.<a href="./src/merge/resources/crm/notes/notes.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/crm/note_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

### Meta

Methods:

- <code title="get /crm/v1/notes/meta/post">client.crm.notes.meta.<a href="./src/merge/resources/crm/notes/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Opportunities

Types:

```python
from merge.types.crm import Opportunity, OpportunityResponse
```

Methods:

- <code title="post /crm/v1/opportunities">client.crm.opportunities.<a href="./src/merge/resources/crm/opportunities/opportunities.py">create</a>(\*\*<a href="src/merge/types/crm/opportunity_create_params.py">params</a>) -> <a href="./src/merge/types/crm/opportunity_response.py">OpportunityResponse</a></code>
- <code title="get /crm/v1/opportunities/{id}">client.crm.opportunities.<a href="./src/merge/resources/crm/opportunities/opportunities.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/opportunity_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/opportunity.py">Opportunity</a></code>
- <code title="patch /crm/v1/opportunities/{id}">client.crm.opportunities.<a href="./src/merge/resources/crm/opportunities/opportunities.py">update</a>(id, \*\*<a href="src/merge/types/crm/opportunity_update_params.py">params</a>) -> <a href="./src/merge/types/crm/opportunity_response.py">OpportunityResponse</a></code>
- <code title="get /crm/v1/opportunities">client.crm.opportunities.<a href="./src/merge/resources/crm/opportunities/opportunities.py">list</a>(\*\*<a href="src/merge/types/crm/opportunity_list_params.py">params</a>) -> <a href="./src/merge/types/crm/opportunity.py">SyncPage[Opportunity]</a></code>
- <code title="get /crm/v1/opportunities/remote-field-classes">client.crm.opportunities.<a href="./src/merge/resources/crm/opportunities/opportunities.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/crm/opportunity_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

### Meta

Methods:

- <code title="get /crm/v1/opportunities/meta/post">client.crm.opportunities.meta.<a href="./src/merge/resources/crm/opportunities/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>
- <code title="get /crm/v1/opportunities/meta/patch/{id}">client.crm.opportunities.meta.<a href="./src/merge/resources/crm/opportunities/meta.py">for_update</a>(id) -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Stages

Types:

```python
from merge.types.crm import Stage
```

Methods:

- <code title="get /crm/v1/stages/{id}">client.crm.stages.<a href="./src/merge/resources/crm/stages.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/stage_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/stage.py">Stage</a></code>
- <code title="get /crm/v1/stages">client.crm.stages.<a href="./src/merge/resources/crm/stages.py">list</a>(\*\*<a href="src/merge/types/crm/stage_list_params.py">params</a>) -> <a href="./src/merge/types/crm/stage.py">SyncPage[Stage]</a></code>
- <code title="get /crm/v1/stages/remote-field-classes">client.crm.stages.<a href="./src/merge/resources/crm/stages.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/crm/stage_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

## Tasks

Types:

```python
from merge.types.crm import Task, TaskCreateResponse
```

Methods:

- <code title="post /crm/v1/tasks">client.crm.tasks.<a href="./src/merge/resources/crm/tasks/tasks.py">create</a>(\*\*<a href="src/merge/types/crm/task_create_params.py">params</a>) -> <a href="./src/merge/types/crm/task_create_response.py">TaskCreateResponse</a></code>
- <code title="get /crm/v1/tasks/{id}">client.crm.tasks.<a href="./src/merge/resources/crm/tasks/tasks.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/task_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/task.py">Task</a></code>
- <code title="patch /crm/v1/tasks/{id}">client.crm.tasks.<a href="./src/merge/resources/crm/tasks/tasks.py">update</a>(id, \*\*<a href="src/merge/types/crm/task_update_params.py">params</a>) -> <a href="./src/merge/types/crm/task_create_response.py">TaskCreateResponse</a></code>
- <code title="get /crm/v1/tasks">client.crm.tasks.<a href="./src/merge/resources/crm/tasks/tasks.py">list</a>(\*\*<a href="src/merge/types/crm/task_list_params.py">params</a>) -> <a href="./src/merge/types/crm/task.py">SyncPage[Task]</a></code>
- <code title="get /crm/v1/tasks/remote-field-classes">client.crm.tasks.<a href="./src/merge/resources/crm/tasks/tasks.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/crm/task_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

### Meta

Methods:

- <code title="get /crm/v1/tasks/meta/post">client.crm.tasks.meta.<a href="./src/merge/resources/crm/tasks/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>
- <code title="get /crm/v1/tasks/meta/patch/{id}">client.crm.tasks.meta.<a href="./src/merge/resources/crm/tasks/meta.py">for_update</a>(id) -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Users

Types:

```python
from merge.types.crm import User
```

Methods:

- <code title="get /crm/v1/users/{id}">client.crm.users.<a href="./src/merge/resources/crm/users.py">retrieve</a>(id, \*\*<a href="src/merge/types/crm/user_retrieve_params.py">params</a>) -> <a href="./src/merge/types/crm/user.py">User</a></code>
- <code title="get /crm/v1/users">client.crm.users.<a href="./src/merge/resources/crm/users.py">list</a>(\*\*<a href="src/merge/types/crm/user_list_params.py">params</a>) -> <a href="./src/merge/types/crm/user.py">SyncPage[User]</a></code>
- <code title="post /crm/v1/users/ignore/{model_id}">client.crm.users.<a href="./src/merge/resources/crm/users.py">ignore_row</a>(model_id, \*\*<a href="src/merge/types/crm/user_ignore_row_params.py">params</a>) -> None</code>
- <code title="get /crm/v1/users/remote-field-classes">client.crm.users.<a href="./src/merge/resources/crm/users.py">list_remote_field_classes</a>(\*\*<a href="src/merge/types/crm/user_list_remote_field_classes_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_field_class.py">SyncPage[shared.RemoteFieldClass]</a></code>

## AccountDetails

Methods:

- <code title="get /crm/v1/account-details">client.crm.account_details.<a href="./src/merge/resources/crm/account_details.py">retrieve</a>() -> <a href="./src/merge/types/shared/account_detail.py">shared.AccountDetail</a></code>

## AccountTokens

Methods:

- <code title="get /crm/v1/account-token/{public_token}">client.crm.account_tokens.<a href="./src/merge/resources/crm/account_tokens.py">retrieve</a>(public_token) -> <a href="./src/merge/types/shared/account_token.py">shared.AccountToken</a></code>

## LinkTokens

Methods:

- <code title="post /crm/v1/link-token">client.crm.link_tokens.<a href="./src/merge/resources/crm/link_tokens.py">create</a>(\*\*<a href="src/merge/types/crm/link_token_create_params.py">params</a>) -> <a href="./src/merge/types/shared/link_token.py">shared.LinkToken</a></code>

## AvailableActions

Methods:

- <code title="get /crm/v1/available-actions">client.crm.available_actions.<a href="./src/merge/resources/crm/available_actions.py">retrieve</a>() -> <a href="./src/merge/types/shared/available_action.py">shared.AvailableAction</a></code>

## RemoteKeys

Methods:

- <code title="post /crm/v1/generate-key">client.crm.remote_keys.<a href="./src/merge/resources/crm/remote_keys.py">generate</a>(\*\*<a href="src/merge/types/crm/remote_key_generate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>
- <code title="post /crm/v1/regenerate-key">client.crm.remote_keys.<a href="./src/merge/resources/crm/remote_keys.py">regenerate</a>(\*\*<a href="src/merge/types/crm/remote_key_regenerate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>

## Issues

Methods:

- <code title="get /crm/v1/issues/{id}">client.crm.issues.<a href="./src/merge/resources/crm/issues.py">retrieve</a>(id) -> <a href="./src/merge/types/shared/issue.py">shared.Issue</a></code>
- <code title="get /crm/v1/issues">client.crm.issues.<a href="./src/merge/resources/crm/issues.py">list</a>(\*\*<a href="src/merge/types/crm/issue_list_params.py">params</a>) -> <a href="./src/merge/types/shared/issue.py">SyncPage[shared.Issue]</a></code>

## CommonModelScopes

Methods:

- <code title="get /crm/v1/common-model-scopes">client.crm.common_model_scopes.<a href="./src/merge/resources/crm/common_model_scopes.py">retrieve</a>(\*\*<a href="src/merge/types/crm/common_model_scope_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>
- <code title="post /crm/v1/common-model-scopes">client.crm.common_model_scopes.<a href="./src/merge/resources/crm/common_model_scopes.py">update</a>(\*\*<a href="src/merge/types/crm/common_model_scope_update_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>

## PassthroughRequests

Methods:

- <code title="post /crm/v1/passthrough">client.crm.passthrough_requests.<a href="./src/merge/resources/crm/passthrough_requests.py">send</a>(\*\*<a href="src/merge/types/crm/passthrough_request_send_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_response.py">shared.RemoteResponse</a></code>

## SyncStatus

Types:

```python
from merge.types.crm import SyncStatusResyncResponse
```

Methods:

- <code title="get /crm/v1/sync-status">client.crm.sync_status.<a href="./src/merge/resources/crm/sync_status.py">list</a>(\*\*<a href="src/merge/types/crm/sync_status_list_params.py">params</a>) -> <a href="./src/merge/types/shared/sync_status.py">SyncPage[shared.SyncStatus]</a></code>
- <code title="post /crm/v1/sync-status/resync">client.crm.sync_status.<a href="./src/merge/resources/crm/sync_status.py">resync</a>() -> <a href="./src/merge/types/crm/sync_status_resync_response.py">SyncStatusResyncResponse</a></code>

## WebhookReceivers

Types:

```python
from merge.types.crm import WebhookReceiverListResponse
```

Methods:

- <code title="post /crm/v1/webhook-receivers">client.crm.webhook_receivers.<a href="./src/merge/resources/crm/webhook_receivers.py">create</a>(\*\*<a href="src/merge/types/crm/webhook_receiver_create_params.py">params</a>) -> <a href="./src/merge/types/shared/webhook_receiver.py">shared.WebhookReceiver</a></code>
- <code title="get /crm/v1/webhook-receivers">client.crm.webhook_receivers.<a href="./src/merge/resources/crm/webhook_receivers.py">list</a>() -> <a href="./src/merge/types/crm/webhook_receiver_list_response.py">WebhookReceiverListResponse</a></code>

## LinkedAccounts

Methods:

- <code title="get /crm/v1/linked-accounts">client.crm.linked_accounts.<a href="./src/merge/resources/crm/linked_accounts.py">list</a>(\*\*<a href="src/merge/types/crm/linked_account_list_params.py">params</a>) -> <a href="./src/merge/types/shared/account_details_and_actions.py">SyncPage[shared.AccountDetailsAndActions]</a></code>
- <code title="post /crm/v1/delete-account">client.crm.linked_accounts.<a href="./src/merge/resources/crm/linked_accounts.py">delete</a>() -> None</code>

## SelectiveSync

Types:

```python
from merge.types.crm import (
    SelectiveSyncReplaceConfigurationsResponse,
    SelectiveSyncListConfigurationsResponse,
)
```

Methods:

- <code title="get /crm/v1/selective-sync/configurations">client.crm.selective_sync.<a href="./src/merge/resources/crm/selective_sync.py">list_configurations</a>() -> <a href="./src/merge/types/crm/selective_sync_list_configurations_response.py">SelectiveSyncListConfigurationsResponse</a></code>
- <code title="get /crm/v1/selective-sync/meta">client.crm.selective_sync.<a href="./src/merge/resources/crm/selective_sync.py">list_metadata</a>(\*\*<a href="src/merge/types/crm/selective_sync_list_metadata_params.py">params</a>) -> <a href="./src/merge/types/shared/condition_schema.py">SyncPage[shared.ConditionSchema]</a></code>
- <code title="put /crm/v1/selective-sync/configurations">client.crm.selective_sync.<a href="./src/merge/resources/crm/selective_sync.py">replace_configurations</a>(\*\*<a href="src/merge/types/crm/selective_sync_replace_configurations_params.py">params</a>) -> <a href="./src/merge/types/crm/selective_sync_replace_configurations_response.py">SelectiveSyncReplaceConfigurationsResponse</a></code>

# Marketing

## Actions

Types:

```python
from merge.types.marketing import Action, ActionResponse
```

Methods:

- <code title="post /mktg/v1/actions">client.marketing.actions.<a href="./src/merge/resources/marketing/actions/actions.py">create</a>(\*\*<a href="src/merge/types/marketing/action_create_params.py">params</a>) -> <a href="./src/merge/types/marketing/action_response.py">ActionResponse</a></code>
- <code title="get /mktg/v1/actions/{id}">client.marketing.actions.<a href="./src/merge/resources/marketing/actions/actions.py">retrieve</a>(id, \*\*<a href="src/merge/types/marketing/action_retrieve_params.py">params</a>) -> <a href="./src/merge/types/marketing/action.py">Action</a></code>
- <code title="get /mktg/v1/actions">client.marketing.actions.<a href="./src/merge/resources/marketing/actions/actions.py">list</a>(\*\*<a href="src/merge/types/marketing/action_list_params.py">params</a>) -> <a href="./src/merge/types/marketing/action.py">SyncPage[Action]</a></code>

### Meta

Methods:

- <code title="get /mktg/v1/actions/meta/post">client.marketing.actions.meta.<a href="./src/merge/resources/marketing/actions/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Automations

Types:

```python
from merge.types.marketing import Automation, AutomationResponse
```

Methods:

- <code title="post /mktg/v1/automations">client.marketing.automations.<a href="./src/merge/resources/marketing/automations/automations.py">create</a>(\*\*<a href="src/merge/types/marketing/automation_create_params.py">params</a>) -> <a href="./src/merge/types/marketing/automation_response.py">AutomationResponse</a></code>
- <code title="get /mktg/v1/automations/{id}">client.marketing.automations.<a href="./src/merge/resources/marketing/automations/automations.py">retrieve</a>(id, \*\*<a href="src/merge/types/marketing/automation_retrieve_params.py">params</a>) -> <a href="./src/merge/types/marketing/automation.py">Automation</a></code>
- <code title="get /mktg/v1/automations">client.marketing.automations.<a href="./src/merge/resources/marketing/automations/automations.py">list</a>(\*\*<a href="src/merge/types/marketing/automation_list_params.py">params</a>) -> <a href="./src/merge/types/marketing/automation.py">SyncPage[Automation]</a></code>
- <code title="get /mktg/v1/automations/{parent_id}/recipients">client.marketing.automations.<a href="./src/merge/resources/marketing/automations/automations.py">list_recipients</a>(parent_id, \*\*<a href="src/merge/types/marketing/automation_list_recipients_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">SyncPage[shared.Contact]</a></code>

### Meta

Methods:

- <code title="get /mktg/v1/automations/meta/post">client.marketing.automations.meta.<a href="./src/merge/resources/marketing/automations/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Campaigns

Types:

```python
from merge.types.marketing import Campaign, CampaignResponse
```

Methods:

- <code title="post /mktg/v1/campaigns">client.marketing.campaigns.<a href="./src/merge/resources/marketing/campaigns/campaigns.py">create</a>(\*\*<a href="src/merge/types/marketing/campaign_create_params.py">params</a>) -> <a href="./src/merge/types/marketing/campaign_response.py">CampaignResponse</a></code>
- <code title="get /mktg/v1/campaigns/{id}">client.marketing.campaigns.<a href="./src/merge/resources/marketing/campaigns/campaigns.py">retrieve</a>(id, \*\*<a href="src/merge/types/marketing/campaign_retrieve_params.py">params</a>) -> <a href="./src/merge/types/marketing/campaign.py">Campaign</a></code>
- <code title="get /mktg/v1/campaigns">client.marketing.campaigns.<a href="./src/merge/resources/marketing/campaigns/campaigns.py">list</a>(\*\*<a href="src/merge/types/marketing/campaign_list_params.py">params</a>) -> <a href="./src/merge/types/marketing/campaign.py">SyncPage[Campaign]</a></code>
- <code title="get /mktg/v1/campaigns/{parent_id}/contacts">client.marketing.campaigns.<a href="./src/merge/resources/marketing/campaigns/campaigns.py">list_contacts</a>(parent_id, \*\*<a href="src/merge/types/marketing/campaign_list_contacts_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">SyncPage[shared.Contact]</a></code>

### Meta

Methods:

- <code title="get /mktg/v1/campaigns/meta/post">client.marketing.campaigns.meta.<a href="./src/merge/resources/marketing/campaigns/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Contacts

Types:

```python
from merge.types.marketing import ContactResponse
```

Methods:

- <code title="post /mktg/v1/contacts">client.marketing.contacts.<a href="./src/merge/resources/marketing/contacts/contacts.py">create</a>(\*\*<a href="src/merge/types/marketing/contact_create_params.py">params</a>) -> <a href="./src/merge/types/marketing/contact_response.py">ContactResponse</a></code>
- <code title="get /mktg/v1/contacts/{id}">client.marketing.contacts.<a href="./src/merge/resources/marketing/contacts/contacts.py">retrieve</a>(id, \*\*<a href="src/merge/types/marketing/contact_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">shared.Contact</a></code>
- <code title="get /mktg/v1/contacts">client.marketing.contacts.<a href="./src/merge/resources/marketing/contacts/contacts.py">list</a>(\*\*<a href="src/merge/types/marketing/contact_list_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">SyncPage[shared.Contact]</a></code>

### Meta

Methods:

- <code title="get /mktg/v1/contacts/meta/post">client.marketing.contacts.meta.<a href="./src/merge/resources/marketing/contacts/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Emails

Types:

```python
from merge.types.marketing import Email
```

Methods:

- <code title="get /mktg/v1/emails/{id}">client.marketing.emails.<a href="./src/merge/resources/marketing/emails.py">retrieve</a>(id, \*\*<a href="src/merge/types/marketing/email_retrieve_params.py">params</a>) -> <a href="./src/merge/types/marketing/email.py">Email</a></code>
- <code title="get /mktg/v1/emails">client.marketing.emails.<a href="./src/merge/resources/marketing/emails.py">list</a>(\*\*<a href="src/merge/types/marketing/email_list_params.py">params</a>) -> <a href="./src/merge/types/marketing/email.py">SyncPage[Email]</a></code>
- <code title="get /mktg/v1/emails/{parent_id}/recipients">client.marketing.emails.<a href="./src/merge/resources/marketing/emails.py">list_recipients</a>(parent_id, \*\*<a href="src/merge/types/marketing/email_list_recipients_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">SyncPage[shared.Contact]</a></code>

## Events

Types:

```python
from merge.types.marketing import Event
```

Methods:

- <code title="get /mktg/v1/events/{id}">client.marketing.events.<a href="./src/merge/resources/marketing/events.py">retrieve</a>(id, \*\*<a href="src/merge/types/marketing/event_retrieve_params.py">params</a>) -> <a href="./src/merge/types/marketing/event.py">Event</a></code>
- <code title="get /mktg/v1/events">client.marketing.events.<a href="./src/merge/resources/marketing/events.py">list</a>(\*\*<a href="src/merge/types/marketing/event_list_params.py">params</a>) -> <a href="./src/merge/types/marketing/event.py">SyncPage[Event]</a></code>
- <code title="get /mktg/v1/events/{parent_id}/contacts">client.marketing.events.<a href="./src/merge/resources/marketing/events.py">list_contacts</a>(parent_id, \*\*<a href="src/merge/types/marketing/event_list_contacts_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">SyncPage[shared.Contact]</a></code>

## ContactLists

Types:

```python
from merge.types.marketing import ContactList, ContactListCreateResponse
```

Methods:

- <code title="post /mktg/v1/lists">client.marketing.contact_lists.<a href="./src/merge/resources/marketing/contact_lists/contact_lists.py">create</a>(\*\*<a href="src/merge/types/marketing/contact_list_create_params.py">params</a>) -> <a href="./src/merge/types/marketing/contact_list_create_response.py">ContactListCreateResponse</a></code>
- <code title="get /mktg/v1/lists/{id}">client.marketing.contact_lists.<a href="./src/merge/resources/marketing/contact_lists/contact_lists.py">retrieve</a>(id, \*\*<a href="src/merge/types/marketing/contact_list_retrieve_params.py">params</a>) -> <a href="./src/merge/types/marketing/contact_list.py">ContactList</a></code>
- <code title="get /mktg/v1/lists">client.marketing.contact_lists.<a href="./src/merge/resources/marketing/contact_lists/contact_lists.py">list</a>(\*\*<a href="src/merge/types/marketing/contact_list_list_params.py">params</a>) -> <a href="./src/merge/types/marketing/contact_list.py">SyncPage[ContactList]</a></code>
- <code title="get /mktg/v1/lists/{parent_id}/subscribers">client.marketing.contact_lists.<a href="./src/merge/resources/marketing/contact_lists/contact_lists.py">list_subscribers</a>(parent_id, \*\*<a href="src/merge/types/marketing/contact_list_list_subscribers_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">SyncPage[shared.Contact]</a></code>

### Meta

Methods:

- <code title="get /mktg/v1/lists/meta/post">client.marketing.contact_lists.meta.<a href="./src/merge/resources/marketing/contact_lists/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Messages

Types:

```python
from merge.types.marketing import Message
```

Methods:

- <code title="get /mktg/v1/messages/{id}">client.marketing.messages.<a href="./src/merge/resources/marketing/messages.py">retrieve</a>(id, \*\*<a href="src/merge/types/marketing/message_retrieve_params.py">params</a>) -> <a href="./src/merge/types/marketing/message.py">Message</a></code>
- <code title="get /mktg/v1/messages">client.marketing.messages.<a href="./src/merge/resources/marketing/messages.py">list</a>(\*\*<a href="src/merge/types/marketing/message_list_params.py">params</a>) -> <a href="./src/merge/types/marketing/message.py">SyncPage[Message]</a></code>
- <code title="get /mktg/v1/messages/{parent_id}/recipients">client.marketing.messages.<a href="./src/merge/resources/marketing/messages.py">list_recipients</a>(parent_id, \*\*<a href="src/merge/types/marketing/message_list_recipients_params.py">params</a>) -> <a href="./src/merge/types/shared/contact.py">SyncPage[shared.Contact]</a></code>

## Templates

Types:

```python
from merge.types.marketing import Template, TemplateResponse
```

Methods:

- <code title="post /mktg/v1/templates">client.marketing.templates.<a href="./src/merge/resources/marketing/templates/templates.py">create</a>(\*\*<a href="src/merge/types/marketing/template_create_params.py">params</a>) -> <a href="./src/merge/types/marketing/template_response.py">TemplateResponse</a></code>
- <code title="get /mktg/v1/templates/{id}">client.marketing.templates.<a href="./src/merge/resources/marketing/templates/templates.py">retrieve</a>(id, \*\*<a href="src/merge/types/marketing/template_retrieve_params.py">params</a>) -> <a href="./src/merge/types/marketing/template.py">Template</a></code>
- <code title="get /mktg/v1/templates">client.marketing.templates.<a href="./src/merge/resources/marketing/templates/templates.py">list</a>(\*\*<a href="src/merge/types/marketing/template_list_params.py">params</a>) -> <a href="./src/merge/types/marketing/template.py">SyncPage[Template]</a></code>

### Meta

Methods:

- <code title="get /mktg/v1/templates/meta/post">client.marketing.templates.meta.<a href="./src/merge/resources/marketing/templates/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Users

Types:

```python
from merge.types.marketing import User
```

Methods:

- <code title="get /mktg/v1/users/{id}">client.marketing.users.<a href="./src/merge/resources/marketing/users.py">retrieve</a>(id, \*\*<a href="src/merge/types/marketing/user_retrieve_params.py">params</a>) -> <a href="./src/merge/types/marketing/user.py">User</a></code>
- <code title="get /mktg/v1/users">client.marketing.users.<a href="./src/merge/resources/marketing/users.py">list</a>(\*\*<a href="src/merge/types/marketing/user_list_params.py">params</a>) -> <a href="./src/merge/types/marketing/user.py">SyncPage[User]</a></code>

## AccountDetails

Methods:

- <code title="get /mktg/v1/account-details">client.marketing.account_details.<a href="./src/merge/resources/marketing/account_details.py">retrieve</a>() -> <a href="./src/merge/types/shared/account_detail.py">shared.AccountDetail</a></code>

## AccountTokens

Methods:

- <code title="get /mktg/v1/account-token/{public_token}">client.marketing.account_tokens.<a href="./src/merge/resources/marketing/account_tokens.py">retrieve</a>(public_token) -> <a href="./src/merge/types/shared/account_token.py">shared.AccountToken</a></code>

## LinkTokens

Methods:

- <code title="post /mktg/v1/link-token">client.marketing.link_tokens.<a href="./src/merge/resources/marketing/link_tokens.py">create</a>(\*\*<a href="src/merge/types/marketing/link_token_create_params.py">params</a>) -> <a href="./src/merge/types/shared/link_token.py">shared.LinkToken</a></code>

## AvailableActions

Methods:

- <code title="get /mktg/v1/available-actions">client.marketing.available_actions.<a href="./src/merge/resources/marketing/available_actions.py">retrieve</a>() -> <a href="./src/merge/types/shared/available_action.py">shared.AvailableAction</a></code>

## RemoteKeys

Methods:

- <code title="post /mktg/v1/generate-key">client.marketing.remote_keys.<a href="./src/merge/resources/marketing/remote_keys.py">generate</a>(\*\*<a href="src/merge/types/marketing/remote_key_generate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>
- <code title="post /mktg/v1/regenerate-key">client.marketing.remote_keys.<a href="./src/merge/resources/marketing/remote_keys.py">regenerate</a>(\*\*<a href="src/merge/types/marketing/remote_key_regenerate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>

## Issues

Methods:

- <code title="get /mktg/v1/issues/{id}">client.marketing.issues.<a href="./src/merge/resources/marketing/issues.py">retrieve</a>(id) -> <a href="./src/merge/types/shared/issue.py">shared.Issue</a></code>
- <code title="get /mktg/v1/issues">client.marketing.issues.<a href="./src/merge/resources/marketing/issues.py">list</a>(\*\*<a href="src/merge/types/marketing/issue_list_params.py">params</a>) -> <a href="./src/merge/types/shared/issue.py">SyncPage[shared.Issue]</a></code>

## CommonModelScopes

Methods:

- <code title="get /mktg/v1/common-model-scopes">client.marketing.common_model_scopes.<a href="./src/merge/resources/marketing/common_model_scopes.py">retrieve</a>(\*\*<a href="src/merge/types/marketing/common_model_scope_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>
- <code title="post /mktg/v1/common-model-scopes">client.marketing.common_model_scopes.<a href="./src/merge/resources/marketing/common_model_scopes.py">update</a>(\*\*<a href="src/merge/types/marketing/common_model_scope_update_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>

## PassthroughRequests

Methods:

- <code title="post /mktg/v1/passthrough">client.marketing.passthrough_requests.<a href="./src/merge/resources/marketing/passthrough_requests.py">send</a>(\*\*<a href="src/merge/types/marketing/passthrough_request_send_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_response.py">shared.RemoteResponse</a></code>

## SyncStatus

Types:

```python
from merge.types.marketing import SyncStatusResyncResponse
```

Methods:

- <code title="get /mktg/v1/sync-status">client.marketing.sync_status.<a href="./src/merge/resources/marketing/sync_status.py">list</a>(\*\*<a href="src/merge/types/marketing/sync_status_list_params.py">params</a>) -> <a href="./src/merge/types/shared/sync_status.py">SyncPage[shared.SyncStatus]</a></code>
- <code title="post /mktg/v1/sync-status/resync">client.marketing.sync_status.<a href="./src/merge/resources/marketing/sync_status.py">resync</a>() -> <a href="./src/merge/types/marketing/sync_status_resync_response.py">SyncStatusResyncResponse</a></code>

## WebhookReceivers

Types:

```python
from merge.types.marketing import WebhookReceiverListResponse
```

Methods:

- <code title="post /mktg/v1/webhook-receivers">client.marketing.webhook_receivers.<a href="./src/merge/resources/marketing/webhook_receivers.py">create</a>(\*\*<a href="src/merge/types/marketing/webhook_receiver_create_params.py">params</a>) -> <a href="./src/merge/types/shared/webhook_receiver.py">shared.WebhookReceiver</a></code>
- <code title="get /mktg/v1/webhook-receivers">client.marketing.webhook_receivers.<a href="./src/merge/resources/marketing/webhook_receivers.py">list</a>() -> <a href="./src/merge/types/marketing/webhook_receiver_list_response.py">WebhookReceiverListResponse</a></code>

## LinkedAccounts

Methods:

- <code title="get /mktg/v1/linked-accounts">client.marketing.linked_accounts.<a href="./src/merge/resources/marketing/linked_accounts.py">list</a>(\*\*<a href="src/merge/types/marketing/linked_account_list_params.py">params</a>) -> <a href="./src/merge/types/shared/account_details_and_actions.py">SyncPage[shared.AccountDetailsAndActions]</a></code>
- <code title="post /mktg/v1/delete-account">client.marketing.linked_accounts.<a href="./src/merge/resources/marketing/linked_accounts.py">delete</a>() -> None</code>

## SelectiveSync

Types:

```python
from merge.types.marketing import (
    SelectiveSyncReplaceConfigurationsResponse,
    SelectiveSyncListConfigurationsResponse,
)
```

Methods:

- <code title="get /mktg/v1/selective-sync/configurations">client.marketing.selective_sync.<a href="./src/merge/resources/marketing/selective_sync.py">list_configurations</a>() -> <a href="./src/merge/types/marketing/selective_sync_list_configurations_response.py">SelectiveSyncListConfigurationsResponse</a></code>
- <code title="get /mktg/v1/selective-sync/meta">client.marketing.selective_sync.<a href="./src/merge/resources/marketing/selective_sync.py">list_metadata</a>(\*\*<a href="src/merge/types/marketing/selective_sync_list_metadata_params.py">params</a>) -> <a href="./src/merge/types/shared/condition_schema.py">SyncPage[shared.ConditionSchema]</a></code>
- <code title="put /mktg/v1/selective-sync/configurations">client.marketing.selective_sync.<a href="./src/merge/resources/marketing/selective_sync.py">replace_configurations</a>(\*\*<a href="src/merge/types/marketing/selective_sync_replace_configurations_params.py">params</a>) -> <a href="./src/merge/types/marketing/selective_sync_replace_configurations_response.py">SelectiveSyncReplaceConfigurationsResponse</a></code>

# FileStorage

## Drives

Types:

```python
from merge.types.file_storage import Drive
```

Methods:

- <code title="get /filestorage/v1/drives/{id}">client.file_storage.drives.<a href="./src/merge/resources/file_storage/drives.py">retrieve</a>(id, \*\*<a href="src/merge/types/file_storage/drive_retrieve_params.py">params</a>) -> <a href="./src/merge/types/file_storage/drive.py">Drive</a></code>
- <code title="get /filestorage/v1/drives">client.file_storage.drives.<a href="./src/merge/resources/file_storage/drives.py">list</a>(\*\*<a href="src/merge/types/file_storage/drive_list_params.py">params</a>) -> <a href="./src/merge/types/file_storage/drive.py">SyncPage[Drive]</a></code>

## Files

Types:

```python
from merge.types.file_storage import File, FileResponse
```

Methods:

- <code title="post /filestorage/v1/files">client.file_storage.files.<a href="./src/merge/resources/file_storage/files/files.py">create</a>(\*\*<a href="src/merge/types/file_storage/file_create_params.py">params</a>) -> <a href="./src/merge/types/file_storage/file_response.py">FileResponse</a></code>
- <code title="get /filestorage/v1/files/{id}">client.file_storage.files.<a href="./src/merge/resources/file_storage/files/files.py">retrieve</a>(id, \*\*<a href="src/merge/types/file_storage/file_retrieve_params.py">params</a>) -> <a href="./src/merge/types/file_storage/file.py">File</a></code>
- <code title="get /filestorage/v1/files">client.file_storage.files.<a href="./src/merge/resources/file_storage/files/files.py">list</a>(\*\*<a href="src/merge/types/file_storage/file_list_params.py">params</a>) -> <a href="./src/merge/types/file_storage/file.py">SyncPage[File]</a></code>
- <code title="get /filestorage/v1/files/{id}/download">client.file_storage.files.<a href="./src/merge/resources/file_storage/files/files.py">download</a>(id) -> None</code>

### Meta

Methods:

- <code title="get /filestorage/v1/files/meta/post">client.file_storage.files.meta.<a href="./src/merge/resources/file_storage/files/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Folders

Types:

```python
from merge.types.file_storage import Folder, FolderResponse
```

Methods:

- <code title="post /filestorage/v1/folders">client.file_storage.folders.<a href="./src/merge/resources/file_storage/folders/folders.py">create</a>(\*\*<a href="src/merge/types/file_storage/folder_create_params.py">params</a>) -> <a href="./src/merge/types/file_storage/folder_response.py">FolderResponse</a></code>
- <code title="get /filestorage/v1/folders/{id}">client.file_storage.folders.<a href="./src/merge/resources/file_storage/folders/folders.py">retrieve</a>(id, \*\*<a href="src/merge/types/file_storage/folder_retrieve_params.py">params</a>) -> <a href="./src/merge/types/file_storage/folder.py">Folder</a></code>
- <code title="get /filestorage/v1/folders">client.file_storage.folders.<a href="./src/merge/resources/file_storage/folders/folders.py">list</a>(\*\*<a href="src/merge/types/file_storage/folder_list_params.py">params</a>) -> <a href="./src/merge/types/file_storage/folder.py">SyncPage[Folder]</a></code>

### Meta

Methods:

- <code title="get /filestorage/v1/folders/meta/post">client.file_storage.folders.meta.<a href="./src/merge/resources/file_storage/folders/meta.py">for_create</a>() -> <a href="./src/merge/types/shared/meta_response.py">shared.MetaResponse</a></code>

## Groups

Types:

```python
from merge.types.file_storage import Group
```

Methods:

- <code title="get /filestorage/v1/groups/{id}">client.file_storage.groups.<a href="./src/merge/resources/file_storage/groups.py">retrieve</a>(id, \*\*<a href="src/merge/types/file_storage/group_retrieve_params.py">params</a>) -> <a href="./src/merge/types/file_storage/group.py">Group</a></code>
- <code title="get /filestorage/v1/groups">client.file_storage.groups.<a href="./src/merge/resources/file_storage/groups.py">list</a>(\*\*<a href="src/merge/types/file_storage/group_list_params.py">params</a>) -> <a href="./src/merge/types/file_storage/group.py">SyncPage[Group]</a></code>

## Users

Types:

```python
from merge.types.file_storage import User
```

Methods:

- <code title="get /filestorage/v1/users/{id}">client.file_storage.users.<a href="./src/merge/resources/file_storage/users.py">retrieve</a>(id, \*\*<a href="src/merge/types/file_storage/user_retrieve_params.py">params</a>) -> <a href="./src/merge/types/file_storage/user.py">User</a></code>
- <code title="get /filestorage/v1/users">client.file_storage.users.<a href="./src/merge/resources/file_storage/users.py">list</a>(\*\*<a href="src/merge/types/file_storage/user_list_params.py">params</a>) -> <a href="./src/merge/types/file_storage/user.py">SyncPage[User]</a></code>

## AccountDetails

Methods:

- <code title="get /filestorage/v1/account-details">client.file_storage.account_details.<a href="./src/merge/resources/file_storage/account_details.py">retrieve</a>() -> <a href="./src/merge/types/shared/account_detail.py">shared.AccountDetail</a></code>

## AccountTokens

Methods:

- <code title="get /filestorage/v1/account-token/{public_token}">client.file_storage.account_tokens.<a href="./src/merge/resources/file_storage/account_tokens.py">retrieve</a>(public_token) -> <a href="./src/merge/types/shared/account_token.py">shared.AccountToken</a></code>

## LinkTokens

Methods:

- <code title="post /filestorage/v1/link-token">client.file_storage.link_tokens.<a href="./src/merge/resources/file_storage/link_tokens.py">create</a>(\*\*<a href="src/merge/types/file_storage/link_token_create_params.py">params</a>) -> <a href="./src/merge/types/shared/link_token.py">shared.LinkToken</a></code>

## AvailableActions

Methods:

- <code title="get /filestorage/v1/available-actions">client.file_storage.available_actions.<a href="./src/merge/resources/file_storage/available_actions.py">retrieve</a>() -> <a href="./src/merge/types/shared/available_action.py">shared.AvailableAction</a></code>

## RemoteKeys

Methods:

- <code title="post /filestorage/v1/generate-key">client.file_storage.remote_keys.<a href="./src/merge/resources/file_storage/remote_keys.py">generate</a>(\*\*<a href="src/merge/types/file_storage/remote_key_generate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>
- <code title="post /filestorage/v1/regenerate-key">client.file_storage.remote_keys.<a href="./src/merge/resources/file_storage/remote_keys.py">regenerate</a>(\*\*<a href="src/merge/types/file_storage/remote_key_regenerate_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_key.py">shared.RemoteKey</a></code>

## Issues

Methods:

- <code title="get /filestorage/v1/issues/{id}">client.file_storage.issues.<a href="./src/merge/resources/file_storage/issues.py">retrieve</a>(id) -> <a href="./src/merge/types/shared/issue.py">shared.Issue</a></code>
- <code title="get /filestorage/v1/issues">client.file_storage.issues.<a href="./src/merge/resources/file_storage/issues.py">list</a>(\*\*<a href="src/merge/types/file_storage/issue_list_params.py">params</a>) -> <a href="./src/merge/types/shared/issue.py">SyncPage[shared.Issue]</a></code>

## CommonModelScopes

Methods:

- <code title="get /filestorage/v1/common-model-scopes">client.file_storage.common_model_scopes.<a href="./src/merge/resources/file_storage/common_model_scopes.py">retrieve</a>(\*\*<a href="src/merge/types/file_storage/common_model_scope_retrieve_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>
- <code title="post /filestorage/v1/common-model-scopes">client.file_storage.common_model_scopes.<a href="./src/merge/resources/file_storage/common_model_scopes.py">update</a>(\*\*<a href="src/merge/types/file_storage/common_model_scope_update_params.py">params</a>) -> <a href="./src/merge/types/shared/common_model_scope.py">shared.CommonModelScope</a></code>

## PassthroughRequests

Methods:

- <code title="post /filestorage/v1/passthrough">client.file_storage.passthrough_requests.<a href="./src/merge/resources/file_storage/passthrough_requests.py">send</a>(\*\*<a href="src/merge/types/file_storage/passthrough_request_send_params.py">params</a>) -> <a href="./src/merge/types/shared/remote_response.py">shared.RemoteResponse</a></code>

## SyncStatus

Types:

```python
from merge.types.file_storage import SyncStatusResyncResponse
```

Methods:

- <code title="get /filestorage/v1/sync-status">client.file_storage.sync_status.<a href="./src/merge/resources/file_storage/sync_status.py">list</a>(\*\*<a href="src/merge/types/file_storage/sync_status_list_params.py">params</a>) -> <a href="./src/merge/types/shared/sync_status.py">SyncPage[shared.SyncStatus]</a></code>
- <code title="post /filestorage/v1/sync-status/resync">client.file_storage.sync_status.<a href="./src/merge/resources/file_storage/sync_status.py">resync</a>() -> <a href="./src/merge/types/file_storage/sync_status_resync_response.py">SyncStatusResyncResponse</a></code>

## WebhookReceivers

Types:

```python
from merge.types.file_storage import WebhookReceiverListResponse
```

Methods:

- <code title="post /filestorage/v1/webhook-receivers">client.file_storage.webhook_receivers.<a href="./src/merge/resources/file_storage/webhook_receivers.py">create</a>(\*\*<a href="src/merge/types/file_storage/webhook_receiver_create_params.py">params</a>) -> <a href="./src/merge/types/shared/webhook_receiver.py">shared.WebhookReceiver</a></code>
- <code title="get /filestorage/v1/webhook-receivers">client.file_storage.webhook_receivers.<a href="./src/merge/resources/file_storage/webhook_receivers.py">list</a>() -> <a href="./src/merge/types/file_storage/webhook_receiver_list_response.py">WebhookReceiverListResponse</a></code>

## LinkedAccounts

Methods:

- <code title="get /filestorage/v1/linked-accounts">client.file_storage.linked_accounts.<a href="./src/merge/resources/file_storage/linked_accounts.py">list</a>(\*\*<a href="src/merge/types/file_storage/linked_account_list_params.py">params</a>) -> <a href="./src/merge/types/shared/account_details_and_actions.py">SyncPage[shared.AccountDetailsAndActions]</a></code>
- <code title="post /filestorage/v1/delete-account">client.file_storage.linked_accounts.<a href="./src/merge/resources/file_storage/linked_accounts.py">delete</a>() -> None</code>

## SelectiveSync

Types:

```python
from merge.types.file_storage import (
    SelectiveSyncReplaceConfigurationsResponse,
    SelectiveSyncListConfigurationsResponse,
)
```

Methods:

- <code title="get /filestorage/v1/selective-sync/configurations">client.file_storage.selective_sync.<a href="./src/merge/resources/file_storage/selective_sync.py">list_configurations</a>() -> <a href="./src/merge/types/file_storage/selective_sync_list_configurations_response.py">SelectiveSyncListConfigurationsResponse</a></code>
- <code title="get /filestorage/v1/selective-sync/meta">client.file_storage.selective_sync.<a href="./src/merge/resources/file_storage/selective_sync.py">list_metadata</a>(\*\*<a href="src/merge/types/file_storage/selective_sync_list_metadata_params.py">params</a>) -> <a href="./src/merge/types/shared/condition_schema.py">SyncPage[shared.ConditionSchema]</a></code>
- <code title="put /filestorage/v1/selective-sync/configurations">client.file_storage.selective_sync.<a href="./src/merge/resources/file_storage/selective_sync.py">replace_configurations</a>(\*\*<a href="src/merge/types/file_storage/selective_sync_replace_configurations_params.py">params</a>) -> <a href="./src/merge/types/file_storage/selective_sync_replace_configurations_response.py">SelectiveSyncReplaceConfigurationsResponse</a></code>