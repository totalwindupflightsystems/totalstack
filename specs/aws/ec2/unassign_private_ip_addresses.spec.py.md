---
id: "@specs/aws/ec2/unassign_private_ip_addresses"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_UnassignPrivateIpAddresses"
---

# UnassignPrivateIpAddresses

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/unassign_private_ip_addresses
> **spec:implements:** @kind:operation UnassignPrivateIpAddresses
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_UnassignPrivateIpAddresses.spec.md

Unassigns the specified secondary private IP addresses or IPv4 Prefix Delegation prefixes from a network interface.

## Input Shape: UnassignPrivateIpAddressesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Ipv4Prefixes | list[str] |  | The IPv4 prefixes to unassign from the network interface. |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the network interface. |
| PrivateIpAddresses | list[str] |  | The secondary private IP addresses to unassign from the network interface. You can specify this option multiple times to |

## Implementation

```speclang
def unassign_private_ip_addresses(store, request: dict) -> dict:
    """Unassigns the specified secondary private IP addresses or IPv4 Prefix Delegation prefixes from a network interface."""
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")

    if store.unassign_private_ip_addressess(network_interface_id):
        raise ResourceInUseException(f"Resource network_interface_id already exists")

    record = {
        "Ipv4Prefixes": ipv4_prefixes,
        "NetworkInterfaceId": network_interface_id,
        "PrivateIpAddresses": private_ip_addresses,
    }

    store.unassign_private_ip_addressess(network_interface_id, record)

    return {
    }
```
