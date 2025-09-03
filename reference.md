# Reference
## Ats AccountDetails
<details><summary><code>client.ats.account_details.<a href="src/merge/resources/ats/resources/account_details/client.py">retrieve</a>()</code></summary>
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
client.ats.account_details.retrieve()

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

## Ats AccountToken
<details><summary><code>client.ats.account_token.<a href="src/merge/resources/ats/resources/account_token/client.py">retrieve</a>(...)</code></summary>
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
client.ats.account_token.retrieve(
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

## Ats Activities
<details><summary><code>client.ats.activities.<a href="src/merge/resources/ats/resources/activities/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Activity` objects.
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
client.ats.activities.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[typing.Literal["user"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[ActivitiesListRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[ActivitiesListRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` — If provided, will only return activities done by this user.
    
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

<details><summary><code>client.ats.activities.<a href="src/merge/resources/ats/resources/activities/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Activity` object with the given values.
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
from merge.resources.ats import ActivityRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.activities.create(
    model=ActivityRequest(),
    remote_user_id="remote_user_id",
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

**model:** `ActivityRequest` 
    
</dd>
</dl>

<dl>
<dd>

**remote_user_id:** `str` 
    
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

<details><summary><code>client.ats.activities.<a href="src/merge/resources/ats/resources/activities/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Activity` object with the given `id`.
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
client.ats.activities.retrieve(
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

**expand:** `typing.Optional[typing.Literal["user"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[ActivitiesRetrieveRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[ActivitiesRetrieveRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ats.activities.<a href="src/merge/resources/ats/resources/activities/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Activity` POSTs.
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
client.ats.activities.meta_post_retrieve()

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

## Ats Applications
<details><summary><code>client.ats.applications.<a href="src/merge/resources/ats/resources/applications/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Application` objects.
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
client.ats.applications.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**candidate_id:** `typing.Optional[str]` — If provided, will only return applications for this candidate.
    
</dd>
</dl>

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

**credited_to_id:** `typing.Optional[str]` — If provided, will only return applications credited to this user.
    
</dd>
</dl>

<dl>
<dd>

**current_stage_id:** `typing.Optional[str]` — If provided, will only return applications at this interview stage.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[ApplicationsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**job_id:** `typing.Optional[str]` — If provided, will only return applications for this job.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**reject_reason_id:** `typing.Optional[str]` — If provided, will only return applications with this reject reason.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` — If provided, will only return applications with this source.
    
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

<details><summary><code>client.ats.applications.<a href="src/merge/resources/ats/resources/applications/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Application` object with the given values.
For certain integrations, but not all, our API detects duplicate candidates and will associate applications with existing records in the third-party. New candidates are created and automatically linked to the application.

See our [Help Center article](https://help.merge.dev/en/articles/10012366-updates-to-post-applications-oct-2024) for detailed support per integration.
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
from merge.resources.ats import ApplicationRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.applications.create(
    model=ApplicationRequest(),
    remote_user_id="remote_user_id",
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

**model:** `ApplicationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**remote_user_id:** `str` 
    
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

<details><summary><code>client.ats.applications.<a href="src/merge/resources/ats/resources/applications/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Application` object with the given `id`.
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
client.ats.applications.retrieve(
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

**expand:** `typing.Optional[ApplicationsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.ats.applications.<a href="src/merge/resources/ats/resources/applications/client.py">change_stage_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the `current_stage` field of an `Application` object
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
client.ats.applications.change_stage_create(
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

**job_interview_stage:** `typing.Optional[str]` — The interview stage to move the application to.
    
</dd>
</dl>

<dl>
<dd>

**remote_user_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats.applications.<a href="src/merge/resources/ats/resources/applications/client.py">meta_post_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Application` POSTs.
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
client.ats.applications.meta_post_retrieve()

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

**application_remote_template_id:** `typing.Optional[str]` — The template ID associated with the nested application in the request.
    
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

## Ats AsyncPassthrough
<details><summary><code>client.ats.async_passthrough.<a href="src/merge/resources/ats/resources/async_passthrough/client.py">create</a>(...)</code></summary>
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
from merge.resources.ats import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.async_passthrough.create(
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

<details><summary><code>client.ats.async_passthrough.<a href="src/merge/resources/ats/resources/async_passthrough/client.py">retrieve</a>(...)</code></summary>
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
client.ats.async_passthrough.retrieve(
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

## Ats Attachments
<details><summary><code>client.ats.attachments.<a href="src/merge/resources/ats/resources/attachments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Attachment` objects.
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
client.ats.attachments.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**candidate_id:** `typing.Optional[str]` — If provided, will only return attachments for this candidate.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["candidate"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["attachment_type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["attachment_type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ats.attachments.<a href="src/merge/resources/ats/resources/attachments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Attachment` object with the given values.
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
from merge.resources.ats import AttachmentRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.attachments.create(
    model=AttachmentRequest(),
    remote_user_id="remote_user_id",
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

**model:** `AttachmentRequest` 
    
</dd>
</dl>

<dl>
<dd>

**remote_user_id:** `str` 
    
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

<details><summary><code>client.ats.attachments.<a href="src/merge/resources/ats/resources/attachments/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Attachment` object with the given `id`.
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
client.ats.attachments.retrieve(
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

**expand:** `typing.Optional[typing.Literal["candidate"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[typing.Literal["attachment_type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["attachment_type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ats.attachments.<a href="src/merge/resources/ats/resources/attachments/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Attachment` POSTs.
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
client.ats.attachments.meta_post_retrieve()

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

## Ats AuditTrail
<details><summary><code>client.ats.audit_trail.<a href="src/merge/resources/ats/resources/audit_trail/client.py">list</a>(...)</code></summary>
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
client.ats.audit_trail.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

## Ats AvailableActions
<details><summary><code>client.ats.available_actions.<a href="src/merge/resources/ats/resources/available_actions/client.py">retrieve</a>()</code></summary>
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
client.ats.available_actions.retrieve()

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

## Ats Candidates
<details><summary><code>client.ats.candidates.<a href="src/merge/resources/ats/resources/candidates/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Candidate` objects.
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
client.ats.candidates.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**email_addresses:** `typing.Optional[str]` — If provided, will only return candidates with these email addresses; multiple addresses can be separated by commas.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[CandidatesListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — If provided, will only return candidates with this first name.
    
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

**last_name:** `typing.Optional[str]` — If provided, will only return candidates with this last name.
    
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

**tags:** `typing.Optional[str]` — If provided, will only return candidates with these tags; multiple tags can be separated by commas.
    
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

<details><summary><code>client.ats.candidates.<a href="src/merge/resources/ats/resources/candidates/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Candidate` object with the given values.
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
from merge.resources.ats import CandidateRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.candidates.create(
    model=CandidateRequest(),
    remote_user_id="remote_user_id",
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

**model:** `CandidateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**remote_user_id:** `str` 
    
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

<details><summary><code>client.ats.candidates.<a href="src/merge/resources/ats/resources/candidates/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Candidate` object with the given `id`.
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
client.ats.candidates.retrieve(
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

**expand:** `typing.Optional[CandidatesRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.ats.candidates.<a href="src/merge/resources/ats/resources/candidates/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a `Candidate` object with the given `id`.
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
from merge.resources.ats import PatchedCandidateRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.candidates.partial_update(
    id="id",
    model=PatchedCandidateRequest(),
    remote_user_id="remote_user_id",
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

**model:** `PatchedCandidateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**remote_user_id:** `str` 
    
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

<details><summary><code>client.ats.candidates.<a href="src/merge/resources/ats/resources/candidates/client.py">ignore_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.
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
from merge.resources.ats import ReasonEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.candidates.ignore_create(
    model_id="model_id",
    reason=ReasonEnum.GENERAL_CUSTOMER_REQUEST,
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

**model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `IgnoreCommonModelRequestReason` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` 
    
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

<details><summary><code>client.ats.candidates.<a href="src/merge/resources/ats/resources/candidates/client.py">meta_patch_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Candidate` PATCHs.
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
client.ats.candidates.meta_patch_retrieve(
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

<details><summary><code>client.ats.candidates.<a href="src/merge/resources/ats/resources/candidates/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Candidate` POSTs.
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
client.ats.candidates.meta_post_retrieve()

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

## Ats Scopes
<details><summary><code>client.ats.scopes.<a href="src/merge/resources/ats/resources/scopes/client.py">default_scopes_retrieve</a>()</code></summary>
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
client.ats.scopes.default_scopes_retrieve()

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

<details><summary><code>client.ats.scopes.<a href="src/merge/resources/ats/resources/scopes/client.py">linked_account_scopes_retrieve</a>()</code></summary>
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
client.ats.scopes.linked_account_scopes_retrieve()

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

<details><summary><code>client.ats.scopes.<a href="src/merge/resources/ats/resources/scopes/client.py">linked_account_scopes_create</a>(...)</code></summary>
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
from merge.resources.ats import (
    FieldPermissionDeserializerRequest,
    IndividualCommonModelScopeDeserializerRequest,
    ModelPermissionDeserializerRequest,
)

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.scopes.linked_account_scopes_create(
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

## Ats DeleteAccount
<details><summary><code>client.ats.delete_account.<a href="src/merge/resources/ats/resources/delete_account/client.py">delete</a>()</code></summary>
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
client.ats.delete_account.delete()

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

## Ats Departments
<details><summary><code>client.ats.departments.<a href="src/merge/resources/ats/resources/departments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Department` objects.
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
client.ats.departments.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.ats.departments.<a href="src/merge/resources/ats/resources/departments/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Department` object with the given `id`.
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
client.ats.departments.retrieve(
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

## Ats Eeocs
<details><summary><code>client.ats.eeocs.<a href="src/merge/resources/ats/resources/eeocs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `EEOC` objects.
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
client.ats.eeocs.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**candidate_id:** `typing.Optional[str]` — If provided, will only return EEOC info for this candidate.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["candidate"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[EeocsListRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[EeocsListRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ats.eeocs.<a href="src/merge/resources/ats/resources/eeocs/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `EEOC` object with the given `id`.
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
client.ats.eeocs.retrieve(
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

**expand:** `typing.Optional[typing.Literal["candidate"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[EeocsRetrieveRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[EeocsRetrieveRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Ats FieldMapping
<details><summary><code>client.ats.field_mapping.<a href="src/merge/resources/ats/resources/field_mapping/client.py">field_mappings_retrieve</a>(...)</code></summary>
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
client.ats.field_mapping.field_mappings_retrieve()

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

<details><summary><code>client.ats.field_mapping.<a href="src/merge/resources/ats/resources/field_mapping/client.py">field_mappings_create</a>(...)</code></summary>
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
client.ats.field_mapping.field_mappings_create(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ats.field_mapping.<a href="src/merge/resources/ats/resources/field_mapping/client.py">field_mappings_destroy</a>(...)</code></summary>
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
client.ats.field_mapping.field_mappings_destroy(
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

<details><summary><code>client.ats.field_mapping.<a href="src/merge/resources/ats/resources/field_mapping/client.py">field_mappings_partial_update</a>(...)</code></summary>
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
client.ats.field_mapping.field_mappings_partial_update(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ats.field_mapping.<a href="src/merge/resources/ats/resources/field_mapping/client.py">remote_fields_retrieve</a>(...)</code></summary>
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
client.ats.field_mapping.remote_fields_retrieve()

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

<details><summary><code>client.ats.field_mapping.<a href="src/merge/resources/ats/resources/field_mapping/client.py">target_fields_retrieve</a>()</code></summary>
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
client.ats.field_mapping.target_fields_retrieve()

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

## Ats GenerateKey
<details><summary><code>client.ats.generate_key.<a href="src/merge/resources/ats/resources/generate_key/client.py">create</a>(...)</code></summary>
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
client.ats.generate_key.create(
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

## Ats Interviews
<details><summary><code>client.ats.interviews.<a href="src/merge/resources/ats/resources/interviews/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `ScheduledInterview` objects.
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
client.ats.interviews.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**application_id:** `typing.Optional[str]` — If provided, will only return interviews for this application.
    
</dd>
</dl>

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

**expand:** `typing.Optional[InterviewsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**job_id:** `typing.Optional[str]` — If provided, wll only return interviews organized for this job.
    
</dd>
</dl>

<dl>
<dd>

**job_interview_stage_id:** `typing.Optional[str]` — If provided, will only return interviews at this stage.
    
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

**organizer_id:** `typing.Optional[str]` — If provided, will only return interviews organized by this user.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ats.interviews.<a href="src/merge/resources/ats/resources/interviews/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `ScheduledInterview` object with the given values.
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
from merge.resources.ats import ScheduledInterviewRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.interviews.create(
    model=ScheduledInterviewRequest(),
    remote_user_id="remote_user_id",
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

**model:** `ScheduledInterviewRequest` 
    
</dd>
</dl>

<dl>
<dd>

**remote_user_id:** `str` 
    
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

<details><summary><code>client.ats.interviews.<a href="src/merge/resources/ats/resources/interviews/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `ScheduledInterview` object with the given `id`.
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
client.ats.interviews.retrieve(
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

**expand:** `typing.Optional[InterviewsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ats.interviews.<a href="src/merge/resources/ats/resources/interviews/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `ScheduledInterview` POSTs.
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
client.ats.interviews.meta_post_retrieve()

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

## Ats Issues
<details><summary><code>client.ats.issues.<a href="src/merge/resources/ats/resources/issues/client.py">list</a>(...)</code></summary>
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.issues.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

<details><summary><code>client.ats.issues.<a href="src/merge/resources/ats/resources/issues/client.py">retrieve</a>(...)</code></summary>
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
client.ats.issues.retrieve(
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

## Ats JobInterviewStages
<details><summary><code>client.ats.job_interview_stages.<a href="src/merge/resources/ats/resources/job_interview_stages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `JobInterviewStage` objects.
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
client.ats.job_interview_stages.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[typing.Literal["job"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**job_id:** `typing.Optional[str]` — If provided, will only return interview stages for this job.
    
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

<details><summary><code>client.ats.job_interview_stages.<a href="src/merge/resources/ats/resources/job_interview_stages/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `JobInterviewStage` object with the given `id`.
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
client.ats.job_interview_stages.retrieve(
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

**expand:** `typing.Optional[typing.Literal["job"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Ats JobPostings
<details><summary><code>client.ats.job_postings.<a href="src/merge/resources/ats/resources/job_postings/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `JobPosting` objects.
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
client.ats.job_postings.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[typing.Literal["job"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**status:** `typing.Optional[JobPostingsListRequestStatus]` 

If provided, will only return Job Postings with this status. Options: ('PUBLISHED', 'CLOSED', 'DRAFT', 'INTERNAL', 'PENDING')

* `PUBLISHED` - PUBLISHED
* `CLOSED` - CLOSED
* `DRAFT` - DRAFT
* `INTERNAL` - INTERNAL
* `PENDING` - PENDING
    
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

<details><summary><code>client.ats.job_postings.<a href="src/merge/resources/ats/resources/job_postings/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `JobPosting` object with the given `id`.
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
client.ats.job_postings.retrieve(
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

**expand:** `typing.Optional[typing.Literal["job"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Ats Jobs
<details><summary><code>client.ats.jobs.<a href="src/merge/resources/ats/resources/jobs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Job` objects.
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
client.ats.jobs.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**code:** `typing.Optional[str]` — If provided, will only return jobs with this code.
    
</dd>
</dl>

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

**expand:** `typing.Optional[JobsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**offices:** `typing.Optional[str]` — If provided, will only return jobs for this office; multiple offices can be separated by commas.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[JobsListRequestStatus]` 

If provided, will only return jobs with this status. Options: ('OPEN', 'CLOSED', 'DRAFT', 'ARCHIVED', 'PENDING')

* `OPEN` - OPEN
* `CLOSED` - CLOSED
* `DRAFT` - DRAFT
* `ARCHIVED` - ARCHIVED
* `PENDING` - PENDING
    
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

<details><summary><code>client.ats.jobs.<a href="src/merge/resources/ats/resources/jobs/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Job` object with the given `id`.
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
client.ats.jobs.retrieve(
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

**expand:** `typing.Optional[JobsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ats.jobs.<a href="src/merge/resources/ats/resources/jobs/client.py">screening_questions_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `ScreeningQuestion` objects.
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
client.ats.jobs.screening_questions_list(
    job_id="job_id",
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**job_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[JobsScreeningQuestionsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Ats LinkToken
<details><summary><code>client.ats.link_token.<a href="src/merge/resources/ats/resources/link_token/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a link token to be used when linking a new end user.
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
from merge.resources.ats import CategoriesEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.link_token.create(
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

## Ats LinkedAccounts
<details><summary><code>client.ats.linked_accounts.<a href="src/merge/resources/ats/resources/linked_accounts/client.py">list</a>(...)</code></summary>
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

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.linked_accounts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

## Ats Offers
<details><summary><code>client.ats.offers.<a href="src/merge/resources/ats/resources/offers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Offer` objects.
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
client.ats.offers.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**application_id:** `typing.Optional[str]` — If provided, will only return offers for this application.
    
</dd>
</dl>

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

**creator_id:** `typing.Optional[str]` — If provided, will only return offers created by this user.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[OffersListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ats.offers.<a href="src/merge/resources/ats/resources/offers/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Offer` object with the given `id`.
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
client.ats.offers.retrieve(
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

**expand:** `typing.Optional[OffersRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Ats Offices
<details><summary><code>client.ats.offices.<a href="src/merge/resources/ats/resources/offices/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Office` objects.
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
client.ats.offices.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.ats.offices.<a href="src/merge/resources/ats/resources/offices/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Office` object with the given `id`.
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
client.ats.offices.retrieve(
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

## Ats Passthrough
<details><summary><code>client.ats.passthrough.<a href="src/merge/resources/ats/resources/passthrough/client.py">create</a>(...)</code></summary>
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
from merge.resources.ats import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ats.passthrough.create(
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

## Ats RegenerateKey
<details><summary><code>client.ats.regenerate_key.<a href="src/merge/resources/ats/resources/regenerate_key/client.py">create</a>(...)</code></summary>
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
client.ats.regenerate_key.create(
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

## Ats RejectReasons
<details><summary><code>client.ats.reject_reasons.<a href="src/merge/resources/ats/resources/reject_reasons/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RejectReason` objects.
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
client.ats.reject_reasons.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.ats.reject_reasons.<a href="src/merge/resources/ats/resources/reject_reasons/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `RejectReason` object with the given `id`.
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
client.ats.reject_reasons.retrieve(
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

## Ats Scorecards
<details><summary><code>client.ats.scorecards.<a href="src/merge/resources/ats/resources/scorecards/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Scorecard` objects.
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
client.ats.scorecards.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**application_id:** `typing.Optional[str]` — If provided, will only return scorecards for this application.
    
</dd>
</dl>

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

**expand:** `typing.Optional[ScorecardsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**interview_id:** `typing.Optional[str]` — If provided, will only return scorecards for this interview.
    
</dd>
</dl>

<dl>
<dd>

**interviewer_id:** `typing.Optional[str]` — If provided, will only return scorecards for this interviewer.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["overall_recommendation"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["overall_recommendation"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ats.scorecards.<a href="src/merge/resources/ats/resources/scorecards/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Scorecard` object with the given `id`.
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
client.ats.scorecards.retrieve(
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

**expand:** `typing.Optional[ScorecardsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[typing.Literal["overall_recommendation"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["overall_recommendation"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Ats SyncStatus
<details><summary><code>client.ats.sync_status.<a href="src/merge/resources/ats/resources/sync_status/client.py">list</a>(...)</code></summary>
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
client.ats.sync_status.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
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

## Ats ForceResync
<details><summary><code>client.ats.force_resync.<a href="src/merge/resources/ats/resources/force_resync/client.py">sync_status_resync_create</a>()</code></summary>
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
client.ats.force_resync.sync_status_resync_create()

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

## Ats Tags
<details><summary><code>client.ats.tags.<a href="src/merge/resources/ats/resources/tags/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Tag` objects.
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
client.ats.tags.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

## Ats Users
<details><summary><code>client.ats.users.<a href="src/merge/resources/ats/resources/users/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteUser` objects.
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
client.ats.users.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**email:** `typing.Optional[str]` — If provided, will only return remote users with the given email address
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["access_role"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["access_role"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ats.users.<a href="src/merge/resources/ats/resources/users/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `RemoteUser` object with the given `id`.
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
client.ats.users.retrieve(
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

**remote_fields:** `typing.Optional[typing.Literal["access_role"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["access_role"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Ats WebhookReceivers
<details><summary><code>client.ats.webhook_receivers.<a href="src/merge/resources/ats/resources/webhook_receivers/client.py">list</a>()</code></summary>
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
client.ats.webhook_receivers.list()

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

<details><summary><code>client.ats.webhook_receivers.<a href="src/merge/resources/ats/resources/webhook_receivers/client.py">create</a>(...)</code></summary>
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
client.ats.webhook_receivers.create(
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

## Crm AccountDetails
<details><summary><code>client.crm.account_details.<a href="src/merge/resources/crm/resources/account_details/client.py">retrieve</a>()</code></summary>
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
client.crm.account_details.retrieve()

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

## Crm AccountToken
<details><summary><code>client.crm.account_token.<a href="src/merge/resources/crm/resources/account_token/client.py">retrieve</a>(...)</code></summary>
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
client.crm.account_token.retrieve(
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

## Crm Accounts
<details><summary><code>client.crm.accounts.<a href="src/merge/resources/crm/resources/accounts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Account` objects.
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
client.crm.accounts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[typing.Literal["owner"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

**name:** `typing.Optional[str]` — If provided, will only return accounts with this name.
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` — If provided, will only return accounts with this owner.
    
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

<details><summary><code>client.crm.accounts.<a href="src/merge/resources/crm/resources/accounts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Account` object with the given values.
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
from merge.resources.crm import AccountRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.accounts.create(
    model=AccountRequest(),
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

**model:** `AccountRequest` 
    
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

<details><summary><code>client.crm.accounts.<a href="src/merge/resources/crm/resources/accounts/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Account` object with the given `id`.
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
client.crm.accounts.retrieve(
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

**expand:** `typing.Optional[typing.Literal["owner"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.accounts.<a href="src/merge/resources/crm/resources/accounts/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an `Account` object with the given `id`.
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
from merge.resources.crm import PatchedAccountRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.accounts.partial_update(
    id="id",
    model=PatchedAccountRequest(),
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

**model:** `PatchedAccountRequest` 
    
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

<details><summary><code>client.crm.accounts.<a href="src/merge/resources/crm/resources/accounts/client.py">meta_patch_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `CRMAccount` PATCHs.
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
client.crm.accounts.meta_patch_retrieve(
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

<details><summary><code>client.crm.accounts.<a href="src/merge/resources/crm/resources/accounts/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `CRMAccount` POSTs.
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
client.crm.accounts.meta_post_retrieve()

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

<details><summary><code>client.crm.accounts.<a href="src/merge/resources/crm/resources/accounts/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.accounts.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm AsyncPassthrough
<details><summary><code>client.crm.async_passthrough.<a href="src/merge/resources/crm/resources/async_passthrough/client.py">create</a>(...)</code></summary>
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
from merge.resources.crm import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.async_passthrough.create(
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

<details><summary><code>client.crm.async_passthrough.<a href="src/merge/resources/crm/resources/async_passthrough/client.py">retrieve</a>(...)</code></summary>
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
client.crm.async_passthrough.retrieve(
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

## Crm AuditTrail
<details><summary><code>client.crm.audit_trail.<a href="src/merge/resources/crm/resources/audit_trail/client.py">list</a>(...)</code></summary>
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
client.crm.audit_trail.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

## Crm AvailableActions
<details><summary><code>client.crm.available_actions.<a href="src/merge/resources/crm/resources/available_actions/client.py">retrieve</a>()</code></summary>
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
client.crm.available_actions.retrieve()

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

## Crm Contacts
<details><summary><code>client.crm.contacts.<a href="src/merge/resources/crm/resources/contacts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Contact` objects.
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
client.crm.contacts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**account_id:** `typing.Optional[str]` — If provided, will only return contacts with this account.
    
</dd>
</dl>

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

**email_addresses:** `typing.Optional[str]` — If provided, will only return contacts matching the email addresses; multiple email_addresses can be separated by commas.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[ContactsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[str]` — If provided, will only return contacts matching the phone numbers; multiple phone numbers can be separated by commas.
    
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

<details><summary><code>client.crm.contacts.<a href="src/merge/resources/crm/resources/contacts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Contact` object with the given values.
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
from merge.resources.crm import ContactRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.contacts.create(
    model=ContactRequest(),
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

**model:** `ContactRequest` 
    
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

<details><summary><code>client.crm.contacts.<a href="src/merge/resources/crm/resources/contacts/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Contact` object with the given `id`.
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
client.crm.contacts.retrieve(
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

**expand:** `typing.Optional[ContactsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.contacts.<a href="src/merge/resources/crm/resources/contacts/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a `Contact` object with the given `id`.
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
from merge.resources.crm import PatchedContactRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.contacts.partial_update(
    id="id",
    model=PatchedContactRequest(),
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

**model:** `PatchedContactRequest` 
    
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

<details><summary><code>client.crm.contacts.<a href="src/merge/resources/crm/resources/contacts/client.py">ignore_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.
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
from merge.resources.crm import IgnoreCommonModelRequest, ReasonEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.contacts.ignore_create(
    model_id="model_id",
    request=IgnoreCommonModelRequest(
        reason=ReasonEnum.GENERAL_CUSTOMER_REQUEST,
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

**model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `IgnoreCommonModelRequest` 
    
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

<details><summary><code>client.crm.contacts.<a href="src/merge/resources/crm/resources/contacts/client.py">meta_patch_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `CRMContact` PATCHs.
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
client.crm.contacts.meta_patch_retrieve(
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

<details><summary><code>client.crm.contacts.<a href="src/merge/resources/crm/resources/contacts/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `CRMContact` POSTs.
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
client.crm.contacts.meta_post_retrieve()

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

<details><summary><code>client.crm.contacts.<a href="src/merge/resources/crm/resources/contacts/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.contacts.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm CustomObjectClasses
<details><summary><code>client.crm.custom_object_classes.<a href="src/merge/resources/crm/resources/custom_object_classes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `CustomObjectClass` objects.
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
client.crm.custom_object_classes.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[typing.Literal["fields"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.crm.custom_object_classes.<a href="src/merge/resources/crm/resources/custom_object_classes/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `CustomObjectClass` object with the given `id`.
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
client.crm.custom_object_classes.retrieve(
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

**expand:** `typing.Optional[typing.Literal["fields"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Crm AssociationTypes
<details><summary><code>client.crm.association_types.<a href="src/merge/resources/crm/resources/association_types/client.py">custom_object_classes_association_types_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `AssociationType` objects.
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
client.crm.association_types.custom_object_classes_association_types_list(
    custom_object_class_id="custom_object_class_id",
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**custom_object_class_id:** `str` 
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["target_object_classes"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.crm.association_types.<a href="src/merge/resources/crm/resources/association_types/client.py">custom_object_classes_association_types_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `AssociationType` object with the given values.
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
from merge.resources.crm import (
    AssociationTypeRequestRequest,
    ObjectClassDescriptionRequest,
    OriginTypeEnum,
)

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.association_types.custom_object_classes_association_types_create(
    custom_object_class_id="custom_object_class_id",
    model=AssociationTypeRequestRequest(
        source_object_class=ObjectClassDescriptionRequest(
            id="id",
            origin_type=OriginTypeEnum.CUSTOM_OBJECT,
        ),
        target_object_classes=[
            ObjectClassDescriptionRequest(
                id="id",
                origin_type=OriginTypeEnum.CUSTOM_OBJECT,
            )
        ],
        remote_key_name="remote_key_name",
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

**custom_object_class_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `AssociationTypeRequestRequest` 
    
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

<details><summary><code>client.crm.association_types.<a href="src/merge/resources/crm/resources/association_types/client.py">custom_object_classes_association_types_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `AssociationType` object with the given `id`.
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
client.crm.association_types.custom_object_classes_association_types_retrieve(
    custom_object_class_id="custom_object_class_id",
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

**custom_object_class_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Literal["target_object_classes"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.crm.association_types.<a href="src/merge/resources/crm/resources/association_types/client.py">custom_object_classes_association_types_meta_post_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `CRMAssociationType` POSTs.
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
client.crm.association_types.custom_object_classes_association_types_meta_post_retrieve(
    custom_object_class_id="custom_object_class_id",
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

**custom_object_class_id:** `str` 
    
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

## Crm CustomObjects
<details><summary><code>client.crm.custom_objects.<a href="src/merge/resources/crm/resources/custom_objects/client.py">custom_object_classes_custom_objects_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `CustomObject` objects.
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
client.crm.custom_objects.custom_object_classes_custom_objects_list(
    custom_object_class_id="custom_object_class_id",
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**custom_object_class_id:** `str` 
    
</dd>
</dl>

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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.custom_objects.<a href="src/merge/resources/crm/resources/custom_objects/client.py">custom_object_classes_custom_objects_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `CustomObject` object with the given values.
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
from merge.resources.crm import CustomObjectRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.custom_objects.custom_object_classes_custom_objects_create(
    custom_object_class_id="custom_object_class_id",
    model=CustomObjectRequest(
        fields={"test_field": "hello"},
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

**custom_object_class_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `CustomObjectRequest` 
    
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

<details><summary><code>client.crm.custom_objects.<a href="src/merge/resources/crm/resources/custom_objects/client.py">custom_object_classes_custom_objects_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `CustomObject` object with the given `id`.
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
client.crm.custom_objects.custom_object_classes_custom_objects_retrieve(
    custom_object_class_id="custom_object_class_id",
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

**custom_object_class_id:** `str` 
    
</dd>
</dl>

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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.custom_objects.<a href="src/merge/resources/crm/resources/custom_objects/client.py">custom_object_classes_custom_objects_meta_post_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `CRMCustomObject` POSTs.
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
client.crm.custom_objects.custom_object_classes_custom_objects_meta_post_retrieve(
    custom_object_class_id="custom_object_class_id",
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

**custom_object_class_id:** `str` 
    
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

<details><summary><code>client.crm.custom_objects.<a href="src/merge/resources/crm/resources/custom_objects/client.py">custom_object_classes_custom_objects_remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.custom_objects.custom_object_classes_custom_objects_remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm Associations
<details><summary><code>client.crm.associations.<a href="src/merge/resources/crm/resources/associations/client.py">custom_object_classes_custom_objects_associations_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Association` objects.
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
client.crm.associations.custom_object_classes_custom_objects_associations_list(
    custom_object_class_id="custom_object_class_id",
    object_id="object_id",
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**custom_object_class_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**association_type_id:** `typing.Optional[str]` — If provided, will only return opportunities with this association_type.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["association_type"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.crm.associations.<a href="src/merge/resources/crm/resources/associations/client.py">custom_object_classes_custom_objects_associations_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an Association between `source_object_id` and `target_object_id` of type `association_type_id`.
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
client.crm.associations.custom_object_classes_custom_objects_associations_update(
    association_type_id="association_type_id",
    source_class_id="source_class_id",
    source_object_id="source_object_id",
    target_class_id="target_class_id",
    target_object_id="target_object_id",
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

**association_type_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_class_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_object_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**target_class_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**target_object_id:** `str` 
    
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

## Crm Scopes
<details><summary><code>client.crm.scopes.<a href="src/merge/resources/crm/resources/scopes/client.py">default_scopes_retrieve</a>()</code></summary>
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
client.crm.scopes.default_scopes_retrieve()

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

<details><summary><code>client.crm.scopes.<a href="src/merge/resources/crm/resources/scopes/client.py">linked_account_scopes_retrieve</a>()</code></summary>
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
client.crm.scopes.linked_account_scopes_retrieve()

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

<details><summary><code>client.crm.scopes.<a href="src/merge/resources/crm/resources/scopes/client.py">linked_account_scopes_create</a>(...)</code></summary>
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
from merge.resources.crm import (
    FieldPermissionDeserializerRequest,
    IndividualCommonModelScopeDeserializerRequest,
    ModelPermissionDeserializerRequest,
)

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.scopes.linked_account_scopes_create(
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

## Crm DeleteAccount
<details><summary><code>client.crm.delete_account.<a href="src/merge/resources/crm/resources/delete_account/client.py">delete</a>()</code></summary>
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
client.crm.delete_account.delete()

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

## Crm EngagementTypes
<details><summary><code>client.crm.engagement_types.<a href="src/merge/resources/crm/resources/engagement_types/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `EngagementType` objects.
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
client.crm.engagement_types.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.engagement_types.<a href="src/merge/resources/crm/resources/engagement_types/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `EngagementType` object with the given `id`.
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
client.crm.engagement_types.retrieve(
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

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.engagement_types.<a href="src/merge/resources/crm/resources/engagement_types/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.engagement_types.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm Engagements
<details><summary><code>client.crm.engagements.<a href="src/merge/resources/crm/resources/engagements/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Engagement` objects.
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
client.crm.engagements.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[EngagementsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

**started_after:** `typing.Optional[dt.datetime]` — If provided, will only return engagements started after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[dt.datetime]` — If provided, will only return engagements started before this datetime.
    
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

<details><summary><code>client.crm.engagements.<a href="src/merge/resources/crm/resources/engagements/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Engagement` object with the given values.
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
from merge.resources.crm import EngagementRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.engagements.create(
    model=EngagementRequest(),
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

**model:** `EngagementRequest` 
    
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

<details><summary><code>client.crm.engagements.<a href="src/merge/resources/crm/resources/engagements/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Engagement` object with the given `id`.
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
client.crm.engagements.retrieve(
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

**expand:** `typing.Optional[EngagementsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.engagements.<a href="src/merge/resources/crm/resources/engagements/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an `Engagement` object with the given `id`.
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
from merge.resources.crm import PatchedEngagementRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.engagements.partial_update(
    id="id",
    model=PatchedEngagementRequest(),
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

**model:** `PatchedEngagementRequest` 
    
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

<details><summary><code>client.crm.engagements.<a href="src/merge/resources/crm/resources/engagements/client.py">meta_patch_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Engagement` PATCHs.
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
client.crm.engagements.meta_patch_retrieve(
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

<details><summary><code>client.crm.engagements.<a href="src/merge/resources/crm/resources/engagements/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Engagement` POSTs.
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
client.crm.engagements.meta_post_retrieve()

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

<details><summary><code>client.crm.engagements.<a href="src/merge/resources/crm/resources/engagements/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.engagements.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm FieldMapping
<details><summary><code>client.crm.field_mapping.<a href="src/merge/resources/crm/resources/field_mapping/client.py">field_mappings_retrieve</a>(...)</code></summary>
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
client.crm.field_mapping.field_mappings_retrieve()

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

<details><summary><code>client.crm.field_mapping.<a href="src/merge/resources/crm/resources/field_mapping/client.py">field_mappings_create</a>(...)</code></summary>
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
client.crm.field_mapping.field_mappings_create(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.crm.field_mapping.<a href="src/merge/resources/crm/resources/field_mapping/client.py">field_mappings_destroy</a>(...)</code></summary>
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
client.crm.field_mapping.field_mappings_destroy(
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

<details><summary><code>client.crm.field_mapping.<a href="src/merge/resources/crm/resources/field_mapping/client.py">field_mappings_partial_update</a>(...)</code></summary>
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
client.crm.field_mapping.field_mappings_partial_update(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.crm.field_mapping.<a href="src/merge/resources/crm/resources/field_mapping/client.py">remote_fields_retrieve</a>(...)</code></summary>
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
client.crm.field_mapping.remote_fields_retrieve()

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

<details><summary><code>client.crm.field_mapping.<a href="src/merge/resources/crm/resources/field_mapping/client.py">target_fields_retrieve</a>()</code></summary>
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
client.crm.field_mapping.target_fields_retrieve()

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

## Crm GenerateKey
<details><summary><code>client.crm.generate_key.<a href="src/merge/resources/crm/resources/generate_key/client.py">create</a>(...)</code></summary>
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
client.crm.generate_key.create(
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

## Crm Issues
<details><summary><code>client.crm.issues.<a href="src/merge/resources/crm/resources/issues/client.py">list</a>(...)</code></summary>
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.issues.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

<details><summary><code>client.crm.issues.<a href="src/merge/resources/crm/resources/issues/client.py">retrieve</a>(...)</code></summary>
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
client.crm.issues.retrieve(
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

## Crm Leads
<details><summary><code>client.crm.leads.<a href="src/merge/resources/crm/resources/leads/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Lead` objects.
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
client.crm.leads.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**converted_account_id:** `typing.Optional[str]` — If provided, will only return leads with this account.
    
</dd>
</dl>

<dl>
<dd>

**converted_contact_id:** `typing.Optional[str]` — If provided, will only return leads with this contact.
    
</dd>
</dl>

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

**email_addresses:** `typing.Optional[str]` — If provided, will only return contacts matching the email addresses; multiple email_addresses can be separated by commas.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[LeadsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

**owner_id:** `typing.Optional[str]` — If provided, will only return leads with this owner.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**phone_numbers:** `typing.Optional[str]` — If provided, will only return contacts matching the phone numbers; multiple phone numbers can be separated by commas.
    
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

<details><summary><code>client.crm.leads.<a href="src/merge/resources/crm/resources/leads/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Lead` object with the given values.
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
from merge.resources.crm import LeadRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.leads.create(
    model=LeadRequest(),
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

**model:** `LeadRequest` 
    
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

<details><summary><code>client.crm.leads.<a href="src/merge/resources/crm/resources/leads/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Lead` object with the given `id`.
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
client.crm.leads.retrieve(
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

**expand:** `typing.Optional[LeadsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.leads.<a href="src/merge/resources/crm/resources/leads/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Lead` POSTs.
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
client.crm.leads.meta_post_retrieve()

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

<details><summary><code>client.crm.leads.<a href="src/merge/resources/crm/resources/leads/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.leads.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm LinkToken
<details><summary><code>client.crm.link_token.<a href="src/merge/resources/crm/resources/link_token/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a link token to be used when linking a new end user.
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
from merge.resources.crm import CategoriesEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.link_token.create(
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

## Crm LinkedAccounts
<details><summary><code>client.crm.linked_accounts.<a href="src/merge/resources/crm/resources/linked_accounts/client.py">list</a>(...)</code></summary>
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

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.linked_accounts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

## Crm Notes
<details><summary><code>client.crm.notes.<a href="src/merge/resources/crm/resources/notes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Note` objects.
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
client.crm.notes.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**account_id:** `typing.Optional[str]` — If provided, will only return notes with this account.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — If provided, will only return notes with this contact.
    
</dd>
</dl>

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

**expand:** `typing.Optional[NotesListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

**opportunity_id:** `typing.Optional[str]` — If provided, will only return notes with this opportunity.
    
</dd>
</dl>

<dl>
<dd>

**owner_id:** `typing.Optional[str]` — If provided, will only return notes with this owner.
    
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

<details><summary><code>client.crm.notes.<a href="src/merge/resources/crm/resources/notes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Note` object with the given values.
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
from merge.resources.crm import NoteRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.notes.create(
    model=NoteRequest(),
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

**model:** `NoteRequest` 
    
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

<details><summary><code>client.crm.notes.<a href="src/merge/resources/crm/resources/notes/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Note` object with the given `id`.
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
client.crm.notes.retrieve(
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

**expand:** `typing.Optional[NotesRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.notes.<a href="src/merge/resources/crm/resources/notes/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Note` POSTs.
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
client.crm.notes.meta_post_retrieve()

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

<details><summary><code>client.crm.notes.<a href="src/merge/resources/crm/resources/notes/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.notes.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm Opportunities
<details><summary><code>client.crm.opportunities.<a href="src/merge/resources/crm/resources/opportunities/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Opportunity` objects.
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
client.crm.opportunities.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**account_id:** `typing.Optional[str]` — If provided, will only return opportunities with this account.
    
</dd>
</dl>

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

**expand:** `typing.Optional[OpportunitiesListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

**owner_id:** `typing.Optional[str]` — If provided, will only return opportunities with this owner.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_created_after:** `typing.Optional[dt.datetime]` — If provided, will only return opportunities created in the third party platform after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**stage_id:** `typing.Optional[str]` — If provided, will only return opportunities with this stage.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[OpportunitiesListRequestStatus]` 

If provided, will only return opportunities with this status. Options: ('OPEN', 'WON', 'LOST')

* `OPEN` - OPEN
* `WON` - WON
* `LOST` - LOST
    
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

<details><summary><code>client.crm.opportunities.<a href="src/merge/resources/crm/resources/opportunities/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Opportunity` object with the given values.
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
from merge.resources.crm import OpportunityRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.opportunities.create(
    model=OpportunityRequest(),
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

**model:** `OpportunityRequest` 
    
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

<details><summary><code>client.crm.opportunities.<a href="src/merge/resources/crm/resources/opportunities/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Opportunity` object with the given `id`.
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
client.crm.opportunities.retrieve(
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

**expand:** `typing.Optional[OpportunitiesRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.crm.opportunities.<a href="src/merge/resources/crm/resources/opportunities/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an `Opportunity` object with the given `id`.
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
from merge.resources.crm import PatchedOpportunityRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.opportunities.partial_update(
    id="id",
    model=PatchedOpportunityRequest(),
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

**model:** `PatchedOpportunityRequest` 
    
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

<details><summary><code>client.crm.opportunities.<a href="src/merge/resources/crm/resources/opportunities/client.py">meta_patch_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Opportunity` PATCHs.
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
client.crm.opportunities.meta_patch_retrieve(
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

<details><summary><code>client.crm.opportunities.<a href="src/merge/resources/crm/resources/opportunities/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Opportunity` POSTs.
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
client.crm.opportunities.meta_post_retrieve()

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

<details><summary><code>client.crm.opportunities.<a href="src/merge/resources/crm/resources/opportunities/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.opportunities.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm Passthrough
<details><summary><code>client.crm.passthrough.<a href="src/merge/resources/crm/resources/passthrough/client.py">create</a>(...)</code></summary>
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
from merge.resources.crm import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.passthrough.create(
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

## Crm RegenerateKey
<details><summary><code>client.crm.regenerate_key.<a href="src/merge/resources/crm/resources/regenerate_key/client.py">create</a>(...)</code></summary>
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
client.crm.regenerate_key.create(
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

## Crm Stages
<details><summary><code>client.crm.stages.<a href="src/merge/resources/crm/resources/stages/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Stage` objects.
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
client.crm.stages.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.stages.<a href="src/merge/resources/crm/resources/stages/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Stage` object with the given `id`.
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
client.crm.stages.retrieve(
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

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.stages.<a href="src/merge/resources/crm/resources/stages/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.stages.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm SyncStatus
<details><summary><code>client.crm.sync_status.<a href="src/merge/resources/crm/resources/sync_status/client.py">list</a>(...)</code></summary>
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
client.crm.sync_status.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
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

## Crm ForceResync
<details><summary><code>client.crm.force_resync.<a href="src/merge/resources/crm/resources/force_resync/client.py">sync_status_resync_create</a>()</code></summary>
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
client.crm.force_resync.sync_status_resync_create()

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

## Crm Tasks
<details><summary><code>client.crm.tasks.<a href="src/merge/resources/crm/resources/tasks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Task` objects.
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
client.crm.tasks.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[TasksListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.tasks.<a href="src/merge/resources/crm/resources/tasks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Task` object with the given values.
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
from merge.resources.crm import TaskRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.tasks.create(
    model=TaskRequest(),
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

**model:** `TaskRequest` 
    
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

<details><summary><code>client.crm.tasks.<a href="src/merge/resources/crm/resources/tasks/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Task` object with the given `id`.
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
client.crm.tasks.retrieve(
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

**expand:** `typing.Optional[TasksRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.tasks.<a href="src/merge/resources/crm/resources/tasks/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a `Task` object with the given `id`.
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
from merge.resources.crm import PatchedTaskRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.tasks.partial_update(
    id="id",
    model=PatchedTaskRequest(),
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

**model:** `PatchedTaskRequest` 
    
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

<details><summary><code>client.crm.tasks.<a href="src/merge/resources/crm/resources/tasks/client.py">meta_patch_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Task` PATCHs.
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
client.crm.tasks.meta_patch_retrieve(
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

<details><summary><code>client.crm.tasks.<a href="src/merge/resources/crm/resources/tasks/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Task` POSTs.
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
client.crm.tasks.meta_post_retrieve()

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

<details><summary><code>client.crm.tasks.<a href="src/merge/resources/crm/resources/tasks/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.tasks.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm Users
<details><summary><code>client.crm.users.<a href="src/merge/resources/crm/resources/users/client.py">list</a>(...)</code></summary>
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.users.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**email:** `typing.Optional[str]` — If provided, will only return users with this email.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.users.<a href="src/merge/resources/crm/resources/users/client.py">retrieve</a>(...)</code></summary>
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
client.crm.users.retrieve(
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

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.crm.users.<a href="src/merge/resources/crm/resources/users/client.py">ignore_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.
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
from merge.resources.crm import IgnoreCommonModelRequest, ReasonEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.crm.users.ignore_create(
    model_id="model_id",
    request=IgnoreCommonModelRequest(
        reason=ReasonEnum.GENERAL_CUSTOMER_REQUEST,
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

**model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `IgnoreCommonModelRequest` 
    
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

<details><summary><code>client.crm.users.<a href="src/merge/resources/crm/resources/users/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.crm.users.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Crm WebhookReceivers
<details><summary><code>client.crm.webhook_receivers.<a href="src/merge/resources/crm/resources/webhook_receivers/client.py">list</a>()</code></summary>
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
client.crm.webhook_receivers.list()

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

<details><summary><code>client.crm.webhook_receivers.<a href="src/merge/resources/crm/resources/webhook_receivers/client.py">create</a>(...)</code></summary>
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
client.crm.webhook_receivers.create(
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
client.filestorage.audit_trail.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.drives.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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
client.filestorage.field_mapping.field_mappings_retrieve()

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
client.filestorage.field_mapping.remote_fields_retrieve()

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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.files.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[FilesListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**expand:** `typing.Optional[FilesRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

Returns metadata to construct an authenticated file download request for a singular file, allowing you to download file directly from the third-party.
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

**mime_type:** `typing.Optional[str]` — If provided, specifies the export format of the file to be downloaded. For information on supported export formats, please refer to our <a href='https://help.merge.dev/en/articles/8615316-file-export-and-download-specification' target='_blank'>export format help center article</a>.
    
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

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.files.download_request_meta_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.folders.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[FoldersListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

**expand:** `typing.Optional[FoldersRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.groups.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[typing.Literal["child_groups"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**expand:** `typing.Optional[typing.Literal["child_groups"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.issues.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

Creates a link token to be used when linking a new end user.
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

**language:** `typing.Optional[LanguageEnum]` 

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

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.linked_accounts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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
client.filestorage.sync_status.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.filestorage.users.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

## Hris AccountDetails
<details><summary><code>client.hris.account_details.<a href="src/merge/resources/hris/resources/account_details/client.py">retrieve</a>()</code></summary>
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
client.hris.account_details.retrieve()

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

## Hris AccountToken
<details><summary><code>client.hris.account_token.<a href="src/merge/resources/hris/resources/account_token/client.py">retrieve</a>(...)</code></summary>
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
client.hris.account_token.retrieve(
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

## Hris AsyncPassthrough
<details><summary><code>client.hris.async_passthrough.<a href="src/merge/resources/hris/resources/async_passthrough/client.py">create</a>(...)</code></summary>
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
from merge.resources.hris import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.async_passthrough.create(
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

<details><summary><code>client.hris.async_passthrough.<a href="src/merge/resources/hris/resources/async_passthrough/client.py">retrieve</a>(...)</code></summary>
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
client.hris.async_passthrough.retrieve(
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

## Hris AuditTrail
<details><summary><code>client.hris.audit_trail.<a href="src/merge/resources/hris/resources/audit_trail/client.py">list</a>(...)</code></summary>
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
client.hris.audit_trail.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

## Hris AvailableActions
<details><summary><code>client.hris.available_actions.<a href="src/merge/resources/hris/resources/available_actions/client.py">retrieve</a>()</code></summary>
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
client.hris.available_actions.retrieve()

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

## Hris BankInfo
<details><summary><code>client.hris.bank_info.<a href="src/merge/resources/hris/resources/bank_info/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `BankInfo` objects.
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
client.hris.bank_info.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**account_type:** `typing.Optional[BankInfoListRequestAccountType]` 

If provided, will only return BankInfo's with this account type. Options: ('SAVINGS', 'CHECKING')

* `SAVINGS` - SAVINGS
* `CHECKING` - CHECKING
    
</dd>
</dl>

<dl>
<dd>

**bank_name:** `typing.Optional[str]` — If provided, will only return BankInfo's with this bank name.
    
</dd>
</dl>

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

**employee_id:** `typing.Optional[str]` — If provided, will only return bank accounts for this employee.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Literal["employee"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**order_by:** `typing.Optional[BankInfoListRequestOrderBy]` — Overrides the default ordering for this endpoint. Possible values include: remote_created_at, -remote_created_at.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["account_type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["account_type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.hris.bank_info.<a href="src/merge/resources/hris/resources/bank_info/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `BankInfo` object with the given `id`.
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
client.hris.bank_info.retrieve(
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

**expand:** `typing.Optional[typing.Literal["employee"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[typing.Literal["account_type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["account_type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Hris Benefits
<details><summary><code>client.hris.benefits.<a href="src/merge/resources/hris/resources/benefits/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Benefit` objects.
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
client.hris.benefits.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**employee_id:** `typing.Optional[str]` — If provided, will return the benefits associated with the employee.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Literal["employee"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.hris.benefits.<a href="src/merge/resources/hris/resources/benefits/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Benefit` object with the given `id`.
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
client.hris.benefits.retrieve(
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

**expand:** `typing.Optional[typing.Literal["employee"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Hris Companies
<details><summary><code>client.hris.companies.<a href="src/merge/resources/hris/resources/companies/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Company` objects.
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
client.hris.companies.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.hris.companies.<a href="src/merge/resources/hris/resources/companies/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Company` object with the given `id`.
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
client.hris.companies.retrieve(
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

## Hris Scopes
<details><summary><code>client.hris.scopes.<a href="src/merge/resources/hris/resources/scopes/client.py">default_scopes_retrieve</a>()</code></summary>
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
client.hris.scopes.default_scopes_retrieve()

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

<details><summary><code>client.hris.scopes.<a href="src/merge/resources/hris/resources/scopes/client.py">linked_account_scopes_retrieve</a>()</code></summary>
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
client.hris.scopes.linked_account_scopes_retrieve()

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

<details><summary><code>client.hris.scopes.<a href="src/merge/resources/hris/resources/scopes/client.py">linked_account_scopes_create</a>(...)</code></summary>
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
from merge.resources.hris import (
    FieldPermissionDeserializerRequest,
    IndividualCommonModelScopeDeserializerRequest,
    ModelPermissionDeserializerRequest,
)

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.scopes.linked_account_scopes_create(
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

## Hris DeleteAccount
<details><summary><code>client.hris.delete_account.<a href="src/merge/resources/hris/resources/delete_account/client.py">delete</a>()</code></summary>
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
client.hris.delete_account.delete()

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

## Hris Dependents
<details><summary><code>client.hris.dependents.<a href="src/merge/resources/hris/resources/dependents/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Dependent` objects.
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
client.hris.dependents.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**include_sensitive_fields:** `typing.Optional[bool]` — Whether to include sensitive fields (such as social security numbers) in the response.
    
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

<details><summary><code>client.hris.dependents.<a href="src/merge/resources/hris/resources/dependents/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Dependent` object with the given `id`.
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
client.hris.dependents.retrieve(
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

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_sensitive_fields:** `typing.Optional[bool]` — Whether to include sensitive fields (such as social security numbers) in the response.
    
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

## Hris EmployeePayrollRuns
<details><summary><code>client.hris.employee_payroll_runs.<a href="src/merge/resources/hris/resources/employee_payroll_runs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `EmployeePayrollRun` objects.
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
client.hris.employee_payroll_runs.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**employee_id:** `typing.Optional[str]` — If provided, will only return employee payroll runs for this employee.
    
</dd>
</dl>

<dl>
<dd>

**ended_after:** `typing.Optional[dt.datetime]` — If provided, will only return employee payroll runs ended after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**ended_before:** `typing.Optional[dt.datetime]` — If provided, will only return employee payroll runs ended before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[EmployeePayrollRunsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**payroll_run_id:** `typing.Optional[str]` — If provided, will only return employee payroll runs for this employee.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**started_after:** `typing.Optional[dt.datetime]` — If provided, will only return employee payroll runs started after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[dt.datetime]` — If provided, will only return employee payroll runs started before this datetime.
    
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

<details><summary><code>client.hris.employee_payroll_runs.<a href="src/merge/resources/hris/resources/employee_payroll_runs/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `EmployeePayrollRun` object with the given `id`.
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
client.hris.employee_payroll_runs.retrieve(
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

**expand:** `typing.Optional[EmployeePayrollRunsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Hris Employees
<details><summary><code>client.hris.employees.<a href="src/merge/resources/hris/resources/employees/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Employee` objects.
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
client.hris.employees.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return employees for this company.
    
</dd>
</dl>

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

**display_full_name:** `typing.Optional[str]` — If provided, will only return employees with this display name.
    
</dd>
</dl>

<dl>
<dd>

**employment_status:** `typing.Optional[EmployeesListRequestEmploymentStatus]` 

If provided, will only return employees with this employment status.

* `ACTIVE` - ACTIVE
* `PENDING` - PENDING
* `INACTIVE` - INACTIVE
    
</dd>
</dl>

<dl>
<dd>

**employment_type:** `typing.Optional[str]` — If provided, will only return employees that have an employment of the specified employment_type.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[EmployeesListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — If provided, will only return employees with this first name.
    
</dd>
</dl>

<dl>
<dd>

**groups:** `typing.Optional[str]` — If provided, will only return employees matching the group ids; multiple groups can be separated by commas.
    
</dd>
</dl>

<dl>
<dd>

**home_location_id:** `typing.Optional[str]` — If provided, will only return employees for this home location.
    
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

**include_sensitive_fields:** `typing.Optional[bool]` — Whether to include sensitive fields (such as social security numbers) in the response.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**job_title:** `typing.Optional[str]` — If provided, will only return employees that have an employment of the specified job_title.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — If provided, will only return employees with this last name.
    
</dd>
</dl>

<dl>
<dd>

**manager_id:** `typing.Optional[str]` — If provided, will only return employees for this manager.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**pay_group_id:** `typing.Optional[str]` — If provided, will only return employees for this pay group
    
</dd>
</dl>

<dl>
<dd>

**personal_email:** `typing.Optional[str]` — If provided, will only return Employees with this personal email
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[EmployeesListRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[EmployeesListRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**started_after:** `typing.Optional[dt.datetime]` — If provided, will only return employees that started after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[dt.datetime]` — If provided, will only return employees that started before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**team_id:** `typing.Optional[str]` — If provided, will only return employees for this team.
    
</dd>
</dl>

<dl>
<dd>

**terminated_after:** `typing.Optional[dt.datetime]` — If provided, will only return employees that were terminated after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**terminated_before:** `typing.Optional[dt.datetime]` — If provided, will only return employees that were terminated before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**work_email:** `typing.Optional[str]` — If provided, will only return Employees with this work email
    
</dd>
</dl>

<dl>
<dd>

**work_location_id:** `typing.Optional[str]` — If provided, will only return employees for this location.
    
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

<details><summary><code>client.hris.employees.<a href="src/merge/resources/hris/resources/employees/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Employee` object with the given values.
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
from merge.resources.hris import EmployeeRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.employees.create(
    model=EmployeeRequest(),
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

**model:** `EmployeeRequest` 
    
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

<details><summary><code>client.hris.employees.<a href="src/merge/resources/hris/resources/employees/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Employee` object with the given `id`.
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
client.hris.employees.retrieve(
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

**expand:** `typing.Optional[EmployeesRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_sensitive_fields:** `typing.Optional[bool]` — Whether to include sensitive fields (such as social security numbers) in the response.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[EmployeesRetrieveRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[EmployeesRetrieveRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.hris.employees.<a href="src/merge/resources/hris/resources/employees/client.py">ignore_create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The "reason" and "message" fields in the request body will be stored for audit purposes.
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
from merge.resources.hris import ReasonEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.employees.ignore_create(
    model_id="model_id",
    reason=ReasonEnum.GENERAL_CUSTOMER_REQUEST,
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

**model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `IgnoreCommonModelRequestReason` 
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` 
    
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

<details><summary><code>client.hris.employees.<a href="src/merge/resources/hris/resources/employees/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Employee` POSTs.
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
client.hris.employees.meta_post_retrieve()

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

## Hris EmployerBenefits
<details><summary><code>client.hris.employer_benefits.<a href="src/merge/resources/hris/resources/employer_benefits/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `EmployerBenefit` objects.
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
client.hris.employer_benefits.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.hris.employer_benefits.<a href="src/merge/resources/hris/resources/employer_benefits/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `EmployerBenefit` object with the given `id`.
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
client.hris.employer_benefits.retrieve(
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

## Hris Employments
<details><summary><code>client.hris.employments.<a href="src/merge/resources/hris/resources/employments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Employment` objects.
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
client.hris.employments.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**employee_id:** `typing.Optional[str]` — If provided, will only return employments for this employee.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[EmploymentsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**order_by:** `typing.Optional[EmploymentsListRequestOrderBy]` — Overrides the default ordering for this endpoint. Possible values include: effective_date, -effective_date.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[EmploymentsListRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[EmploymentsListRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.hris.employments.<a href="src/merge/resources/hris/resources/employments/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Employment` object with the given `id`.
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
client.hris.employments.retrieve(
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

**expand:** `typing.Optional[EmploymentsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[EmploymentsRetrieveRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[EmploymentsRetrieveRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Hris FieldMapping
<details><summary><code>client.hris.field_mapping.<a href="src/merge/resources/hris/resources/field_mapping/client.py">field_mappings_retrieve</a>(...)</code></summary>
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
client.hris.field_mapping.field_mappings_retrieve()

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

<details><summary><code>client.hris.field_mapping.<a href="src/merge/resources/hris/resources/field_mapping/client.py">field_mappings_create</a>(...)</code></summary>
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
client.hris.field_mapping.field_mappings_create(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hris.field_mapping.<a href="src/merge/resources/hris/resources/field_mapping/client.py">field_mappings_destroy</a>(...)</code></summary>
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
client.hris.field_mapping.field_mappings_destroy(
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

<details><summary><code>client.hris.field_mapping.<a href="src/merge/resources/hris/resources/field_mapping/client.py">field_mappings_partial_update</a>(...)</code></summary>
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
client.hris.field_mapping.field_mappings_partial_update(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.hris.field_mapping.<a href="src/merge/resources/hris/resources/field_mapping/client.py">remote_fields_retrieve</a>(...)</code></summary>
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
client.hris.field_mapping.remote_fields_retrieve()

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

<details><summary><code>client.hris.field_mapping.<a href="src/merge/resources/hris/resources/field_mapping/client.py">target_fields_retrieve</a>()</code></summary>
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
client.hris.field_mapping.target_fields_retrieve()

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

## Hris GenerateKey
<details><summary><code>client.hris.generate_key.<a href="src/merge/resources/hris/resources/generate_key/client.py">create</a>(...)</code></summary>
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
client.hris.generate_key.create(
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

## Hris Groups
<details><summary><code>client.hris.groups.<a href="src/merge/resources/hris/resources/groups/client.py">list</a>(...)</code></summary>
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.groups.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_commonly_used_as_team:** `typing.Optional[str]` — If provided, specifies whether to return only Group objects which refer to a team in the third party platform. Note that this is an opinionated view based on how a team may be represented in the third party platform.
    
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

**names:** `typing.Optional[str]` — If provided, will only return groups with these names. Multiple values can be separated by commas.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**types:** `typing.Optional[str]` — If provided, will only return groups of these types. Multiple values can be separated by commas.
    
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

<details><summary><code>client.hris.groups.<a href="src/merge/resources/hris/resources/groups/client.py">retrieve</a>(...)</code></summary>
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
client.hris.groups.retrieve(
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

**remote_fields:** `typing.Optional[typing.Literal["type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Hris Issues
<details><summary><code>client.hris.issues.<a href="src/merge/resources/hris/resources/issues/client.py">list</a>(...)</code></summary>
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.issues.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

<details><summary><code>client.hris.issues.<a href="src/merge/resources/hris/resources/issues/client.py">retrieve</a>(...)</code></summary>
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
client.hris.issues.retrieve(
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

## Hris LinkToken
<details><summary><code>client.hris.link_token.<a href="src/merge/resources/hris/resources/link_token/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a link token to be used when linking a new end user.
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
from merge.resources.hris import CategoriesEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.link_token.create(
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

## Hris LinkedAccounts
<details><summary><code>client.hris.linked_accounts.<a href="src/merge/resources/hris/resources/linked_accounts/client.py">list</a>(...)</code></summary>
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

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.linked_accounts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

## Hris Locations
<details><summary><code>client.hris.locations.<a href="src/merge/resources/hris/resources/locations/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Location` objects.
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
client.hris.locations.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**location_type:** `typing.Optional[LocationsListRequestLocationType]` 

If provided, will only return locations with this location_type

* `HOME` - HOME
* `WORK` - WORK
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[LocationsListRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[LocationsListRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.hris.locations.<a href="src/merge/resources/hris/resources/locations/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Location` object with the given `id`.
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
client.hris.locations.retrieve(
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

**remote_fields:** `typing.Optional[LocationsRetrieveRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[LocationsRetrieveRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Hris Passthrough
<details><summary><code>client.hris.passthrough.<a href="src/merge/resources/hris/resources/passthrough/client.py">create</a>(...)</code></summary>
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
from merge.resources.hris import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.passthrough.create(
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

## Hris PayGroups
<details><summary><code>client.hris.pay_groups.<a href="src/merge/resources/hris/resources/pay_groups/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `PayGroup` objects.
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
client.hris.pay_groups.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.hris.pay_groups.<a href="src/merge/resources/hris/resources/pay_groups/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `PayGroup` object with the given `id`.
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
client.hris.pay_groups.retrieve(
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

## Hris PayrollRuns
<details><summary><code>client.hris.payroll_runs.<a href="src/merge/resources/hris/resources/payroll_runs/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `PayrollRun` objects.
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
client.hris.payroll_runs.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**ended_after:** `typing.Optional[dt.datetime]` — If provided, will only return payroll runs ended after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**ended_before:** `typing.Optional[dt.datetime]` — If provided, will only return payroll runs ended before this datetime.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[PayrollRunsListRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**run_type:** `typing.Optional[PayrollRunsListRequestRunType]` 

If provided, will only return PayrollRun's with this status. Options: ('REGULAR', 'OFF_CYCLE', 'CORRECTION', 'TERMINATION', 'SIGN_ON_BONUS')

* `REGULAR` - REGULAR
* `OFF_CYCLE` - OFF_CYCLE
* `CORRECTION` - CORRECTION
* `TERMINATION` - TERMINATION
* `SIGN_ON_BONUS` - SIGN_ON_BONUS
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[PayrollRunsListRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**started_after:** `typing.Optional[dt.datetime]` — If provided, will only return payroll runs started after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[dt.datetime]` — If provided, will only return payroll runs started before this datetime.
    
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

<details><summary><code>client.hris.payroll_runs.<a href="src/merge/resources/hris/resources/payroll_runs/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `PayrollRun` object with the given `id`.
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
client.hris.payroll_runs.retrieve(
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

**remote_fields:** `typing.Optional[PayrollRunsRetrieveRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[PayrollRunsRetrieveRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Hris RegenerateKey
<details><summary><code>client.hris.regenerate_key.<a href="src/merge/resources/hris/resources/regenerate_key/client.py">create</a>(...)</code></summary>
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
client.hris.regenerate_key.create(
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

## Hris SyncStatus
<details><summary><code>client.hris.sync_status.<a href="src/merge/resources/hris/resources/sync_status/client.py">list</a>(...)</code></summary>
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
client.hris.sync_status.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
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

## Hris ForceResync
<details><summary><code>client.hris.force_resync.<a href="src/merge/resources/hris/resources/force_resync/client.py">sync_status_resync_create</a>()</code></summary>
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
client.hris.force_resync.sync_status_resync_create()

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

## Hris Teams
<details><summary><code>client.hris.teams.<a href="src/merge/resources/hris/resources/teams/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Team` objects.
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
client.hris.teams.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[typing.Literal["parent_team"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**parent_team_id:** `typing.Optional[str]` — If provided, will only return teams with this parent team.
    
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

<details><summary><code>client.hris.teams.<a href="src/merge/resources/hris/resources/teams/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Team` object with the given `id`.
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
client.hris.teams.retrieve(
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

**expand:** `typing.Optional[typing.Literal["parent_team"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Hris TimeOff
<details><summary><code>client.hris.time_off.<a href="src/merge/resources/hris/resources/time_off/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `TimeOff` objects.
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
client.hris.time_off.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**approver_id:** `typing.Optional[str]` — If provided, will only return time off for this approver.
    
</dd>
</dl>

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

**employee_id:** `typing.Optional[str]` — If provided, will only return time off for this employee.
    
</dd>
</dl>

<dl>
<dd>

**ended_after:** `typing.Optional[dt.datetime]` — If provided, will only return employees that ended after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**ended_before:** `typing.Optional[dt.datetime]` — If provided, will only return time-offs that ended before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[TimeOffListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[TimeOffListRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**request_type:** `typing.Optional[TimeOffListRequestRequestType]` 

If provided, will only return TimeOff with this request type. Options: ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER', 'BEREAVEMENT')

* `VACATION` - VACATION
* `SICK` - SICK
* `PERSONAL` - PERSONAL
* `JURY_DUTY` - JURY_DUTY
* `VOLUNTEER` - VOLUNTEER
* `BEREAVEMENT` - BEREAVEMENT
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[TimeOffListRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**started_after:** `typing.Optional[dt.datetime]` — If provided, will only return time-offs that started after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[dt.datetime]` — If provided, will only return time-offs that started before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[TimeOffListRequestStatus]` 

If provided, will only return TimeOff with this status. Options: ('REQUESTED', 'APPROVED', 'DECLINED', 'CANCELLED', 'DELETED')

* `REQUESTED` - REQUESTED
* `APPROVED` - APPROVED
* `DECLINED` - DECLINED
* `CANCELLED` - CANCELLED
* `DELETED` - DELETED
    
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

<details><summary><code>client.hris.time_off.<a href="src/merge/resources/hris/resources/time_off/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `TimeOff` object with the given values.
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
from merge.resources.hris import TimeOffRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.time_off.create(
    model=TimeOffRequest(),
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

**model:** `TimeOffRequest` 
    
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

<details><summary><code>client.hris.time_off.<a href="src/merge/resources/hris/resources/time_off/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `TimeOff` object with the given `id`.
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
client.hris.time_off.retrieve(
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

**expand:** `typing.Optional[TimeOffRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[TimeOffRetrieveRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[TimeOffRetrieveRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.hris.time_off.<a href="src/merge/resources/hris/resources/time_off/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `TimeOff` POSTs.
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
client.hris.time_off.meta_post_retrieve()

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

## Hris TimeOffBalances
<details><summary><code>client.hris.time_off_balances.<a href="src/merge/resources/hris/resources/time_off_balances/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `TimeOffBalance` objects.
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
client.hris.time_off_balances.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**employee_id:** `typing.Optional[str]` — If provided, will only return time off balances for this employee.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Literal["employee"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**policy_type:** `typing.Optional[TimeOffBalancesListRequestPolicyType]` 

If provided, will only return TimeOffBalance with this policy type. Options: ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER', 'BEREAVEMENT')

* `VACATION` - VACATION
* `SICK` - SICK
* `PERSONAL` - PERSONAL
* `JURY_DUTY` - JURY_DUTY
* `VOLUNTEER` - VOLUNTEER
* `BEREAVEMENT` - BEREAVEMENT
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["policy_type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["policy_type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.hris.time_off_balances.<a href="src/merge/resources/hris/resources/time_off_balances/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `TimeOffBalance` object with the given `id`.
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
client.hris.time_off_balances.retrieve(
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

**expand:** `typing.Optional[typing.Literal["employee"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[typing.Literal["policy_type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["policy_type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Hris TimesheetEntries
<details><summary><code>client.hris.timesheet_entries.<a href="src/merge/resources/hris/resources/timesheet_entries/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `TimesheetEntry` objects.
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
client.hris.timesheet_entries.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**employee_id:** `typing.Optional[str]` — If provided, will only return timesheet entries for this employee.
    
</dd>
</dl>

<dl>
<dd>

**ended_after:** `typing.Optional[dt.datetime]` — If provided, will only return timesheet entries ended after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**ended_before:** `typing.Optional[dt.datetime]` — If provided, will only return timesheet entries ended before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Literal["employee"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**order_by:** `typing.Optional[TimesheetEntriesListRequestOrderBy]` — Overrides the default ordering for this endpoint. Possible values include: start_time, -start_time.
    
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

**started_after:** `typing.Optional[dt.datetime]` — If provided, will only return timesheet entries started after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[dt.datetime]` — If provided, will only return timesheet entries started before this datetime.
    
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

<details><summary><code>client.hris.timesheet_entries.<a href="src/merge/resources/hris/resources/timesheet_entries/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `TimesheetEntry` object with the given values.
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
from merge.resources.hris import TimesheetEntryRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.hris.timesheet_entries.create(
    model=TimesheetEntryRequest(),
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

**model:** `TimesheetEntryRequest` 
    
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

<details><summary><code>client.hris.timesheet_entries.<a href="src/merge/resources/hris/resources/timesheet_entries/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `TimesheetEntry` object with the given `id`.
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
client.hris.timesheet_entries.retrieve(
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

**expand:** `typing.Optional[typing.Literal["employee"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.hris.timesheet_entries.<a href="src/merge/resources/hris/resources/timesheet_entries/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `TimesheetEntry` POSTs.
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
client.hris.timesheet_entries.meta_post_retrieve()

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

## Hris WebhookReceivers
<details><summary><code>client.hris.webhook_receivers.<a href="src/merge/resources/hris/resources/webhook_receivers/client.py">list</a>()</code></summary>
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
client.hris.webhook_receivers.list()

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

<details><summary><code>client.hris.webhook_receivers.<a href="src/merge/resources/hris/resources/webhook_receivers/client.py">create</a>(...)</code></summary>
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
client.hris.webhook_receivers.create(
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

## Ticketing AccountDetails
<details><summary><code>client.ticketing.account_details.<a href="src/merge/resources/ticketing/resources/account_details/client.py">retrieve</a>()</code></summary>
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
client.ticketing.account_details.retrieve()

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

## Ticketing AccountToken
<details><summary><code>client.ticketing.account_token.<a href="src/merge/resources/ticketing/resources/account_token/client.py">retrieve</a>(...)</code></summary>
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
client.ticketing.account_token.retrieve(
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

## Ticketing Accounts
<details><summary><code>client.ticketing.accounts.<a href="src/merge/resources/ticketing/resources/accounts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Account` objects.
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
client.ticketing.accounts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.ticketing.accounts.<a href="src/merge/resources/ticketing/resources/accounts/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Account` object with the given `id`.
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
client.ticketing.accounts.retrieve(
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

## Ticketing AsyncPassthrough
<details><summary><code>client.ticketing.async_passthrough.<a href="src/merge/resources/ticketing/resources/async_passthrough/client.py">create</a>(...)</code></summary>
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
from merge.resources.ticketing import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.async_passthrough.create(
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

<details><summary><code>client.ticketing.async_passthrough.<a href="src/merge/resources/ticketing/resources/async_passthrough/client.py">retrieve</a>(...)</code></summary>
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
client.ticketing.async_passthrough.retrieve(
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

## Ticketing Attachments
<details><summary><code>client.ticketing.attachments.<a href="src/merge/resources/ticketing/resources/attachments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Attachment` objects.
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
client.ticketing.attachments.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[typing.Literal["ticket"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_created_after:** `typing.Optional[dt.datetime]` — If provided, will only return attachments created in the third party platform after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `typing.Optional[str]` — If provided, will only return comments for this ticket.
    
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

<details><summary><code>client.ticketing.attachments.<a href="src/merge/resources/ticketing/resources/attachments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Attachment` object with the given values.
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
from merge.resources.ticketing import AttachmentRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.attachments.create(
    model=AttachmentRequest(),
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

**model:** `AttachmentRequest` 
    
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

<details><summary><code>client.ticketing.attachments.<a href="src/merge/resources/ticketing/resources/attachments/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Attachment` object with the given `id`.
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
client.ticketing.attachments.retrieve(
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

**expand:** `typing.Optional[typing.Literal["ticket"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.ticketing.attachments.<a href="src/merge/resources/ticketing/resources/attachments/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `TicketingAttachment` POSTs.
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
client.ticketing.attachments.meta_post_retrieve()

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

## Ticketing AuditTrail
<details><summary><code>client.ticketing.audit_trail.<a href="src/merge/resources/ticketing/resources/audit_trail/client.py">list</a>(...)</code></summary>
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
client.ticketing.audit_trail.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

## Ticketing AvailableActions
<details><summary><code>client.ticketing.available_actions.<a href="src/merge/resources/ticketing/resources/available_actions/client.py">retrieve</a>()</code></summary>
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
client.ticketing.available_actions.retrieve()

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

## Ticketing Collections
<details><summary><code>client.ticketing.collections.<a href="src/merge/resources/ticketing/resources/collections/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Collection` objects.
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
client.ticketing.collections.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**collection_type:** `typing.Optional[str]` — If provided, will only return collections of the given type.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["parent_collection"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**parent_collection_id:** `typing.Optional[str]` — If provided, will only return collections whose parent collection matches the given id.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["collection_type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["collection_type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ticketing.collections.<a href="src/merge/resources/ticketing/resources/collections/client.py">viewers_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Viewer` objects that point to a User id or Team id that is either an assignee or viewer on a `Collection` with the given id. [Learn more.](https://help.merge.dev/en/articles/10333658-ticketing-access-control-list-acls)
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
client.ticketing.collections.viewers_list(
    collection_id="collection_id",
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**collection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[CollectionsViewersListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.ticketing.collections.<a href="src/merge/resources/ticketing/resources/collections/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Collection` object with the given `id`.
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
client.ticketing.collections.retrieve(
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

**expand:** `typing.Optional[typing.Literal["parent_collection"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[typing.Literal["collection_type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["collection_type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Ticketing Comments
<details><summary><code>client.ticketing.comments.<a href="src/merge/resources/ticketing/resources/comments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Comment` objects.
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
client.ticketing.comments.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[CommentsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_created_after:** `typing.Optional[dt.datetime]` — If provided, will only return Comments created in the third party platform after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**ticket_id:** `typing.Optional[str]` — If provided, will only return comments for this ticket.
    
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

<details><summary><code>client.ticketing.comments.<a href="src/merge/resources/ticketing/resources/comments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Comment` object with the given values.
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
from merge.resources.ticketing import CommentRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.comments.create(
    model=CommentRequest(),
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

**model:** `CommentRequest` 
    
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

<details><summary><code>client.ticketing.comments.<a href="src/merge/resources/ticketing/resources/comments/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Comment` object with the given `id`.
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
client.ticketing.comments.retrieve(
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

**expand:** `typing.Optional[CommentsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.ticketing.comments.<a href="src/merge/resources/ticketing/resources/comments/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Comment` POSTs.
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
client.ticketing.comments.meta_post_retrieve()

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

## Ticketing Contacts
<details><summary><code>client.ticketing.contacts.<a href="src/merge/resources/ticketing/resources/contacts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Contact` objects.
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
client.ticketing.contacts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[typing.Literal["account"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.ticketing.contacts.<a href="src/merge/resources/ticketing/resources/contacts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Contact` object with the given values.
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
from merge.resources.ticketing import ContactRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.contacts.create(
    model=ContactRequest(),
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

**model:** `ContactRequest` 
    
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

<details><summary><code>client.ticketing.contacts.<a href="src/merge/resources/ticketing/resources/contacts/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Contact` object with the given `id`.
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
client.ticketing.contacts.retrieve(
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

**expand:** `typing.Optional[typing.Literal["account"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.ticketing.contacts.<a href="src/merge/resources/ticketing/resources/contacts/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `TicketingContact` POSTs.
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
client.ticketing.contacts.meta_post_retrieve()

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

## Ticketing Scopes
<details><summary><code>client.ticketing.scopes.<a href="src/merge/resources/ticketing/resources/scopes/client.py">default_scopes_retrieve</a>()</code></summary>
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
client.ticketing.scopes.default_scopes_retrieve()

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

<details><summary><code>client.ticketing.scopes.<a href="src/merge/resources/ticketing/resources/scopes/client.py">linked_account_scopes_retrieve</a>()</code></summary>
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
client.ticketing.scopes.linked_account_scopes_retrieve()

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

<details><summary><code>client.ticketing.scopes.<a href="src/merge/resources/ticketing/resources/scopes/client.py">linked_account_scopes_create</a>(...)</code></summary>
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
from merge.resources.ticketing import (
    FieldPermissionDeserializerRequest,
    IndividualCommonModelScopeDeserializerRequest,
    ModelPermissionDeserializerRequest,
)

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.scopes.linked_account_scopes_create(
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

## Ticketing DeleteAccount
<details><summary><code>client.ticketing.delete_account.<a href="src/merge/resources/ticketing/resources/delete_account/client.py">delete</a>()</code></summary>
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
client.ticketing.delete_account.delete()

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

## Ticketing FieldMapping
<details><summary><code>client.ticketing.field_mapping.<a href="src/merge/resources/ticketing/resources/field_mapping/client.py">field_mappings_retrieve</a>(...)</code></summary>
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
client.ticketing.field_mapping.field_mappings_retrieve()

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

<details><summary><code>client.ticketing.field_mapping.<a href="src/merge/resources/ticketing/resources/field_mapping/client.py">field_mappings_create</a>(...)</code></summary>
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
client.ticketing.field_mapping.field_mappings_create(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.field_mapping.<a href="src/merge/resources/ticketing/resources/field_mapping/client.py">field_mappings_destroy</a>(...)</code></summary>
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
client.ticketing.field_mapping.field_mappings_destroy(
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

<details><summary><code>client.ticketing.field_mapping.<a href="src/merge/resources/ticketing/resources/field_mapping/client.py">field_mappings_partial_update</a>(...)</code></summary>
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
client.ticketing.field_mapping.field_mappings_partial_update(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ticketing.field_mapping.<a href="src/merge/resources/ticketing/resources/field_mapping/client.py">remote_fields_retrieve</a>(...)</code></summary>
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
client.ticketing.field_mapping.remote_fields_retrieve()

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

<details><summary><code>client.ticketing.field_mapping.<a href="src/merge/resources/ticketing/resources/field_mapping/client.py">target_fields_retrieve</a>()</code></summary>
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
client.ticketing.field_mapping.target_fields_retrieve()

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

## Ticketing GenerateKey
<details><summary><code>client.ticketing.generate_key.<a href="src/merge/resources/ticketing/resources/generate_key/client.py">create</a>(...)</code></summary>
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
client.ticketing.generate_key.create(
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

## Ticketing Issues
<details><summary><code>client.ticketing.issues.<a href="src/merge/resources/ticketing/resources/issues/client.py">list</a>(...)</code></summary>
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.issues.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

<details><summary><code>client.ticketing.issues.<a href="src/merge/resources/ticketing/resources/issues/client.py">retrieve</a>(...)</code></summary>
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
client.ticketing.issues.retrieve(
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

## Ticketing LinkToken
<details><summary><code>client.ticketing.link_token.<a href="src/merge/resources/ticketing/resources/link_token/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a link token to be used when linking a new end user.
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
from merge.resources.ticketing import CategoriesEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.link_token.create(
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

## Ticketing LinkedAccounts
<details><summary><code>client.ticketing.linked_accounts.<a href="src/merge/resources/ticketing/resources/linked_accounts/client.py">list</a>(...)</code></summary>
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

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.linked_accounts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

## Ticketing Passthrough
<details><summary><code>client.ticketing.passthrough.<a href="src/merge/resources/ticketing/resources/passthrough/client.py">create</a>(...)</code></summary>
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
from merge.resources.ticketing import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.passthrough.create(
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

## Ticketing Projects
<details><summary><code>client.ticketing.projects.<a href="src/merge/resources/ticketing/resources/projects/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Project` objects.
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
client.ticketing.projects.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.ticketing.projects.<a href="src/merge/resources/ticketing/resources/projects/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Project` object with the given `id`.
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
client.ticketing.projects.retrieve(
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

<details><summary><code>client.ticketing.projects.<a href="src/merge/resources/ticketing/resources/projects/client.py">users_list</a>(...)</code></summary>
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.projects.users_list(
    parent_id="parent_id",
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**parent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[ProjectsUsersListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Ticketing RegenerateKey
<details><summary><code>client.ticketing.regenerate_key.<a href="src/merge/resources/ticketing/resources/regenerate_key/client.py">create</a>(...)</code></summary>
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
client.ticketing.regenerate_key.create(
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

## Ticketing Roles
<details><summary><code>client.ticketing.roles.<a href="src/merge/resources/ticketing/resources/roles/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Role` objects.
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
client.ticketing.roles.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.ticketing.roles.<a href="src/merge/resources/ticketing/resources/roles/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Role` object with the given `id`.
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
client.ticketing.roles.retrieve(
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

## Ticketing SyncStatus
<details><summary><code>client.ticketing.sync_status.<a href="src/merge/resources/ticketing/resources/sync_status/client.py">list</a>(...)</code></summary>
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
client.ticketing.sync_status.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
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

## Ticketing ForceResync
<details><summary><code>client.ticketing.force_resync.<a href="src/merge/resources/ticketing/resources/force_resync/client.py">sync_status_resync_create</a>()</code></summary>
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
client.ticketing.force_resync.sync_status_resync_create()

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

## Ticketing Tags
<details><summary><code>client.ticketing.tags.<a href="src/merge/resources/ticketing/resources/tags/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Tag` objects.
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
client.ticketing.tags.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.ticketing.tags.<a href="src/merge/resources/ticketing/resources/tags/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Tag` object with the given `id`.
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
client.ticketing.tags.retrieve(
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

## Ticketing Teams
<details><summary><code>client.ticketing.teams.<a href="src/merge/resources/ticketing/resources/teams/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Team` objects.
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
client.ticketing.teams.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.ticketing.teams.<a href="src/merge/resources/ticketing/resources/teams/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Team` object with the given `id`.
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
client.ticketing.teams.retrieve(
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

## Ticketing Tickets
<details><summary><code>client.ticketing.tickets.<a href="src/merge/resources/ticketing/resources/tickets/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Ticket` objects.
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
client.ticketing.tickets.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**account_id:** `typing.Optional[str]` — If provided, will only return tickets for this account.
    
</dd>
</dl>

<dl>
<dd>

**assignee_ids:** `typing.Optional[str]` — If provided, will only return tickets assigned to the assignee_ids; multiple assignee_ids can be separated by commas.
    
</dd>
</dl>

<dl>
<dd>

**collection_ids:** `typing.Optional[str]` — If provided, will only return tickets assigned to the collection_ids; multiple collection_ids can be separated by commas.
    
</dd>
</dl>

<dl>
<dd>

**completed_after:** `typing.Optional[dt.datetime]` — If provided, will only return tickets completed after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**completed_before:** `typing.Optional[dt.datetime]` — If provided, will only return tickets completed before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — If provided, will only return tickets for this contact.
    
</dd>
</dl>

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

**due_after:** `typing.Optional[dt.datetime]` — If provided, will only return tickets due after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**due_before:** `typing.Optional[dt.datetime]` — If provided, will only return tickets due before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[TicketsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**parent_ticket_id:** `typing.Optional[str]` — If provided, will only return sub tickets of the parent_ticket_id.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[TicketsListRequestPriority]` 

If provided, will only return tickets of this priority.

* `URGENT` - URGENT
* `HIGH` - HIGH
* `NORMAL` - NORMAL
* `LOW` - LOW
    
</dd>
</dl>

<dl>
<dd>

**remote_created_after:** `typing.Optional[dt.datetime]` — If provided, will only return tickets created in the third party platform after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**remote_created_before:** `typing.Optional[dt.datetime]` — If provided, will only return tickets created in the third party platform before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[TicketsListRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**remote_updated_after:** `typing.Optional[dt.datetime]` — If provided, will only return tickets updated in the third party platform after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**remote_updated_before:** `typing.Optional[dt.datetime]` — If provided, will only return tickets updated in the third party platform before this datetime.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[TicketsListRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — If provided, will only return tickets of this status.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — If provided, will only return tickets matching the tags; multiple tags can be separated by commas.
    
</dd>
</dl>

<dl>
<dd>

**ticket_type:** `typing.Optional[str]` — If provided, will only return tickets of this type.
    
</dd>
</dl>

<dl>
<dd>

**ticket_url:** `typing.Optional[str]` — If provided, will only return tickets where the URL matches or contains the substring
    
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

<details><summary><code>client.ticketing.tickets.<a href="src/merge/resources/ticketing/resources/tickets/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Ticket` object with the given values.
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
from merge.resources.ticketing import TicketRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.tickets.create(
    model=TicketRequest(),
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

**model:** `TicketRequest` 
    
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

<details><summary><code>client.ticketing.tickets.<a href="src/merge/resources/ticketing/resources/tickets/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Ticket` object with the given `id`.
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
client.ticketing.tickets.retrieve(
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

**expand:** `typing.Optional[TicketsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[TicketsRetrieveRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[TicketsRetrieveRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.ticketing.tickets.<a href="src/merge/resources/ticketing/resources/tickets/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a `Ticket` object with the given `id`.
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
from merge.resources.ticketing import PatchedTicketRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.tickets.partial_update(
    id="id",
    model=PatchedTicketRequest(),
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

**model:** `PatchedTicketRequest` 
    
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

<details><summary><code>client.ticketing.tickets.<a href="src/merge/resources/ticketing/resources/tickets/client.py">viewers_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Viewer` objects that point to a User id or Team id that is either an assignee or viewer on a `Ticket` with the given id. [Learn more.](https://help.merge.dev/en/articles/10333658-ticketing-access-control-list-acls)
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
client.ticketing.tickets.viewers_list(
    ticket_id="ticket_id",
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**ticket_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[TicketsViewersListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.ticketing.tickets.<a href="src/merge/resources/ticketing/resources/tickets/client.py">meta_patch_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Ticket` PATCHs.
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
client.ticketing.tickets.meta_patch_retrieve(
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

<details><summary><code>client.ticketing.tickets.<a href="src/merge/resources/ticketing/resources/tickets/client.py">meta_post_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Ticket` POSTs.
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
client.ticketing.tickets.meta_post_retrieve()

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

**collection_id:** `typing.Optional[str]` — If provided, will only return tickets for this collection.
    
</dd>
</dl>

<dl>
<dd>

**ticket_type:** `typing.Optional[str]` — If provided, will only return tickets for this ticket type.
    
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

<details><summary><code>client.ticketing.tickets.<a href="src/merge/resources/ticketing/resources/tickets/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.ticketing.tickets.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Optional[str]` — If provided, will only return remote field classes with the `ids` in this list
    
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Ticketing Users
<details><summary><code>client.ticketing.users.<a href="src/merge/resources/ticketing/resources/users/client.py">list</a>(...)</code></summary>
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.ticketing.users.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[UsersListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**team:** `typing.Optional[str]` — If provided, will only return users matching in this team.
    
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

<details><summary><code>client.ticketing.users.<a href="src/merge/resources/ticketing/resources/users/client.py">retrieve</a>(...)</code></summary>
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
client.ticketing.users.retrieve(
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

**expand:** `typing.Optional[UsersRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Ticketing WebhookReceivers
<details><summary><code>client.ticketing.webhook_receivers.<a href="src/merge/resources/ticketing/resources/webhook_receivers/client.py">list</a>()</code></summary>
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
client.ticketing.webhook_receivers.list()

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

<details><summary><code>client.ticketing.webhook_receivers.<a href="src/merge/resources/ticketing/resources/webhook_receivers/client.py">create</a>(...)</code></summary>
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
client.ticketing.webhook_receivers.create(
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

## Accounting AccountDetails
<details><summary><code>client.accounting.account_details.<a href="src/merge/resources/accounting/resources/account_details/client.py">retrieve</a>()</code></summary>
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
client.accounting.account_details.retrieve()

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

## Accounting AccountToken
<details><summary><code>client.accounting.account_token.<a href="src/merge/resources/accounting/resources/account_token/client.py">retrieve</a>(...)</code></summary>
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
client.accounting.account_token.retrieve(
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

## Accounting AccountingPeriods
<details><summary><code>client.accounting.accounting_periods.<a href="src/merge/resources/accounting/resources/accounting_periods/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `AccountingPeriod` objects.
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
client.accounting.accounting_periods.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.accounting.accounting_periods.<a href="src/merge/resources/accounting/resources/accounting_periods/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `AccountingPeriod` object with the given `id`.
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
client.accounting.accounting_periods.retrieve(
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

## Accounting Accounts
<details><summary><code>client.accounting.accounts.<a href="src/merge/resources/accounting/resources/accounts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Account` objects.
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
client.accounting.accounts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**account_type:** `typing.Optional[str]` — If provided, will only return accounts with the passed in enum.
    
</dd>
</dl>

<dl>
<dd>

**classification:** `typing.Optional[str]` — If provided, will only return accounts with this classification.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — If provided, will only return accounts for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**name:** `typing.Optional[str]` — If provided, will only return Accounts with this name.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[AccountsListRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[AccountsListRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — If provided, will only return accounts with this status.
    
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

<details><summary><code>client.accounting.accounts.<a href="src/merge/resources/accounting/resources/accounts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Account` object with the given values.
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
from merge.resources.accounting import AccountRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.accounts.create(
    model=AccountRequest(),
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

**model:** `AccountRequest` 
    
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

<details><summary><code>client.accounting.accounts.<a href="src/merge/resources/accounting/resources/accounts/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Account` object with the given `id`.
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
client.accounting.accounts.retrieve(
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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[AccountsRetrieveRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[AccountsRetrieveRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.accounting.accounts.<a href="src/merge/resources/accounting/resources/accounts/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Account` POSTs.
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
client.accounting.accounts.meta_post_retrieve()

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

## Accounting Addresses
<details><summary><code>client.accounting.addresses.<a href="src/merge/resources/accounting/resources/addresses/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Address` object with the given `id`.
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
client.accounting.addresses.retrieve(
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

**remote_fields:** `typing.Optional[typing.Literal["type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Accounting AsyncPassthrough
<details><summary><code>client.accounting.async_passthrough.<a href="src/merge/resources/accounting/resources/async_passthrough/client.py">create</a>(...)</code></summary>
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
from merge.resources.accounting import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.async_passthrough.create(
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

<details><summary><code>client.accounting.async_passthrough.<a href="src/merge/resources/accounting/resources/async_passthrough/client.py">retrieve</a>(...)</code></summary>
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
client.accounting.async_passthrough.retrieve(
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

## Accounting AsyncTasks
<details><summary><code>client.accounting.async_tasks.<a href="src/merge/resources/accounting/resources/async_tasks/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `AsyncPostTask` object with the given `id`.
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
client.accounting.async_tasks.retrieve(
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

## Accounting Attachments
<details><summary><code>client.accounting.attachments.<a href="src/merge/resources/accounting/resources/attachments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `AccountingAttachment` objects.
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
client.accounting.attachments.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return accounting attachments for this company.
    
</dd>
</dl>

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

<details><summary><code>client.accounting.attachments.<a href="src/merge/resources/accounting/resources/attachments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `AccountingAttachment` object with the given values.
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
from merge.resources.accounting import AccountingAttachmentRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.attachments.create(
    model=AccountingAttachmentRequest(),
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

**model:** `AccountingAttachmentRequest` 
    
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

<details><summary><code>client.accounting.attachments.<a href="src/merge/resources/accounting/resources/attachments/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `AccountingAttachment` object with the given `id`.
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
client.accounting.attachments.retrieve(
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

<details><summary><code>client.accounting.attachments.<a href="src/merge/resources/accounting/resources/attachments/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `AccountingAttachment` POSTs.
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
client.accounting.attachments.meta_post_retrieve()

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

## Accounting AuditTrail
<details><summary><code>client.accounting.audit_trail.<a href="src/merge/resources/accounting/resources/audit_trail/client.py">list</a>(...)</code></summary>
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
client.accounting.audit_trail.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

## Accounting AvailableActions
<details><summary><code>client.accounting.available_actions.<a href="src/merge/resources/accounting/resources/available_actions/client.py">retrieve</a>()</code></summary>
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
client.accounting.available_actions.retrieve()

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

## Accounting BalanceSheets
<details><summary><code>client.accounting.balance_sheets.<a href="src/merge/resources/accounting/resources/balance_sheets/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `BalanceSheet` objects.
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
client.accounting.balance_sheets.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return balance sheets for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.accounting.balance_sheets.<a href="src/merge/resources/accounting/resources/balance_sheets/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `BalanceSheet` object with the given `id`.
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
client.accounting.balance_sheets.retrieve(
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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Accounting BankFeedAccounts
<details><summary><code>client.accounting.bank_feed_accounts.<a href="src/merge/resources/accounting/resources/bank_feed_accounts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `BankFeedAccount` objects.
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
client.accounting.bank_feed_accounts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.accounting.bank_feed_accounts.<a href="src/merge/resources/accounting/resources/bank_feed_accounts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `BankFeedAccount` object with the given values.
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
from merge.resources.accounting import BankFeedAccountRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.bank_feed_accounts.create(
    model=BankFeedAccountRequest(),
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

**model:** `BankFeedAccountRequest` 
    
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

<details><summary><code>client.accounting.bank_feed_accounts.<a href="src/merge/resources/accounting/resources/bank_feed_accounts/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `BankFeedAccount` object with the given `id`.
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
client.accounting.bank_feed_accounts.retrieve(
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

<details><summary><code>client.accounting.bank_feed_accounts.<a href="src/merge/resources/accounting/resources/bank_feed_accounts/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `BankFeedAccount` POSTs.
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
client.accounting.bank_feed_accounts.meta_post_retrieve()

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

## Accounting BankFeedTransactions
<details><summary><code>client.accounting.bank_feed_transactions.<a href="src/merge/resources/accounting/resources/bank_feed_transactions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `BankFeedTransaction` objects.
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
client.accounting.bank_feed_transactions.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[typing.Literal["bank_feed_account"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**is_processed:** `typing.Optional[bool]` — If provided, will only return bank feed transactions with this is_processed value
    
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

<details><summary><code>client.accounting.bank_feed_transactions.<a href="src/merge/resources/accounting/resources/bank_feed_transactions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `BankFeedTransaction` object with the given values.
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
from merge.resources.accounting import BankFeedTransactionRequestRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.bank_feed_transactions.create(
    model=BankFeedTransactionRequestRequest(),
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

**model:** `BankFeedTransactionRequestRequest` 
    
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

<details><summary><code>client.accounting.bank_feed_transactions.<a href="src/merge/resources/accounting/resources/bank_feed_transactions/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `BankFeedTransaction` object with the given `id`.
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
client.accounting.bank_feed_transactions.retrieve(
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

**expand:** `typing.Optional[typing.Literal["bank_feed_account"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.accounting.bank_feed_transactions.<a href="src/merge/resources/accounting/resources/bank_feed_transactions/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `BankFeedTransaction` POSTs.
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
client.accounting.bank_feed_transactions.meta_post_retrieve()

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

## Accounting CashFlowStatements
<details><summary><code>client.accounting.cash_flow_statements.<a href="src/merge/resources/accounting/resources/cash_flow_statements/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `CashFlowStatement` objects.
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
client.accounting.cash_flow_statements.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return cash flow statements for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.accounting.cash_flow_statements.<a href="src/merge/resources/accounting/resources/cash_flow_statements/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `CashFlowStatement` object with the given `id`.
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
client.accounting.cash_flow_statements.retrieve(
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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Accounting CompanyInfo
<details><summary><code>client.accounting.company_info.<a href="src/merge/resources/accounting/resources/company_info/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `CompanyInfo` objects.
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
client.accounting.company_info.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expand:** `typing.Optional[CompanyInfoListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.accounting.company_info.<a href="src/merge/resources/accounting/resources/company_info/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `CompanyInfo` object with the given `id`.
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
client.accounting.company_info.retrieve(
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

**expand:** `typing.Optional[CompanyInfoRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Accounting Contacts
<details><summary><code>client.accounting.contacts.<a href="src/merge/resources/accounting/resources/contacts/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Contact` objects.
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
client.accounting.contacts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return contacts for this company.
    
</dd>
</dl>

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

**email_address:** `typing.Optional[str]` — If provided, will only return Contacts that match this email.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[ContactsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**is_customer:** `typing.Optional[str]` — If provided, will only return Contacts that are denoted as customers.
    
</dd>
</dl>

<dl>
<dd>

**is_supplier:** `typing.Optional[str]` — If provided, will only return Contacts that are denoted as suppliers.
    
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

**name:** `typing.Optional[str]` — If provided, will only return Contacts that match this name.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — If provided, will only return Contacts that match this status.
    
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

<details><summary><code>client.accounting.contacts.<a href="src/merge/resources/accounting/resources/contacts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Contact` object with the given values.
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
from merge.resources.accounting import ContactRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.contacts.create(
    model=ContactRequest(),
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

**model:** `ContactRequest` 
    
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

<details><summary><code>client.accounting.contacts.<a href="src/merge/resources/accounting/resources/contacts/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Contact` object with the given `id`.
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
client.accounting.contacts.retrieve(
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

**expand:** `typing.Optional[ContactsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.accounting.contacts.<a href="src/merge/resources/accounting/resources/contacts/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Contact` POSTs.
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
client.accounting.contacts.meta_post_retrieve()

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

<details><summary><code>client.accounting.contacts.<a href="src/merge/resources/accounting/resources/contacts/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.contacts.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Accounting CreditNotes
<details><summary><code>client.accounting.credit_notes.<a href="src/merge/resources/accounting/resources/credit_notes/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `CreditNote` objects.
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
client.accounting.credit_notes.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return credit notes for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[CreditNotesListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[CreditNotesListRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[CreditNotesListRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**transaction_date_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**transaction_date_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
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

<details><summary><code>client.accounting.credit_notes.<a href="src/merge/resources/accounting/resources/credit_notes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `CreditNote` object with the given values.
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
from merge.resources.accounting import CreditNoteRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.credit_notes.create(
    model=CreditNoteRequest(),
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

**model:** `CreditNoteRequest` 
    
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

<details><summary><code>client.accounting.credit_notes.<a href="src/merge/resources/accounting/resources/credit_notes/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `CreditNote` object with the given `id`.
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
client.accounting.credit_notes.retrieve(
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

**expand:** `typing.Optional[CreditNotesRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[CreditNotesRetrieveRequestRemoteFields]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[CreditNotesRetrieveRequestShowEnumOrigins]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.accounting.credit_notes.<a href="src/merge/resources/accounting/resources/credit_notes/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `CreditNote` POSTs.
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
client.accounting.credit_notes.meta_post_retrieve()

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

## Accounting Scopes
<details><summary><code>client.accounting.scopes.<a href="src/merge/resources/accounting/resources/scopes/client.py">default_scopes_retrieve</a>()</code></summary>
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
client.accounting.scopes.default_scopes_retrieve()

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

<details><summary><code>client.accounting.scopes.<a href="src/merge/resources/accounting/resources/scopes/client.py">linked_account_scopes_retrieve</a>()</code></summary>
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
client.accounting.scopes.linked_account_scopes_retrieve()

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

<details><summary><code>client.accounting.scopes.<a href="src/merge/resources/accounting/resources/scopes/client.py">linked_account_scopes_create</a>(...)</code></summary>
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
from merge.resources.accounting import (
    FieldPermissionDeserializerRequest,
    IndividualCommonModelScopeDeserializerRequest,
    ModelPermissionDeserializerRequest,
)

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.scopes.linked_account_scopes_create(
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

## Accounting DeleteAccount
<details><summary><code>client.accounting.delete_account.<a href="src/merge/resources/accounting/resources/delete_account/client.py">delete</a>()</code></summary>
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
client.accounting.delete_account.delete()

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

## Accounting Employees
<details><summary><code>client.accounting.employees.<a href="src/merge/resources/accounting/resources/employees/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Employee` objects.
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
client.accounting.employees.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return employees for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.accounting.employees.<a href="src/merge/resources/accounting/resources/employees/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Employee` object with the given `id`.
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
client.accounting.employees.retrieve(
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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Accounting ExpenseReports
<details><summary><code>client.accounting.expense_reports.<a href="src/merge/resources/accounting/resources/expense_reports/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `ExpenseReport` objects.
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
client.accounting.expense_reports.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return expense reports for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[ExpenseReportsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.accounting.expense_reports.<a href="src/merge/resources/accounting/resources/expense_reports/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `ExpenseReport` object with the given values.
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
from merge.resources.accounting import ExpenseReportRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.expense_reports.create(
    model=ExpenseReportRequest(
        tracking_categories=[
            "a1b2c3d4-e5f6-4a5b-9c3d-2e1f0a9b8c7d",
            "d4c3b2a1-9e8f-7g6h-5i4j-3k2l1m0n9o8p",
        ],
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

**model:** `ExpenseReportRequest` 
    
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

<details><summary><code>client.accounting.expense_reports.<a href="src/merge/resources/accounting/resources/expense_reports/client.py">lines_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `ExpenseReportLine` objects that point to a `ExpenseReport` with the given id.
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
client.accounting.expense_reports.lines_list(
    expense_report_id="expense_report_id",
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**expense_report_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[ExpenseReportsLinesListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
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

<details><summary><code>client.accounting.expense_reports.<a href="src/merge/resources/accounting/resources/expense_reports/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `ExpenseReport` object with the given `id`.
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
client.accounting.expense_reports.retrieve(
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

**expand:** `typing.Optional[ExpenseReportsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.accounting.expense_reports.<a href="src/merge/resources/accounting/resources/expense_reports/client.py">lines_remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.expense_reports.lines_remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

<details><summary><code>client.accounting.expense_reports.<a href="src/merge/resources/accounting/resources/expense_reports/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `ExpenseReport` POSTs.
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
client.accounting.expense_reports.meta_post_retrieve()

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

<details><summary><code>client.accounting.expense_reports.<a href="src/merge/resources/accounting/resources/expense_reports/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.expense_reports.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Accounting Expenses
<details><summary><code>client.accounting.expenses.<a href="src/merge/resources/accounting/resources/expenses/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Expense` objects.
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
client.accounting.expenses.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return expenses for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[ExpensesListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

**transaction_date_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**transaction_date_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
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

<details><summary><code>client.accounting.expenses.<a href="src/merge/resources/accounting/resources/expenses/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Expense` object with the given values.
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
from merge.resources.accounting import ExpenseRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.expenses.create(
    model=ExpenseRequest(),
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

**model:** `ExpenseRequest` 
    
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

<details><summary><code>client.accounting.expenses.<a href="src/merge/resources/accounting/resources/expenses/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Expense` object with the given `id`.
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
client.accounting.expenses.retrieve(
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

**expand:** `typing.Optional[ExpensesRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.accounting.expenses.<a href="src/merge/resources/accounting/resources/expenses/client.py">lines_remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.expenses.lines_remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

<details><summary><code>client.accounting.expenses.<a href="src/merge/resources/accounting/resources/expenses/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Expense` POSTs.
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
client.accounting.expenses.meta_post_retrieve()

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

<details><summary><code>client.accounting.expenses.<a href="src/merge/resources/accounting/resources/expenses/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.expenses.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Accounting FieldMapping
<details><summary><code>client.accounting.field_mapping.<a href="src/merge/resources/accounting/resources/field_mapping/client.py">field_mappings_retrieve</a>(...)</code></summary>
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
client.accounting.field_mapping.field_mappings_retrieve()

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

<details><summary><code>client.accounting.field_mapping.<a href="src/merge/resources/accounting/resources/field_mapping/client.py">field_mappings_create</a>(...)</code></summary>
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
client.accounting.field_mapping.field_mappings_create(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.field_mapping.<a href="src/merge/resources/accounting/resources/field_mapping/client.py">field_mappings_destroy</a>(...)</code></summary>
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
client.accounting.field_mapping.field_mappings_destroy(
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

<details><summary><code>client.accounting.field_mapping.<a href="src/merge/resources/accounting/resources/field_mapping/client.py">field_mappings_partial_update</a>(...)</code></summary>
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
client.accounting.field_mapping.field_mappings_partial_update(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.field_mapping.<a href="src/merge/resources/accounting/resources/field_mapping/client.py">remote_fields_retrieve</a>(...)</code></summary>
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
client.accounting.field_mapping.remote_fields_retrieve()

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

<details><summary><code>client.accounting.field_mapping.<a href="src/merge/resources/accounting/resources/field_mapping/client.py">target_fields_retrieve</a>()</code></summary>
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
client.accounting.field_mapping.target_fields_retrieve()

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

## Accounting GeneralLedgerTransactions
<details><summary><code>client.accounting.general_ledger_transactions.<a href="src/merge/resources/accounting/resources/general_ledger_transactions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `GeneralLedgerTransaction` objects.
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
client.accounting.general_ledger_transactions.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return general ledger transactions for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[GeneralLedgerTransactionsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**posted_date_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects posted after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**posted_date_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects posted before this datetime.
    
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

<details><summary><code>client.accounting.general_ledger_transactions.<a href="src/merge/resources/accounting/resources/general_ledger_transactions/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `GeneralLedgerTransaction` object with the given `id`.
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
client.accounting.general_ledger_transactions.retrieve(
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

**expand:** `typing.Optional[GeneralLedgerTransactionsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Accounting GenerateKey
<details><summary><code>client.accounting.generate_key.<a href="src/merge/resources/accounting/resources/generate_key/client.py">create</a>(...)</code></summary>
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
client.accounting.generate_key.create(
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

## Accounting IncomeStatements
<details><summary><code>client.accounting.income_statements.<a href="src/merge/resources/accounting/resources/income_statements/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `IncomeStatement` objects.
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
client.accounting.income_statements.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return income statements for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.accounting.income_statements.<a href="src/merge/resources/accounting/resources/income_statements/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `IncomeStatement` object with the given `id`.
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
client.accounting.income_statements.retrieve(
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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Accounting Invoices
<details><summary><code>client.accounting.invoices.<a href="src/merge/resources/accounting/resources/invoices/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Invoice` objects.
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
client.accounting.invoices.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return invoices for this company.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — If provided, will only return invoices for this contact.
    
</dd>
</dl>

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

**expand:** `typing.Optional[InvoicesListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**issue_date_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**issue_date_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
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

**number:** `typing.Optional[str]` — If provided, will only return Invoices with this number.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[InvoicesListRequestStatus]` 

If provided, will only return Invoices with this status.

* `PAID` - PAID
* `DRAFT` - DRAFT
* `SUBMITTED` - SUBMITTED
* `PARTIALLY_PAID` - PARTIALLY_PAID
* `OPEN` - OPEN
* `VOID` - VOID
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[InvoicesListRequestType]` 

If provided, will only return Invoices with this type.

* `ACCOUNTS_RECEIVABLE` - ACCOUNTS_RECEIVABLE
* `ACCOUNTS_PAYABLE` - ACCOUNTS_PAYABLE
    
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

<details><summary><code>client.accounting.invoices.<a href="src/merge/resources/accounting/resources/invoices/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Invoice` object with the given values.
            Including a `PurchaseOrder` id in the `purchase_orders` property will generate an Accounts Payable Invoice from the specified Purchase Order(s).
            
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
from merge.resources.accounting import InvoiceRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.invoices.create(
    model=InvoiceRequest(),
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

**model:** `InvoiceRequest` 
    
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

<details><summary><code>client.accounting.invoices.<a href="src/merge/resources/accounting/resources/invoices/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Invoice` object with the given `id`.
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
client.accounting.invoices.retrieve(
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

**expand:** `typing.Optional[InvoicesRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["type"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["type"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.accounting.invoices.<a href="src/merge/resources/accounting/resources/invoices/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an `Invoice` object with the given `id`.
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
from merge.resources.accounting import InvoiceRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.invoices.partial_update(
    id="id",
    model=InvoiceRequest(),
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

**model:** `InvoiceRequest` 
    
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

<details><summary><code>client.accounting.invoices.<a href="src/merge/resources/accounting/resources/invoices/client.py">line_items_remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.invoices.line_items_remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

<details><summary><code>client.accounting.invoices.<a href="src/merge/resources/accounting/resources/invoices/client.py">meta_patch_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Invoice` PATCHs.
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
client.accounting.invoices.meta_patch_retrieve(
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

<details><summary><code>client.accounting.invoices.<a href="src/merge/resources/accounting/resources/invoices/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Invoice` POSTs.
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
client.accounting.invoices.meta_post_retrieve()

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

<details><summary><code>client.accounting.invoices.<a href="src/merge/resources/accounting/resources/invoices/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.invoices.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Accounting Issues
<details><summary><code>client.accounting.issues.<a href="src/merge/resources/accounting/resources/issues/client.py">list</a>(...)</code></summary>
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
from merge import Merge

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.issues.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

<details><summary><code>client.accounting.issues.<a href="src/merge/resources/accounting/resources/issues/client.py">retrieve</a>(...)</code></summary>
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
client.accounting.issues.retrieve(
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

## Accounting Items
<details><summary><code>client.accounting.items.<a href="src/merge/resources/accounting/resources/items/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Item` objects.
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
client.accounting.items.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return items for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[ItemsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.accounting.items.<a href="src/merge/resources/accounting/resources/items/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an `Item` object with the given values.
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
from merge.resources.accounting import ItemRequestRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.items.create(
    model=ItemRequestRequest(),
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

**model:** `ItemRequestRequest` 
    
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

<details><summary><code>client.accounting.items.<a href="src/merge/resources/accounting/resources/items/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `Item` object with the given `id`.
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
client.accounting.items.retrieve(
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

**expand:** `typing.Optional[ItemsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.accounting.items.<a href="src/merge/resources/accounting/resources/items/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an `Item` object with the given `id`.
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
from merge.resources.accounting import PatchedItemRequestRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.items.partial_update(
    id="id",
    model=PatchedItemRequestRequest(),
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

**model:** `PatchedItemRequestRequest` 
    
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

<details><summary><code>client.accounting.items.<a href="src/merge/resources/accounting/resources/items/client.py">meta_patch_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Item` PATCHs.
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
client.accounting.items.meta_patch_retrieve(
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

<details><summary><code>client.accounting.items.<a href="src/merge/resources/accounting/resources/items/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Item` POSTs.
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
client.accounting.items.meta_post_retrieve()

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

## Accounting JournalEntries
<details><summary><code>client.accounting.journal_entries.<a href="src/merge/resources/accounting/resources/journal_entries/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `JournalEntry` objects.
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
client.accounting.journal_entries.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return journal entries for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[JournalEntriesListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

**transaction_date_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**transaction_date_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
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

<details><summary><code>client.accounting.journal_entries.<a href="src/merge/resources/accounting/resources/journal_entries/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `JournalEntry` object with the given values.
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
from merge.resources.accounting import JournalEntryRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.journal_entries.create(
    model=JournalEntryRequest(),
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

**model:** `JournalEntryRequest` 
    
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

<details><summary><code>client.accounting.journal_entries.<a href="src/merge/resources/accounting/resources/journal_entries/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `JournalEntry` object with the given `id`.
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
client.accounting.journal_entries.retrieve(
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

**expand:** `typing.Optional[JournalEntriesRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.accounting.journal_entries.<a href="src/merge/resources/accounting/resources/journal_entries/client.py">lines_remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.journal_entries.lines_remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

<details><summary><code>client.accounting.journal_entries.<a href="src/merge/resources/accounting/resources/journal_entries/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `JournalEntry` POSTs.
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
client.accounting.journal_entries.meta_post_retrieve()

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

<details><summary><code>client.accounting.journal_entries.<a href="src/merge/resources/accounting/resources/journal_entries/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.journal_entries.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Accounting LinkToken
<details><summary><code>client.accounting.link_token.<a href="src/merge/resources/accounting/resources/link_token/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a link token to be used when linking a new end user.
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
from merge.resources.accounting import CategoriesEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.link_token.create(
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

## Accounting LinkedAccounts
<details><summary><code>client.accounting.linked_accounts.<a href="src/merge/resources/accounting/resources/linked_accounts/client.py">list</a>(...)</code></summary>
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

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.linked_accounts.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
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

## Accounting Passthrough
<details><summary><code>client.accounting.passthrough.<a href="src/merge/resources/accounting/resources/passthrough/client.py">create</a>(...)</code></summary>
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
from merge.resources.accounting import DataPassthroughRequest, MethodEnum

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.passthrough.create(
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

## Accounting PaymentMethods
<details><summary><code>client.accounting.payment_methods.<a href="src/merge/resources/accounting/resources/payment_methods/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `PaymentMethod` objects.
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
client.accounting.payment_methods.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

<details><summary><code>client.accounting.payment_methods.<a href="src/merge/resources/accounting/resources/payment_methods/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `PaymentMethod` object with the given `id`.
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
client.accounting.payment_methods.retrieve(
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

## Accounting PaymentTerms
<details><summary><code>client.accounting.payment_terms.<a href="src/merge/resources/accounting/resources/payment_terms/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `PaymentTerm` objects.
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
client.accounting.payment_terms.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
</dd>
</dl>

<dl>
<dd>

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.accounting.payment_terms.<a href="src/merge/resources/accounting/resources/payment_terms/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `PaymentTerm` object with the given `id`.
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
client.accounting.payment_terms.retrieve(
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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Accounting Payments
<details><summary><code>client.accounting.payments.<a href="src/merge/resources/accounting/resources/payments/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Payment` objects.
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
client.accounting.payments.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**account_id:** `typing.Optional[str]` — If provided, will only return payments for this account.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — If provided, will only return payments for this company.
    
</dd>
</dl>

<dl>
<dd>

**contact_id:** `typing.Optional[str]` — If provided, will only return payments for this contact.
    
</dd>
</dl>

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

**expand:** `typing.Optional[PaymentsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

**transaction_date_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**transaction_date_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
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

<details><summary><code>client.accounting.payments.<a href="src/merge/resources/accounting/resources/payments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `Payment` object with the given values.
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
from merge.resources.accounting import PaymentRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.payments.create(
    model=PaymentRequest(),
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

**model:** `PaymentRequest` 
    
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

<details><summary><code>client.accounting.payments.<a href="src/merge/resources/accounting/resources/payments/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Payment` object with the given `id`.
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
client.accounting.payments.retrieve(
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

**expand:** `typing.Optional[PaymentsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
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

<details><summary><code>client.accounting.payments.<a href="src/merge/resources/accounting/resources/payments/client.py">partial_update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a `Payment` object with the given `id`.
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
from merge.resources.accounting import PatchedPaymentRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.payments.partial_update(
    id="id",
    model=PatchedPaymentRequest(),
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

**model:** `PatchedPaymentRequest` 
    
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

<details><summary><code>client.accounting.payments.<a href="src/merge/resources/accounting/resources/payments/client.py">line_items_remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.payments.line_items_remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

<details><summary><code>client.accounting.payments.<a href="src/merge/resources/accounting/resources/payments/client.py">meta_patch_retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Payment` PATCHs.
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
client.accounting.payments.meta_patch_retrieve(
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

<details><summary><code>client.accounting.payments.<a href="src/merge/resources/accounting/resources/payments/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `Payment` POSTs.
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
client.accounting.payments.meta_post_retrieve()

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

<details><summary><code>client.accounting.payments.<a href="src/merge/resources/accounting/resources/payments/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.payments.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Accounting PhoneNumbers
<details><summary><code>client.accounting.phone_numbers.<a href="src/merge/resources/accounting/resources/phone_numbers/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an `AccountingPhoneNumber` object with the given `id`.
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
client.accounting.phone_numbers.retrieve(
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

## Accounting Projects
<details><summary><code>client.accounting.projects.<a href="src/merge/resources/accounting/resources/projects/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Project` objects.
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
client.accounting.projects.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return projects for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[ProjectsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.accounting.projects.<a href="src/merge/resources/accounting/resources/projects/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Project` object with the given `id`.
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
client.accounting.projects.retrieve(
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

**expand:** `typing.Optional[ProjectsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Accounting PurchaseOrders
<details><summary><code>client.accounting.purchase_orders.<a href="src/merge/resources/accounting/resources/purchase_orders/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `PurchaseOrder` objects.
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
client.accounting.purchase_orders.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return purchase orders for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[PurchaseOrdersListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**issue_date_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**issue_date_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
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

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.accounting.purchase_orders.<a href="src/merge/resources/accounting/resources/purchase_orders/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `PurchaseOrder` object with the given values.
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
from merge.resources.accounting import PurchaseOrderRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.purchase_orders.create(
    model=PurchaseOrderRequest(),
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

**model:** `PurchaseOrderRequest` 
    
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

<details><summary><code>client.accounting.purchase_orders.<a href="src/merge/resources/accounting/resources/purchase_orders/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `PurchaseOrder` object with the given `id`.
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
client.accounting.purchase_orders.retrieve(
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

**expand:** `typing.Optional[PurchaseOrdersRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_data:** `typing.Optional[bool]` — Whether to include the original data Merge fetched from the third-party to produce these models.
    
</dd>
</dl>

<dl>
<dd>

**include_remote_fields:** `typing.Optional[bool]` — Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.
    
</dd>
</dl>

<dl>
<dd>

**include_shell_data:** `typing.Optional[bool]` — Whether to include shell records. Shell records are empty records (they may contain some metadata but all other fields are null).
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

<details><summary><code>client.accounting.purchase_orders.<a href="src/merge/resources/accounting/resources/purchase_orders/client.py">line_items_remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.purchase_orders.line_items_remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

<details><summary><code>client.accounting.purchase_orders.<a href="src/merge/resources/accounting/resources/purchase_orders/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `PurchaseOrder` POSTs.
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
client.accounting.purchase_orders.meta_post_retrieve()

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

<details><summary><code>client.accounting.purchase_orders.<a href="src/merge/resources/accounting/resources/purchase_orders/client.py">remote_field_classes_list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `RemoteFieldClass` objects.
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
client.accounting.purchase_orders.remote_field_classes_list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**is_common_model_field:** `typing.Optional[bool]` — If provided, will only return remote field classes with this is_common_model_field value
    
</dd>
</dl>

<dl>
<dd>

**is_custom:** `typing.Optional[bool]` — If provided, will only return remote fields classes with this is_custom value
    
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

## Accounting RegenerateKey
<details><summary><code>client.accounting.regenerate_key.<a href="src/merge/resources/accounting/resources/regenerate_key/client.py">create</a>(...)</code></summary>
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
client.accounting.regenerate_key.create(
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

## Accounting SyncStatus
<details><summary><code>client.accounting.sync_status.<a href="src/merge/resources/accounting/resources/sync_status/client.py">list</a>(...)</code></summary>
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
client.accounting.sync_status.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**cursor:** `typing.Optional[str]` — The pagination cursor value.
    
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

## Accounting ForceResync
<details><summary><code>client.accounting.force_resync.<a href="src/merge/resources/accounting/resources/force_resync/client.py">sync_status_resync_create</a>()</code></summary>
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
client.accounting.force_resync.sync_status_resync_create()

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

## Accounting TaxRates
<details><summary><code>client.accounting.tax_rates.<a href="src/merge/resources/accounting/resources/tax_rates/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `TaxRate` objects.
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
client.accounting.tax_rates.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return tax rates for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**name:** `typing.Optional[str]` — If provided, will only return TaxRates with this name.
    
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

<details><summary><code>client.accounting.tax_rates.<a href="src/merge/resources/accounting/resources/tax_rates/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `TaxRate` object with the given `id`.
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
client.accounting.tax_rates.retrieve(
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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Accounting TrackingCategories
<details><summary><code>client.accounting.tracking_categories.<a href="src/merge/resources/accounting/resources/tracking_categories/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `TrackingCategory` objects.
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
client.accounting.tracking_categories.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**category_type:** `typing.Optional[str]` — If provided, will only return tracking categories with this type.
    
</dd>
</dl>

<dl>
<dd>

**company_id:** `typing.Optional[str]` — If provided, will only return tracking categories for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**name:** `typing.Optional[str]` — If provided, will only return tracking categories with this name.
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of results to return per page.
    
</dd>
</dl>

<dl>
<dd>

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**remote_id:** `typing.Optional[str]` — The API provider's ID for the given object.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — If provided, will only return tracking categories with this status.
    
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

<details><summary><code>client.accounting.tracking_categories.<a href="src/merge/resources/accounting/resources/tracking_categories/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `TrackingCategory` object with the given `id`.
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
client.accounting.tracking_categories.retrieve(
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

**expand:** `typing.Optional[typing.Literal["company"]]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**remote_fields:** `typing.Optional[typing.Literal["status"]]` — Deprecated. Use show_enum_origins.
    
</dd>
</dl>

<dl>
<dd>

**show_enum_origins:** `typing.Optional[typing.Literal["status"]]` — A comma separated list of enum field names for which you'd like the original values to be returned, instead of Merge's normalized enum values. [Learn more](https://help.merge.dev/en/articles/8950958-show_enum_origins-query-parameter)
    
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

## Accounting Transactions
<details><summary><code>client.accounting.transactions.<a href="src/merge/resources/accounting/resources/transactions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `Transaction` objects.
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
client.accounting.transactions.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return accounting transactions for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[TransactionsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**transaction_date_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**transaction_date_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
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

<details><summary><code>client.accounting.transactions.<a href="src/merge/resources/accounting/resources/transactions/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `Transaction` object with the given `id`.
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
client.accounting.transactions.retrieve(
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

**expand:** `typing.Optional[TransactionsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

## Accounting VendorCredits
<details><summary><code>client.accounting.vendor_credits.<a href="src/merge/resources/accounting/resources/vendor_credits/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of `VendorCredit` objects.
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
client.accounting.vendor_credits.list(
    cursor="cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw",
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

**company_id:** `typing.Optional[str]` — If provided, will only return vendor credits for this company.
    
</dd>
</dl>

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

**expand:** `typing.Optional[VendorCreditsListRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

**transaction_date_after:** `typing.Optional[dt.datetime]` — If provided, will only return objects created after this datetime.
    
</dd>
</dl>

<dl>
<dd>

**transaction_date_before:** `typing.Optional[dt.datetime]` — If provided, will only return objects created before this datetime.
    
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

<details><summary><code>client.accounting.vendor_credits.<a href="src/merge/resources/accounting/resources/vendor_credits/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a `VendorCredit` object with the given values.
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
from merge.resources.accounting import VendorCreditRequest

client = Merge(
    account_token="YOUR_ACCOUNT_TOKEN",
    api_key="YOUR_API_KEY",
)
client.accounting.vendor_credits.create(
    model=VendorCreditRequest(),
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

**model:** `VendorCreditRequest` 
    
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

<details><summary><code>client.accounting.vendor_credits.<a href="src/merge/resources/accounting/resources/vendor_credits/client.py">retrieve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a `VendorCredit` object with the given `id`.
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
client.accounting.vendor_credits.retrieve(
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

**expand:** `typing.Optional[VendorCreditsRetrieveRequestExpand]` — Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.
    
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

<details><summary><code>client.accounting.vendor_credits.<a href="src/merge/resources/accounting/resources/vendor_credits/client.py">meta_post_retrieve</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns metadata for `VendorCredit` POSTs.
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
client.accounting.vendor_credits.meta_post_retrieve()

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

## Accounting WebhookReceivers
<details><summary><code>client.accounting.webhook_receivers.<a href="src/merge/resources/accounting/resources/webhook_receivers/client.py">list</a>()</code></summary>
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
client.accounting.webhook_receivers.list()

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

<details><summary><code>client.accounting.webhook_receivers.<a href="src/merge/resources/accounting/resources/webhook_receivers/client.py">create</a>(...)</code></summary>
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
client.accounting.webhook_receivers.create(
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

