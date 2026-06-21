---
id: "@specs/aws/lightsail/get_auto_snapshots"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_GetAutoSnapshots"
---

# GetAutoSnapshots

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/get_auto_snapshots
> **spec:implements:** @kind:operation GetAutoSnapshots
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_GetAutoSnapshots.spec.md

Returns the available automatic snapshots for an instance or disk. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: GetAutoSnapshotsRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| resourceName | Any  # complex shape | ✓ | The name of the source instance or disk from which to get automatic snapshot information. |

## Output Shape: GetAutoSnapshotsResult

- **autoSnapshots** (list[Any  # complex shape]): An array of objects that describe the automatic snapshots that are available for the specified source instance or disk.
- **resourceName** (Any  # complex shape): The name of the source instance or disk for the automatic snapshots.
- **resourceType** (Any  # complex shape): The resource type of the automatic snapshot. The possible values are Instance , and Disk .

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
def get_auto_snapshots(store, request: dict) -> dict:
    """Returns the available automatic snapshots for an instance or disk. For more information, see the Amazon Lightsail Developer Guide ."""
    resource_name = request.get("resourceName", "").strip() if isinstance(request.get("resourceName"), str) else request.get("resourceName")
    if not resource_name:
        raise ValidationException("resourceName is required")

    resource = store.auto_snapshotss(resource_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource resource_name not found")
    return {"resourceName": resource_name, **resource}
```
