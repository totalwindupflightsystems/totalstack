---
id: "@specs/aws/ec2/copy_volumes"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CopyVolumes"
---

# CopyVolumes

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/copy_volumes
> **spec:implements:** @kind:operation CopyVolumes
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CopyVolumes.spec.md

Creates a crash-consistent, point-in-time copy of an existing Amazon EBS volume within the same Availability Zone. The volume copy can be attached to an Amazon EC2 instance once it reaches the available state. For more information, see Copy an Amazon EBS volume .

## Input Shape: CopyVolumesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Iops | int |  | The number of I/O operations per second (IOPS) to provision for the volume copy. Required for io1 and io2 volumes. Optio |
| MultiAttachEnabled | bool |  | Indicates whether to enable Amazon EBS Multi-Attach for the volume copy. If you enable Multi-Attach, you can attach the  |
| Size | int |  | The size of the volume copy, in GiBs. The size must be equal to or greater than the size of the source volume. If not sp |
| SourceVolumeId | Any  # complex shape | ✓ | The ID of the source EBS volume to copy. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the volume copy during creation. |
| Throughput | int |  | The throughput to provision for the volume copy, in MiB/s. Supported for gp3 volumes only. Omit for all other volume typ |
| VolumeType | Any  # complex shape |  | The volume type for the volume copy. If not specified, the volume type defaults to gp2 . |

## Output Shape: CopyVolumesResult

- **Volumes** (list[Any  # complex shape]): Information about the volume copy.

## Implementation

```speclang
def copy_volumes(store, request: dict) -> dict:
    """Creates a crash-consistent, point-in-time copy of an existing Amazon EBS volume within the same Availability Zone. The volume copy can be attached to an Amazon EC2 instance once it reaches the availab"""
    source_volume_id = request.get("SourceVolumeId", "").strip() if isinstance(request.get("SourceVolumeId"), str) else request.get("SourceVolumeId")
    if not source_volume_id:
        raise ValidationException("SourceVolumeId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("CopyVolumes", request)
```
