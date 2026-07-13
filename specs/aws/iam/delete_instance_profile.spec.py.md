---
id: "@specs/aws/iam/delete_instance_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteInstanceProfile"
---

# DeleteInstanceProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_instance_profile
> **spec:implements:** @kind:operation DeleteInstanceProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteInstanceProfile.spec.md

Deletes the specified instance profile. The instance profile must not have an associated role. Make sure that you do not have any Amazon EC2 instances running with the instance profile you are about to delete. Deleting a role or instance profile that is associated with a running instance will break any applications running on the instance. For more information about instance profiles, see Using instance profiles in the IAM User Guide .

## Input Shape: DeleteInstanceProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| InstanceProfileName | Any  # complex shape | ✓ | The name of the instance profile to delete. This parameter allows (through its regex pattern ) a string of characters co |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **DeleteConflictException**: The request was rejected because it attempted to delete a resource that has attached subordinate entities. The error message describes these entities.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_instance_profile(store, request: dict) -> dict:
    """Deletes the specified instance profile. The instance profile must not have an associated role. Make sure that you do not have any Amazon EC2 instances running with the instance profile you are about t"""
    instance_profile_name = request.get("InstanceProfileName", "").strip() if isinstance(request.get("InstanceProfileName"), str) else request.get("InstanceProfileName")

    if not store.instance_profiles(instance_profile_name):
        raise ResourceNotFoundException(f"Resource instance_profile_name not found")
    store.delete_instance_profiles(instance_profile_name)
    return {}
```
