---
id: "@specs/aws/iam/create_instance_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateInstanceProfile"
---

# CreateInstanceProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_instance_profile
> **spec:implements:** @kind:operation CreateInstanceProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateInstanceProfile.spec.md

Creates a new instance profile. For information about instance profiles, see Using roles for applications on Amazon EC2 in the IAM User Guide , and Instance profiles in the Amazon EC2 User Guide . For information about the number of instance profiles you can create, see IAM object quotas in the IAM User Guide .

## Input Shape: CreateInstanceProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| InstanceProfileName | Any  # complex shape | ✓ | The name of the instance profile to create. This parameter allows (through its regex pattern ) a string of characters co |
| Path | Any  # complex shape |  | The path to the instance profile. For more information about paths, see IAM Identifiers in the IAM User Guide . This par |
| Tags | Any  # complex shape |  | A list of tags that you want to attach to the newly created IAM instance profile. Each tag consists of a key name and an |

## Output Shape: CreateInstanceProfileResponse

- **InstanceProfile** (Any  # complex shape): A structure containing details about the new instance profile.

## Errors
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **InvalidInputException**: The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ConcurrentModificationException**: The request was rejected because multiple requests to change this object were submitted simultaneously. Wait a few minutes and submit your request again.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_instance_profile(store, request: dict) -> dict:
    """Creates a new instance profile. For information about instance profiles, see Using roles for applications on Amazon EC2 in the IAM User Guide , and Instance profiles in the Amazon EC2 User Guide . For"""
    instance_profile_name = request.get("InstanceProfileName", "").strip() if isinstance(request.get("InstanceProfileName"), str) else request.get("InstanceProfileName")
    if not instance_profile_name:
        raise ValidationException("InstanceProfileName is required")

    if store.instance_profiles(instance_profile_name):
        raise ResourceInUseException(f"Resource instance_profile_name already exists")

    record = {
        "InstanceProfileName": instance_profile_name,
        "Path": path,
        "Tags": tags,
    }

    store.instance_profiles(instance_profile_name, record)

    return {
        "InstanceProfile": record.get("InstanceProfile", {}),
    }
```
