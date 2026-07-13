---
id: "@specs/aws/ec2/delete_coip_pool"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteCoipPool"
---

# DeleteCoipPool

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_coip_pool
> **spec:implements:** @kind:operation DeleteCoipPool
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteCoipPool.spec.md

Deletes a pool of customer-owned IP (CoIP) addresses.

## Input Shape: DeleteCoipPoolRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| CoipPoolId | Any  # complex shape | ✓ | The ID of the CoIP pool that you want to delete. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |

## Output Shape: DeleteCoipPoolResult

- **CoipPool** (Any  # complex shape): Information about the CoIP address pool.

## Implementation

```speclang
def delete_coip_pool(store, request: dict) -> dict:
    """Deletes a pool of customer-owned IP (CoIP) addresses."""
    coip_pool_id = request.get("CoipPoolId", "").strip() if isinstance(request.get("CoipPoolId"), str) else request.get("CoipPoolId")

    if not store.coip_pools(coip_pool_id):
        raise ResourceNotFoundException(f"Resource coip_pool_id not found")
    store.delete_coip_pools(coip_pool_id)
    return {}
```
