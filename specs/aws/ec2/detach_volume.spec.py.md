---
id: "@specs/aws/ec2/detach_volume"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DetachVolume"
---

# DetachVolume

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/detach_volume
> **spec:implements:** @kind:operation DetachVolume
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DetachVolume.spec.md

Detaches an EBS volume from an instance. Make sure to unmount any file systems on the device within your operating system before detaching the volume. Failure to do so can result in the volume becoming stuck in the busy state while detaching. If this happens, detachment can be delayed indefinitely until you unmount the volume, force detachment, reboot the instance, or all three. If an EBS volume is the root device of an instance, it can't be detached while the instance is running. To detach the root volume, stop the instance first. When a volume with an Amazon Web Services Marketplace product code is detached from an instance, the product code is no longer associated with the instance. You can't detach or force detach volumes that are attached to Amazon Web Services-managed resources. Attempting to do this results in the UnsupportedOperationException exception. For more information, see Detach an Amazon EBS volume in the Amazon EBS User Guide .

## Input Shape: DetachVolumeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Device | str |  | The device name. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Force | bool |  | Forces detachment if the previous detachment attempt did not occur cleanly (for example, logging into an instance, unmou |
| InstanceId | Any  # complex shape |  | The ID of the instance. If you are detaching a Multi-Attach enabled volume, you must specify an instance ID. |
| VolumeId | Any  # complex shape | ✓ | The ID of the volume. |

## Output Shape: VolumeAttachment

- **AssociatedResource** (str): The ARN of the Amazon Web Services-managed resource to which the volume is attached.
- **AttachTime** (Any  # complex shape): The time stamp when the attachment initiated.
- **DeleteOnTermination** (bool): Indicates whether the EBS volume is deleted on instance termination.
- **Device** (str): The device name. If the volume is attached to an Amazon Web Services-managed resource, this parameter returns null .
- **EbsCardIndex** (int): The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.
- **InstanceId** (str): The ID of the instance. If the volume is attached to an Amazon Web Services-managed resource, this parameter returns nul
- **InstanceOwningService** (str): The service principal of the Amazon Web Services service that owns the underlying resource to which the volume is attach
- **State** (Any  # complex shape): The attachment state of the volume.
- **VolumeId** (str): The ID of the volume.

## Implementation

```speclang
def detach_volume(store, request: dict) -> dict:
    """Detaches an EBS volume from an instance. Make sure to unmount any file systems on the device within your operating system before detaching the volume. Failure to do so can result in the volume becomin"""
    volume_id = request.get("VolumeId", "").strip() if isinstance(request.get("VolumeId"), str) else request.get("VolumeId")
    if not volume_id:
        raise ValidationException("VolumeId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachVolume", request)
```
