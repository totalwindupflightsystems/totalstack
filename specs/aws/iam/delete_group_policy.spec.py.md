---
id: "@specs/aws/iam/delete_group_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteGroupPolicy"
---

# DeleteGroupPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_group_policy
> **spec:implements:** @kind:operation DeleteGroupPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteGroupPolicy.spec.md

Deletes the specified inline policy that is embedded in the specified IAM group. A group can also have managed policies attached to it. To detach a managed policy from a group, use DetachGroupPolicy . For more information about policies, refer to Managed policies and inline policies in the IAM User Guide .

## Input Shape: DeleteGroupPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GroupName | Any  # complex shape | ✓ | The name (friendly name, not ARN) identifying the group that the policy is embedded in. This parameter allows (through i |
| PolicyName | Any  # complex shape | ✓ | The name identifying the policy document to delete. This parameter allows (through its regex pattern ) a string of chara |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_group_policy(store, request: dict) -> dict:
    """Deletes the specified inline policy that is embedded in the specified IAM group. A group can also have managed policies attached to it. To detach a managed policy from a group, use DetachGroupPolicy ."""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    policy_name = request.get("PolicyName", "").strip() if isinstance(request.get("PolicyName"), str) else request.get("PolicyName")

    if not store.group_policys(group_name):
        raise ResourceNotFoundException(f"Resource group_name not found")
    store.delete_group_policys(group_name)
    return {}
```
