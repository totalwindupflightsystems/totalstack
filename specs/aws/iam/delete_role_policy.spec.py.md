---
id: "@specs/aws/iam/delete_role_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteRolePolicy"
---

# DeleteRolePolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_role_policy
> **spec:implements:** @kind:operation DeleteRolePolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteRolePolicy.spec.md

Deletes the specified inline policy that is embedded in the specified IAM role. A role can also have managed policies attached to it. To detach a managed policy from a role, use DetachRolePolicy . For more information about policies, refer to Managed policies and inline policies in the IAM User Guide .

## Input Shape: DeleteRolePolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyName | Any  # complex shape | ✓ | The name of the inline policy to delete from the specified IAM role. This parameter allows (through its regex pattern )  |
| RoleName | Any  # complex shape | ✓ | The name (friendly name, not ARN) identifying the role that the policy is embedded in. This parameter allows (through it |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_role_policy(store, request: dict) -> dict:
    """Deletes the specified inline policy that is embedded in the specified IAM role. A role can also have managed policies attached to it. To detach a managed policy from a role, use DetachRolePolicy . For"""
    policy_name = request.get("PolicyName", "").strip() if isinstance(request.get("PolicyName"), str) else request.get("PolicyName")
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")

    if not store.role_policys(policy_name):
        raise ResourceNotFoundException(f"Resource policy_name not found")
    store.delete_role_policys(policy_name)
    return {}
```
