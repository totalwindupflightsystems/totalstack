---
id: "@specs/aws/ec2/reset_address_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ResetAddressAttribute"
---

# ResetAddressAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/reset_address_attribute
> **spec:implements:** @kind:operation ResetAddressAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ResetAddressAttribute.spec.md

Resets the attribute of the specified IP address. For requirements, see Using reverse DNS for email applications .

## Input Shape: ResetAddressAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationId | Any  # complex shape | ✓ | [EC2-VPC] The allocation ID. |
| Attribute | Any  # complex shape | ✓ | The attribute of the IP address. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: ResetAddressAttributeResult

- **Address** (Any  # complex shape): Information about the IP address.

## Implementation

```speclang
def reset_address_attribute(store, request: dict) -> dict:
    """Resets the attribute of the specified IP address. For requirements, see Using reverse DNS for email applications ."""
    allocation_id = request.get("AllocationId", "").strip() if isinstance(request.get("AllocationId"), str) else request.get("AllocationId")
    if not allocation_id:
        raise ValidationException("AllocationId is required")
    attribute = request.get("Attribute", "").strip() if isinstance(request.get("Attribute"), str) else request.get("Attribute")
    if not attribute:
        raise ValidationException("Attribute is required")

    if store.reset_address_attributes(allocation_id):
        raise ResourceInUseException(f"Resource allocation_id already exists")

    record = {
        "AllocationId": allocation_id,
        "Attribute": attribute,
        "DryRun": dry_run,
    }

    store.reset_address_attributes(allocation_id, record)

    return {
        "Address": record.get("Address", {}),
    }
```
