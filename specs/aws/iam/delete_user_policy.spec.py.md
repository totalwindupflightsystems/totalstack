---
id: "@specs/aws/iam/delete_user_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteUserPolicy"
---

# DeleteUserPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_user_policy
> **spec:implements:** @kind:operation DeleteUserPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteUserPolicy.spec.md

Deletes the specified inline policy that is embedded in the specified IAM user. A user can also have managed policies attached to it. To detach a managed policy from a user, use DetachUserPolicy . For more information about policies, refer to Managed policies and inline policies in the IAM User Guide .

## Input Shape: DeleteUserPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyName | Any  # complex shape | ✓ | The name identifying the policy document to delete. This parameter allows (through its regex pattern ) a string of chara |
| UserName | Any  # complex shape | ✓ | The name (friendly name, not ARN) identifying the user that the policy is embedded in. This parameter allows (through it |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_user_policy(store, request: dict) -> dict:
    """Deletes the specified inline policy that is embedded in the specified IAM user. A user can also have managed policies attached to it. To detach a managed policy from a user, use DetachUserPolicy . For"""
    policy_name = request.get("PolicyName", "").strip() if isinstance(request.get("PolicyName"), str) else request.get("PolicyName")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")

    if not store.user_policys(user_name):
        raise ResourceNotFoundException(f"Resource user_name not found")
    store.delete_user_policys(user_name)
    return {}
```
