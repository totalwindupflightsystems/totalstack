---
id: "@specs/aws/eks/docs/API_OidcIdentityProviderConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OidcIdentityProviderConfig"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# OidcIdentityProviderConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_OidcIdentityProviderConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OidcIdentityProviderConfig
<a name="API_OidcIdentityProviderConfig"></a>

An object representing the configuration for an OpenID Connect (OIDC) identity provider. 

## Contents
<a name="API_OidcIdentityProviderConfig_Contents"></a>

 ** clientId **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-clientId"></a>
This is also known as *audience*. The ID of the client application that makes authentication requests to the OIDC identity provider.  
Type: String  
Required: No

 ** clusterName **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-clusterName"></a>
The name of your cluster.  
Type: String  
Required: No

 ** groupsClaim **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-groupsClaim"></a>
The JSON web token (JWT) claim that the provider uses to return your groups.  
Type: String  
Required: No

 ** groupsPrefix **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-groupsPrefix"></a>
The prefix that is prepended to group claims to prevent clashes with existing names (such as `system:` groups). For example, the value` oidc:` creates group names like `oidc:engineering` and `oidc:infra`. The prefix can't contain `system:`   
Type: String  
Required: No

 ** identityProviderConfigArn **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-identityProviderConfigArn"></a>
The ARN of the configuration.  
Type: String  
Required: No

 ** identityProviderConfigName **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-identityProviderConfigName"></a>
The name of the configuration.  
Type: String  
Required: No

 ** issuerUrl **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-issuerUrl"></a>
The URL of the OIDC identity provider that allows the API server to discover public signing keys for verifying tokens.  
Type: String  
Required: No

 ** requiredClaims **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-requiredClaims"></a>
The key-value pairs that describe required claims in the identity token. If set, each claim is verified to be present in the token with a matching value.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 63.  
Value Length Constraints: Minimum length of 1. Maximum length of 253.  
Required: No

 ** status **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-status"></a>
The status of the OIDC identity provider.  
Type: String  
Valid Values: `CREATING | DELETING | ACTIVE`   
Required: No

 ** tags **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: No

 ** usernameClaim **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-usernameClaim"></a>
The JSON Web token (JWT) claim that is used as the username.  
Type: String  
Required: No

 ** usernamePrefix **   <a name="AmazonEKS-Type-OidcIdentityProviderConfig-usernamePrefix"></a>
The prefix that is prepended to username claims to prevent clashes with existing names. The prefix can't contain `system:`   
Type: String  
Required: No

## See Also
<a name="API_OidcIdentityProviderConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/OidcIdentityProviderConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/OidcIdentityProviderConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/OidcIdentityProviderConfig) 