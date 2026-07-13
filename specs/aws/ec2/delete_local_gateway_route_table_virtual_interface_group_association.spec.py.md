---
id: "@specs/aws/ec2/delete_local_gateway_route_table_virtual_interface_group_association"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation"
---

# DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_local_gateway_route_table_virtual_interface_group_association
> **spec:implements:** @kind:operation DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation.spec.md

Deletes a local gateway route table virtual interface group association.

## Input Shape: DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayRouteTableVirtualInterfaceGroupAssociationId | Any  # complex shape | ✓ | The ID of the local gateway route table virtual interface group association. |

## Output Shape: DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult

- **LocalGatewayRouteTableVirtualInterfaceGroupAssociation** (Any  # complex shape): Information about the association.

## Implementation

```speclang
def delete_local_gateway_route_table_virtual_interface_group_association(store, request: dict) -> dict:
    """Deletes a local gateway route table virtual interface group association."""
    local_gateway_route_table_virtual_interface_group_association_id = request.get("LocalGatewayRouteTableVirtualInterfaceGroupAssociationId", "").strip() if isinstance(request.get("LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"), str) else request.get("LocalGatewayRouteTableVirtualInterfaceGroupAssociationId")

    if not store.local_gateway_route_table_virtual_interface_group_associations(local_gateway_route_table_virtual_interface_group_association_id):
        raise ResourceNotFoundException(f"Resource local_gateway_route_table_virtual_interface_group_association_id not found")
    store.delete_local_gateway_route_table_virtual_interface_group_associations(local_gateway_route_table_virtual_interface_group_association_id)
    return {}
```
