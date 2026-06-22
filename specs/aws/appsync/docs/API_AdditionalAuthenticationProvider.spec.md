---
id: "@specs/aws/appsync/docs/API_AdditionalAuthenticationProvider"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AdditionalAuthenticationProvider"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# AdditionalAuthenticationProvider

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_AdditionalAuthenticationProvider
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AdditionalAuthenticationProvider
<a name="API_AdditionalAuthenticationProvider"></a>

Describes an additional authentication provider.

## Contents
<a name="API_AdditionalAuthenticationProvider_Contents"></a>

 ** authenticationType **   <a name="appsync-Type-AdditionalAuthenticationProvider-authenticationType"></a>
The authentication type: API key, AWS Identity and Access Management (IAM), OpenID Connect (OIDC), Amazon Cognito user pools, or AWS Lambda.  
Type: String  
Valid Values: `API_KEY | AWS_IAM | AMAZON_COGNITO_USER_POOLS | OPENID_CONNECT | AWS_LAMBDA`   
Required: No

 ** lambdaAuthorizerConfig **   <a name="appsync-Type-AdditionalAuthenticationProvider-lambdaAuthorizerConfig"></a>
Configuration for Lambda function authorization.  
Type: [LambdaAuthorizerConfig](API_LambdaAuthorizerConfig.md) object  
Required: No

 ** openIDConnectConfig **   <a name="appsync-Type-AdditionalAuthenticationProvider-openIDConnectConfig"></a>
The OIDC configuration.  
Type: [OpenIDConnectConfig](API_OpenIDConnectConfig.md) object  
Required: No

 ** userPoolConfig **   <a name="appsync-Type-AdditionalAuthenticationProvider-userPoolConfig"></a>
The Amazon Cognito user pool configuration.  
Type: [CognitoUserPoolConfig](API_CognitoUserPoolConfig.md) object  
Required: No

## See Also
<a name="API_AdditionalAuthenticationProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/AdditionalAuthenticationProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/AdditionalAuthenticationProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/AdditionalAuthenticationProvider) 