---
id: "@specs/aws/iam/attach_user_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_AttachUserPolicy"
---

# AttachUserPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/attach_user_policy
> **spec:implements:** @kind:operation AttachUserPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_AttachUserPolicy.spec.md

Attaches the specified managed policy to the specified user. You use this operation to attach a managed policy to a user. To embed an inline policy in a user, use PutUserPolicy . As a best practice, you can validate your IAM policies. To learn more, see Validating IAM policies in the IAM User Guide . For more information about policies, see Managed policies and inline policies in the IAM User Guide .

## Input Shape: AttachUserPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM policy you want to attach. For more information about ARNs, see Amazon Resourc |
| UserName | Any  # complex shape | ✓ | The name (friendly name, not ARN) of the IAM user to attach the policy to. This parameter allows (through its regex patt |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **PolicyNotAttachableException**: The request failed because Amazon Web Services service role policies can only be attached to the service-linked role for that service.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def attach_user_policy(store, request: dict) -> dict:
    """Attaches the specified managed policy to the specified user. You use this operation to attach a managed policy to a user. To embed an inline policy in a user, use PutUserPolicy . As a best practice, y"""
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachUserPolicy", request)
```
