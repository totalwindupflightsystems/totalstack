---
id: "@specs/aws/sts/assume_role_with_saml"
version: 1.0.0
target_lang: py
owned-by: codegen
model_pool: code-gen
status: active
depends_on:
  - "@specs/aws/sts/plan"
  - "@specs/aws/sts/docs/API_AssumeRoleWithSAML"
---

# AssumeRoleWithSAML

> **spec:trace:** specs/aws/sts/sts.spec.plan.md#operation-inventory
> **spec:id:** @specs/aws/sts/assume_role_with_saml
> **spec:implements:** @kind:operation AssumeRoleWithSAML
> **AWS Protocol:** query
> **HTTP:** POST /
> **@ref:** specs/aws/sts/docs/API_AssumeRoleWithSAML.spec.md

Returns a set of temporary security credentials for users who have been authenticated via a SAML authentication response. This operation provides a mechanism for tying an enterprise identity store or directory to role-based Amazon Web Services access without user-specific credentials or configuration. For a comparison of AssumeRoleWithSAML with the other API operations that produce temporary credentials, see Requesting Temporary Security Credentials and Compare STS credentials in the IAM User Guide . The temporary security credentials returned by this operation consist of an access key ID, a secret access key, and a security token. Applications can use these temporary security credentials to sign calls to Amazon Web Services services. AssumeRoleWithSAML will not work on IAM Identity Center managed roles. These roles' names start with AWSReservedSSO_ . Session Duration By default, the temporary security credentials created by AssumeRoleWithSAML last for one hour. However, you can use the optional DurationSeconds parameter to specify the duration of your session. Your role session lasts for the duration that you specify, or until the time specified in the SAML authentication response's SessionNotOnOrAfter value, whichever is shorter. You can provide a DurationSeconds value from 900 seconds (15 minutes) up to the maximum session duration setting for the role. This setting can have a value from 1 hour to 12 hours. To learn how to view the maximum value for your role, see View the Maximum Session Duration Setting for a Role in the IAM User Guide . The maximum session duration limit applies when you use the AssumeRole* API operations or the assume-role* CLI commands. However the limit does not apply when you use those operations to create a console URL. For more information, see Using IAM Roles in the IAM User Guide . Role chaining limits your CLI or Amazon Web Services API role session to a maximum of one hour. When you use the AssumeRole API operation to assume a role, you can specify the duration of your role session with the DurationSeconds parameter. You can specify a parameter value of up to 43200 seconds (12 hours), depending on the maximum session duration setting for your role. However, if you assume a role using role chaining and provide a DurationSeconds parameter value greater than one hour, the operation fails. Permissions The temporary security credentials created by AssumeRoleWithSAML can be used to make API calls to any Amazon Web Services service with the following exception: you cannot call the STS GetFederationToken or GetSessionToken API operations. (Optional) You can pass inline or managed session policies to this operation. You can pass a single JSON policy document to use as an inline session policy. You can also specify up to 10 managed policy Amazon Resource Names (ARNs) to use as managed session policies. The plaintext that you use for both inline and managed session policies can't exceed 2,048 characters. Passing policies to this operation returns new temporary credentials. The resulting session's permissions are the intersection of the role's identity-based policy and the session policies. You can use the role's temporary credentials in subsequent Amazon Web Services API calls to access resources in the account that owns the role. You cannot use session policies to grant more permissions than those allowed by the identity-based policy of the role that is being assumed. For more information, see Session Policies in the IAM User Guide . Calling AssumeRoleWithSAML does not require the use of Amazon Web Services security credentials. The identity of the caller is validated by using keys in the metadata document that is uploaded for the SAML provider entity for your identity provider. Calling AssumeRoleWithSAML can result in an entry in your CloudTrail logs. The entry includes the value in the NameID element of the SAML assertion. We recommend that you use a NameIDType that is not associated with any personally identifiable information (PII). For example, you could instead use the persistent identifier ( urn:oasis:names:tc:SAML:2.0:nameid-format:persistent ). Tags (Optional) You can configure your IdP to pass attributes into your SAML assertion as session tags. Each session tag consists of a key name and an associated value. For more information about session tags, see Passing Session Tags in STS in the IAM User Guide . You can pass up to 50 session tags. The plaintext session tag keys can’t exceed 128 characters and the values can’t exceed 256 characters. For these and additional limits, see IAM and STS Character Limits in the IAM User Guide . An Amazon Web Services conversion compresses the passed inline session policy, managed policy ARNs, and session tags into a packed binary format that has a separate limit. Your request can fail for this limit even if your plaintext meets the other requirements. The PackedPolicySize response element indicates by percentage how close the policies and tags for your request are to the upper size limit. You can pass a session tag with the same key as a tag that is attached to the role. When you do, session tags override the role's tags with the same key. An administrator must grant you the permissions necessary to pass session tags. The administrator can also create granular permissions to allow you to pass only specific session tags. For more information, see Tutorial: Using Tags for Attribute-Based Access Control in the IAM User Guide . You can set the session tags as transitive. Transitive tags persist during role chaining. For more information, see Chaining Roles with Session Tags in the IAM User Guide . SAML Configuration Before your application can call AssumeRoleWithSAML , you must configure your SAML identity provider (IdP) to issue the claims required by Amazon Web Services. Additionally, you must use Identity and Access Management (IAM) to create a SAML provider entity in your Amazon Web Services account that represents your identity provider. You must also create an IAM role that specifies this SAML provider in its trust policy. For more information, see the following resources: About SAML 2.0-based Federation in the IAM User Guide . Creating SAML Identity Providers in the IAM User Guide . Configuring a Relying Party and Claims in the IAM User Guide . Creating a Role for SAML 2.0 Federation in the IAM User Guide .

## Input Shape: AssumeRoleWithSAMLRequest

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| DurationSeconds | Any  # complex shape |  | The duration, in seconds, of the role session. Your role session lasts for the duration that you specify for the Duratio |
| Policy | Any  # complex shape |  | An IAM policy in JSON format that you want to use as an inline session policy. This parameter is optional. Passing polic |
| PolicyArns | Any  # complex shape |  | The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as managed session policies. The polic |
| PrincipalArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP. |
| RoleArn | Any  # complex shape | ✓ | The Amazon Resource Name (ARN) of the role that the caller is assuming. |
| SAMLAssertion | Any  # complex shape | ✓ | The base64 encoded SAML authentication response provided by the IdP. For more information, see Configuring a Relying Par |

## Output Shape: AssumeRoleWithSAMLResponse

- **AssumedRoleUser** (Any  # complex shape): The identifiers for the temporary security credentials that the operation returns.
- **Audience** (Any  # complex shape): The value of the Recipient attribute of the SubjectConfirmationData element of the SAML assertion.
- **Credentials** (Any  # complex shape): The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) tok
- **Issuer** (Any  # complex shape): The value of the Issuer element of the SAML assertion.
- **NameQualifier** (Any  # complex shape): A hash value based on the concatenation of the following: The Issuer response value. The Amazon Web Services account ID.
- **PackedPolicySize** (Any  # complex shape): A percentage value that indicates the packed size of the session policies and session tags combined passed in the reques
- **SourceIdentity** (Any  # complex shape): The value in the SourceIdentity attribute in the SAML assertion. The source identity value persists across chained role 
- **Subject** (Any  # complex shape): The value of the NameID element in the Subject element of the SAML assertion.
- **SubjectType** (Any  # complex shape): The format of the name ID, as defined by the Format attribute in the NameID element of the SAML assertion. Typical examp

## Errors
- **MalformedPolicyDocumentException**: The request was rejected because the policy document was malformed. The error message describes the specific error.
- **PackedPolicyTooLargeException**: The request was rejected because the total packed size of the session policies and session tags combined was too large. An Amazon Web Services conversion compresses the session policy document, sessio
- **IDPRejectedClaimException**: The identity provider (IdP) reported that authentication failed. This might be because the claim is invalid. If this error is returned for the AssumeRoleWithWebIdentity operation, it can also mean tha
- **InvalidIdentityTokenException**: The web identity token that was passed could not be validated by Amazon Web Services. Get a new identity token from the identity provider and then retry the request.
- **ExpiredTokenException**: The web identity token that was passed is expired or is not valid. Get a new identity token from the identity provider and then retry the request.
- **RegionDisabledException**: STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate STS in that region. For more in

## Implementation

```speclang
def assume_role_with_saml(store, request: dict) -> dict:
    """Returns a set of temporary security credentials for users who have been authenticated via a SAML authentication response. This operation provides a mechanism for tying an enterprise identity store or """
    principal_arn = request.get("PrincipalArn", "").strip() if isinstance(request.get("PrincipalArn"), str) else request.get("PrincipalArn")
    if not principal_arn:
        raise ValidationException("PrincipalArn is required")
    role_arn = request.get("RoleArn", "").strip() if isinstance(request.get("RoleArn"), str) else request.get("RoleArn")
    if not role_arn:
        raise ValidationException("RoleArn is required")
    saml_assertion = request.get("SAMLAssertion", "").strip() if isinstance(request.get("SAMLAssertion"), str) else request.get("SAMLAssertion")
    if not saml_assertion:
        raise ValidationException("SAMLAssertion is required")

    # Auto-generated handler — operation not classified as CRUD
    return store.execute("AssumeRoleWithSAML", request)
```
