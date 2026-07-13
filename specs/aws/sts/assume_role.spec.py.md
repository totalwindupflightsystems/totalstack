---
id: "@specs/aws/sts/assume_role"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_AssumeRole"
---

# AssumeRole

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/assume_role
> **spec:implements:** @kind:operation AssumeRole
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_AssumeRole.spec.md

Returns a set of temporary security credentials that you can use to access Amazon Web Services resources. These temporary credentials consist of an access key ID, a secret access key, and a security token. Typically, you use AssumeRole within your account or for cross-account access. For a comparison of AssumeRole with other API operations that produce temporary credentials, see Requesting Temporary Security Credentials and Compare STS credentials in the IAM User Guide . Permissions The temporary security credentials created by AssumeRole can be used to make API calls to any Amazon Web Services service with the following exception: You cannot call the Amazon Web Services STS GetFederationToken or GetSessionToken API operations. (Optional) You can pass inline or managed session policies to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies. The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide . When you create a role, you create two policies: a role trust policy that specifies who can assume the role, and a permissions policy that specifies what can be done with the role. You specify the trusted principal that is allowed to assume the role in the role trust policy. To assume a role from a different account, your Amazon Web Services account must be trusted by the role. The trust relationship is defined in the role's trust policy when the role is created. That trust policy states which accounts are allowed to delegate that access to users in the account. A user who wants to access a role in a different account must also have permissions that are delegated from the account administrator. The administrator must attach a policy that allows the user to call AssumeRole for the ARN of the role in the other account. To allow a user to assume a role in the same account, you can do either of the following: Attach a policy to the user that allows the user to call AssumeRole (as long as the role's trust policy trusts the account). Add the user as a principal directly in the role's trust policy. You can do either because the role’s trust policy acts as an IAM resource-based policy. When a resource-based policy grants access to a principal in the same account, no additional identity-based policy is required. For more information about trust policies and resource-based policies, see IAM Policies in the IAM User Guide . Tags (Optional) You can pass tag key-value pairs to your session. These tags are called session tags. For more information about session tags, see Passing Session Tags in STS in the IAM User Guide . An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see Tutorial: Using Tags for Attribute-Based Access Control in the IAM User Guide . You can set the session tags as transitive. Transitive tags persist during role chaining. For more information, see Chaining Roles with Session Tags in the IAM User Guide . Using MFA with AssumeRole (Optional) You can include multi-factor authentication (MFA) information when you call AssumeRole . This is useful for cross-account scenarios to ensure that the user that assumes the role has been authenticated with an Amazon Web Services MFA device. In that scenario, the trust policy of the role being assumed includes a condition that tests for MFA authentication. If the caller does not include valid MFA information, the request to assume the role is denied. The condition in a trust policy that tests for MFA authentication might look like the following example. "Condition": {"Bool": {"aws:MultiFactorAuthPresent": true}} For more information, see Configuring MFA-Protected API Access in the IAM User Guide guide. To use MFA with AssumeRole , you pass values for the SerialNumber and TokenCode parameters. The SerialNumber value identifies the user's hardware or virtual MFA device. The TokenCode is the time-based one-time password (TOTP) that the MFA device produces.

## Input Shape: AssumeRoleRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DurationSeconds | Any  # complex shape |  | The duration, in seconds, of the role session. The value specified can range from 900 seconds (15 minutes) up to the max |
| ExternalId | Any  # complex shape |  | A unique identifier that might be required when you assume a role in another account. If the administrator of the accoun |
| Policy | Any  # complex shape |  | An IAM policy in JSON format that you want to use as an inline session policy. This parameter is optional. Passing polic |
| PolicyArns | Any  # complex shape |  | The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The polic |
| ProvidedContexts | Any  # complex shape |  | A list of previously acquired trusted context assertions in the format of a JSON array. The trusted context assertion is |
| RoleArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the role to assume. |
| RoleSessionName | Any  # complex shape | ✓ | An identifier for the assumed role session. Use the role session name to uniquely identify a session when the same role  |
| SerialNumber | Any  # complex shape |  | The identification number of the MFA device that is associated with the user who is making the AssumeRole call. Specify  |
| SourceIdentity | Any  # complex shape |  | The source identity specified by the principal that is calling the AssumeRole operation. The source identity value persi |
| Tags | Any  # complex shape |  | A list of session tags that you want to pass. Each session tag consists of a key name and an associated value. For more  |
| TokenCode | Any  # complex shape |  | The value provided by the MFA device, if the trust policy of the role being assumed requires MFA. (In other words, if th |
| TransitiveTagKeys | Any  # complex shape |  | A list of keys for session tags that you want to set as transitive. If you set a tag key as transitive, the correspondin |

## Output Shape: AssumeRoleResponse

- **AssumedRoleUser** (Any  # complex shape): The Amazon Resource Name (ARN) and the assumed role ID, which are identifiers that you can use to refer to the resulting
- **Credentials** (Any  # complex shape): The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) tok
- **PackedPolicySize** (Any  # complex shape): A percentage value that indicates the packed size of the session policies and session tags combined passed in the reques
- **SourceIdentity** (Any  # complex shape): The source identity specified by the principal that is calling the AssumeRole operation. You can require users to specif

## Errors
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **PackedPolicyTooLargeException**: The request was rejected because the total packed size of the session policies and session tags combined was too large. An Amazon Web Services conversion compresses the session policy document, sessio
- **RegionDisabledException**: STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more in
- **ExpiredTokenException**: The web identity token that was passed is expired or is not valid. Get a new identity token from the identity provider and then retry the request.

## Implementation

```speclang
def assume_role(store, request: dict) -> dict:
    """Returns a set of temporary security credentials that you can use to access Amazon Web Services resources. These temporary credentials consist of an access key ID, a secret access key, and a security t"""
    role_arn = request.get("RoleArn", "").strip() if isinstance(request.get("RoleArn"), str) else request.get("RoleArn")
    if not role_arn:
        raise ValidationException("RoleArn is required")
    role_session_name = request.get("RoleSessionName", "").strip() if isinstance(request.get("RoleSessionName"), str) else request.get("RoleSessionName")
    if not role_session_name:
        raise ValidationException("RoleSessionName is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssumeRole", request)
```
