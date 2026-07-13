---
id: "@specs/aws/iam/update_login_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateLoginProfile"
---

# UpdateLoginProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_login_profile
> **spec:implements:** @kind:operation UpdateLoginProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateLoginProfile.spec.md

Changes the password for the specified IAM user. You can use the CLI, the Amazon Web Services API, or the Users page in the IAM console to change the password for any IAM user. Use ChangePassword to change your own password in the My Security Credentials page in the Amazon Web Services Management Console. For more information about modifying passwords, see Managing passwords in the IAM User Guide .

## Input Shape: UpdateLoginProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Password | Any  # complex shape |  | The new password for the specified IAM user. The regex pattern used to validate this parameter is a string of characters |
| PasswordResetRequired | Any  # complex shape |  | Allows this new password to be used only once by requiring the specified IAM user to set a new password on next sign-in. |
| UserName | Any  # complex shape | ✓ | The name of the user whose password you want to update. This parameter allows (through its regex pattern ) a string of c |

## Errors
- **EntityTemporarilyUnmodifiableException**: The request was rejected because it referenced an entity that is temporarily unmodifiable, such as a user name that was deleted and then recreated. The error indicates that the request is likely to su
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **PasswordPolicyViolationException**: The request was rejected because the provided password did not meet the requirements imposed by the account password policy.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def update_login_profile(store, request: dict) -> dict:
    """Changes the password for the specified IAM user. You can use the CLI, the Amazon Web Services API, or the Users page in the IAM console to change the password for any IAM user. Use ChangePassword to c"""
    user_name = request.get("UserName", "").strip() if isinstance(request.get("UserName"), str) else request.get("UserName")
    if not user_name:
        raise ValidationException("UserName is required")

    resource = store.login_profiles(user_name)
    if not resource:
        raise ResourceNotFoundException(f"Resource user_name not found")

    # Update mutable fields
    if "Password" in request:
        resource["Password"] = password
    if "PasswordResetRequired" in request:
        resource["PasswordResetRequired"] = password_reset_required

    store.login_profiles(user_name, resource)
    return resource
```
