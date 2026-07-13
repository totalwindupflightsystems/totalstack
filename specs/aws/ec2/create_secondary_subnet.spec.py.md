---
id: "@specs/aws/ec2/create_secondary_subnet"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateSecondarySubnet"
---

# CreateSecondarySubnet

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_secondary_subnet
> **spec:implements:** @kind:operation CreateSecondarySubnet
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateSecondarySubnet.spec.md

Creates a secondary subnet in a secondary network. A secondary subnet CIDR block must not overlap with the CIDR block of an existing secondary subnet in the secondary network. After you create a secondary subnet, you can't change its CIDR block. The allowed size for a secondary subnet CIDR block is between /28 netmask (16 IP addresses) and /12 netmask (1,048,576 IP addresses). Amazon reserves the first four IP addresses and the last IP address in each secondary subnet for internal use.

## Input Shape: CreateSecondarySubnetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AvailabilityZone | Any  # complex shape |  | The Availability Zone for the secondary subnet. You cannot specify both AvailabilityZone and AvailabilityZoneId in the s |
| AvailabilityZoneId | Any  # complex shape |  | The ID of the Availability Zone for the secondary subnet. This option is preferred over AvailabilityZone as it provides  |
| ClientToken | str |  | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see E |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Ipv4CidrBlock | str | ✓ | The IPv4 CIDR block for the secondary subnet. The CIDR block size must be between /12 and /28. |
| SecondaryNetworkId | Any  # complex shape | ✓ | The ID of the secondary network in which to create the secondary subnet. |
| TagSpecifications | list[Any  # complex shape] |  | The tags to assign to the secondary subnet. |

## Output Shape: CreateSecondarySubnetResult

- **ClientToken** (str): Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided
- **SecondarySubnet** (Any  # complex shape): Information about the secondary subnet.

## Implementation

```speclang
def create_secondary_subnet(store, request: dict) -> dict:
    """Creates a secondary subnet in a secondary network. A secondary subnet CIDR block must not overlap with the CIDR block of an existing secondary subnet in the secondary network. After you create a secon"""
    ipv4_cidr_block = request.get("Ipv4CidrBlock", "").strip() if isinstance(request.get("Ipv4CidrBlock"), str) else request.get("Ipv4CidrBlock")
    if not ipv4_cidr_block:
        raise ValidationException("Ipv4CidrBlock is required")
    secondary_network_id = request.get("SecondaryNetworkId", "").strip() if isinstance(request.get("SecondaryNetworkId"), str) else request.get("SecondaryNetworkId")
    if not secondary_network_id:
        raise ValidationException("SecondaryNetworkId is required")

    if store.secondary_subnets(ipv4_cidr_block):
        raise ResourceInUseException(f"Resource ipv4_cidr_block already exists")

    record = {
        "ClientToken": client_token,
        "AvailabilityZone": availability_zone,
        "AvailabilityZoneId": availability_zone_id,
        "DryRun": dry_run,
        "Ipv4CidrBlock": ipv4_cidr_block,
        "SecondaryNetworkId": secondary_network_id,
        "TagSpecifications": tag_specifications,
    }

    store.secondary_subnets(ipv4_cidr_block, record)

    return {
        "SecondarySubnet": record.get("SecondarySubnet", {}),
        "ClientToken": record.get("ClientToken", {}),
    }
```
