---
id: "@specs/aws/ec2/create_subnet"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateSubnet"
---

# CreateSubnet

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_subnet
> **spec:implements:** @kind:operation CreateSubnet
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateSubnet.spec.md

Creates a subnet in the specified VPC. For an IPv4 only subnet, specify an IPv4 CIDR block. If the VPC has an IPv6 CIDR block, you can create an IPv6 only subnet or a dual stack subnet instead. For an IPv6 only subnet, specify an IPv6 CIDR block. For a dual stack subnet, specify both an IPv4 CIDR block and an IPv6 CIDR block. A subnet CIDR block must not overlap the CIDR block of an existing subnet in the VPC. After you create a subnet, you can't change its CIDR block. The allowed size for an IPv4 subnet is between a /28 netmask (16 IP addresses) and a /16 netmask (65,536 IP addresses). Amazon Web Services reserves both the first four and the last IPv4 address in each subnet's CIDR block. They're not available for your use. If you've associated an IPv6 CIDR block with your VPC, you can associate an IPv6 CIDR block with a subnet when you create it. If you add more than one subnet to a VPC, they're set up in a star topology with a logical router in the middle. When you stop an instance in a subnet, it retains its private IPv4 address. It's therefore possible to have a subnet with no running instances (they're all stopped), but no remaining IP addresses available. For more information, see Subnets in the Amazon VPC User Guide .

## Input Shape: CreateSubnetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AvailabilityZone | str |  | The Availability Zone or Local Zone for the subnet. Default: Amazon Web Services selects one for you. If you create more |
| AvailabilityZoneId | str |  | The AZ ID or the Local Zone ID of the subnet. |
| CidrBlock | str |  | The IPv4 network range for the subnet, in CIDR notation. For example, 10.0.0.0/24 . We modify the specified CIDR block t |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Ipv4IpamPoolId | Any  # complex shape |  | An IPv4 IPAM pool ID for the subnet. |
| Ipv4NetmaskLength | Any  # complex shape |  | An IPv4 netmask length for the subnet. |
| Ipv6CidrBlock | str |  | The IPv6 network range for the subnet, in CIDR notation. This parameter is required for an IPv6 only subnet. |
| Ipv6IpamPoolId | Any  # complex shape |  | An IPv6 IPAM pool ID for the subnet. |
| Ipv6Native | bool |  | Indicates whether to create an IPv6 only subnet. |
| Ipv6NetmaskLength | Any  # complex shape |  | An IPv6 netmask length for the subnet. |
| OutpostArn | str |  | The Amazon Resource Name (ARN) of the Outpost. If you specify an Outpost ARN, you must also specify the Availability Zon |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the subnet. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: CreateSubnetResult

- **Subnet** (Any  # complex shape): Information about the subnet.

## Implementation

```speclang
def create_subnet(store, request: dict) -> dict:
    """Creates a subnet in the specified VPC. For an IPv4 only subnet, specify an IPv4 CIDR block. If the VPC has an IPv6 CIDR block, you can create an IPv6 only subnet or a dual stack subnet instead. For an"""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    if store.subnets(vpc_id):
        raise ResourceInUseException(f"Resource vpc_id already exists")

    record = {
        "TagSpecifications": tag_specifications,
        "AvailabilityZone": availability_zone,
        "AvailabilityZoneId": availability_zone_id,
        "CidrBlock": cidr_block,
        "Ipv6CidrBlock": ipv6_cidr_block,
        "OutpostArn": outpost_arn,
        "VpcId": vpc_id,
        "Ipv6Native": ipv6_native,
        "Ipv4IpamPoolId": ipv4_ipam_pool_id,
        "Ipv4NetmaskLength": ipv4_netmask_length,
        "Ipv6IpamPoolId": ipv6_ipam_pool_id,
        "Ipv6NetmaskLength": ipv6_netmask_length,
        "DryRun": dry_run,
    }

    store.subnets(vpc_id, record)

    return {
        "Subnet": record.get("Subnet", {}),
    }
```
