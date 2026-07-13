---
id: "@specs/aws/ec2/delete_network_interface"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteNetworkInterface"
---

# DeleteNetworkInterface

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_network_interface
> **spec:implements:** @kind:operation DeleteNetworkInterface
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteNetworkInterface.spec.md

Deletes the specified network interface. You must detach the network interface before you can delete it.

## Input Shape: DeleteNetworkInterfaceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the network interface. |

## Implementation

```speclang
def delete_network_interface(store, request: dict) -> dict:
    """Deletes the specified network interface. You must detach the network interface before you can delete it."""
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")

    if not store.network_interfaces(network_interface_id):
        raise ResourceNotFoundException(f"Resource network_interface_id not found")
    store.delete_network_interfaces(network_interface_id)
    return {}
```
