---
id: "@specs/aws/ec2/create_network_interface_permission"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateNetworkInterfacePermission"
---

# CreateNetworkInterfacePermission

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_network_interface_permission
> **spec:implements:** @kind:operation CreateNetworkInterfacePermission
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateNetworkInterfacePermission.spec.md

Grants an Amazon Web Services-authorized account permission to attach the specified network interface to an instance in their account. You can grant permission to a single Amazon Web Services account only, and only one account at a time.

## Input Shape: CreateNetworkInterfacePermissionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AwsAccountId | str |  | The Amazon Web Services account ID. |
| AwsService | str |  | The Amazon Web Services service. Currently not supported. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the network interface. |
| Permission | Any  # complex shape | ✓ | The type of permission to grant. |

## Output Shape: CreateNetworkInterfacePermissionResult

- **InterfacePermission** (Any  # complex shape): Information about the permission for the network interface.

## Implementation

```speclang
def create_network_interface_permission(store, request: dict) -> dict:
    """Grants an Amazon Web Services-authorized account permission to attach the specified network interface to an instance in their account. You can grant permission to a single Amazon Web Services account """
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")
    permission = request.get("Permission", "").strip() if isinstance(request.get("Permission"), str) else request.get("Permission")
    if not permission:
        raise ValidationException("Permission is required")

    if store.network_interface_permissions(network_interface_id):
        raise ResourceInUseException(f"Resource network_interface_id already exists")

    record = {
        "NetworkInterfaceId": network_interface_id,
        "AwsAccountId": aws_account_id,
        "AwsService": aws_service,
        "Permission": permission,
        "DryRun": dry_run,
    }

    store.network_interface_permissions(network_interface_id, record)

    return {
        "InterfacePermission": record.get("InterfacePermission", {}),
    }
```
