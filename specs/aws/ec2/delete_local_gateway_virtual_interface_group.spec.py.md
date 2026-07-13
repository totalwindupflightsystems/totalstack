---
id: "@specs/aws/ec2/delete_local_gateway_virtual_interface_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteLocalGatewayVirtualInterfaceGroup"
---

# DeleteLocalGatewayVirtualInterfaceGroup

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_local_gateway_virtual_interface_group
> **spec:implements:** @kind:operation DeleteLocalGatewayVirtualInterfaceGroup
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteLocalGatewayVirtualInterfaceGroup.spec.md

Delete the specified local gateway interface group.

## Input Shape: DeleteLocalGatewayVirtualInterfaceGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayVirtualInterfaceGroupId | Any  # complex shape | ✓ | The ID of the local gateway virtual interface group to delete. |

## Output Shape: DeleteLocalGatewayVirtualInterfaceGroupResult

- **LocalGatewayVirtualInterfaceGroup** (Any  # complex shape): Information about the deleted local gateway virtual interface group.

## Implementation

```speclang
def delete_local_gateway_virtual_interface_group(store, request: dict) -> dict:
    """Delete the specified local gateway interface group."""
    local_gateway_virtual_interface_group_id = request.get("LocalGatewayVirtualInterfaceGroupId", "").strip() if isinstance(request.get("LocalGatewayVirtualInterfaceGroupId"), str) else request.get("LocalGatewayVirtualInterfaceGroupId")

    if not store.local_gateway_virtual_interface_groups(local_gateway_virtual_interface_group_id):
        raise ResourceNotFoundException(f"Resource local_gateway_virtual_interface_group_id not found")
    store.delete_local_gateway_virtual_interface_groups(local_gateway_virtual_interface_group_id)
    return {}
```
