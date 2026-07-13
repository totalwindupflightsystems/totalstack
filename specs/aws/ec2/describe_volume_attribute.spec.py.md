---
id: "@specs/aws/ec2/describe_volume_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DescribeVolumeAttribute"
---

# DescribeVolumeAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/describe_volume_attribute
> **spec:implements:** @kind:operation DescribeVolumeAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DescribeVolumeAttribute.spec.md

Describes the specified attribute of the specified volume. You can specify only one attribute at a time. For more information about EBS volumes, see Amazon EBS volumes in the Amazon EBS User Guide .

## Input Shape: DescribeVolumeAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape | ✓ | The attribute of the volume. This parameter is required. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VolumeId | Any  # complex shape | ✓ | The ID of the volume. |

## Output Shape: DescribeVolumeAttributeResult

- **AutoEnableIO** (Any  # complex shape): The state of autoEnableIO attribute.
- **ProductCodes** (list[Any  # complex shape]): A list of product codes.
- **VolumeId** (str): The ID of the volume.

## Implementation

```speclang
def describe_volume_attribute(store, request: dict) -> dict:
    """Describes the specified attribute of the specified volume. You can specify only one attribute at a time. For more information about EBS volumes, see Amazon EBS volumes in the Amazon EBS User Guide ."""
    attribute = request.get("Attribute", "").strip() if isinstance(request.get("Attribute"), str) else request.get("Attribute")
    if not attribute:
        raise ValidationException("Attribute is required")
    volume_id = request.get("VolumeId", "").strip() if isinstance(request.get("VolumeId"), str) else request.get("VolumeId")
    if not volume_id:
        raise ValidationException("VolumeId is required")

    resource = store.volume_attributes(volume_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource volume_id not found")
    return {"VolumeId": volume_id, **resource}
```
