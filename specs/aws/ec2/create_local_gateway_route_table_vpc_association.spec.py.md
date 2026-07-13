---
id: "@specs/aws/ec2/create_local_gateway_route_table_vpc_association"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateLocalGatewayRouteTableVpcAssociation"
---

# CreateLocalGatewayRouteTableVpcAssociation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_local_gateway_route_table_vpc_association
> **spec:implements:** @kind:operation CreateLocalGatewayRouteTableVpcAssociation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateLocalGatewayRouteTableVpcAssociation.spec.md

Associates the specified VPC with the specified local gateway route table.

## Input Shape: CreateLocalGatewayRouteTableVpcAssociationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the local gateway route table. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the local gateway route table VPC association. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: CreateLocalGatewayRouteTableVpcAssociationResult

- **LocalGatewayRouteTableVpcAssociation** (Any  # complex shape): Information about the association.

## Implementation

```speclang
def create_local_gateway_route_table_vpc_association(store, request: dict) -> dict:
    """Associates the specified VPC with the specified local gateway route table."""
    local_gateway_route_table_id = request.get("LocalGatewayRouteTableId", "").strip() if isinstance(request.get("LocalGatewayRouteTableId"), str) else request.get("LocalGatewayRouteTableId")
    if not local_gateway_route_table_id:
        raise ValidationException("LocalGatewayRouteTableId is required")
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    if store.local_gateway_route_table_vpc_associations(vpc_id):
        raise ResourceInUseException(f"Resource vpc_id already exists")

    record = {
        "LocalGatewayRouteTableId": local_gateway_route_table_id,
        "VpcId": vpc_id,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.local_gateway_route_table_vpc_associations(vpc_id, record)

    return {
        "LocalGatewayRouteTableVpcAssociation": record.get("LocalGatewayRouteTableVpcAssociation", {}),
    }
```
