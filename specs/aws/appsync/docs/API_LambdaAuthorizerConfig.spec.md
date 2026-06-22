---
id: "@specs/aws/appsync/docs/API_LambdaAuthorizerConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LambdaAuthorizerConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# LambdaAuthorizerConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_LambdaAuthorizerConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LambdaAuthorizerConfig
<a name="API_LambdaAuthorizerConfig"></a>

A `LambdaAuthorizerConfig` specifies how to authorize AWS AppSync API access when using the `AWS_LAMBDA` authorizer mode. Be aware that an AWS AppSync API can have only one AWS Lambda authorizer configured at a time.

## Contents
<a name="API_LambdaAuthorizerConfig_Contents"></a>

 ** authorizerUri **   <a name="appsync-Type-LambdaAuthorizerConfig-authorizerUri"></a>
The Amazon Resource Name (ARN) of the Lambda function to be called for authorization. This can be a standard Lambda ARN, a version ARN (`.../v3`), or an alias ARN.   
 **Note**: This Lambda function must have the following resource-based policy assigned to it. When configuring Lambda authorizers in the console, this is done for you. To use the AWS Command Line Interface (AWS CLI), run the following:  
 `aws lambda add-permission --function-name "arn:aws:lambda:us-east-2:111122223333:function:my-function" --statement-id "appsync" --principal appsync.amazonaws.com --action lambda:InvokeFunction`   
Type: String  
Required: Yes

 ** authorizerResultTtlInSeconds **   <a name="appsync-Type-LambdaAuthorizerConfig-authorizerResultTtlInSeconds"></a>
The number of seconds a response should be cached for. The default is 0 seconds, which disables caching. If you don't specify a value for `authorizerResultTtlInSeconds`, the default value is used. The maximum value is one hour (3600 seconds). The Lambda function can override this by returning a `ttlOverride` key in its response.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 3600.  
Required: No

 ** identityValidationExpression **   <a name="appsync-Type-LambdaAuthorizerConfig-identityValidationExpression"></a>
A regular expression for validation of tokens before the Lambda function is called.  
Type: String  
Required: No

## See Also
<a name="API_LambdaAuthorizerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/LambdaAuthorizerConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/LambdaAuthorizerConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/LambdaAuthorizerConfig) 