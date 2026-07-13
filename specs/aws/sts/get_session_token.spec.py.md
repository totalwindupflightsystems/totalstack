---
id: "@specs/aws/sts/get_session_token"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_GetSessionToken"
---

# GetSessionToken

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/get_session_token
> **spec:implements:** @kind:operation GetSessionToken
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_GetSessionToken.spec.md

Returns a set of temporary credentials for an Amazon Web Services account or IAM user. The credentials consist of an access key ID, a secret access key, and a security token. Typically, you use GetSessionToken if you want to use MFA to protect programmatic calls to specific Amazon Web Services API operations like Amazon EC2 StopInstances . MFA-enabled IAM users must call GetSessionToken and submit an MFA code that is associated with their MFA device. Using the temporary security credentials that the call returns, IAM users can then make programmatic calls to API operations that require MFA authentication. An incorrect MFA code causes the API to return an access denied error. For a comparison of GetSessionToken with the other API operations that produce temporary credentials, see Requesting Temporary Security Credentials and Compare STS credentials in the IAM User Guide . No permissions are required for users to perform this operation. The purpose of the sts:GetSessionToken operation is to authenticate the user using MFA. You cannot use policies to control authentication operations. For more information, see Permissions for GetSessionToken in the IAM User Guide . Session Duration The GetSessionToken operation must be called by using the long-term Amazon Web Services security credentials of an IAM user. Credentials that are created by IAM users are valid for the duration that you specify. This duration can range from 900 seconds (15 minutes) up to a maximum of 129,600 seconds (36 hours), with a default of 43,200 seconds (12 hours). Credentials based on account credentials can range from 900 seconds (15 minutes) up to 3,600 seconds (1 hour), with a default of 1 hour. Permissions The temporary security credentials created by GetSessionToken can be used to make API calls to any Amazon Web Services service with the following exceptions: You cannot call any IAM API operations unless MFA authentication information is included in the request. You cannot call any STS API except AssumeRole or GetCallerIdentity . The credentials that GetSessionToken returns are based on permissions associated with the IAM user whose credentials were used to call the operation. The temporary credentials have the same permissions as the IAM user. Although it is possible to call GetSessionToken using the security credentials of an Amazon Web Services account root user rather than an IAM user, we do not recommend it. If GetSessionToken is called using root user credentials, the temporary credentials have root user permissions. For more information, see Safeguard your root user credentials and don't use them for everyday tasks in the IAM User Guide For more information about using GetSessionToken to create temporary credentials, see Temporary Credentials for Users in Untrusted Environments in the IAM User Guide .

## Input Shape: GetSessionTokenRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DurationSeconds | Any  # complex shape |  | The duration, in seconds, that the credentials should remain valid. Acceptable durations for IAM user sessions range fro |
| SerialNumber | Any  # complex shape |  | The identification number of the MFA device that is associated with the IAM user who is making the GetSessionToken call. |
| TokenCode | Any  # complex shape |  | The value provided by the MFA device, if MFA is required. If any policy requires the IAM user to submit an MFA code, spe |

## Output Shape: GetSessionTokenResponse

- **Credentials** (Any  # complex shape): The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) tok

## Errors
- **RegionDisabledException**: STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more in

## Implementation

```speclang
def get_session_token(store, request: dict) -> dict:
    """Returns a set of temporary credentials for an Amazon Web Services account or IAM user. The credentials consist of an access key ID, a secret access key, and a security token. Typically, you use GetSes"""

    # Auto-generated get handler — verify resource key
    return store.get_resource(request)
```
