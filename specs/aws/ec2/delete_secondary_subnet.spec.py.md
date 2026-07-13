---
id: "@specs/aws/ec2/delete_secondary_subnet"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteSecondarySubnet"
---

# DeleteSecondarySubnet

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_secondary_subnet
> **spec:implements:** @kind:operation DeleteSecondarySubnet
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteSecondarySubnet.spec.md

Deletes a secondary subnet. A secondary subnet must not contain any secondary interfaces prior to deletion.

## Input Shape: DeleteSecondarySubnetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| SecondarySubnetId | Any  # complex shape | ✓ | The ID of the secondary subnet to delete. |

## Output Shape: DeleteSecondarySubnetResult

- **ClientToken** (str): Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided
- **SecondarySubnet** (Any  # complex shape): Information about the secondary subnet being deleted.

## Implementation

```speclang
def delete_secondary_subnet(store, request: dict) -> dict:
    """Deletes a secondary subnet. A secondary subnet must not contain any secondary interfaces prior to deletion."""
    secondary_subnet_id = request.get("SecondarySubnetId", "").strip() if isinstance(request.get("SecondarySubnetId"), str) else request.get("SecondarySubnetId")

    if not store.secondary_subnets(secondary_subnet_id):
        raise ResourceNotFoundException(f"Resource secondary_subnet_id not found")
    store.delete_secondary_subnets(secondary_subnet_id)
    return {}
```
