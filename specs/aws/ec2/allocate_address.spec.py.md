---
id: "@specs/aws/ec2/allocate_address"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AllocateAddress"
---

# AllocateAddress

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/allocate_address
> **spec:implements:** @kind:operation AllocateAddress
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AllocateAddress.spec.md

Allocates an Elastic IP address to your Amazon Web Services account. After you allocate the Elastic IP address you can associate it with an instance or network interface. After you release an Elastic IP address, it is released to the IP address pool and can be allocated to a different Amazon Web Services account. You can allocate an Elastic IP address from one of the following address pools: Amazon's pool of IPv4 addresses Public IPv4 address range that you own and bring to your Amazon Web Services account using Bring Your Own IP Addresses (BYOIP) An IPv4 IPAM pool with an Amazon-provided or BYOIP public IPv4 address range IPv4 addresses from your on-premises network made available for use with an Outpost using a customer-owned IP address pool (CoIP pool) For more information, see Elastic IP Addresses in the Amazon EC2 User Guide . If you release an Elastic IP address, you might be able to recover it. You cannot recover an Elastic IP address that you released after it is allocated to another Amazon Web Services account. To attempt to recover an Elastic IP address that you released, specify it in this operation. You can allocate a carrier IP address which is a public IP address from a telecommunication carrier, to a network interface which resides in a subnet in a Wavelength Zone (for example an EC2 instance).

## Input Shape: AllocateAddressRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Address | Any  # complex shape |  | The Elastic IP address to recover or an IPv4 address from an address pool. |
| CustomerOwnedIpv4Pool | str |  | The ID of a customer-owned address pool. Use this parameter to let Amazon EC2 select an address from the address pool. A |
| Domain | Any  # complex shape |  | The network ( vpc ). |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| IpamPoolId | Any  # complex shape |  | The ID of an IPAM pool which has an Amazon-provided or BYOIP public IPv4 CIDR provisioned to it. For more information, s |
| NetworkBorderGroup | str |  | A unique set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addres |
| PublicIpv4Pool | Any  # complex shape |  | The ID of an address pool that you own. Use this parameter to let Amazon EC2 select an address from the address pool. To |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the Elastic IP address. |

## Output Shape: AllocateAddressResult

- **AllocationId** (str): The ID that represents the allocation of the Elastic IP address.
- **CarrierIp** (str): The carrier IP address. Available only for network interfaces that reside in a subnet in a Wavelength Zone.
- **CustomerOwnedIp** (str): The customer-owned IP address.
- **CustomerOwnedIpv4Pool** (str): The ID of the customer-owned address pool.
- **Domain** (Any  # complex shape): The network ( vpc ).
- **NetworkBorderGroup** (str): The set of Availability Zones, Local Zones, or Wavelength Zones from which Amazon Web Services advertises IP addresses.
- **PublicIp** (str): The Amazon-owned IP address. Not available when using an address pool that you own.
- **PublicIpv4Pool** (str): The ID of an address pool that you own.

## Implementation

```speclang
def allocate_address(store, request: dict) -> dict:
    """Allocates an Elastic IP address to your Amazon Web Services account. After you allocate the Elastic IP address you can associate it with an instance or network interface. After you release an Elastic """


    record = {
        "Domain": domain,
        "Address": address,
        "PublicIpv4Pool": public_ipv4_pool,
        "NetworkBorderGroup": network_border_group,
        "CustomerOwnedIpv4Pool": customer_owned_ipv4_pool,
        "TagSpecifications": tag_specifications,
        "IpamPoolId": ipam_pool_id,
        "DryRun": dry_run,
    }

    store.allocate_addresss(record)

    return {
        "AllocationId": record.get("AllocationId", {}),
        "PublicIpv4Pool": record.get("PublicIpv4Pool", {}),
        "NetworkBorderGroup": record.get("NetworkBorderGroup", {}),
        "Domain": record.get("Domain", {}),
        "CustomerOwnedIp": record.get("CustomerOwnedIp", {}),
        "CustomerOwnedIpv4Pool": record.get("CustomerOwnedIpv4Pool", {}),
        "CarrierIp": record.get("CarrierIp", {}),
        "PublicIp": record.get("PublicIp", {}),
    }
```
