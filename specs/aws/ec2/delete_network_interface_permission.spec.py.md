---
id: "@specs/aws/ec2/delete_network_interface_permission"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteNetworkInterfacePermission"
---

# DeleteNetworkInterfacePermission

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_network_interface_permission
> **spec:implements:** @kind:operation DeleteNetworkInterfacePermission
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteNetworkInterfacePermission.spec.md

Deletes a permission for a network interface. By default, you cannot delete the permission if the account for which you're removing the permission has attached the network interface to an instance. However, you can force delete the permission, regardless of any attachment.

## Input Shape: DeleteNetworkInterfacePermissionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Force | bool |  | Specify true to remove the permission even if the network interface is attached to an instance. |
| NetworkInterfacePermissionId | Any  # complex shape | ✓ | The ID of the network interface permission. |

## Output Shape: DeleteNetworkInterfacePermissionResult

- **Return** (bool): Is true if the request succeeds and an error otherwise.

## Implementation

```speclang
def delete_network_interface_permission(store, request: dict) -> dict:
    """Deletes a permission for a network interface. By default, you cannot delete the permission if the account for which you're removing the permission has attached the network interface to an instance. Ho"""
    network_interface_permission_id = request.get("NetworkInterfacePermissionId", "").strip() if isinstance(request.get("NetworkInterfacePermissionId"), str) else request.get("NetworkInterfacePermissionId")

    if not store.network_interface_permissions(network_interface_permission_id):
        raise ResourceNotFoundException(f"Resource network_interface_permission_id not found")
    store.delete_network_interface_permissions(network_interface_permission_id)
    return {}
```
