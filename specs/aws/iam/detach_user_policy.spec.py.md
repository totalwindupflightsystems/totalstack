---
id: "@specs/aws/iam/detach_user_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DetachUserPolicy"
---

# DetachUserPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/detach_user_policy
> **spec:implements:** @kind:operation DetachUserPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DetachUserPolicy.spec.md

Removes the specified managed policy from the specified user. A user can also have inline policies embedded with it. To delete an inline policy, use DeleteUserPolicy . For information about policies, see Managed policies and inline policies in the IAM User Guide .

## Input Shape: DetachUserPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM policy you want to detach. For more information about ARNs, see Amazon Resourc |
| UserName | Any  # complex shape | ✓ | The name (friendly name, not ARN) of the IAM user to detach the policy from. This parameter allows (through its regex pa |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def detach_user_policy(store, request: dict) -> dict:
    """Removes the specified managed policy from the specified user. A user can also have inline policies embedded with it. To delete an inline policy, use DeleteUserPolicy . For information about policies, """
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachUserPolicy", request)
```
