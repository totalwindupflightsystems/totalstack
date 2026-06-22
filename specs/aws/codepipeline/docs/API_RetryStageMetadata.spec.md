---
id: "@specs/aws/codepipeline/docs/API_RetryStageMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RetryStageMetadata"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RetryStageMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RetryStageMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RetryStageMetadata
<a name="API_RetryStageMetadata"></a>

The details of a specific automatic retry on stage failure, including the attempt number and trigger.

## Contents
<a name="API_RetryStageMetadata_Contents"></a>

 ** autoStageRetryAttempt **   <a name="CodePipeline-Type-RetryStageMetadata-autoStageRetryAttempt"></a>
The number of attempts for a specific stage with automatic retry on stage failure. One attempt is allowed for automatic stage retry on failure.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** latestRetryTrigger **   <a name="CodePipeline-Type-RetryStageMetadata-latestRetryTrigger"></a>
The latest trigger for a specific stage where manual or automatic retries have been made upon stage failure.  
Type: String  
Valid Values: `AutomatedStageRetry | ManualStageRetry`   
Required: No

 ** manualStageRetryAttempt **   <a name="CodePipeline-Type-RetryStageMetadata-manualStageRetryAttempt"></a>
The number of attempts for a specific stage where manual retries have been made upon stage failure.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

## See Also
<a name="API_RetryStageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RetryStageMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RetryStageMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RetryStageMetadata) 