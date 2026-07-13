---
id: "@specs/aws/iam/update_account_password_policy"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/iam/plan"
  - "@specs/aws/iam/docs/API_UpdateAccountPasswordPolicy"
---

# UpdateAccountPasswordPolicy

> **spec:trace:** specs/aws/iam/iam.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/iam/update_account_password_policy
> **spec:implements:** @kind:operation UpdateAccountPasswordPolicy
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/iam/docs/API_UpdateAccountPasswordPolicy.spec.md

Updates the password policy settings for the Amazon Web Services account. This operation does not support partial updates. No parameters are required, but if you do not specify a parameter, that parameter's value reverts to its default value. See the Request Parameters section for each parameter's default value. Also note that some parameters do not allow the default parameter to be explicitly set. Instead, to invoke the default value, do not include that parameter when you invoke the operation. For more information about using a password policy, see Managing an IAM password policy in the IAM User Guide .

## Input Shape: UpdateAccountPasswordPolicyRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| AllowUsersToChangePassword | Any  # complex shape |  | Allows all IAM users in your account to use the Amazon Web Services Management Console to change their own passwords. Fo |
| HardExpiry | Any  # complex shape |  | Prevents IAM users who are accessing the account via the Amazon Web Services Management Console from setting a new conso |
| MaxPasswordAge | Any  # complex shape |  | The number of days that an IAM user password is valid. If you do not specify a value for this parameter, then the operat |
| MinimumPasswordLength | Any  # complex shape |  | The minimum number of characters allowed in an IAM user password. If you do not specify a value for this parameter, then |
| PasswordReusePrevention | Any  # complex shape |  | Specifies the number of previous passwords that IAM users are prevented from reusing. If you do not specify a value for  |
| RequireLowercaseCharacters | Any  # complex shape |  | Specifies whether IAM user passwords must contain at least one lowercase character from the ISO basic Latin alphabet (a  |
| RequireNumbers | Any  # complex shape |  | Specifies whether IAM user passwords must contain at least one numeric character (0 to 9). If you do not specify a value |
| RequireSymbols | Any  # complex shape |  | Specifies whether IAM user passwords must contain at least one of the following non-alphanumeric characters: ! @ # $ % ^ |
| RequireUppercaseCharacters | Any  # complex shape |  | Specifies whether IAM user passwords must contain at least one uppercase character from the ISO basic Latin alphabet (A  |

## Errors
- **NoSuchEntityException**: The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **LimitExceededException**: The request was rejected because it attempted to create resources beyond the current Amazon Web Services account limits. The error message describes the limit exceeded.
- **ServiceFailureException**: The request processing has failed because of an unknown error, exception or failure.

## Implementation

```speclang
def update_account_password_policy(store, request: dict) -> dict:
    """Updates the password policy settings for the Amazon Web Services account. This operation does not support partial updates. No parameters are required, but if you do not specify a parameter, that param"""

```
