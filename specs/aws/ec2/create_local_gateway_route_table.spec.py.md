---
id: "@specs/aws/ec2/create_local_gateway_route_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateLocalGatewayRouteTable"
---

# CreateLocalGatewayRouteTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_local_gateway_route_table
> **spec:implements:** @kind:operation CreateLocalGatewayRouteTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateLocalGatewayRouteTable.spec.md

Creates a local gateway route table.

## Input Shape: CreateLocalGatewayRouteTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayId | Any  # complex shape | ✓ | The ID of the local gateway. |
| Mode | Any  # complex shape |  | The mode of the local gateway route table. |
| TagSpecifications | list[Any  # complex shape] |  | The tags assigned to the local gateway route table. |

## Output Shape: CreateLocalGatewayRouteTableResult

- **LocalGatewayRouteTable** (Any  # complex shape): Information about the local gateway route table.

## Implementation

```speclang
def create_local_gateway_route_table(store, request: dict) -> dict:
    """Creates a local gateway route table."""
    local_gateway_id = request.get("LocalGatewayId", "").strip() if isinstance(request.get("LocalGatewayId"), str) else request.get("LocalGatewayId")
    if not local_gateway_id:
        raise ValidationException("LocalGatewayId is required")

    if store.local_gateway_route_tables(local_gateway_id):
        raise ResourceInUseException(f"Resource local_gateway_id already exists")

    record = {
        "LocalGatewayId": local_gateway_id,
        "Mode": mode,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.local_gateway_route_tables(local_gateway_id, record)

    return {
        "LocalGatewayRouteTable": record.get("LocalGatewayRouteTable", {}),
    }
```
