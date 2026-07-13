---
id: "@specs/aws/iam/get_login_profile"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_GetLoginProfile"
---

# GetLoginProfile

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/get_login_profile
> **spec:implements:** @kind:operation GetLoginProfile
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_GetLoginProfile.spec.md

Retrieves the user name for the specified IAM user. A login profile is created when you create a password for the user to access the Amazon Web Services Management Console. If the user does not exist or does not have a password, the operation returns a 404 ( NoSuchEntity ) error. If you create an IAM user with access to the console, the CreateDate reflects the date you created the initial password for the user. If you create an IAM user with programmatic access, and then later add a password for the user to access the Amazon Web Services Management Console, the CreateDate reflects the initial password creation date. A user with programmatic access does not have a login profile unless you create a password for the user to access the Amazon Web Services Management Console.

## Input Shape: GetLoginProfileRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| UserName | Any  # complex shape |  | The name of the user whose login profile you want to retrieve. This parameter is optional. If no user name is included,  |

## Output Shape: GetLoginProfileResponse

- **LoginProfile** (Any  # complex shape): A structure containing the user name and the profile creation date for the user.

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def get_login_profile(store, request: dict) -> dict:
    """Retrieves the user name for the specified IAM user. A login profile is created when you create a password for the user to access the Amazon Web Services Management Console. If the user does not exist """

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
