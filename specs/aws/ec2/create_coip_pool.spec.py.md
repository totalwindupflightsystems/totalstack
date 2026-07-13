---
id: "@specs/aws/ec2/create_coip_pool"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateCoipPool"
---

# CreateCoipPool

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_coip_pool
> **spec:implements:** @kind:operation CreateCoipPool
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateCoipPool.spec.md

Creates a pool of customer-owned IP (CoIP) addresses.

## Input Shape: CreateCoipPoolRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the local gateway route table. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the CoIP address pool. |

## Output Shape: CreateCoipPoolResult

- **CoipPool** (Any  # complex shape): Information about the CoIP address pool.

## Implementation

```speclang
def create_coip_pool(store, request: dict) -> dict:
    """Creates a pool of customer-owned IP (CoIP) addresses."""
    local_gateway_route_table_id = request.get("LocalGatewayRouteTableId", "").strip() if isinstance(request.get("LocalGatewayRouteTableId"), str) else request.get("LocalGatewayRouteTableId")
    if not local_gateway_route_table_id:
        raise ValidationException("LocalGatewayRouteTableId is required")

    if store.coip_pools(local_gateway_route_table_id):
        raise ResourceInUseException(f"Resource local_gateway_route_table_id already exists")

    record = {
        "LocalGatewayRouteTableId": local_gateway_route_table_id,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.coip_pools(local_gateway_route_table_id, record)

    return {
        "CoipPool": record.get("CoipPool", {}),
    }
```
