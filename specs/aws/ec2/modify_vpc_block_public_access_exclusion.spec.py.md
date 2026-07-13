---
id: "@specs/aws/ec2/modify_vpc_block_public_access_exclusion"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_ModifyVpcBlockPublicAccessExclusion"
---

# ModifyVpcBlockPublicAccessExclusion

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/modify_vpc_block_public_access_exclusion
> **spec:implements:** @kind:operation ModifyVpcBlockPublicAccessExclusion
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_ModifyVpcBlockPublicAccessExclusion.spec.md

Modify VPC Block Public Access (BPA) exclusions. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional or egress-only access. You can create BPA exclusions for VPCs and subnets even when BPA is not enabled on the account to ensure that there is no traffic disruption to the exclusions when VPC BPA is turned on.

## Input Shape: ModifyVpcBlockPublicAccessExclusionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ExclusionId | Any  # complex shape | ✓ | The ID of an exclusion. |
| InternetGatewayExclusionMode | Any  # complex shape | ✓ | The exclusion mode for internet gateway traffic. allow-bidirectional : Allow all internet traffic to and from the exclud |

## Output Shape: ModifyVpcBlockPublicAccessExclusionResult

- **VpcBlockPublicAccessExclusion** (Any  # complex shape): Details related to the exclusion.

## Implementation

```speclang
def modify_vpc_block_public_access_exclusion(store, request: dict) -> dict:
    """Modify VPC Block Public Access (BPA) exclusions. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional or"""
    exclusion_id = request.get("ExclusionId", "").strip() if isinstance(request.get("ExclusionId"), str) else request.get("ExclusionId")
    if not exclusion_id:
        raise ValidationException("ExclusionId is required")
    internet_gateway_exclusion_mode = request.get("InternetGatewayExclusionMode", "").strip() if isinstance(request.get("InternetGatewayExclusionMode"), str) else request.get("InternetGatewayExclusionMode")
    if not internet_gateway_exclusion_mode:
        raise ValidationException("InternetGatewayExclusionMode is required")

    resource = store.vpc_block_public_access_exclusions(exclusion_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource exclusion_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.vpc_block_public_access_exclusions(exclusion_id, resource)
    return resource
```
