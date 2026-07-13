---
id: "@specs/aws/ec2/create_delegate_mac_volume_ownership_task"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateDelegateMacVolumeOwnershipTask"
---

# CreateDelegateMacVolumeOwnershipTask

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_delegate_mac_volume_ownership_task
> **spec:implements:** @kind:operation CreateDelegateMacVolumeOwnershipTask
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateDelegateMacVolumeOwnershipTask.spec.md

Delegates ownership of the Amazon EBS root volume for an Apple silicon Mac instance to an administrative user.

## Input Shape: CreateDelegateMacVolumeOwnershipTaskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceId | Any  # complex shape | ✓ | The ID of the Amazon EC2 Mac instance. |
| MacCredentials | Any  # complex shape | ✓ | Specifies the following credentials: Internal disk administrative user Username - Only the default administrative user ( |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the volume ownership delegation task. |

## Output Shape: CreateDelegateMacVolumeOwnershipTaskResult

- **MacModificationTask** (Any  # complex shape): Information about the volume ownership delegation task.

## Implementation

```speclang
def create_delegate_mac_volume_ownership_task(store, request: dict) -> dict:
    """Delegates ownership of the Amazon EBS root volume for an Apple silicon Mac instance to an administrative user."""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    mac_credentials = request.get("MacCredentials", "").strip() if isinstance(request.get("MacCredentials"), str) else request.get("MacCredentials")
    if not mac_credentials:
        raise ValidationException("MacCredentials is required")

    if store.delegate_mac_volume_ownership_tasks(instance_id):
        raise ResourceInUseException(f"Resource instance_id already exists")

    record = {
        "ClientToken": client_token,
        "DryRun": dry_run,
        "InstanceId": instance_id,
        "MacCredentials": mac_credentials,
        "TagSpecifications": tag_specifications,
    }

    store.delegate_mac_volume_ownership_tasks(instance_id, record)

    return {
        "MacModificationTask": record.get("MacModificationTask", {}),
    }
```
