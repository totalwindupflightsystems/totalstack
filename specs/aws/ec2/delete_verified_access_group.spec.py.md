---
id: "@specs/aws/ec2/delete_verified_access_group"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_DeleteVerifiedAccessGroup"
---

# DeleteVerifiedAccessGroup

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/delete_verified_access_group
> **spec:implements:** @kind:operation DeleteVerifiedAccessGroup
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_DeleteVerifiedAccessGroup.spec.md

Delete an Amazon Web Services Verified Access group.

## Input Shape: DeleteVerifiedAccessGroupRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| ClientToken | str |  | A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information |
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VerifiedAccessGroupId | Any  # complex shape | ✓ | The ID of the Verified Access group. |

## Output Shape: DeleteVerifiedAccessGroupResult

- **VerifiedAccessGroup** (Any  # complex shape): Details about the Verified Access group.

## Implementation

```speclang
def delete_verified_access_group(store, request: dict) -> dict:
    """Delete an Amazon Web Services Verified Access group."""
    verified_access_group_id = request.get("VerifiedAccessGroupId", "").strip() if isinstance(request.get("VerifiedAccessGroupId"), str) else request.get("VerifiedAccessGroupId")

    if not store.verified_access_groups(verified_access_group_id):
        raise ResourceNotFoundException(f"Resource verified_access_group_id not found")
    store.delete_verified_access_groups(verified_access_group_id)
    return {}
```
