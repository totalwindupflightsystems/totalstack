---
id: "@specs/aws/cognito-identity/docs/API_CognitoIdentityProvider"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CognitoIdentityProvider"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# CognitoIdentityProvider

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_CognitoIdentityProvider
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CognitoIdentityProvider
<a name="API_CognitoIdentityProvider"></a>

A provider representing an Amazon Cognito user pool and its client ID.

## Contents
<a name="API_CognitoIdentityProvider_Contents"></a>

 ** ClientId **   <a name="CognitoIdentity-Type-CognitoIdentityProvider-ClientId"></a>
The client ID for the Amazon Cognito user pool.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\w_]+`   
Required: No

 ** ProviderName **   <a name="CognitoIdentity-Type-CognitoIdentityProvider-ProviderName"></a>
The provider name for an Amazon Cognito user pool. For example, `cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\w._:/-]+`   
Required: No

 ** ServerSideTokenCheck **   <a name="CognitoIdentity-Type-CognitoIdentityProvider-ServerSideTokenCheck"></a>
TRUE if server-side token validation is enabled for the identity provider’s token.  
Once you set `ServerSideTokenCheck` to TRUE for an identity pool, that identity pool will check with the integrated user pools to make sure that the user has not been globally signed out or deleted before the identity pool provides an OIDC token or AWS credentials for the user.  
If the user is signed out or deleted, the identity pool will return a 400 Not Authorized error.  
Type: Boolean  
Required: No

## See Also
<a name="API_CognitoIdentityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/CognitoIdentityProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/CognitoIdentityProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/CognitoIdentityProvider) 