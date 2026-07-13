---
id: "@specs/aws/ec2/delete_vpc_block_public_access_exclusion"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVpcBlockPublicAccessExclusion"
---

# DeleteVpcBlockPublicAccessExclusion

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_vpc_block_public_access_exclusion
> **spec:implements:** @kind:operation DeleteVpcBlockPublicAccessExclusion
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVpcBlockPublicAccessExclusion.spec.md

Delete a VPC Block Public Access (BPA) exclusion. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional or egress-only access. You can create BPA exclusions for VPCs and subnets even when BPA is not enabled on the account to ensure that there is no traffic disruption to the exclusions when VPC BPA is turned on. To learn more about VPC BPA, see Block public access to VPCs and subnets in the Amazon VPC User Guide .

## Input Shape: DeleteVpcBlockPublicAccessExclusionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| ExclusionId | Any  # complex shape | ✓ | The ID of the exclusion. |

## Output Shape: DeleteVpcBlockPublicAccessExclusionResult

- **VpcBlockPublicAccessExclusion** (Any  # complex shape): Details about an exclusion.

## Implementation

```speclang
def delete_vpc_block_public_access_exclusion(store, request: dict) -> dict:
    """Delete a VPC Block Public Access (BPA) exclusion. A VPC BPA exclusion is a mode that can be applied to a single VPC or subnet that exempts it from the account’s BPA mode and will allow bidirectional o"""
    exclusion_id = request.get("ExclusionId", "").strip() if isinstance(request.get("ExclusionId"), str) else request.get("ExclusionId")

    if not store.vpc_block_public_access_exclusions(exclusion_id):
        raise ResourceNotFoundException(f"Resource exclusion_id not found")
    store.delete_vpc_block_public_access_exclusions(exclusion_id)
    return {}
```
