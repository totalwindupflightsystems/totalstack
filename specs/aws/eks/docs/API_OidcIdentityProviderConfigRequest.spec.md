---
id: "@specs/aws/eks/docs/API_OidcIdentityProviderConfigRequest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OidcIdentityProviderConfigRequest"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# OidcIdentityProviderConfigRequest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_OidcIdentityProviderConfigRequest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OidcIdentityProviderConfigRequest
<a name="API_OidcIdentityProviderConfigRequest"></a>

An object representing an OpenID Connect (OIDC) configuration. Before associating an OIDC identity provider to your cluster, review the considerations in [Authenticating users for your cluster from an OIDC identity provider](https://docs.aws.amazon.com/eks/latest/userguide/authenticate-oidc-identity-provider.html) in the *Amazon EKS User Guide*.

## Contents
<a name="API_OidcIdentityProviderConfigRequest_Contents"></a>

 ** clientId **   <a name="AmazonEKS-Type-OidcIdentityProviderConfigRequest-clientId"></a>
This is also known as *audience*. The ID for the client application that makes authentication requests to the OIDC identity provider.  
Type: String  
Required: Yes

 ** identityProviderConfigName **   <a name="AmazonEKS-Type-OidcIdentityProviderConfigRequest-identityProviderConfigName"></a>
The name of the OIDC provider configuration.  
Type: String  
Required: Yes

 ** issuerUrl **   <a name="AmazonEKS-Type-OidcIdentityProviderConfigRequest-issuerUrl"></a>
The URL of the OIDC identity provider that allows the API server to discover public signing keys for verifying tokens. The URL must begin with `https://` and should correspond to the `iss` claim in the provider's OIDC ID tokens. Based on the OIDC standard, path components are allowed but query parameters are not. Typically the URL consists of only a hostname, like `https://server.example.org` or `https://example.com`. This URL should point to the level below `.well-known/openid-configuration` and must be publicly accessible over the internet.  
Type: String  
Required: Yes

 ** groupsClaim **   <a name="AmazonEKS-Type-OidcIdentityProviderConfigRequest-groupsClaim"></a>
The JWT claim that the provider uses to return your groups.  
Type: String  
Required: No

 ** groupsPrefix **   <a name="AmazonEKS-Type-OidcIdentityProviderConfigRequest-groupsPrefix"></a>
The prefix that is prepended to group claims to prevent clashes with existing names (such as `system:` groups). For example, the value` oidc:` will create group names like `oidc:engineering` and `oidc:infra`.  
Type: String  
Required: No

 ** requiredClaims **   <a name="AmazonEKS-Type-OidcIdentityProviderConfigRequest-requiredClaims"></a>
The key value pairs that describe required claims in the identity token. If set, each claim is verified to be present in the token with a matching value. For the maximum number of claims that you can require, see [Amazon EKS service quotas](https://docs.aws.amazon.com/eks/latest/userguide/service-quotas.html) in the *Amazon EKS User Guide*.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 63.  
Value Length Constraints: Minimum length of 1. Maximum length of 253.  
Required: No

 ** usernameClaim **   <a name="AmazonEKS-Type-OidcIdentityProviderConfigRequest-usernameClaim"></a>
The JSON Web Token (JWT) claim to use as the username. The default is `sub`, which is expected to be a unique identifier of the end user. You can choose other claims, such as `email` or `name`, depending on the OIDC identity provider. Claims other than `email` are prefixed with the issuer URL to prevent naming clashes with other plug-ins.  
Type: String  
Required: No

 ** usernamePrefix **   <a name="AmazonEKS-Type-OidcIdentityProviderConfigRequest-usernamePrefix"></a>
The prefix that is prepended to username claims to prevent clashes with existing names. If you do not provide this field, and `username` is a value other than `email`, the prefix defaults to `issuerurl#`. You can use the value `-` to disable all prefixing.  
Type: String  
Required: No

## See Also
<a name="API_OidcIdentityProviderConfigRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/OidcIdentityProviderConfigRequest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/OidcIdentityProviderConfigRequest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/OidcIdentityProviderConfigRequest) 