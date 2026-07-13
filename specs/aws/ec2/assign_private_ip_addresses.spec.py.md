---
id: "@specs/aws/ec2/assign_private_ip_addresses"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssignPrivateIpAddresses"
---

# AssignPrivateIpAddresses

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/assign_private_ip_addresses
> **spec:implements:** @kind:operation AssignPrivateIpAddresses
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssignPrivateIpAddresses.spec.md

Assigns the specified secondary private IP addresses to the specified network interface. You can specify specific secondary IP addresses, or you can specify the number of secondary IP addresses to be automatically assigned from the subnet's CIDR block range. The number of secondary IP addresses that you can assign to an instance varies by instance type. For more information about Elastic IP addresses, see Elastic IP Addresses in the Amazon EC2 User Guide . When you move a secondary private IP address to another network interface, any Elastic IP address that is associated with the IP address is also moved. Remapping an IP address is an asynchronous operation. When you move an IP address from one network interface to another, check network/interfaces/macs/mac/local-ipv4s in the instance metadata to confirm that the remapping is complete. You must specify either the IP addresses or the IP address count in the request. You can optionally use Prefix Delegation on the network interface. You must specify either the IPv4 Prefix Delegation prefixes, or the IPv4 Prefix Delegation count. For information, see Assigning prefixes to network interfaces in the Amazon EC2 User Guide .

## Input Shape: AssignPrivateIpAddressesRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllowReassignment | bool |  | Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassig |
| Ipv4PrefixCount | int |  | The number of IPv4 prefixes that Amazon Web Services automatically assigns to the network interface. You can't use this  |
| Ipv4Prefixes | list[str] |  | One or more IPv4 prefixes assigned to the network interface. You can't use this option if you use the Ipv4PrefixCount op |
| NetworkInterfaceId | Any  # complex shape | ✓ | The ID of the network interface. |
| PrivateIpAddresses | list[str] |  | The IP addresses to be assigned as a secondary private IP address to the network interface. You can't specify this param |
| SecondaryPrivateIpAddressCount | int |  | The number of secondary IP addresses to assign to the network interface. You can't specify this parameter when also spec |

## Output Shape: AssignPrivateIpAddressesResult

- **AssignedIpv4Prefixes** (list[Any  # complex shape]): The IPv4 prefixes that are assigned to the network interface.
- **AssignedPrivateIpAddresses** (list[Any  # complex shape]): The private IP addresses assigned to the network interface.
- **NetworkInterfaceId** (str): The ID of the network interface.

## Implementation

```speclang
def assign_private_ip_addresses(store, request: dict) -> dict:
    """Assigns the specified secondary private IP addresses to the specified network interface. You can specify specific secondary IP addresses, or you can specify the number of secondary IP addresses to be """
    network_interface_id = request.get("NetworkInterfaceId", "").strip() if isinstance(request.get("NetworkInterfaceId"), str) else request.get("NetworkInterfaceId")
    if not network_interface_id:
        raise ValidationException("NetworkInterfaceId is required")

    if store.assign_private_ip_addressess(network_interface_id):
        raise ResourceInUseException(f"Resource network_interface_id already exists")

    record = {
        "Ipv4Prefixes": ipv4_prefixes,
        "Ipv4PrefixCount": ipv4_prefix_count,
        "NetworkInterfaceId": network_interface_id,
        "PrivateIpAddresses": private_ip_addresses,
        "SecondaryPrivateIpAddressCount": secondary_private_ip_address_count,
        "AllowReassignment": allow_reassignment,
    }

    store.assign_private_ip_addressess(network_interface_id, record)

    return {
        "NetworkInterfaceId": network_interface_id,
        "AssignedPrivateIpAddresses": record.get("AssignedPrivateIpAddresses", {}),
        "AssignedIpv4Prefixes": record.get("AssignedIpv4Prefixes", {}),
    }
```
