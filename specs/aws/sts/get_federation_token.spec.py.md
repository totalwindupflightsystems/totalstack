---
id: "@specs/aws/sts/get_federation_token"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_GetFederationToken"
---

# GetFederationToken

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/get_federation_token
> **spec:implements:** @kind:operation GetFederationToken
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_GetFederationToken.spec.md

Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a user. A typical use is in a proxy application that gets temporary security credentials on behalf of distributed applications inside a corporate network. You must call the GetFederationToken operation using the long-term security credentials of an IAM user. As a result, this call is appropriate in contexts where those credentials can be safeguarded, usually in a server-based application. For a comparison of GetFederationToken with the other API operations that produce temporary credentials, see Requesting Temporary Security Credentials and Compare STS credentials in the IAM User Guide . Although it is possible to call GetFederationToken using the security credentials of an Amazon Web Services account root user rather than an IAM user that you create for the purpose of a proxy application, we do not recommend it. For more information, see Safeguard your root user credentials and don't use them for everyday tasks in the IAM User Guide . You can create a mobile-based or browser-based app that can authenticate users using a web identity provider like Login with Amazon, Facebook, Google, or an OpenID Connect-compatible identity provider. In this case, we recommend that you use Amazon Cognito or AssumeRoleWithWebIdentity . For more information, see Federation Through a Web-based Identity Provider in the IAM User Guide . Session duration The temporary credentials are valid for the specified duration, from 900 seconds (15 minutes) up to a maximum of 129,600 seconds (36 hours). The default session duration is 43,200 seconds (12 hours). Temporary credentials obtained by using the root user credentials have a maximum duration of 3,600 seconds (1 hour). Permissions You can use the temporary credentials created by GetFederationToken in any Amazon Web Services service with the following exceptions: You cannot call any IAM operations using the CLI or the Amazon Web Services API. This limitation does not apply to console sessions. You cannot call any STS operations except GetCallerIdentity . You can use temporary credentials for single sign-on (SSO) to the console. You must pass an inline or managed session policy to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies. The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. Though the session policy parameters are optional, if you do not pass a policy, then the resulting federated user session has no permissions. When you pass session policies, the session permissions are the intersection of the IAM user policies and the session policies that you pass. This gives you a way to further restrict the permissions for a federated user. You cannot use session policies to grant more permissions than those that are defined in the permissions policy of the IAM user. For more information, see Session Policies in the IAM User Guide . For information about using GetFederationToken to create temporary security credentials, see GetFederationToken—Federation Through a Custom Identity Broker . You can use the credentials to access a resource that has a resource-based policy. If that policy specifically references the federated user session in the Principal element of the policy, the session has the permissions allowed by the policy. These permissions are granted in addition to the permissions granted by the session policies. Tags (Optional) You can pass tag key-value pairs to your session. These are called session tags. For more information about session tags, see Passing Session Tags in STS in the IAM User Guide . You can create a mobile-based or browser-based app that can authenticate users using a web identity provider like Login with Amazon, Facebook, Google, or an OpenID Connect-compatible identity provider. In this case, we recommend that you use Amazon Cognito or AssumeRoleWithWebIdentity . For more information, see Federation Through a Web-based Identity Provider in the IAM User Guide . An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see Tutorial: Using Tags for Attribute-Based Access Control in the IAM User Guide . Tag key–value pairs are not case sensitive, but case is preserved. This means that you cannot have separate Department and department tag keys. Assume that the user that you are federating has the Department = Marketing tag and you pass the department = engineering session tag. Department and department are not saved as separate tags, and the session tag passed in the request takes precedence over the user tag.

## Input Shape: GetFederationTokenRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DurationSeconds | Any  # complex shape |  | The duration, in seconds, that the session should last. Acceptable durations for federation sessions range from 900 seco |
| Name | Any  # complex shape | ✓ | The name of the federated user. The name is used as an identifier for the temporary security credentials (such as Bob ). |
| Policy | Any  # complex shape |  | An IAM policy in JSON format that you want to use as an inline session policy. You must pass an inline or managed sessio |
| PolicyArns | Any  # complex shape |  | The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as a managed session policy. The polic |
| Tags | Any  # complex shape |  | A list of session tags. Each session tag consists of a key name and an associated value. For more information about sess |

## Output Shape: GetFederationTokenResponse

- **Credentials** (Any  # complex shape): The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) tok
- **FederatedUser** (Any  # complex shape): Identifiers for the federated user associated with the credentials (such as arn:aws:sts::123456789012:federated-user/Bob
- **PackedPolicySize** (Any  # complex shape): A percentage value that indicates the packed size of the session policies and session tags combined passed in the reques

## Errors
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **PackedPolicyTooLargeException**: The request was rejected because the total packed size of the session policies and session tags combined was too large. An Amazon Web Services conversion compresses the session policy document, sessio
- **RegionDisabledException**: STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more in

## Implementation

```speclang
def get_federation_token(store, request: dict) -> dict:
    """Returns a set of temporary security credentials (consisting of an access key ID, a secret access key, and a security token) for a user. A typical use is in a proxy application that gets temporary secu"""
    name = request.get("Name", "").strip() if isinstance(request.get("Name"), str) else request.get("Name")
    if not name:
        raise ValidationException("Name is required")

    resource = store.federation_tokens(name)
    if not resource:
        raise ResourceNotFoundException(f"Resource name not found")
    return {"Name": name, **resource}
```
