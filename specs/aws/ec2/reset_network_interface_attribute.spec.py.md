---
id: "@specs/aws/ec2/reset_network_interface_attribute"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ResetNetworkInterfaceAttribute"
---

# ResetNetworkInterfaceAttribute

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/reset_network_interface_attribute
> **spec:implements:** @kind:operation ResetNetworkInterfaceAttribute
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ResetNetworkInterfaceAttribute.spec.md

Resets a network interface attribute. You can specify only one attribute at a time.

## Input Shape: ResetNetworkInterfaceAttributeRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the network interface. |
| SourceDestCheck | str |  | The source/destination checking attribute. Resets the value to true . |

## Implementation

```speclang
def reset_network_interface_attribute(store, request: dict) -> dict:
    """Resets a network interface attribute. You can specify only one attribute at a time."""
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")

    resource = store.reset_network_interface_attributes(network_interface_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource network_interface_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run
    if "SourceDestCheck" in request:
        resource["SourceDestCheck"] = source_dest_check

    store.reset_network_interface_attributes(network_interface_id, resource)
    return resource
```
