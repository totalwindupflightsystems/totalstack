---
id: "@specs/aws/iam/add_role_to_instance_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_AddRoleToInstanceProfile"
---

# AddRoleToInstanceProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/add_role_to_instance_profile
> **spec:implements:** @kind:operation AddRoleToInstanceProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_AddRoleToInstanceProfile.spec.md

Adds the specified IAM role to the specified instance profile. An instance profile can contain only one role, and this quota cannot be increased. You can remove the existing role and then add a different role to an instance profile. You must then wait for the change to appear across all of Amazon Web Services because of eventual consistency . To force the change, you must disassociate the instance profile and then associate the instance profile , or you can stop your instance and then restart it. The caller of this operation must be granted the PassRole permission on the IAM role by a permissions policy. When using the iam:AssociatedResourceArn condition in a policy to restrict the PassRole IAM action, special considerations apply if the policy is intended to define access for the AddRoleToInstanceProfile action. In this case, you cannot specify a Region or instance ID in the EC2 instance ARN. The ARN value must be arn:aws:ec2:*:CallerAccountId:instance/* . Using any other ARN value may lead to unexpected evaluation results. For more information about roles, see IAM roles in the IAM User Guide . For more information about instance profiles, see Using instance profiles in the IAM User Guide .

## Input Shape: AddRoleToInstanceProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| InstanceProfileName | Any  # complex shape | ✓ | The name of the instance profile to update. This parameter allows (through its regex pattern ) a string of characters co |
| RoleName | Any  # complex shape | ✓ | The name of the role to add. This parameter allows (through its regex pattern ) a string of characters consisting of upp |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **UnmodifiableEntityException**: The request was rejected because service-linked roles are protected Amazon Web Services resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def add_role_to_instance_profile(store, request: dict) -> dict:
    """Adds the specified IAM role to the specified instance profile. An instance profile can contain only one role, and this quota cannot be increased. You can remove the existing role and then add a differ"""
    instance_profile_name = request.get("InstanceProfileName", "").strip() if isinstance(request.get("InstanceProfileName"), str) else request.get("InstanceProfileName")
    if not instance_profile_name:
        raise ValidationException("InstanceProfileName is required")
    role_name = request.get("RoleName", "").strip() if isinstance(request.get("RoleName"), str) else request.get("RoleName")
    if not role_name:
        raise ValidationException("RoleName is required")

    if store.role_to_instance_profiles(role_name):
        raise ResourceInUseException(f"Resource role_name already exists")

    record = {
        "InstanceProfileName": instance_profile_name,
        "RoleName": role_name,
    }

    store.role_to_instance_profiles(role_name, record)

    return {
    }
```
