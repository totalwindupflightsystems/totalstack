---
id: "@specs/aws/iam/delete_login_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_DeleteLoginProfile"
---

# DeleteLoginProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/delete_login_profile
> **spec:implements:** @kind:operation DeleteLoginProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_DeleteLoginProfile.spec.md

Deletes the password for the specified IAM user or root user, For more information, see Managing passwords for IAM users . You can use the CLI, the Amazon Web Services API, or the Users page in the IAM console to delete a password for any IAM user. You can use ChangePassword to update, but not delete, your own password in the My Security Credentials page in the Amazon Web Services Management Console. Deleting a user's password does not prevent a user from accessing Amazon Web Services through the command line interface or the API. To prevent all user access, you must also either make any access keys inactive or delete them. For more information about making keys inactive or deleting them, see UpdateAccessKey and DeleteAccessKey .

## Input Shape: DeleteLoginProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| UserName | Any  # complex shape |  | The name of the user whose password you want to delete. This parameter is optional. If no user name is included, it defa |

## Errors
- **EntityTemporarilyUnmodifiableException**: The request was rejected because it referenced an entity that is temporarily unmodifiable, such as a user name that was deleted and then recreated. The error indicates that the request is likely to su
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def delete_login_profile(store, request: dict) -> dict:
    """Deletes the password for the specified IAM user or root user, For more information, see Managing passwords for IAM users . You can use the CLI, the Amazon Web Services API, or the Users page in the IA"""

    return {}
```
