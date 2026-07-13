---
id: "@specs/aws/ec2/create_vpc_block_public_access_exclusion"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_CreateVpcBlockPublicAccessExclusion"
---

# CreateVpcBlockPublicAccessExclusion

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/create_vpc_block_public_access_exclusion
> **spec:implements:** @kind:operation CreateVpcBlockPublicAccessExclusion
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_CreateVpcBlockPublicAccessExclusion.spec.md

Create a VPC Block Public Access (BPA) exclusion. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional or egress-only access. You can create BPA exclusions for VPCs and subnets even when BPA is not enabled on the account to ensure that there is no traffic disruption to the exclusions when VPC BPA is turned on. To learn more about VPC BPA, see Block public access to VPCs and subnets in the Amazon VPC User Guide .

## Input Shape: CreateVpcBlockPublicAccessExclusionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| InternetGatewayExclusionMode | Any  # complex shape | ✓ | The exclusion mode for internet gateway traffic. allow-bidirectional : Allow all internet traffic to and from the exclud |
| SubnetId | Any  # complex shape |  | A subnet ID. |
| TagSpecifications | list[Any  # complex shape] |  | tag - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value  |
| VpcId | Any  # complex shape |  | A VPC ID. |

## Output Shape: CreateVpcBlockPublicAccessExclusionResult

- **VpcBlockPublicAccessExclusion** (Any  # complex shape): Details about an exclusion.

## Implementation

```speclang
def create_vpc_block_public_access_exclusion(store, request: dict) -> dict:
    """Create a VPC Block Public Access (BPA) exclusion. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional o"""
    internet_gateway_exclusion_mode = request.get("InternetGatewayExclusionMode", "").strip() if isinstance(request.get("InternetGatewayExclusionMode"), str) else request.get("InternetGatewayExclusionMode")
    if not internet_gateway_exclusion_mode:
        raise ValidationException("InternetGatewayExclusionMode is required")

    if store.vpc_block_public_access_exclusions(internet_gateway_exclusion_mode):
        raise ResourceInUseException(f"Resource internet_gateway_exclusion_mode already exists")

    record = {
        "DryRun": dry_run,
        "SubnetId": subnet_id,
        "VpcId": vpc_id,
        "InternetGatewayExclusionMode": internet_gateway_exclusion_mode,
        "TagSpecifications": tag_specifications,
    }

    store.vpc_block_public_access_exclusions(internet_gateway_exclusion_mode, record)

    return {
        "VpcBlockPublicAccessExclusion": record.get("VpcBlockPublicAccessExclusion", {}),
    }
```
