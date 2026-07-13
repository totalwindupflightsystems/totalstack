---
id: "@specs/aws/iam/delete_policy_version"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeletePolicyVersion"
---

# DeletePolicyVersion

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_policy_version
> **spec:implements:** @kind:operation DeletePolicyVersion
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeletePolicyVersion.spec.md

Deletes the specified version from the specified managed policy. You cannot delete the default version from a policy using this operation. To delete the default version from a policy, use DeletePolicy . To find out which version of a policy is marked as the default version, use ListPolicyVersions . For information about versions for managed policies, see Versioning for managed policies in the IAM User Guide .

## Input Shape: DeletePolicyVersionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM policy from which you want to delete a version. For more information about ARN |
| VersionId | Any  # complex shape | ✓ | The policy version to delete. This parameter allows (through its regex pattern ) a string of characters that consists of |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **DeleteConflictException**: The request was rejected because it attempted to delete a resource that has attached subordinate entities. The error message describes these entities.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_policy_version(store, request: dict) -> dict:
    """Deletes the specified version from the specified managed policy. You cannot delete the default version from a policy using this operation. To delete the default version from a policy, use DeletePolicy"""
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    version_id = request.get("VersionId", "").strip() if isinstance(request.get("VersionId"), str) else request.get("VersionId")

    if not store.policy_versions(version_id):
        raise ResourceNotFoundException(f"Resource version_id not found")
    store.delete_policy_versions(version_id)
    return {}
```
