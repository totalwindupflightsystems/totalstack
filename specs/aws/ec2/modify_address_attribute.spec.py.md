---
id: "@specs/aws/ec2/modify_address_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyAddressAttribute"
---

# ModifyAddressAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_address_attribute
> **spec:implements:** @kind:operation ModifyAddressAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyAddressAttribute.spec.md

Modifies an attribute of the specified Elastic IP address. For requirements, see Using reverse DNS for email applications .

## Input Shape: ModifyAddressAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllocationId | Any  # complex shape | ✓ | [EC2-VPC] The allocation ID. |
| DomainName | str |  | The domain name to modify for the IP address. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: ModifyAddressAttributeResult

- **Address** (Any  # complex shape): Information about the Elastic IP address.

## Implementation

```speclang
def modify_address_attribute(store, request: dict) -> dict:
    """Modifies an attribute of the specified Elastic IP address. For requirements, see Using reverse DNS for email applications ."""
    allocation_id = request.get("AllocationId", "").strip() if isinstance(request.get("AllocationId"), str) else request.get("AllocationId")
    if not allocation_id:
        raise ValidationException("AllocationId is required")

    if store.address_attributes(allocation_id):
        raise ResourceInUseException(f"Resource allocation_id already exists")

    record = {
        "AllocationId": allocation_id,
        "DomainName": domain_name,
        "DryRun": dry_run,
    }

    store.address_attributes(allocation_id, record)

    return {
        "Address": record.get("Address", {}),
    }
```
