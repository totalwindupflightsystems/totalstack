---
id: "@specs/aws/ec2/create_vpc"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpc"
---

# CreateVpc

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpc
> **spec:implements:** @kind:operation CreateVpc
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpc.spec.md

Creates a VPC with the specified CIDR blocks. A VPC must have an associated IPv4 CIDR block. You can choose an IPv4 CIDR block or an IPAM-allocated IPv4 CIDR block. You can optionally associate an IPv6 CIDR block with a VPC. You can choose an IPv6 CIDR block, an Amazon-provided IPv6 CIDR block, an IPAM-allocated IPv6 CIDR block, or an IPv6 CIDR block that you brought to Amazon Web Services. For more information, see IP addressing for your VPCs and subnets in the Amazon VPC User Guide . By default, each instance that you launch in the VPC has the default DHCP options, which include only a default DNS server that we provide (AmazonProvidedDNS). For more information, see DHCP option sets in the Amazon VPC User Guide . You can specify DNS options and tenancy for a VPC when you create it. You can't change the tenancy of a VPC after you create it. For more information, see VPC configuration options in the Amazon VPC User Guide .

## Input Shape: CreateVpcRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AmazonProvidedIpv6CidrBlock | bool |  | Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP add |
| CidrBlock | str |  | The IPv4 network range for the VPC, in CIDR notation. For example, 10.0.0.0/16 . We modify the specified CIDR block to i |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InstanceTenancy | Any  # complex shape |  | The tenancy options for instances launched into the VPC. For default , instances are launched with shared tenancy by def |
| Ipv4IpamPoolId | Any  # complex shape |  | The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see What is IPAM? in t |
| Ipv4NetmaskLength | Any  # complex shape |  | The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool.  |
| Ipv6CidrBlock | str |  | The IPv6 CIDR block from the IPv6 address pool. You must also specify Ipv6Pool in the request. To let Amazon choose the  |
| Ipv6CidrBlockNetworkBorderGroup | str |  | The name of the location from which we advertise the IPV6 CIDR block. Use this parameter to limit the address to this lo |
| Ipv6IpamPoolId | Any  # complex shape |  | The ID of an IPv6 IPAM pool which will be used to allocate this VPC an IPv6 CIDR. IPAM is a VPC feature that you can use |
| Ipv6NetmaskLength | Any  # complex shape |  | The netmask length of the IPv6 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool.  |
| Ipv6Pool | Any  # complex shape |  | The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the VPC. |
| VpcEncryptionControl | Any  # complex shape |  | Specifies the encryption control configuration to apply to the VPC during creation. VPC Encryption Control enables you t |

## Output Shape: CreateVpcResult

- **Vpc** (Any  # complex shape): Information about the VPC.

## Implementation

```speclang
def create_vpc(store, request: dict) -> dict:
    """Creates a VPC with the specified CIDR blocks. A VPC must have an associated IPv4 CIDR block. You can choose an IPv4 CIDR block or an IPAM-allocated IPv4 CIDR block. You can optionally associate an IPv"""


    record = {
        "CidrBlock": cidr_block,
        "Ipv6Pool": ipv6_pool,
        "Ipv6CidrBlock": ipv6_cidr_block,
        "Ipv4IpamPoolId": ipv4_ipam_pool_id,
        "Ipv4NetmaskLength": ipv4_netmask_length,
        "Ipv6IpamPoolId": ipv6_ipam_pool_id,
        "Ipv6NetmaskLength": ipv6_netmask_length,
        "Ipv6CidrBlockNetworkBorderGroup": ipv6_cidr_block_network_border_group,
        "VpcEncryptionControl": vpc_encryption_control,
        "TagSpecifications": tag_specifications,
        "DryRun": dry_run,
        "InstanceTenancy": instance_tenancy,
        "AmazonProvidedIpv6CidrBlock": amazon_provided_ipv6_cidr_block,
    }

    store.vpcs(record)

    return {
        "Vpc": record.get("Vpc", {}),
    }
```
