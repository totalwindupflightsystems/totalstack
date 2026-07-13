---
id: "@specs/aws/iam/detach_group_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DetachGroupPolicy"
---

# DetachGroupPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/detach_group_policy
> **spec:implements:** @kind:operation DetachGroupPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DetachGroupPolicy.spec.md

Removes the specified managed policy from the specified IAM group. A group can also have inline policies embedded with it. To delete an inline policy, use DeleteGroupPolicy . For information about policies, see Managed policies and inline policies in the IAM User Guide .

## Input Shape: DetachGroupPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| GroupName | Any  # complex shape | ✓ | The name (friendly name, not ARN) of the IAM group to detach the policy from. This parameter allows (through its regex p |
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM policy you want to detach. For more information about ARNs, see Amazon Resourc |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def detach_group_policy(store, request: dict) -> dict:
    """Removes the specified managed policy from the specified IAM group. A group can also have inline policies embedded with it. To delete an inline policy, use DeleteGroupPolicy . For information about pol"""
    group_name = request.get("GroupName", "").strip() if isinstance(request.get("GroupName"), str) else request.get("GroupName")
    if not group_name:
        raise ValidationException("GroupName is required")
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("DetachGroupPolicy", request)
```
