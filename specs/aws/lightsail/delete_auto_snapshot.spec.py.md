---
id: "@specs/aws/lightsail/delete_auto_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_DeleteAutoSnapshot"
---

# DeleteAutoSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/delete_auto_snapshot
> **spec:implements:** @kind:operation DeleteAutoSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_DeleteAutoSnapshot.spec.md

Deletes an automatic snapshot of an instance or disk. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: DeleteAutoSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| date | Any  # complex shape | ✓ | The date of the automatic snapshot to delete in YYYY-MM-DD format. Use the get auto snapshots operation to get the avail |
| resourceName | Any  # complex shape | ✓ | The name of the source instance or disk from which to delete the automatic snapshot. |

## Output Shape: DeleteAutoSnapshotResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.

## Implementation

```speclang
def delete_auto_snapshot(store, request: dict) -> dict:
    """Deletes an automatic snapshot of an instance or disk. For more information, see the Amazon Lightsail Developer Guide ."""
    date = request.get("date", "").strip() if isinstance(request.get("date"), str) else request.get("date")
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")

    if not store.auto_snapshots(resource_name):
        raise ResourceNotFoundException(f"Resource resource_name not found")
    store.delete_auto_snapshots(resource_name)
    return {}
```
