---
id: "@specs/aws/ec2/enable_vpc_classic_link"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_EnableVpcClassicLink"
---

# EnableVpcClassicLink

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/enable_vpc_classic_link
> **spec:implements:** @kind:operation EnableVpcClassicLink
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_EnableVpcClassicLink.spec.md

This action is deprecated. Enables a VPC for ClassicLink. You can then link EC2-Classic instances to your ClassicLink-enabled VPC to allow communication over private IP addresses. You cannot enable your VPC for ClassicLink if any of your VPC route tables have existing routes for address ranges within the 10.0.0.0/8 IP address range, excluding local routes for VPCs in the 10.0.0.0/16 and 10.1.0.0/16 IP address ranges.

## Input Shape: EnableVpcClassicLinkRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: EnableVpcClassicLinkResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def enable_vpc_classic_link(store, request: dict) -> dict:
    """This action is deprecated. Enables a VPC for ClassicLink. You can then link EC2-Classic instances to your ClassicLink-enabled VPC to allow communication over private IP addresses. You cannot enable yo"""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    resource = store.enable_vpc_classic_links(vpc_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.enable_vpc_classic_links(vpc_id, resource)
    return resource
```
