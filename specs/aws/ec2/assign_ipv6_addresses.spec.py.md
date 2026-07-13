---
id: "@specs/aws/ec2/assign_ipv6_addresses"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssignIpv6Addresses"
---

# AssignIpv6Addresses

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/assign_ipv6_addresses
> **spec:implements:** @kind:operation AssignIpv6Addresses
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssignIpv6Addresses.spec.md

Assigns the specified IPv6 addresses to the specified network interface. You can specify specific IPv6 addresses, or you can specify the number of IPv6 addresses to be automatically assigned from the subnet's IPv6 CIDR block range. You can assign as many IPv6 addresses to a network interface as you can assign private IPv4 addresses, and the limit varies by instance type. You must specify either the IPv6 addresses or the IPv6 address count in the request. You can optionally use Prefix Delegation on the network interface. You must specify either the IPV6 Prefix Delegation prefixes, or the IPv6 Prefix Delegation count. For information, see Assigning prefixes to network interfaces in the Amazon EC2 User Guide .

## Input Shape: AssignIpv6AddressesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Ipv6AddressCount | int |  | The number of additional IPv6 addresses to assign to the network interface. The specified number of IPv6 addresses are a |
| Ipv6Addresses | list[str] |  | The IPv6 addresses to be assigned to the network interface. You can't use this option if you're specifying a number of I |
| Ipv6PrefixCount | int |  | The number of IPv6 prefixes that Amazon Web Services automatically assigns to the network interface. You cannot use this |
| Ipv6Prefixes | list[str] |  | One or more IPv6 prefixes assigned to the network interface. You can't use this option if you use the Ipv6PrefixCount op |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the network interface. |

## Output Shape: AssignIpv6AddressesResult

- **AssignedIpv6Addresses** (list[str]): The new IPv6 addresses assigned to the network interface. Existing IPv6 addresses that were assigned to the network inte
- **AssignedIpv6Prefixes** (list[str]): The IPv6 prefixes that are assigned to the network interface.
- **NetworkInterfaceId** (str): The ID of the network interface.

## Implementation

```speclang
def assign_ipv6_addresses(store, request: dict) -> dict:
    """Assigns the specified IPv6 addresses to the specified network interface. You can specify specific IPv6 addresses, or you can specify the number of IPv6 addresses to be automatically assigned from the """
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")

    if store.assign_ipv6_addressess(network_interface_id):
        raise ResourceInUseException(f"Resource network_interface_id already exists")

    record = {
        "Ipv6PrefixCount": ipv6_prefix_count,
        "Ipv6Prefixes": ipv6_prefixes,
        "NetworkInterfaceId": network_interface_id,
        "Ipv6Addresses": ipv6_addresses,
        "Ipv6AddressCount": ipv6_address_count,
    }

    store.assign_ipv6_addressess(network_interface_id, record)

    return {
        "AssignedIpv6Addresses": record.get("AssignedIpv6Addresses", {}),
        "AssignedIpv6Prefixes": record.get("AssignedIpv6Prefixes", {}),
        "NetworkInterfaceId": network_interface_id,
    }
```
