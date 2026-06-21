---
id: "@specs/aws/lightsail/create_instance_snapshot"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/lightsail/plan"
  - "@specs/aws/lightsail/docs/API_CreateInstanceSnapshot"
---

# CreateInstanceSnapshot

> **spec:trace:** specs/aws/lightsail/lightsail.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/lightsail/create_instance_snapshot
> **spec:implements:** @kind:operation CreateInstanceSnapshot
> **AWS Protocol:** json
> **HTTP:** POST /
> **@ref:** specs/aws/lightsail/docs/API_CreateInstanceSnapshot.spec.md

Creates a snapshot of a specific virtual private server, or instance . You can use a snapshot to create a new instance that is based on that snapshot. The create instance snapshot operation supports tag-based access control via request tags. For more information, see the Amazon Lightsail Developer Guide .

## Input Shape: CreateInstanceSnapshotRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| instanceName | Any  # complex shape | ✓ | The Lightsail instance on which to base your snapshot. |
| instanceSnapshotName | Any  # complex shape | ✓ | The name for your new snapshot. |
| tags | list[Any  # complex shape] |  | The tag keys and optional values to add to the resource during create. Use the TagResource action to tag a resource afte |

## Output Shape: CreateInstanceSnapshotResult

- **operations** (list[Any  # complex shape]): An array of objects that describe the result of the action, such as the status of the request, the timestamp of the requ

## Errors
- **ServiceException**: A general service exception.
- **InvalidInputException**: Lightsail throws this exception when user input does not conform to the validation rules of an input field. Domain and distribution APIs are only available in the N. Virginia ( us-east-1 ) Amazon Web 
- **NotFoundException**: Lightsail throws this exception when it cannot find a resource.
- **OperationFailureException**: Lightsail throws this exception when an operation fails to execute.
- **AccessDeniedException**: Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
- **AccountSetupInProgressException**: Lightsail throws this exception when an account is still in the setup in progress state.
- **RegionSetupInProgressException**: Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
- **UnauthenticatedException**: Lightsail throws this exception when the user has not been authenticated.

## Implementation

```speclang
def create_instance_snapshot(store, request: dict) -> dict:
    """Creates a snapshot of a specific virtual private server, or instance . You can use a snapshot to create a new instance that is based on that snapshot. The create instance snapshot operation supports t"""
    instance_name = request.get("instanceName", "").strip() if isinstance(request.get("instanceName"), str) else request.get("instanceName")
    if not instance_name:
        raise ValidationException("instanceName is required")
    instance_snapshot_name = request.get("instanceSnapshotName", "").strip() if isinstance(request.get("instanceSnapshotName"), str) else request.get("instanceSnapshotName")
    if not instance_snapshot_name:
        raise ValidationException("instanceSnapshotName is required")

    if store.instance_snapshots(instance_snapshot_name):
        raise ResourceInUseException(f"Resource instance_snapshot_name already exists")

    record = {
        "instanceSnapshotName": instance_snapshot_name,
        "instanceName": instance_name,
        "tags": tags,
    }

    store.instance_snapshots(instance_snapshot_name, record)

    return {
        "operations": record.get("operations", {}),
    }
```
