---
id: "@specs/aws/ec2/associate_vpc_cidr_block"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_AssociateVpcCidrBlock"
---

# AssociateVpcCidrBlock

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/associate_vpc_cidr_block
> **spec:implements:** @kind:operation AssociateVpcCidrBlock
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_AssociateVpcCidrBlock.spec.md

Associates a CIDR block with your VPC. You can associate a secondary IPv4 CIDR block, an Amazon-provided IPv6 CIDR block, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP addresses ( BYOIP ). You must specify one of the following in the request: an IPv4 CIDR block, an IPv6 pool, or an Amazon-provided IPv6 CIDR block. For more information about associating CIDR blocks with your VPC and applicable restrictions, see IP addressing for your VPCs and subnets in the Amazon VPC User Guide .

## Input Shape: AssociateVpcCidrBlockRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AmazonProvidedIpv6CidrBlock | bool |  | Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IPv6 a |
| CidrBlock | str |  | An IPv4 CIDR block to associate with the VPC. |
| Ipv4IpamPoolId | Any  # complex shape |  | Associate a CIDR allocated from an IPv4 IPAM pool to a VPC. For more information about Amazon VPC IP Address Manager (IP |
| Ipv4NetmaskLength | Any  # complex shape |  | The netmask length of the IPv4 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool. For m |
| Ipv6CidrBlock | str |  | An IPv6 CIDR block from the IPv6 address pool. You must also specify Ipv6Pool in the request. To let Amazon choose the I |
| Ipv6CidrBlockNetworkBorderGroup | str |  | The name of the location from which we advertise the IPV6 CIDR block. Use this parameter to limit the CIDR block to this |
| Ipv6IpamPoolId | Any  # complex shape |  | Associates a CIDR allocated from an IPv6 IPAM pool to a VPC. For more information about Amazon VPC IP Address Manager (I |
| Ipv6NetmaskLength | Any  # complex shape |  | The netmask length of the IPv6 CIDR you would like to associate from an Amazon VPC IP Address Manager (IPAM) pool. For m |
| Ipv6Pool | Any  # complex shape |  | The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block. |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: AssociateVpcCidrBlockResult

- **CidrBlockAssociation** (Any  # complex shape): Information about the IPv4 CIDR block association.
- **Ipv6CidrBlockAssociation** (Any  # complex shape): Information about the IPv6 CIDR block association.
- **VpcId** (str): The ID of the VPC.

## Implementation

```speclang
def associate_vpc_cidr_block(store, request: dict) -> dict:
    """Associates a CIDR block with your VPC. You can associate a secondary IPv4 CIDR block, an Amazon-provided IPv6 CIDR block, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through b"""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssociateVpcCidrBlock", request)
```
