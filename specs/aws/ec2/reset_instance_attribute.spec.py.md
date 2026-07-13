---
id: "@specs/aws/ec2/reset_instance_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ResetInstanceAttribute"
---

# ResetInstanceAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/reset_instance_attribute
> **spec:implements:** @kind:operation ResetInstanceAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ResetInstanceAttribute.spec.md

Resets an attribute of an instance to its default value. To reset the kernel or ramdisk , the instance must be in a stopped state. To reset the sourceDestCheck , the instance can be either running or stopped. The sourceDestCheck attribute controls whether source/destination checking is enabled. The default value is true , which means checking is enabled. This value must be false for a NAT instance to perform NAT. For more information, see NAT instances in the Amazon VPC User Guide .

## Input Shape: ResetInstanceAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Attribute | Any  # complex shape | ✓ | The attribute to reset. You can only reset the following attributes: kernel | ramdisk | sourceDestCheck . |
| DryRun | bool |  | Checks whether you have the required permissions for the operation, without actually making the request, and provides an |
| InstanceId | Any  # complex shape | ✓ | The ID of the instance. |

## Implementation

```speclang
def reset_instance_attribute(store, request: dict) -> dict:
    """Resets an attribute of an instance to its default value. To reset the kernel or ramdisk , the instance must be in a stopped state. To reset the sourceDestCheck , the instance can be either running or """
    attribute = request.get("Attribute", "").strip() if isinstance(request.get("Attribute"), str) else request.get("Attribute")
    if not attribute:
        raise ValidationException("Attribute is required")
    instance_id = request.get("InstanceId", "").strip() if isinstance(request.get("InstanceId"), str) else request.get("InstanceId")
    if not instance_id:
        raise ValidationException("InstanceId is required")

    resource = store.reset_instance_attributes(instance_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.reset_instance_attributes(instance_id, resource)
    return resource
```
