---
id: "@specs/aws/ec2/unassign_ipv6_addresses"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_UnassignIpv6Addresses"
---

# UnassignIpv6Addresses

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/unassign_ipv6_addresses
> **spec:implements:** @kind:operation UnassignIpv6Addresses
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_UnassignIpv6Addresses.spec.md

Unassigns the specified IPv6 addresses or Prefix Delegation prefixes from a network interface.

## Input Shape: UnassignIpv6AddressesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Ipv6Addresses | list[str] |  | The IPv6 addresses to unassign from the network interface. |
| Ipv6Prefixes | list[str] |  | The IPv6 prefixes to unassign from the network interface. |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the network interface. |

## Output Shape: UnassignIpv6AddressesResult

- **NetworkInterfaceId** (str): The ID of the network interface.
- **UnassignedIpv6Addresses** (list[str]): The IPv6 addresses that have been unassigned from the network interface.
- **UnassignedIpv6Prefixes** (list[str]): The IPv6 prefixes that have been unassigned from the network interface.

## Implementation

```speclang
def unassign_ipv6_addresses(store, request: dict) -> dict:
    """Unassigns the specified IPv6 addresses or Prefix Delegation prefixes from a network interface."""
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")

    if store.unassign_ipv6_addressess(network_interface_id):
        raise ResourceInUseException(f"Resource network_interface_id already exists")

    record = {
        "Ipv6Prefixes": ipv6_prefixes,
        "NetworkInterfaceId": network_interface_id,
        "Ipv6Addresses": ipv6_addresses,
    }

    store.unassign_ipv6_addressess(network_interface_id, record)

    return {
        "NetworkInterfaceId": network_interface_id,
        "UnassignedIpv6Addresses": record.get("UnassignedIpv6Addresses", {}),
        "UnassignedIpv6Prefixes": record.get("UnassignedIpv6Prefixes", {}),
    }
```
