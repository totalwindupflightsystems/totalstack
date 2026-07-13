---
id: "@specs/aws/iam/delete_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeletePolicy"
---

# DeletePolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_policy
> **spec:implements:** @kind:operation DeletePolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeletePolicy.spec.md

Deletes the specified managed policy. Before you can delete a managed policy, you must first detach the policy from all users, groups, and roles that it is attached to. In addition, you must delete all the policy's versions. The following steps describe the process for deleting a managed policy: Detach the policy from all users, groups, and roles that the policy is attached to, using DetachUserPolicy , DetachGroupPolicy , or DetachRolePolicy . To list all the users, groups, and roles that a policy is attached to, use ListEntitiesForPolicy . Delete all versions of the policy using DeletePolicyVersion . To list the policy's versions, use ListPolicyVersions . You cannot use DeletePolicyVersion to delete the version that is marked as the default version. You delete the policy's default version in the next step of the process. Delete the policy (this automatically deletes the policy's default version) using this operation. For information about managed policies, see Managed policies and inline policies in the IAM User Guide .

## Input Shape: DeletePolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM policy you want to delete. For more information about ARNs, see Amazon Resourc |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **DeleteConflictException**: The request was rejected because it attempted to delete a resource that has attached subordinate entities. The error message describes these entities.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_policy(store, request: dict) -> dict:
    """Deletes the specified managed policy. Before you can delete a managed policy, you must first detach the policy from all users, groups, and roles that it is attached to. In addition, you must delete al"""
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")

    if not store.policys(policy_arn):
        raise ResourceNotFoundException(f"Resource policy_arn not found")
    store.delete_policys(policy_arn)
    return {}
```
