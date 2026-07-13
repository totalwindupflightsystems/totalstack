---
id: "@specs/aws/ec2/attach_volume"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AttachVolume"
---

# AttachVolume

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/attach_volume
> **spec:implements:** @kind:operation AttachVolume
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AttachVolume.spec.md

Attaches an Amazon EBS volume to a running or stopped instance, and exposes it to the instance with the specified device name. The maximum number of Amazon EBS volumes that you can attach to an instance depends on the instance type. If you exceed the volume attachment limit for an instance type, the attachment request fails with the AttachmentLimitExceeded error. For more information, see Instance volume limits . After you attach an EBS volume, you must make it available for use. For more information, see Make an EBS volume available for use . If a volume has an Amazon Web Services Marketplace product code: The volume can be attached only to a stopped instance. Amazon Web Services Marketplace product codes are copied from the volume to the instance. You must be subscribed to the product. The instance type and operating system of the instance must support the product. For example, you can't detach a volume from a Windows instance and attach it to a Linux instance. For more information, see Attach an Amazon EBS volume to an instance in the Amazon EBS User Guide .

## Input Shape: AttachVolumeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Device | str | ✓ | The device name (for example, /dev/sdh or xvdh ). |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EbsCardIndex | Any  # complex shape |  | The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0. |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |
| VolumeId | Any  # complex shape | ✓ | The ID of the EBS volume. The volume and instance must be within the same Availability Zone. |

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
def attach_volume(store, request: dict) -> dict:
    """Attaches an Amazon EBS volume to a running or stopped instance, and exposes it to the instance with the specified device name. The maximum number of Amazon EBS volumes that you can attach to an instan"""
    device = request.get("Device", "").strip() if isinstance(request.get("Device"), str) else request.get("Device")
    if not device:
        raise ValidationException("Device is required")
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")
    volume_id = request.get("VolumeId", "").strip() if isinstance(request.get("VolumeId"), str) else request.get("VolumeId")
    if not volume_id:
        raise ValidationException("VolumeId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachVolume", request)
```
