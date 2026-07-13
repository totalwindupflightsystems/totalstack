---
id: "@specs/aws/sts/assume_role_with_web_identity"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_AssumeRoleWithWebIdentity"
---

# AssumeRoleWithWebIdentity

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/assume_role_with_web_identity
> **spec:implements:** @kind:operation AssumeRoleWithWebIdentity
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_AssumeRoleWithWebIdentity.spec.md

Returns a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider. Example providers include the OAuth 2.0 providers Login with Amazon and Facebook, or any OpenID Connect-compatible identity provider such as Google or Amazon Cognito federated identities . For mobile applications, we recommend that you use Amazon Cognito. You can use Amazon Cognito with the Amazon Web Services SDK for iOS Developer Guide and the Amazon Web Services SDK for Android Developer Guide to uniquely identify a user. You can also supply the user with a consistent identity throughout the lifetime of an application. To learn more about Amazon Cognito, see Amazon Cognito identity pools in Amazon Cognito Developer Guide . Calling AssumeRoleWithWebIdentity does not require the use of Amazon Web Services security credentials. Therefore, you can distribute an application (for example, on mobile devices) that requests temporary security credentials without including long-term Amazon Web Services credentials in the application. You also don't need to deploy server-based proxy services that use long-term Amazon Web Services credentials. Instead, the identity of the caller is validated by using a token from the web identity provider. For a comparison of AssumeRoleWithWebIdentity with the other API operations that produce temporary credentials, see Requesting Temporary Security Credentials and Compare STS credentials in the IAM User Guide . The temporary security credentials returned by this API consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to Amazon Web Services service API operations. Session Duration By default, the temporary security credentials created by AssumeRoleWithWebIdentity last for one hour. However, you can use the optional DurationSeconds parameter to specify the duration of your session. You can provide a value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. To learn how to view the maximum value for your role, see Update the maximum session duration for a role in the IAM User Guide . The maximum session duration limit applies when you use the AssumeRole* API operations or the assume-role* CLI commands. However the limit does not apply when you use those operations to create a console URL. For more information, see Using IAM Roles in the IAM User Guide . Permissions The temporary security credentials created by AssumeRoleWithWebIdentity can be used to make API calls to any Amazon Web Services service with the following exception: you cannot call the STS GetFederationToken or GetSessionToken API operations. (Optional) You can pass inline or managed session policies to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies. The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide . Tags (Optional) You can configure your IdP to pass attributes into your web identity token as session tags. Each session tag consists of a key name and an associated value. For more information about session tags, see Passing session tags using AssumeRoleWithWebIdentity in the IAM User Guide . You can pass up to 50 session tags. The plaintext session tag keys can’t exceed 128 characters and the values can’t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide . An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit. You can pass a session tag with the same key as a tag that is attached to the role. When you do, the session tag overrides the role tag with the same key. An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see Tutorial: Using Tags for Attribute-Based Access Control in the IAM User Guide . You can set the session tags as transitive. Transitive tags persist during role chaining. For more information, see Chaining Roles with Session Tags in the IAM User Guide . Identities Before your application can call AssumeRoleWithWebIdentity , you must have an identity token from a supported identity provider and create a role that the application can assume. The role that your application assumes must trust the identity provider that is associated with the identity token. In other words, the identity provider must be specified in the role's trust policy. Calling AssumeRoleWithWebIdentity can result in an entry in your CloudTrail logs. The entry includes the Subject of the provided web identity token. We recommend that you avoid using any personally identifiable information (PII) in this field. For example, you could instead use a GUID or a pairwise identifier, as suggested in the OIDC specification . For more information about how to use OIDC federation and the AssumeRoleWithWebIdentity API, see the following resources: Using Web Identity Federation API Operations for Mobile Apps and Federation Through a Web-based Identity Provider . Amazon Web Services SDK for iOS Developer Guide and Amazon Web Services SDK for Android Developer Guide . These toolkits contain sample apps that show how to invoke the identity providers. The toolkits then show how to use the information from these providers to get and use temporary security credentials.

## Input Shape: AssumeRoleWithWebIdentityRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DurationSeconds | Any  # complex shape |  | The duration, in seconds, of the role session. The value can range from 900 seconds (15 minutes) up to the maximum sessi |
| Policy | Any  # complex shape |  | An IAM policy in JSON format that you want to use as an inline session policy. This parameter is optional. Passing polic |
| PolicyArns | Any  # complex shape |  | The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The polic |
| ProviderId | Any  # complex shape |  | The fully qualified host component of the domain name of the OAuth 2.0 identity provider. Do not specify this value for  |
| RoleArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the role that the caller is assuming. Additional considerations apply to Amazon Cognit |
| RoleSessionName | Any  # complex shape | ✓ | An identifier for the assumed role session. Typically, you pass the name or identifier that is associated with the user  |
| WebIdentityToken | Any  # complex shape | ✓ | The OAuth 2.0 access token or OpenID Connect ID token that is provided by the identity provider. Your application must g |

## Output Shape: AssumeRoleWithWebIdentityResponse

- **AssumedRoleUser** (Any  # complex shape): The Amazon Resource Name (ARN) and the assumed role ID, which are identifiers that you can use to refer to the resulting
- **Audience** (Any  # complex shape): The intended audience (also known as client ID) of the web identity token. This is traditionally the client identifier i
- **Credentials** (Any  # complex shape): The temporary security credentials, which include an access key ID, a secret access key, and a security token. The size 
- **PackedPolicySize** (Any  # complex shape): A percentage value that indicates the packed size of the session policies and session tags combined passed in the reques
- **Provider** (Any  # complex shape): The issuing authority of the web identity token presented. For OpenID Connect ID tokens, this contains the value of the 
- **SourceIdentity** (Any  # complex shape): The value of the source identity that is returned in the JSON web token (JWT) from the identity provider. You can requir
- **SubjectFromWebIdentityToken** (Any  # complex shape): The unique user identifier that is returned by the identity provider. This identifier is associated with the WebIdentity

## Errors
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **PackedPolicyTooLargeException**: The request was rejected because the total packed size of the session policies and session tags combined was too large. An Amazon Web Services conversion compresses the session policy document, sessio
- **IDPRejectedClaimException**: The identity provider (IdP) reported that authentication failed. This might be because the claim is invalid. If this error is returned for the AssumeRoleWithWebIdentity operation, it can also mean tha
- **IDPCommunicationErrorException**: The request could not be fulfilled because the identity provider (IDP) that was asked to verify the incoming identity token could not be reached. This is often a transient error caused by network cond
- **InvalidIdentityTokenException**: The web identity token that was passed could not be validated by Amazon Web Services. Get a new identity token from the identity provider and then retry the request.
- **ExpiredTokenException**: The web identity token that was passed is expired or is not valid. Get a new identity token from the identity provider and then retry the request.
- **RegionDisabledException**: STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more in

## Implementation

```speclang
def assume_role_with_web_identity(store, request: dict) -> dict:
    """Returns a set of temporary security credentials for users who have been authenticated in a mobile or web application with a web identity provider. Example providers include the OAuth 2.0 providers Log"""
    role_arn = request.get("RoleArn", "").strip() if isinstance(request.get("RoleArn"), str) else request.get("RoleArn")
    if not role_arn:
        raise ValidationException("RoleArn is required")
    role_session_name = request.get("RoleSessionName", "").strip() if isinstance(request.get("RoleSessionName"), str) else request.get("RoleSessionName")
    if not role_session_name:
        raise ValidationException("RoleSessionName is required")
    web_identity_token = request.get("WebIdentityToken", "").strip() if isinstance(request.get("WebIdentityToken"), str) else request.get("WebIdentityToken")
    if not web_identity_token:
        raise ValidationException("WebIdentityToken is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssumeRoleWithWebIdentity", request)
```
