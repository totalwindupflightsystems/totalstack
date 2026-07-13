---
id: "@specs/aws/ec2/delete_local_gateway_virtual_interface"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteLocalGatewayVirtualInterface"
---

# DeleteLocalGatewayVirtualInterface

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_local_gateway_virtual_interface
> **spec:implements:** @kind:operation DeleteLocalGatewayVirtualInterface
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteLocalGatewayVirtualInterface.spec.md

Deletes the specified local gateway virtual interface.

## Input Shape: DeleteLocalGatewayVirtualInterfaceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| LocalGatewayVirtualInterfaceId | Any  # complex shape | ✓ | The ID of the local virtual interface to delete. |

## Output Shape: DeleteLocalGatewayVirtualInterfaceResult

- **LocalGatewayVirtualInterface** (Any  # complex shape): Information about the deleted local gateway virtual interface.

## Implementation

```speclang
def delete_local_gateway_virtual_interface(store, request: dict) -> dict:
    """Deletes the specified local gateway virtual interface."""
    local_gateway_virtual_interface_id = request.get("LocalGatewayVirtualInterfaceId", "").strip() if isinstance(request.get("LocalGatewayVirtualInterfaceId"), str) else request.get("LocalGatewayVirtualInterfaceId")

    if not store.local_gateway_virtual_interfaces(local_gateway_virtual_interface_id):
        raise ResourceNotFoundException(f"Resource local_gateway_virtual_interface_id not found")
    store.delete_local_gateway_virtual_interfaces(local_gateway_virtual_interface_id)
    return {}
```
