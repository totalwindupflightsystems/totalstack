---
id: "@specs/aws/ec2/delete_coip_cidr"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteCoipCidr"
---

# DeleteCoipCidr

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_coip_cidr
> **spec:implements:** @kind:operation DeleteCoipCidr
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteCoipCidr.spec.md

Deletes a range of customer-owned IP addresses.

## Input Shape: DeleteCoipCidrRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Cidr | str | ✓ | A customer-owned IP address range that you want to delete. |
| CoipPoolId | Any  # complex shape | ✓ | The ID of the customer-owned address pool. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DeleteCoipCidrResult

- **CoipCidr** (Any  # complex shape): Information about a range of customer-owned IP addresses.

## Implementation

```speclang
def delete_coip_cidr(store, request: dict) -> dict:
    """Deletes a range of customer-owned IP addresses."""
    cidr = request.get("Cidr", "").strip() if isinstance(request.get("Cidr"), str) else request.get("Cidr")
    coip_pool_id = request.get("CoipPoolId", "").strip() if isinstance(request.get("CoipPoolId"), str) else request.get("CoipPoolId")

    if not store.coip_cidrs(coip_pool_id):
        raise ResourceNotFoundException(f"Resource coip_pool_id not found")
    store.delete_coip_cidrs(coip_pool_id)
    return {}
```
