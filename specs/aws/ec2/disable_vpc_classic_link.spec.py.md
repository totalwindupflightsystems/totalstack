---
id: "@specs/aws/ec2/disable_vpc_classic_link"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DisableVpcClassicLink"
---

# DisableVpcClassicLink

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/disable_vpc_classic_link
> **spec:implements:** @kind:operation DisableVpcClassicLink
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DisableVpcClassicLink.spec.md

This action is deprecated. Disables ClassicLink for a VPC. You cannot disable ClassicLink for a VPC that has EC2-Classic instances linked to it.

## Input Shape: DisableVpcClassicLinkRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VpcId | Any  # complex shape | ✓ | The ID of the VPC. |

## Output Shape: DisableVpcClassicLinkResult

- **Return** (bool): Returns true if the request succeeds; otherwise, it returns an error.

## Implementation

```speclang
def disable_vpc_classic_link(store, request: dict) -> dict:
    """This action is deprecated. Disables ClassicLink for a VPC. You cannot disable ClassicLink for a VPC that has EC2-Classic instances linked to it."""
    vpc_id = request.get("VpcId", "").strip() if isinstance(request.get("VpcId"), str) else request.get("VpcId")
    if not vpc_id:
        raise ValidationException("VpcId is required")

    resource = store.disable_vpc_classic_links(vpc_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource vpc_id not found")

    # Update mutable fields
    if "DryRun" in request:
        resource["DryRun"] = dry_run

    store.disable_vpc_classic_links(vpc_id, resource)
    return resource
```
