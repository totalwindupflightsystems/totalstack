---
id: "@specs/aws/ec2/create_local_gateway_route_table_virtual_interface_group_association"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation"
---

# CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_local_gateway_route_table_virtual_interface_group_association
> **spec:implements:** @kind:operation CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation.spec.md

Creates a local gateway route table virtual interface group association.

## Input Shape: CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayRouteTableId | Any  # complex shape | ✓ | The ID of the local gateway route table. |
| LocalGatewayVirtualInterfaceGroupId | Any  # complex shape | ✓ | The ID of the local gateway route table virtual interface group association. |
| TagSpecifications | list[Any  # complex shape] |  | The tags assigned to the local gateway route table virtual interface group association. |

## Output Shape: CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult

- **LocalGatewayRouteTableVirtualInterfaceGroupAssociation** (Any  # complex shape): Information about the local gateway route table virtual interface group association.

## Implementation

```speclang
def create_local_gateway_route_table_virtual_interface_group_association(store, request: dict) -> dict:
    """Creates a local gateway route table virtual interface group association."""
    local_gateway_route_table_id = request.get("LocalGatewayRouteTableId", "").strip() if isinstance(request.get("LocalGatewayRouteTableId"), str) else request.get("LocalGatewayRouteTableId")
    if not local_gateway_route_table_id:
        raise ValidationException("LocalGatewayRouteTableId is required")
    local_gateway_virtual_interface_group_id = request.get("LocalGatewayVirtualInterfaceGroupId", "").strip() if isinstance(request.get("LocalGatewayVirtualInterfaceGroupId"), str) else request.get("LocalGatewayVirtualInterfaceGroupId")
    if not local_gateway_virtual_interface_group_id:
        raise ValidationException("LocalGatewayVirtualInterfaceGroupId is required")

    if store.local_gateway_route_table_virtual_interface_group_associations(local_gateway_virtual_interface_group_id):
        raise ResourceInUseException(f"Resource local_gateway_virtual_interface_group_id already exists")

    record = {
        "LocalGatewayRouteTableId": local_gateway_route_table_id,
        "LocalGatewayVirtualInterfaceGroupId": local_gateway_virtual_interface_group_id,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
    }

    store.local_gateway_route_table_virtual_interface_group_associations(local_gateway_virtual_interface_group_id, record)

    return {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociation": record.get("LocalGatewayRouteTableVirtualInterfaceGroupAssociation", {}),
    }
```
