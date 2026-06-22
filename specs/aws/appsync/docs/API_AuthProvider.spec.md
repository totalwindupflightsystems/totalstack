---
id: "@specs/aws/appsync/docs/API_AuthProvider"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AuthProvider"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# AuthProvider

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_AuthProvider
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AuthProvider
<a name="API_AuthProvider"></a>

Describes an authorization provider.

## Contents
<a name="API_AuthProvider_Contents"></a>

 ** authType **   <a name="appsync-Type-AuthProvider-authType"></a>
The authorization type.  
Type: String  
Valid Values: `API_KEY | AWS_IAM | AMAZON_COGNITO_USER_POOLS | OPENID_CONNECT | AWS_LAMBDA`   
Required: Yes

 ** cognitoConfig **   <a name="appsync-Type-AuthProvider-cognitoConfig"></a>
Describes an Amazon Cognito user pool configuration.  
Type: [CognitoConfig](API_CognitoConfig.md) object  
Required: No

 ** lambdaAuthorizerConfig **   <a name="appsync-Type-AuthProvider-lambdaAuthorizerConfig"></a>
A `LambdaAuthorizerConfig` specifies how to authorize AWS AppSync API access when using the `AWS_LAMBDA` authorizer mode. Be aware that an AWS AppSync API can have only one AWS Lambda authorizer configured at a time.  
Type: [LambdaAuthorizerConfig](API_LambdaAuthorizerConfig.md) object  
Required: No

 ** openIDConnectConfig **   <a name="appsync-Type-AuthProvider-openIDConnectConfig"></a>
Describes an OpenID Connect (OIDC) configuration.  
Type: [OpenIDConnectConfig](API_OpenIDConnectConfig.md) object  
Required: No

## See Also
<a name="API_AuthProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/AuthProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/AuthProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/AuthProvider) 