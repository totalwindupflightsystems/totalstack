---
id: "@specs/aws/iam/set_default_policy_version"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_SetDefaultPolicyVersion"
---

# SetDefaultPolicyVersion

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/set_default_policy_version
> **spec:implements:** @kind:operation SetDefaultPolicyVersion
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_SetDefaultPolicyVersion.spec.md

Sets the specified version of the specified policy as the policy's default (operative) version. This operation affects all users, groups, and roles that the policy is attached to. To list the users, groups, and roles that the policy is attached to, use ListEntitiesForPolicy . For information about managed policies, see Managed policies and inline policies in the IAM User Guide .

## Input Shape: SetDefaultPolicyVersionRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| PolicyArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the IAM policy whose default version you want to set. For more information about ARNs, |
| VersionId | Any  # complex shape | ✓ | The version of the policy to set as the default (operative) version. For more information about managed policy versions, |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def set_default_policy_version(store, request: dict) -> dict:
    """Sets the specified version of the specified policy as the policy's default (operative) version. This operation affects all users, groups, and roles that the policy is attached to. To list the users, g"""
    policy_arn = request.get("PolicyArn", "").strip() if isinstance(request.get("PolicyArn"), str) else request.get("PolicyArn")
    if not policy_arn:
        raise ValidationException("PolicyArn is required")
    version_id = request.get("VersionId", "").strip() if isinstance(request.get("VersionId"), str) else request.get("VersionId")
    if not version_id:
        raise ValidationException("VersionId is required")

    resource = store.set_default_policy_versions(version_id)
    if not resource:
        raise ResourceNotFoundException(f"Resource version_id not found")

    # Update mutable fields

    store.set_default_policy_versions(version_id, resource)
    return resource
```
