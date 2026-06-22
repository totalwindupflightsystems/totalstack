---
id: "@specs/aws/appsync/docs/API_OpenIDConnectConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OpenIDConnectConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# OpenIDConnectConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_OpenIDConnectConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OpenIDConnectConfig
<a name="API_OpenIDConnectConfig"></a>

Describes an OpenID Connect (OIDC) configuration.

## Contents
<a name="API_OpenIDConnectConfig_Contents"></a>

 ** issuer **   <a name="appsync-Type-OpenIDConnectConfig-issuer"></a>
The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of `iss` in the ID token.  
Type: String  
Required: Yes

 ** authTTL **   <a name="appsync-Type-OpenIDConnectConfig-authTTL"></a>
The number of milliseconds that a token is valid after being authenticated.  
Type: Long  
Required: No

 ** clientId **   <a name="appsync-Type-OpenIDConnectConfig-clientId"></a>
The client identifier of the relying party at the OpenID identity provider. This identifier is typically obtained when the relying party is registered with the OpenID identity provider. You can specify a regular expression so that AWS AppSync can validate against multiple client identifiers at a time.  
Type: String  
Required: No

 ** iatTTL **   <a name="appsync-Type-OpenIDConnectConfig-iatTTL"></a>
The number of milliseconds that a token is valid after it's issued to a user.  
Type: Long  
Required: No

## See Also
<a name="API_OpenIDConnectConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/OpenIDConnectConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/OpenIDConnectConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/OpenIDConnectConfig) 