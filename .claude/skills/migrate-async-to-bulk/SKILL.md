---
name: migrate-async-to-bulk
description: Migrate customer code from using async POST (run_async=True) to the new bulk writes API. Use when a customer needs to move from individual async create calls to batched bulk_create/bulk_retrieve. Also handles upgrading from older MergePythonClient versions to 4.0.0.
---

# Migrate Async Posts to Bulk Writes

Migrate customer code from the async POST pattern (individual `create(run_async=True)` calls with `async_tasks.retrieve` polling) to the new bulk writes API (`bulk_create` / `bulk_retrieve`), while upgrading to MergePythonClient v4.0.0.

If the user provides file paths or code, use $ARGUMENTS to locate the code to migrate.

## Background

### Old Pattern (Async Posts)
Customers using async posts typically:
1. Loop through items calling `client.{category}.{resource}.create(model=..., run_async=True)` one at a time
2. Store the returned task/response IDs
3. Poll `client.{category}.async_tasks.retrieve(id=task_id)` for each item
4. Check `AsyncPostTaskStatusEnum.COMPLETED` or `FAILURE` for results

### New Pattern (Bulk Writes)
The bulk writes API:
1. Batches up to 100 items into a single `bulk_create(batch_items=[...])` call
2. Returns a `batch_id` immediately (HTTP 202)
3. Polls `bulk_retrieve(batch_id)` for the entire batch status
4. Each item in the batch has its own `item_id` for correlation and individual status tracking

## Step-by-Step Migration Instructions

### 1. Update the SDK version
Find the customer's dependency file (`requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile`, etc.) and update:
```
# Old
MergePythonClient==2.x.x  # or any version < 4.0.0

# New
MergePythonClient==4.0.0
```

### 2. Update imports
Add the new bulk write types to the customer's imports:
```python
# Add these imports
from merge.resources.accounting import (
    BulkWriteBatchItem,
    BulkWriteBatchResponse,
    BulkWriteBatchResult,
    BulkWriteBatchStatusEnum,
    BulkWriteObjectResult,
    BulkWriteObjectStatusEnum,
)
```

Replace the category (`accounting`) with whatever category the customer is using (e.g., `ats`, `hris`, `crm`, `ticketing`, `filestorage`).

Remove old async task imports if they are no longer needed:
```python
# Remove if no longer used
from merge.resources.accounting import AsyncPostTask, AsyncPostTaskStatusEnum
```

### 3. Identify the async POST pattern
Look for code that matches these patterns:

**Pattern A: Loop with run_async=True**
```python
# OLD
results = []
for item_data in items:
    response = client.accounting.invoices.create(
        model=InvoiceRequest(**item_data),
        run_async=True,
    )
    results.append(response)
```

**Pattern B: Async task polling**
```python
# OLD
task = client.accounting.async_tasks.retrieve(id=task_id)
if task.status == AsyncPostTaskStatusEnum.COMPLETED:
    # handle success
elif task.status == AsyncPostTaskStatusEnum.FAILURE:
    # handle failure
```

### 4. Convert to bulk writes

**Replace the creation loop with batched bulk_create calls:**
```python
# NEW
from merge.resources.accounting import BulkWriteBatchItem

MAX_BATCH_SIZE = 100

# Group items into batches of 100
batch_ids = []
for i in range(0, len(items), MAX_BATCH_SIZE):
    chunk = items[i:i + MAX_BATCH_SIZE]
    batch_items = [
        BulkWriteBatchItem(
            item_id=f"item-{i + j}",  # unique ID for correlation
            model={
                # Map fields from the old InvoiceRequest (or other model) to a dict.
                # The keys should match the common model field names.
                "type": item_data.get("type"),
                "contact": item_data.get("contact"),
                "number": item_data.get("number"),
                "issue_date": item_data.get("issue_date"),
                "due_date": item_data.get("due_date"),
                "line_items": item_data.get("line_items"),
                # ... include all relevant fields
            },
        )
        for j, item_data in enumerate(chunk)
    ]

    response = client.accounting.invoices.bulk_create(
        batch_items=batch_items,
    )
    batch_ids.append(response.batch_id)
```

**Replace the polling loop with bulk_retrieve:**
```python
# NEW
import time

TERMINAL_STATUSES = {
    BulkWriteBatchStatusEnum.SUCCESS,
    BulkWriteBatchStatusEnum.FAILED,
    BulkWriteBatchStatusEnum.PARTIAL_SUCCESS,
}

for batch_id in batch_ids:
    while True:
        result = client.accounting.invoices.bulk_retrieve(batch_id=batch_id)

        if result.status in TERMINAL_STATUSES:
            # Process results
            for obj in result.objects:
                if obj.status == BulkWriteObjectStatusEnum.SUCCESS:
                    # obj.response contains the created object ID
                    # e.g., obj.response["invoice_id"]
                    print(f"Item {obj.item_id} created: {obj.response}")
                elif obj.status == BulkWriteObjectStatusEnum.FAILED:
                    # obj.response contains {"errors": [...], "warnings": [...]}
                    print(f"Item {obj.item_id} failed: {obj.response}")
            break

        time.sleep(2)  # Poll every 2 seconds
```

### 5. Handle the model data conversion

When converting from typed request models (e.g., `InvoiceRequest`) to the bulk write dict format:

- The `model` field in `BulkWriteBatchItem` is a dictionary, not a typed Pydantic model
- Keys should match the common model field names (snake_case)
- Nested objects (like line items) should also be dictionaries
- The field names are the same as the Pydantic model field names

**Example conversion:**
```python
# OLD: Using typed model
from merge.resources.accounting import InvoiceRequest, InvoiceLineItemRequest

invoice = InvoiceRequest(
    type="ACCOUNTS_RECEIVABLE",
    contact="contact-uuid",
    number="INV-001",
    issue_date="2024-01-01",
    due_date="2024-02-01",
    line_items=[
        InvoiceLineItemRequest(
            description="Service fee",
            unit_price=100.0,
            quantity=1.0,
        ),
    ],
)
client.accounting.invoices.create(model=invoice, run_async=True)

# NEW: Using dict for bulk writes
batch_item = BulkWriteBatchItem(
    item_id="inv-001",
    model={
        "type": "ACCOUNTS_RECEIVABLE",
        "contact": "contact-uuid",
        "number": "INV-001",
        "issue_date": "2024-01-01",
        "due_date": "2024-02-01",
        "line_items": [
            {
                "description": "Service fee",
                "unit_price": 100.0,
                "quantity": 1.0,
            },
        ],
    },
)
```

### 6. Update error handling

**Old error handling (per-item):**
```python
# OLD
try:
    response = client.accounting.invoices.create(model=invoice, run_async=True)
except ApiError as e:
    handle_error(e)

# Polling errors
task = client.accounting.async_tasks.retrieve(id=task_id)
if task.status == AsyncPostTaskStatusEnum.FAILURE:
    error_info = task.result.response
```

**New error handling (batch-level + item-level):**
```python
# NEW
from merge.core.api_error import ApiError

try:
    response = client.accounting.invoices.bulk_create(batch_items=batch_items)
except ApiError as e:
    # HTTP-level error (e.g., 400 for >100 items, 403 for feature not enabled)
    handle_error(e)

# Item-level errors are in the bulk_retrieve response
result = client.accounting.invoices.bulk_retrieve(batch_id=response.batch_id)
for obj in result.objects:
    if obj.status == BulkWriteObjectStatusEnum.FAILED:
        errors = obj.response.get("errors", [])
        for error in errors:
            print(f"  Source: {error.get('source')}")
            print(f"  Title: {error.get('title')}")
            print(f"  Detail: {error.get('detail')}")
```

### 7. Key differences to communicate to the customer

| Aspect | Async Posts | Bulk Writes |
|--------|------------|-------------|
| Items per request | 1 | Up to 100 |
| API calls for N items | N create + N poll | ceil(N/100) create + ceil(N/100) poll |
| Item tracking | Task ID from server | Customer-provided item_id |
| Status model | QUEUED → IN_PROGRESS → COMPLETED/FAILURE | ENQUEUED → IN_PROGRESS → SUCCESS/FAILED/PARTIAL_SUCCESS |
| Error granularity | Per request | Per item within batch |
| Response contains | Full model object | Object ID on success, errors on failure |
| Rate limit | 200/min per org | 200/min per linked account |

### 8. Remove dead code
After migration, remove:
- Old `async_tasks.retrieve` polling loops
- Old `AsyncPostTaskStatusEnum` imports and checks
- Old `run_async=True` create call patterns
- Any per-item task ID tracking that's been replaced by batch_id tracking

## Approach

1. **Read all customer code first** to understand their full async post usage pattern
2. **Identify all resources** being created with `run_async=True` (invoices, contacts, payments, etc.)
3. **Map the data flow** — understand how they build request models, handle responses, and track results
4. **Apply the migration** resource by resource, preserving their existing error handling and logging patterns
5. **Update tests** to use the new bulk write patterns
6. **Run tests** to verify the migration works

## Important Notes

- The `bulk_create` / `bulk_retrieve` methods follow the same pattern across all categories and resources. Replace `invoices` with the appropriate resource name (e.g., `contacts`, `payments`, `journal_entries`, etc.)
- The `item_id` in `BulkWriteBatchItem` must be unique within each batch — it's how customers correlate results back to their input data
- Maximum batch size is 100 items. Code must chunk larger datasets.
- The bulk writes API is in closed beta and requires the feature flag `MERGE_FLAG_ENABLE_BULK_WRITES_API` to be enabled for the customer's organization
- Results are stored for 14 days in DynamoDB, after which they expire automatically
