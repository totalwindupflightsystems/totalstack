---
id: "@specs/aws/ec2/delete_local_gateway_route_table_vpc_association"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteLocalGatewayRouteTableVpcAssociation"
---

# DeleteLocalGatewayRouteTableVpcAssociation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_local_gateway_route_table_vpc_association
> **spec:implements:** @kind:operation DeleteLocalGatewayRouteTableVpcAssociation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteLocalGatewayRouteTableVpcAssociation.spec.md

Deletes the specified association between a VPC and local gateway route table.

## Input Shape: DeleteLocalGatewayRouteTableVpcAssociationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayRouteTableVpcAssociationId | Any  # complex shape | ✓ | The ID of the association. |

## Output Shape: DeleteLocalGatewayRouteTableVpcAssociationResult

- **LocalGatewayRouteTableVpcAssociation** (Any  # complex shape): Information about the association.

## Implementation

```speclang
def delete_local_gateway_route_table_vpc_association(store, request: dict) -> dict:
    """Deletes the specified association between a VPC and local gateway route table."""
    local_gateway_route_table_vpc_association_id = request.get("LocalGatewayRouteTableVpcAssociationId", "").strip() if isinstance(request.get("LocalGatewayRouteTableVpcAssociationId"), str) else request.get("LocalGatewayRouteTableVpcAssociationId")

    if not store.local_gateway_route_table_vpc_associations(local_gateway_route_table_vpc_association_id):
        raise ResourceNotFoundException(f"Resource local_gateway_route_table_vpc_association_id not found")
    store.delete_local_gateway_route_table_vpc_associations(local_gateway_route_table_vpc_association_id)
    return {}
```
