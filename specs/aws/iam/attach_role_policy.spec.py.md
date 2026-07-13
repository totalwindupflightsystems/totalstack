---
id: "@specs/aws/iam/attach_role_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_AttachRolePolicy"
---

# AttachRolePolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/attach_role_policy
> **spec:implements:** @kind:operation AttachRolePolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_AttachRolePolicy.spec.md

Attaches the specified managed policy to the specified IAM role. When you attach a managed policy to a role, the managed policy becomes part of the role's permission (access) policy. You cannot use a managed policy as the role's trust policy. The role's trust policy is created at the same time as the role, using CreateRole . You can update a role's trust policy using UpdateAssumerolePolicy . Use this operation to attach a managed policy to a role. To embed an inline policy in a role, use PutRolePolicy . For more information about policies, see Managed policies and inline policies in the IAM User Guide . As a best practice, you can validate your IAM policies. To learn more, see Validating IAM policies in the IAM User Guide .

## Input Shape: AttachRolePolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM policy you want to attach. For more information about ARNs, see Amazon Resourc |
| RoleName | Any  # complex shape | ✓ | The name (friendly name, not ARN) of the role to attach the policy to. This parameter allows (through its regex pattern  |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **PolicyNotAttachableException**: The request failed because Amazon Web Services service role policies can only be attached to the service-linked role for that service.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def attach_role_policy(store, request: dict) -> dict:
    """Attaches the specified managed policy to the specified IAM role. When you attach a managed policy to a role, the managed policy becomes part of the role's permission (access) policy. You cannot use a """
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AttachRolePolicy", request)
```
