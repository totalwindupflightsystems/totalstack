---
id: "@specs/aws/codepipeline/docs/API_LambdaExecutorConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LambdaExecutorConfiguration"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# LambdaExecutorConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_LambdaExecutorConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LambdaExecutorConfiguration
<a name="API_LambdaExecutorConfiguration"></a>

Details about the configuration for the `Lambda` action engine, or executor.

## Contents
<a name="API_LambdaExecutorConfiguration_Contents"></a>

 ** lambdaFunctionArn **   <a name="CodePipeline-Type-LambdaExecutorConfiguration-lambdaFunctionArn"></a>
The ARN of the Lambda function used by the action engine.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Pattern: `arn:aws(-[\w]+)*:lambda:.+:[0-9]{12}:function:.+`   
Required: Yes

## See Also
<a name="API_LambdaExecutorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/LambdaExecutorConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/LambdaExecutorConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/LambdaExecutorConfiguration) 