# Reference
## Filestorage AccountDetails
<details><summary><code>client.filestorage.account_details.<a href="src/merge/resources/filestorage/resources/account_details/client.py">retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details for a linked account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.account_details.retrieve()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage AccountToken
<details><summary><code>client.filestorage.account_token.<a href="src/merge/resources/filestorage/resources/account_token/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the account token for the end user with the provided public token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.account_token.retrieve(
    public_token="public_token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**public_token:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.account_token.<a href="src/merge/resources/filestorage/resources/account_token/client.py">regenerate_create</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange Linked Account account tokens.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.account_token.regenerate_create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage AsyncPassthrough
<details><summary><code>client.filestorage.async_passthrough.<a href="src/merge/resources/filestorage/resources/async_passthrough/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asynchronously pull data from an endpoint not currently supported by Merge.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge
from merge.resources.filestorage import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.async_passthrough.create(
    request=DataPassthroughRequest(
        method=MethodEnum.GET,
        path="/scooters",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `DataPassthroughRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.async_passthrough.<a href="src/merge/resources/filestorage/resources/async_passthrough/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves data from earlier async-passthrough POST request
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.async_passthrough.retrieve(
    async_passthrough_receipt_id="async_passthrough_receipt_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**async_passthrough_receipt_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage AuditTrail
<details><summary><code>client.filestorage.audit_trail.<a href="src/merge/resources/filestorage/resources/audit_trail/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of audit trail events.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.filestorage.audit_trail.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
    end_date="end_date",
    event_type="event_type",
    page_size=1,
    start_date="start_date",
    user_email="user_email",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — If included, will only include audit trail events that occurred before this time
    
</dd>
</dl>

<dl>
<dd>

**event_type:** `typing.Optional[str]` — If included, will only include events with the given event type. Possible values include: `CREATED_REMOTE_PRODUCTION_API_KEY`, `DELETED_REMOTE_PRODUCTION_API_KEY`, `CREATED_TEST_API_KEY`, `DELETED_TEST_API_KEY`, `REGENERATED_PRODUCTION_API_KEY`, `REGENERATED_WEBHOOK_SIGNATURE`, `INVITED_USER`, `TWO_FACTOR_AUTH_ENABLED`, `TWO_FACTOR_AUTH_DISABLED`, `DELETED_LINKED_ACCOUNT`, `DELETED_ALL_COMMON_MODELS_FOR_LINKED_ACCOUNT`, `CREATED_DESTINATION`, `DELETED_DESTINATION`, `CHANGED_DESTINATION`, `CHANGED_SCOPES`, `CHANGED_PERSONAL_INFORMATION`, `CHANGED_ORGANIZATION_SETTINGS`, `ENABLED_INTEGRATION`, `DISABLED_INTEGRATION`, `ENABLED_CATEGORY`, `DISABLED_CATEGORY`, `CHANGED_PASSWORD`, `RESET_PASSWORD`, `ENABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION`, `ENABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT`, `DISABLED_REDACT_UNMAPPED_DATA_FOR_ORGANIZATION`, `DISABLED_REDACT_UNMAPPED_DATA_FOR_LINKED_ACCOUNT`, `CREATED_INTEGRATION_WIDE_FIELD_MAPPING`, `CREATED_LINKED_ACCOUNT_FIELD_MAPPING`, `CHANGED_INTEGRATION_WIDE_FIELD_MAPPING`, `CHANGED_LINKED_ACCOUNT_FIELD_MAPPING`, `DELETED_INTEGRATION_WIDE_FIELD_MAPPING`, `DELETED_LINKED_ACCOUNT_FIELD_MAPPING`, `CREATED_LINKED_ACCOUNT_COMMON_MODEL_OVERRIDE`, `CHANGED_LINKED_ACCOUNT_COMMON_MODEL_OVERRIDE`, `DELETED_LINKED_ACCOUNT_COMMON_MODEL_OVERRIDE`, `FORCED_LINKED_ACCOUNT_RESYNC`, `MUTED_ISSUE`, `GENERATED_MAGIC_LINK`, `ENABLED_MERGE_WEBHOOK`, `DISABLED_MERGE_WEBHOOK`, `MERGE_WEBHOOK_TARGET_CHANGED`, `END_USER_CREDENTIALS_ACCESSED`
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page. The maximum limit is 100.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — If included, will only include audit trail events that occurred after this time
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `typing.Optional[str]` — If provided, this will return events associated with the specified user email. Please note that the email address reflects the user's email at the time of the event, and may not be their current email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage AvailableActions
<details><summary><code>client.filestorage.available_actions.<a href="src/merge/resources/filestorage/resources/available_actions/client.py">retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of models and actions available for an account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.available_actions.retrieve()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage Scopes
<details><summary><code>client.filestorage.scopes.<a href="src/merge/resources/filestorage/resources/scopes/client.py">default_scopes_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the default permissions for Merge Common Models and fields across all Linked Accounts of a given category. [Learn more](https://help.merge.dev/en/articles/5950052-common-model-and-field-scopes).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.scopes.default_scopes_retrieve()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.scopes.<a href="src/merge/resources/filestorage/resources/scopes/client.py">linked_account_scopes_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all available permissions for Merge Common Models and fields for a single Linked Account. [Learn more](https://help.merge.dev/en/articles/5950052-common-model-and-field-scopes).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.scopes.linked_account_scopes_retrieve()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.scopes.<a href="src/merge/resources/filestorage/resources/scopes/client.py">linked_account_scopes_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update permissions for any Common Model or field for a single Linked Account. Any Scopes not set in this POST request will inherit the default Scopes. [Learn more](https://help.merge.dev/en/articles/5950052-common-model-and-field-scopes)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge
from merge.resources.filestorage import (
    FieldPermissionDeserializerRequest,
    IndividualCommonModelScopeDeserializerRequest,
    ModelPermissionDeserializerRequest,
)

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.scopes.linked_account_scopes_create(
    common_models=[
        IndividualCommonModelScopeDeserializerRequest(
            model_name="Employee",
            model_permissions={
                "READ": ModelPermissionDeserializerRequest(
                    is_enabled=True,
                ),
                "WRITE": ModelPermissionDeserializerRequest(
                    is_enabled=False,
                ),
            },
            field_permissions=FieldPermissionDeserializerRequest(
                enabled_fields=["avatar", "home_location"],
                disabled_fields=["work_location"],
            ),
        ),
        IndividualCommonModelScopeDeserializerRequest(
            model_name="Benefit",
            model_permissions={
                "WRITE": ModelPermissionDeserializerRequest(
                    is_enabled=False,
                )
            },
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**common_models:** `typing.Sequence[IndividualCommonModelScopeDeserializerRequest]` — The common models you want to update the scopes for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage DeleteAccount
<details><summary><code>client.filestorage.delete_account.<a href="src/merge/resources/filestorage/resources/delete_account/client.py">delete</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a linked account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.delete_account.delete()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage Drives
<details><summary><code>client.filestorage.drives.<a href="src/merge/resources/filestorage/resources/drives/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Drive` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.filestorage.drives.list(
    created_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    created_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
    include_deleted_data=True,
    include_remote_data=True,
    include_shell_data=True,
    modified_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    modified_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    name="name",
    page_size=1,
    remote_id="remote_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_data:** `typing.Optional[bool]` — Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**modified_after:** `typing.Optional[dt.datetime]` — If provided, only objects synced by Merge after this date time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**modified_before:** `typing.Optional[dt.datetime]` — If provided, only objects synced by Merge before this date time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — If provided, will only return drives with this name. This performs an exact match.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.drives.<a href="src/merge/resources/filestorage/resources/drives/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Drive` object with the given `id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.drives.retrieve(
    id="id",
    include_remote_data=True,
    include_shell_data=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage FieldMapping
<details><summary><code>client.filestorage.field_mapping.<a href="src/merge/resources/filestorage/resources/field_mapping/client.py">field_mappings_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all Field Mappings for this Linked Account. Field Mappings are mappings between third-party Remote Fields and user defined Merge fields. [Learn more](https://docs.merge.dev/supplemental-data/field-mappings/overview/).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.field_mapping.field_mappings_retrieve(
    exclude_remote_field_metadata=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**exclude_remote_field_metadata:** `typing.Optional[bool]` — If `true`, remote fields metadata is excluded from each field mapping instance (i.e. `remote_fields.remote_key_name` and `remote_fields.schema` will be null). This will increase the speed of the request since these fields require some calculations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.field_mapping.<a href="src/merge/resources/filestorage/resources/field_mapping/client.py">field_mappings_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create new Field Mappings that will be available after the next scheduled sync. This will cause the next sync for this Linked Account to sync **ALL** data from start.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.field_mapping.field_mappings_create(
    exclude_remote_field_metadata=True,
    remote_data_iteration_count=1,
    target_field_name="example_target_field_name",
    target_field_description="this is a example description of the target field",
    remote_field_traversal_path=["example_remote_field"],
    remote_method="GET",
    remote_url_path="/example-url-path",
    common_model_name="ExampleCommonModel",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_field_name:** `str` — The name of the target field you want this remote field to map to.
    
</dd>
</dl>

<dl>
<dd>

**target_field_description:** `str` — The description of the target field you want this remote field to map to.
    
</dd>
</dl>

<dl>
<dd>

**remote_field_traversal_path:** `typing.Sequence[typing.Optional[typing.Any]]` — The field traversal path of the remote field listed when you hit the GET /remote-fields endpoint.
    
</dd>
</dl>

<dl>
<dd>

**remote_method:** `str` — The method of the remote endpoint where the remote field is coming from.
    
</dd>
</dl>

<dl>
<dd>

**remote_url_path:** `str` — The path of the remote endpoint where the remote field is coming from.
    
</dd>
</dl>

<dl>
<dd>

**common_model_name:** `str` — The name of the Common Model that the remote field corresponds to in a given category.
    
</dd>
</dl>

<dl>
<dd>

**exclude_remote_field_metadata:** `typing.Optional[bool]` — If `true`, remote fields metadata is excluded from each field mapping instance (i.e. `remote_fields.remote_key_name` and `remote_fields.schema` will be null). This will increase the speed of the request since these fields require some calculations.
    
</dd>
</dl>

<dl>
<dd>

**remote_data_iteration_count:** `typing.Optional[int]` — Number of common model instances to iterate through when fetching remote data for field mappings. Defaults to 250 if not provided.
    
</dd>
</dl>

<dl>
<dd>

**jmes_path:** `typing.Optional[str]` — JMES path to specify json query expression to be used on field mapping.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.field_mapping.<a href="src/merge/resources/filestorage/resources/field_mapping/client.py">field_mappings_destroy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes Field Mappings for a Linked Account. All data related to this Field Mapping will be deleted and these changes will be reflected after the next scheduled sync. This will cause the next sync for this Linked Account to sync **ALL** data from start.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.field_mapping.field_mappings_destroy(
    field_mapping_id="field_mapping_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**field_mapping_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.field_mapping.<a href="src/merge/resources/filestorage/resources/field_mapping/client.py">field_mappings_partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create or update existing Field Mappings for a Linked Account. Changes will be reflected after the next scheduled sync. This will cause the next sync for this Linked Account to sync **ALL** data from start.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.field_mapping.field_mappings_partial_update(
    field_mapping_id="field_mapping_id",
    remote_data_iteration_count=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**field_mapping_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**remote_data_iteration_count:** `typing.Optional[int]` — Number of common model instances to iterate through when fetching remote data for field mappings. Defaults to 250 if not provided.
    
</dd>
</dl>

<dl>
<dd>

**remote_field_traversal_path:** `typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]` — The field traversal path of the remote field listed when you hit the GET /remote-fields endpoint.
    
</dd>
</dl>

<dl>
<dd>

**remote_method:** `typing.Optional[str]` — The method of the remote endpoint where the remote field is coming from.
    
</dd>
</dl>

<dl>
<dd>

**remote_url_path:** `typing.Optional[str]` — The path of the remote endpoint where the remote field is coming from.
    
</dd>
</dl>

<dl>
<dd>

**jmes_path:** `typing.Optional[str]` — JMES path to specify json query expression to be used on field mapping.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.field_mapping.<a href="src/merge/resources/filestorage/resources/field_mapping/client.py">remote_fields_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all remote fields for a Linked Account. Remote fields are third-party fields that are accessible after initial sync if remote_data is enabled. You can use remote fields to override existing Merge fields or map a new Merge field. [Learn more](https://docs.merge.dev/supplemental-data/field-mappings/overview/).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.field_mapping.remote_fields_retrieve(
    common_models="common_models",
    include_example_values="include_example_values",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**common_models:** `typing.Optional[str]` — A comma seperated list of Common Model names. If included, will only return Remote Fields for those Common Models.
    
</dd>
</dl>

<dl>
<dd>

**include_example_values:** `typing.Optional[str]` — If true, will include example values, where available, for remote fields in the 3rd party platform. These examples come from active data from your customers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.field_mapping.<a href="src/merge/resources/filestorage/resources/field_mapping/client.py">target_fields_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all organization-wide Target Fields, this will not include any Linked Account specific Target Fields. Organization-wide Target Fields are additional fields appended to the Merge Common Model for all Linked Accounts in a category. [Learn more](https://docs.merge.dev/supplemental-data/field-mappings/target-fields/).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.field_mapping.target_fields_retrieve()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage Files
<details><summary><code>client.filestorage.files.<a href="src/merge/resources/filestorage/resources/files/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `File` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from merge import Merge
from merge.resources.filestorage.resources.files import FilesListRequestOrderBy

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.filestorage.files.list(
    created_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    created_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
    drive_id="drive_id",
    folder_id="folder_id",
    include_deleted_data=True,
    include_remote_data=True,
    include_shell_data=True,
    mime_type="mime_type",
    modified_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    modified_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    name="name",
    order_by=FilesListRequestOrderBy.CREATED_AT_DESCENDING,
    page_size=1,
    remote_created_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    remote_created_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    remote_id="remote_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**drive_id:** `typing.Optional[str]` — Specifying a drive id returns only the files in that drive. Specifying null returns only the files outside the top-level drive.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[
    typing.Union[
        FilesListRequestExpandItem, typing.Sequence[FilesListRequestExpandItem]
    ]
]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — Specifying a folder id returns only the files in that folder. Specifying null returns only the files in root directory.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_data:** `typing.Optional[bool]` — Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**mime_type:** `typing.Optional[str]` — If provided, will only return files with these mime_types. Multiple values can be separated by commas.
    
</dd>
</dl>

<dl>
<dd>

**modified_after:** `typing.Optional[dt.datetime]` — If provided, only objects synced by Merge after this date time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**modified_before:** `typing.Optional[dt.datetime]` — If provided, only objects synced by Merge before this date time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — If provided, will only return files with this name. This performs an exact match.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[FilesListRequestOrderBy]` — Overrides the default ordering for this endpoint. Possible values include: created_at, -created_at, modified_at, -modified_at.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page. The maximum limit is 100.
    
</dd>
</dl>

<dl>
<dd>

**remote_created_after:** `typing.Optional[dt.datetime]` — If provided, will only return files created in the third party platform after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**remote_created_before:** `typing.Optional[dt.datetime]` — If provided, will only return files created in the third party platform before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.files.<a href="src/merge/resources/filestorage/resources/files/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `File` object with the given values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge
from merge.resources.filestorage import FileRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.files.create(
    is_debug_mode=True,
    run_async=True,
    model=FileRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `FileRequest` 
    
</dd>
</dl>

<dl>
<dd>

**is_debug_mode:** `typing.Optional[bool]` — Whether to include debug fields (such as log file links) in the response.
    
</dd>
</dl>

<dl>
<dd>

**run_async:** `typing.Optional[bool]` — Whether or not third-party updates should be run asynchronously.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.files.<a href="src/merge/resources/filestorage/resources/files/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `File` object with the given `id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.files.retrieve(
    id="id",
    include_remote_data=True,
    include_shell_data=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[
    typing.Union[
        FilesRetrieveRequestExpandItem,
        typing.Sequence[FilesRetrieveRequestExpandItem],
    ]
]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.files.<a href="src/merge/resources/filestorage/resources/files/client.py">download_request_meta_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata to construct an authenticated file download request for a singular file, allowing you to download file directly from the third-party. For information on our download process please refer to our <a href='https://help.merge.dev/articles/10644317' target='_blank'>direct file download help center article</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.files.download_request_meta_retrieve(
    id="id",
    mime_type="mime_type",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mime_type:** `typing.Optional[str]` — If provided, specifies the export format of the file to be downloaded.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.files.<a href="src/merge/resources/filestorage/resources/files/client.py">download_request_meta_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata to construct authenticated file download requests, allowing you to download files directly from the third-party.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge
from merge.resources.filestorage.resources.files import (
    FilesDownloadRequestMetaListRequestOrderBy,
)

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.filestorage.files.download_request_meta_list(
    created_after="created_after",
    created_before="created_before",
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
    include_deleted_data=True,
    mime_types="mime_types",
    modified_after="modified_after",
    modified_before="modified_before",
    order_by=FilesDownloadRequestMetaListRequestOrderBy.CREATED_AT_DESCENDING,
    page_size=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_after:** `typing.Optional[str]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[str]` — If provided, will only return objects created before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — If provided, will only return objects with the given IDs. Comma-separated list of strings.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_data:** `typing.Optional[bool]` — Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    
</dd>
</dl>

<dl>
<dd>

**mime_types:** `typing.Optional[str]` — A comma-separated list of preferred MIME types in order of priority. If supported by the third-party provider, the file(s) will be returned in the first supported MIME type from the list. The default MIME type is PDF. To see supported MIME types by file type, refer to our <a href='https://help.merge.dev/en/articles/8615316-file-export-and-download-specification' target='_blank'>export format help center article</a>.
    
</dd>
</dl>

<dl>
<dd>

**modified_after:** `typing.Optional[str]` — If provided, will only return objects modified after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**modified_before:** `typing.Optional[str]` — If provided, will only return objects modified before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[FilesDownloadRequestMetaListRequestOrderBy]` — Overrides the default ordering for this endpoint. Possible values include: created_at, -created_at, modified_at, -modified_at.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.files.<a href="src/merge/resources/filestorage/resources/files/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `FileStorageFile` POSTs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.files.meta_post_retrieve()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage Folders
<details><summary><code>client.filestorage.folders.<a href="src/merge/resources/filestorage/resources/folders/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Folder` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.filestorage.folders.list(
    created_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    created_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
    drive_id="drive_id",
    include_deleted_data=True,
    include_remote_data=True,
    include_shell_data=True,
    modified_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    modified_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    name="name",
    page_size=1,
    parent_folder_id="parent_folder_id",
    remote_id="remote_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**drive_id:** `typing.Optional[str]` — If provided, will only return folders in this drive.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[
    typing.Union[
        FoldersListRequestExpandItem,
        typing.Sequence[FoldersListRequestExpandItem],
    ]
]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_data:** `typing.Optional[bool]` — Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**modified_after:** `typing.Optional[dt.datetime]` — If provided, only objects synced by Merge after this date time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**modified_before:** `typing.Optional[dt.datetime]` — If provided, only objects synced by Merge before this date time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — If provided, will only return folders with this name. This performs an exact match.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page. The maximum limit is 100.
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `typing.Optional[str]` — If provided, will only return folders in this parent folder. If null, will return folders in root directory.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.folders.<a href="src/merge/resources/filestorage/resources/folders/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Folder` object with the given values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge
from merge.resources.filestorage import FolderRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.folders.create(
    is_debug_mode=True,
    run_async=True,
    model=FolderRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model:** `FolderRequest` 
    
</dd>
</dl>

<dl>
<dd>

**is_debug_mode:** `typing.Optional[bool]` — Whether to include debug fields (such as log file links) in the response.
    
</dd>
</dl>

<dl>
<dd>

**run_async:** `typing.Optional[bool]` — Whether or not third-party updates should be run asynchronously.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.folders.<a href="src/merge/resources/filestorage/resources/folders/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Folder` object with the given `id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.folders.retrieve(
    id="id",
    include_remote_data=True,
    include_shell_data=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[
    typing.Union[
        FoldersRetrieveRequestExpandItem,
        typing.Sequence[FoldersRetrieveRequestExpandItem],
    ]
]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.folders.<a href="src/merge/resources/filestorage/resources/folders/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `FileStorageFolder` POSTs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.folders.meta_post_retrieve()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage GenerateKey
<details><summary><code>client.filestorage.generate_key.<a href="src/merge/resources/filestorage/resources/generate_key/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a remote key.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.generate_key.create(
    name="Remote Deployment Key 1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the remote key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage Groups
<details><summary><code>client.filestorage.groups.<a href="src/merge/resources/filestorage/resources/groups/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Group` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.filestorage.groups.list(
    created_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    created_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
    include_deleted_data=True,
    include_remote_data=True,
    include_shell_data=True,
    modified_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    modified_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    page_size=1,
    remote_id="remote_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[
    typing.Union[
        GroupsListRequestExpandItem,
        typing.Sequence[GroupsListRequestExpandItem],
    ]
]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_data:** `typing.Optional[bool]` — Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**modified_after:** `typing.Optional[dt.datetime]` — If provided, only objects synced by Merge after this date time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**modified_before:** `typing.Optional[dt.datetime]` — If provided, only objects synced by Merge before this date time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page. The maximum limit is 100.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.groups.<a href="src/merge/resources/filestorage/resources/groups/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Group` object with the given `id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.groups.retrieve(
    id="id",
    include_remote_data=True,
    include_shell_data=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[
    typing.Union[
        GroupsRetrieveRequestExpandItem,
        typing.Sequence[GroupsRetrieveRequestExpandItem],
    ]
]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage Issues
<details><summary><code>client.filestorage.issues.<a href="src/merge/resources/filestorage/resources/issues/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets all issues for Organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from merge import Merge
from merge.resources.filestorage.resources.issues import IssuesListRequestStatus

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.filestorage.issues.list(
    account_token="account_token",
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
    end_date="end_date",
    end_user_organization_name="end_user_organization_name",
    first_incident_time_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    first_incident_time_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    include_muted="include_muted",
    integration_name="integration_name",
    last_incident_time_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    last_incident_time_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    linked_account_id="linked_account_id",
    page_size=1,
    start_date="start_date",
    status=IssuesListRequestStatus.ONGOING,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — If included, will only include issues whose most recent action occurred before this time
    
</dd>
</dl>

<dl>
<dd>

**end_user_organization_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_incident_time_after:** `typing.Optional[dt.datetime]` — If provided, will only return issues whose first incident time was after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**first_incident_time_before:** `typing.Optional[dt.datetime]` — If provided, will only return issues whose first incident time was before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**include_muted:** `typing.Optional[str]` — If true, will include muted issues
    
</dd>
</dl>

<dl>
<dd>

**integration_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**last_incident_time_after:** `typing.Optional[dt.datetime]` — If provided, will only return issues whose last incident time was after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**last_incident_time_before:** `typing.Optional[dt.datetime]` — If provided, will only return issues whose last incident time was before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**linked_account_id:** `typing.Optional[str]` — If provided, will only include issues pertaining to the linked account passed in.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page. The maximum limit is 100.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — If included, will only include issues whose most recent action occurred after this time
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[IssuesListRequestStatus]` 

Status of the issue. Options: ('ONGOING', 'RESOLVED')

* `ONGOING` - ONGOING
* `RESOLVED` - RESOLVED
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.issues.<a href="src/merge/resources/filestorage/resources/issues/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific issue.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.issues.retrieve(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage LinkToken
<details><summary><code>client.filestorage.link_token.<a href="src/merge/resources/filestorage/resources/link_token/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a link token to be used when linking a new end user. The link token expires after single use.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge
from merge.resources.filestorage import CategoriesEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.link_token.create(
    end_user_email_address="example@gmail.com",
    end_user_organization_name="Test Organization",
    end_user_origin_id="12345",
    categories=[CategoriesEnum.HRIS, CategoriesEnum.ATS],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**end_user_email_address:** `str` — Your end user's email address. This is purely for identification purposes - setting this value will not cause any emails to be sent.
    
</dd>
</dl>

<dl>
<dd>

**end_user_organization_name:** `str` — Your end user's organization.
    
</dd>
</dl>

<dl>
<dd>

**end_user_origin_id:** `str` — This unique identifier typically represents the ID for your end user in your product's database. This value must be distinct from other Linked Accounts' unique identifiers.
    
</dd>
</dl>

<dl>
<dd>

**categories:** `typing.Sequence[CategoriesEnum]` — The integration categories to show in Merge Link.
    
</dd>
</dl>

<dl>
<dd>

**integration:** `typing.Optional[str]` — The slug of a specific pre-selected integration for this linking flow token. For examples of slugs, see https://docs.merge.dev/guides/merge-link/single-integration/.
    
</dd>
</dl>

<dl>
<dd>

**link_expiry_mins:** `typing.Optional[int]` — An integer number of minutes between [30, 720 or 10080 if for a Magic Link URL] for how long this token is valid. Defaults to 30.
    
</dd>
</dl>

<dl>
<dd>

**should_create_magic_link_url:** `typing.Optional[bool]` — Whether to generate a Magic Link URL. Defaults to false. For more information on Magic Link, see https://merge.dev/blog/integrations-fast-say-hello-to-magic-link.
    
</dd>
</dl>

<dl>
<dd>

**hide_admin_magic_link:** `typing.Optional[bool]` — Whether to generate a Magic Link URL on the Admin Needed screen during the linking flow. Defaults to false. For more information on Magic Link, see https://merge.dev/blog/integrations-fast-say-hello-to-magic-link.
    
</dd>
</dl>

<dl>
<dd>

**common_models:** `typing.Optional[typing.Sequence[CommonModelScopesBodyRequest]]` — An array of objects to specify the models and fields that will be disabled for a given Linked Account. Each object uses model_id, enabled_actions, and disabled_fields to specify the model, method, and fields that are scoped for a given Linked Account.
    
</dd>
</dl>

<dl>
<dd>

**category_common_model_scopes:** `typing.Optional[
    typing.Dict[
        str,
        typing.Optional[
            typing.Sequence[IndividualCommonModelScopeDeserializerRequest]
        ],
    ]
]` — When creating a Link Token, you can set permissions for Common Models that will apply to the account that is going to be linked. Any model or field not specified in link token payload will default to existing settings.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[EndUserDetailsRequestLanguage]` 

The following subset of IETF language tags can be used to configure localization.

* `en` - en
* `de` - de
    
</dd>
</dl>

<dl>
<dd>

**are_syncs_disabled:** `typing.Optional[bool]` — The boolean that indicates whether initial, periodic, and force syncs will be disabled.
    
</dd>
</dl>

<dl>
<dd>

**integration_specific_config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — A JSON object containing integration-specific configuration options.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage LinkedAccounts
<details><summary><code>client.filestorage.linked_accounts.<a href="src/merge/resources/filestorage/resources/linked_accounts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List linked accounts for your organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge
from merge.resources.filestorage.resources.linked_accounts import (
    LinkedAccountsListRequestCategory,
)

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.filestorage.linked_accounts.list(
    category=LinkedAccountsListRequestCategory.ACCOUNTING,
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
    end_user_email_address="end_user_email_address",
    end_user_organization_name="end_user_organization_name",
    end_user_origin_id="end_user_origin_id",
    end_user_origin_ids="end_user_origin_ids",
    id="id",
    ids="ids",
    include_duplicates=True,
    integration_name="integration_name",
    is_test_account="is_test_account",
    page_size=1,
    status="status",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category:** `typing.Optional[LinkedAccountsListRequestCategory]` 

Options: `accounting`, `ats`, `crm`, `filestorage`, `hris`, `mktg`, `ticketing`

* `hris` - hris
* `ats` - ats
* `accounting` - accounting
* `ticketing` - ticketing
* `crm` - crm
* `mktg` - mktg
* `filestorage` - filestorage
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**end_user_email_address:** `typing.Optional[str]` — If provided, will only return linked accounts associated with the given email address.
    
</dd>
</dl>

<dl>
<dd>

**end_user_organization_name:** `typing.Optional[str]` — If provided, will only return linked accounts associated with the given organization name.
    
</dd>
</dl>

<dl>
<dd>

**end_user_origin_id:** `typing.Optional[str]` — If provided, will only return linked accounts associated with the given origin ID.
    
</dd>
</dl>

<dl>
<dd>

**end_user_origin_ids:** `typing.Optional[str]` — Comma-separated list of EndUser origin IDs, making it possible to specify multiple EndUsers at once.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — Comma-separated list of LinkedAccount IDs, making it possible to specify multiple LinkedAccounts at once.
    
</dd>
</dl>

<dl>
<dd>

**include_duplicates:** `typing.Optional[bool]` — If `true`, will include complete production duplicates of the account specified by the `id` query parameter in the response. `id` must be for a complete production linked account.
    
</dd>
</dl>

<dl>
<dd>

**integration_name:** `typing.Optional[str]` — If provided, will only return linked accounts associated with the given integration name.
    
</dd>
</dl>

<dl>
<dd>

**is_test_account:** `typing.Optional[str]` — If included, will only include test linked accounts. If not included, will only include non-test linked accounts.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page. The maximum limit is 100.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Filter by status. Options: `COMPLETE`, `IDLE`, `INCOMPLETE`, `RELINK_NEEDED`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage Passthrough
<details><summary><code>client.filestorage.passthrough.<a href="src/merge/resources/filestorage/resources/passthrough/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pull data from an endpoint not currently supported by Merge.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge
from merge.resources.filestorage import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.passthrough.create(
    request=DataPassthroughRequest(
        method=MethodEnum.GET,
        path="/scooters",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `DataPassthroughRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage RegenerateKey
<details><summary><code>client.filestorage.regenerate_key.<a href="src/merge/resources/filestorage/resources/regenerate_key/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange remote keys.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.regenerate_key.create(
    name="Remote Deployment Key 1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the remote key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage SyncStatus
<details><summary><code>client.filestorage.sync_status.<a href="src/merge/resources/filestorage/resources/sync_status/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get sync status for the current sync and the most recently finished sync. `last_sync_start` represents the most recent time any sync began. `last_sync_finished` represents the most recent time any sync completed. These timestamps may correspond to different sync instances which may result in a sync start time being later than a separate sync completed time. To ensure you are retrieving the latest available data reference the `last_sync_finished` timestamp where `last_sync_result` is `DONE`. Possible values for `status` and `last_sync_result` are `DISABLED`, `DONE`, `FAILED`, `PARTIALLY_SYNCED`, `PAUSED`, `SYNCING`. Learn more about sync status in our [Help Center](https://help.merge.dev/en/articles/8184193-merge-sync-statuses).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.filestorage.sync_status.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
    page_size=1,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page. The maximum limit is 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage ForceResync
<details><summary><code>client.filestorage.force_resync.<a href="src/merge/resources/filestorage/resources/force_resync/client.py">sync_status_resync_create</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Force re-sync of all models. This endpoint is available for monthly, quarterly, and highest sync frequency customers on the Professional or Enterprise plans. Doing so will consume a sync credit for the relevant linked account. Force re-syncs can also be triggered manually in the Merge Dashboard and is available for all customers.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.force_resync.sync_status_resync_create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage Users
<details><summary><code>client.filestorage.users.<a href="src/merge/resources/filestorage/resources/users/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `User` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
response = client.filestorage.users.list(
    created_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    created_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
    email_address="email_address",
    include_deleted_data=True,
    include_remote_data=True,
    include_shell_data=True,
    is_me="is_me",
    modified_after=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    modified_before=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
    page_size=1,
    remote_id="remote_id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**created_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**email_address:** `typing.Optional[str]` — If provided, will only return users with emails equal to this value (case insensitive).
    
</dd>
</dl>

<dl>
<dd>

**include_deleted_data:** `typing.Optional[bool]` — Indicates whether or not this object has been deleted in the third party platform. Full coverage deletion detection is a premium add-on. Native deletion detection is offered for free with limited coverage. [Learn more](https://docs.merge.dev/integrations/hris/supported-features/).
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_me:** `typing.Optional[str]` — If provided, will only return the user object for requestor.
    
</dd>
</dl>

<dl>
<dd>

**modified_after:** `typing.Optional[dt.datetime]` — If provided, only objects synced by Merge after this date time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**modified_before:** `typing.Optional[dt.datetime]` — If provided, only objects synced by Merge before this date time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page. The maximum limit is 100.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.users.<a href="src/merge/resources/filestorage/resources/users/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `User` object with the given `id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.users.retrieve(
    id="id",
    include_remote_data=True,
    include_shell_data=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Filestorage WebhookReceivers
<details><summary><code>client.filestorage.webhook_receivers.<a href="src/merge/resources/filestorage/resources/webhook_receivers/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `WebhookReceiver` objects.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.webhook_receivers.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.filestorage.webhook_receivers.<a href="src/merge/resources/filestorage/resources/webhook_receivers/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `WebhookReceiver` object with the given values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.webhook_receivers.create(
    event="event",
    is_active=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

