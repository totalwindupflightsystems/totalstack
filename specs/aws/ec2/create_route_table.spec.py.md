---
id: "@specs/aws/ec2/create_route_table"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateRouteTable"
---

# CreateRouteTable

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_route_table
> **spec:implements:** @kind:operation CreateRouteTable
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateRouteTable.spec.md

Creates a route table for the specified VPC. After you create a route table, you can add routes and associate the table with a subnet. For more information, see Route tables in the Amazon VPC User Guide .

## Input Shape: CreateRouteTableRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the route table. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: CreateRouteTableResult

- **ClientToken** (str): Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided
- **RouteTable** (Any  # complex shape): Information about the route table.

## Implementation

```speclang
def create_route_table(store, request: dict) -> dict:
    """Creates a route table for the specified VPC. After you create a route table, you can add routes and associate the table with a subnet. For more information, see Route tables in the Amazon VPC User Gui"""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    if store.route_tables(vpc_id):
        raise ResourceInUseException(f"Resource vpc_id already exists")

    record = {
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "DryRun": dry_run,
        "VpcId": vpc_id,
    }

    store.route_tables(vpc_id, record)

    return {
        "RouteTable": record.get("RouteTable", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
