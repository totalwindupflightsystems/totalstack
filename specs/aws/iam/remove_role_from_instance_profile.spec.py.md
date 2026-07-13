---
id: "@specs/aws/iam/remove_role_from_instance_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_RemoveRoleFromInstanceProfile"
---

# RemoveRoleFromInstanceProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/remove_role_from_instance_profile
> **spec:implements:** @kind:operation RemoveRoleFromInstanceProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_RemoveRoleFromInstanceProfile.spec.md

Removes the specified IAM role from the specified Amazon EC2 instance profile. Make sure that you do not have any Amazon EC2 instances running with the role you are about to remove from the instance profile. Removing a role from an instance profile that is associated with a running instance might break any applications running on the instance. For more information about roles, see IAM roles in the IAM User Guide . For more information about instance profiles, see Using instance profiles in the IAM User Guide .

## Input Shape: RemoveRoleFromInstanceProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| InstanceProfileName | Any  # complex shape | ✓ | The name of the instance profile to update. This parameter allows (through its regex pattern ) a string of characters co |
| RoleName | Any  # complex shape | ✓ | The name of the role to remove. This parameter allows (through its regex pattern ) a string of characters consisting of  |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def remove_role_from_instance_profile(store, request: dict) -> dict:
    """Removes the specified IAM role from the specified Amazon EC2 instance profile. Make sure that you do not have any Amazon EC2 instances running with the role you are about to remove from the instance p"""
    instance_profile_name = request.get("InstanceProfileName", "").strip() if isinstance(request.get("InstanceProfileName"), str) else request.get("InstanceProfileName")
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")

    if not store.role_from_instance_profiles(role_name):
        raise ResourceNotFoundException(f"Resource role_name not found")
    store.delete_role_from_instance_profiles(role_name)
    return {}
```
