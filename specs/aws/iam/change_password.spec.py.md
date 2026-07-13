---
id: "@specs/aws/iam/change_password"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_ChangePassword"
---

# ChangePassword

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/change_password
> **spec:implements:** @kind:operation ChangePassword
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_ChangePassword.spec.md

Changes the password of the IAM user who is calling this operation. This operation can be performed using the CLI, the Amazon Web Services API, or the My Security Credentials page in the Amazon Web Services Management Console. The Amazon Web Services account root user password is not affected by this operation. Use UpdateLoginProfile to use the CLI, the Amazon Web Services API, or the Users page in the IAM console to change the password for any IAM user. For more information about modifying passwords, see Managing passwords in the IAM User Guide .

## Input Shape: ChangePasswordRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| NewPassword | Any  # complex shape | ✓ | The new password. The new password must conform to the Amazon Web Services account's password policy, if one exists. The |
| OldPassword | Any  # complex shape | ✓ | The IAM user's current password. |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **InvalidUserTypeException**: The request was rejected because the type of user for the transaction was incorrect.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **EntityTemporarilyUnmodifiableException**: The request was rejected because it referenced an entity that is temporarily unmodifiable, such as a user name that was deleted and then recreated. The error indicates that the request is likely to su
- **PasswordPolicyViolationException**: The request was rejected because the provided password did not meet the requirements imposed by the account password policy.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def change_password(store, request: dict) -> dict:
    """Changes the password of the IAM user who is calling this operation. This operation can be performed using the CLI, the Amazon Web Services API, or the My Security Credentials page in the Amazon Web Se"""
    new_password = request.get("NewPassword", "").strip() if isinstance(request.get("NewPassword"), str) else request.get("NewPassword")
    if not new_password:
        raise ValidationException("NewPassword is required")
    old_password = request.get("OldPassword", "").strip() if isinstance(request.get("OldPassword"), str) else request.get("OldPassword")
    if not old_password:
        raise ValidationException("OldPassword is required")

    resource = store.change_passwords(new_password)
    if not resource:
        raise ResourceNotFoundException(f"Resource new_password not found")

    # Update mutable fields

    store.change_passwords(new_password, resource)
    return resource
```
