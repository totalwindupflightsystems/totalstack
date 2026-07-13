---
id: "@specs/aws/iam/get_instance_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetInstanceProfile"
---

# GetInstanceProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_instance_profile
> **spec:implements:** @kind:operation GetInstanceProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetInstanceProfile.spec.md

Retrieves information about the specified instance profile, including the instance profile's path, GUID, ARN, and role. For more information about instance profiles, see Using instance profiles in the IAM User Guide .

## Input Shape: GetInstanceProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| InstanceProfileName | Any  # complex shape | ✓ | The name of the instance profile to get information about. This parameter allows (through its regex pattern ) a string o |

## Output Shape: GetInstanceProfileResponse

- **InstanceProfile** (Any  # complex shape): A structure containing details about the instance profile.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_instance_profile(store, request: dict) -> dict:
    """Retrieves information about the specified instance profile, including the instance profile's path, GUID, ARN, and role. For more information about instance profiles, see Using instance profiles in the"""
    instance_profile_name = request.get("InstanceProfileName", "").strip() if isinstance(request.get("InstanceProfileName"), str) else request.get("InstanceProfileName")
    if not instance_profile_name:
        raise ValidationException("InstanceProfileName is required")

    resource = store.instance_profiles(instance_profile_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource instance_profile_name not found")
    return {"InstanceProfileName": instance_profile_name, **resource}
```
