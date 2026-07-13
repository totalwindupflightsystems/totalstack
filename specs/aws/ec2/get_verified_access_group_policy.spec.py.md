---
id: "@specs/aws/ec2/get_verified_access_group_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/ec2/plan"
  - "@specs/aws/ec2/docs/API_GetVerifiedAccessGroupPolicy"
---

# GetVerifiedAccessGroupPolicy

> **spec:trace:** specs/aws/ec2/ec2.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/ec2/get_verified_access_group_policy
> **spec:implements:** @kind:operation GetVerifiedAccessGroupPolicy
> **AWS Protocol:** ec2
> **HTTP:** POST /
> **@ref:** specs/aws/ec2/docs/API_GetVerifiedAccessGroupPolicy.spec.md

Shows the contents of the Verified Access policy associated with the group.

## Input Shape: GetVerifiedAccessGroupPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DryRun | bool |  | Checks whether you have the required permissions for the action, without actually making the request, and provides an er |
| VerifiedAccessGroupId | Any  # complex shape | ✓ | The ID of the Verified Access group. |

## Output Shape: GetVerifiedAccessGroupPolicyResult

- **PolicyDocument** (str): The Verified Access policy document.
- **PolicyEnabled** (bool): The status of the Verified Access policy.

## Implementation

```speclang
def get_verified_access_group_policy(store, request: dict) -> dict:
    """Shows the contents of the Verified Access policy associated with the group."""
    verified_access_group_id = request.get("VerifiedAccessGroupId", "").strip() if isinstance(request.get("VerifiedAccessGroupId"), str) else request.get("VerifiedAccessGroupId")
    if not verified_access_group_id:
        raise ValidationException("VerifiedAccessGroupId is required")

    resource = store.verified_access_group_policys(verified_access_group_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource verified_access_group_id not found")
    return {"VerifiedAccessGroupId": verified_access_group_id, **resource}
```
