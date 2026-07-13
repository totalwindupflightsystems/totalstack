---
id: "@specs/aws/iam/create_login_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_CreateLoginProfile"
---

# CreateLoginProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/create_login_profile
> **spec:implements:** @kind:operation CreateLoginProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_CreateLoginProfile.spec.md

Creates a password for the specified IAM user. A password allows an IAM user to access Amazon Web Services services through the Amazon Web Services Management Console. You can use the CLI, the Amazon Web Services API, or the Users page in the IAM console to create a password for any IAM user. Use ChangePassword to update your own existing password in the My Security Credentials page in the Amazon Web Services Management Console. For more information about managing passwords, see Managing passwords in the IAM User Guide .

## Input Shape: CreateLoginProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Password | Any  # complex shape |  | The new password for the user. This parameter must be omitted when you make the request with an AssumeRoot session. It i |
| PasswordResetRequired | Any  # complex shape |  | Specifies whether the user is required to set a new password on next sign-in. |
| UserName | Any  # complex shape |  | The name of the IAM user to create a password for. The user must already exist. This parameter is optional. If no user n |

## Output Shape: CreateLoginProfileResponse

- **LoginProfile** (Any  # complex shape): A structure containing the user name and password create date.

## Errors
- **EntityAlreadyExistsException**: The request was rejected because it attempted to create a resource that already exists.
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **PasswordPolicyViolationException**: The request was rejected because the provided password did not meet the requirements imposed by the account password policy.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def create_login_profile(store, request: dict) -> dict:
    """Creates a password for the specified IAM user. A password allows an IAM user to access Amazon Web Services services through the Amazon Web Services Management Console. You can use the CLI, the Amazon """


    record = {
        "UserName": user_name,
        "Password": password,
        "PasswordResetRequired": password_reset_required,
    }

    store.login_profiles(record)

    return {
        "LoginProfile": record.get("LoginProfile", {}),
    }
```
