---
id: "@specs/aws/ec2/create_default_subnet"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateDefaultSubnet"
---

# CreateDefaultSubnet

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_default_subnet
> **spec:implements:** @kind:operation CreateDefaultSubnet
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateDefaultSubnet.spec.md

Creates a default subnet with a size /20 IPv4 CIDR block in the specified Availability Zone in your default VPC. You can have only one default subnet per Availability Zone. For more information, see Create a default subnet in the Amazon VPC User Guide .

## Input Shape: CreateDefaultSubnetRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AvailabilityZone | Any  # complex shape |  | The Availability Zone in which to create the default subnet. Either AvailabilityZone or AvailabilityZoneId must be speci |
| AvailabilityZoneId | Any  # complex shape |  | The ID of the Availability Zone. Either AvailabilityZone or AvailabilityZoneId must be specified, but not both. |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| Ipv6Native | bool |  | Indicates whether to create an IPv6 only subnet. If you already have a default subnet for this Availability Zone, you mu |

## Output Shape: CreateDefaultSubnetResult

- **Subnet** (Any  # complex shape): Information about the subnet.

## Implementation

```speclang
def create_default_subnet(store, request: dict) -> dict:
    """Creates a default subnet with a size /20 IPv4 CIDR block in the specified Availability Zone in your default VPC. You can have only one default subnet per Availability Zone. For more information, see C"""


    record = {
        "AvailabilityZone": availability_zone,
        "DryRun": dry_run,
        "Ipv6Native": ipv6_native,
        "AvailabilityZoneId": availability_zone_id,
    }

    store.default_subnets(record)

    return {
        "Subnet": record.get("Subnet", {}),
    }
```
