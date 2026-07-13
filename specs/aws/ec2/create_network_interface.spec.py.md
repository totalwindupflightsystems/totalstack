---
id: "@specs/aws/ec2/create_network_interface"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateNetworkInterface"
---

# CreateNetworkInterface

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_network_interface
> **spec:implements:** @kind:operation CreateNetworkInterface
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateNetworkInterface.spec.md

Creates a network interface in the specified subnet. The number of IP addresses you can assign to a network interface varies by instance type. For more information about network interfaces, see Elastic network interfaces in the Amazon EC2 User Guide .

## Input Shape: CreateNetworkInterfaceRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| ConnectionTrackingSpecification | Any  # complex shape |  | A connection tracking specification for the network interface. |
| Description | str |  | A description for the network interface. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| EnablePrimaryIpv6 | bool |  | If you’re creating a network interface in a dual-stack or IPv6-only subnet, you have the option to assign a primary IPv6 |
| Groups | list[Any  # complex shape] |  | The IDs of the security groups. |
| InterfaceType | Any  # complex shape |  | The type of network interface. The default is interface . If you specify efa-only , do not assign any IP addresses to th |
| Ipv4PrefixCount | int |  | The number of IPv4 prefixes that Amazon Web Services automatically assigns to the network interface. You can't specify a |
| Ipv4Prefixes | list[Any  # complex shape] |  | The IPv4 prefixes assigned to the network interface. You can't specify IPv4 prefixes if you've specified one of the foll |
| Ipv6AddressCount | int |  | The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from  |
| Ipv6Addresses | list[Any  # complex shape] |  | The IPv6 addresses from the IPv6 CIDR block range of your subnet. You can't specify IPv6 addresses using this parameter  |
| Ipv6PrefixCount | int |  | The number of IPv6 prefixes that Amazon Web Services automatically assigns to the network interface. You can't specify a |
| Ipv6Prefixes | list[Any  # complex shape] |  | The IPv6 prefixes assigned to the network interface. You can't specify IPv6 prefixes if you've specified one of the foll |
| Operator | Any  # complex shape |  | Reserved for internal use. |
| PrivateIpAddress | str |  | The primary private IPv4 address of the network interface. If you don't specify an IPv4 address, Amazon EC2 selects one  |
| PrivateIpAddresses | list[Any  # complex shape] |  | The private IPv4 addresses. You can't specify private IPv4 addresses if you've specified one of the following: a count o |
| SecondaryPrivateIpAddressCount | int |  | The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary  |
| SubnetId | Any  # complex shape | ✓ | The ID of the subnet to associate with the network interface. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to apply to the new network interface. |

## Output Shape: CreateNetworkInterfaceResult

- **ClientToken** (str): The token to use to retrieve the next page of results. This value is null when there are no more results to return.
- **NetworkInterface** (Any  # complex shape): Information about the network interface.

## Implementation

```speclang
def create_network_interface(store, request: dict) -> dict:
    """Creates a network interface in the specified subnet. The number of IP addresses you can assign to a network interface varies by instance type. For more information about network interfaces, see Elasti"""
    subnet_id = request.get("SubnetId", "").strip() if isinstance(request.get("SubnetId"), str) else request.get("SubnetId")
    if not subnet_id:
        raise ValidationException("SubnetId is required")

    if store.network_interfaces(subnet_id):
        raise ResourceInUseException(f"Resource subnet_id already exists")

    record = {
        "Ipv4Prefixes": ipv4_prefixes,
        "Ipv4PrefixCount": ipv4_prefix_count,
        "Ipv6Prefixes": ipv6_prefixes,
        "Ipv6PrefixCount": ipv6_prefix_count,
        "InterfaceType": interface_type,
        "TagSpecifications": tag_specifications,
        "ClientToken": client_token,
        "EnablePrimaryIpv6": enable_primary_ipv6,
        "ConnectionTrackingSpecification": connection_tracking_specification,
        "Operator": operator,
        "SubnetId": subnet_id,
        "Description": description,
        "PrivateIpAddress": private_ip_address,
        "Groups": groups,
        "PrivateIpAddresses": private_ip_addresses,
        "SecondaryPrivateIpAddressCount": secondary_private_ip_address_count,
        "Ipv6Addresses": ipv6_addresses,
        "Ipv6AddressCount": ipv6_address_count,
        "DryRun": dry_run,
    }

    store.network_interfaces(subnet_id, record)

    return {
        "NetworkInterface": record.get("NetworkInterface", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
