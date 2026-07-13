---
id: "@specs/aws/ec2/delete_subnet"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteSubnet"
---

# DeleteSubnet

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_subnet
> **spec:implements:** @kind:operation DeleteSubnet
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteSubnet.spec.md

Deletes the specified subnet. You must terminate all running instances in the subnet before you can delete the subnet.

## Input Shape: DeleteSubnetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SubnetId | Any  # complex shape | ✓ | The ID of the subnet. |

## Implementation

```speclang
def delete_subnet(store, request: dict) -> dict:
    """Deletes the specified subnet. You must terminate all running instances in the subnet before you can delete the subnet."""
    subnet_id = request.get("SubnetId", "").strip() if isinstance(request.get("SubnetId"), str) else request.get("SubnetId")

    if not store.subnets(subnet_id):
        raise ResourceNotFoundException(f"Resource subnet_id not found")
    store.delete_subnets(subnet_id)
    return {}
```
