---
id: "@specs/aws/ec2/create_replace_root_volume_task"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateReplaceRootVolumeTask"
---

# CreateReplaceRootVolumeTask

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_replace_root_volume_task
> **spec:implements:** @kind:operation CreateReplaceRootVolumeTask
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateReplaceRootVolumeTask.spec.md

Replaces the EBS-backed root volume for a running instance with a new volume that is restored to the original root volume's launch state, that is restored to a specific snapshot taken from the original root volume, or that is restored from an AMI that has the same key characteristics as that of the instance. For more information, see Replace a root volume in the Amazon EC2 User Guide .

## Input Shape: CreateReplaceRootVolumeTaskRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client t |
| DeleteReplacedRootVolume | bool |  | Indicates whether to automatically delete the original root volume after the root volume replacement task completes. To  |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ImageId | Any  # complex shape |  | The ID of the AMI to use to restore the root volume. The specified AMI must have the same product code, billing informat |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance for which to replace the root volume. |
| SnapshotId | Any  # complex shape |  | The ID of the snapshot from which to restore the replacement root volume. The specified snapshot must be a snapshot that |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the root volume replacement task. |
| VolumeInitializationRate | int |  | Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to  |

## Output Shape: CreateReplaceRootVolumeTaskResult

- **ReplaceRootVolumeTask** (Any  # complex shape): Information about the root volume replacement task.

## Implementation

```speclang
def create_replace_root_volume_task(store, request: dict) -> dict:
    """Replaces the EBS-backed root volume for a running instance with a new volume that is restored to the original root volume's launch state, that is restored to a specific snapshot taken from the origina"""
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    if store.replace_root_volume_tasks(instance_id):
        raise ResourceInUseException(f"Resource instance_id already exists")

    record = {
        "InstanceId": instance_id,
        "SnapshotId": snapshot_id,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "TagSpecifications": tag_specifications,
        "ImageId": image_id,
        "DeleteReplacedRootVolume": delete_replaced_root_volume,
        "VolumeInitializationRate": volume_initialization_rate,
    }

    store.replace_root_volume_tasks(instance_id, record)

    return {
        "ReplaceRootVolumeTask": record.get("ReplaceRootVolumeTask", {}),
    }
```
