---
id: "@specs/aws/codepipeline/docs/API_ActionExecutionResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionExecutionResult"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionExecutionResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionExecutionResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionExecutionResult
<a name="API_ActionExecutionResult"></a>

Execution result information, such as the external execution ID.

## Contents
<a name="API_ActionExecutionResult_Contents"></a>

 ** errorDetails **   <a name="CodePipeline-Type-ActionExecutionResult-errorDetails"></a>
Represents information about an error in CodePipeline.  
Type: [ErrorDetails](API_ErrorDetails.md) object  
Required: No

 ** externalExecutionId **   <a name="CodePipeline-Type-ActionExecutionResult-externalExecutionId"></a>
The action provider's external ID for the action execution.  
Type: String  
Required: No

 ** externalExecutionSummary **   <a name="CodePipeline-Type-ActionExecutionResult-externalExecutionSummary"></a>
The action provider's summary for the action execution.  
Type: String  
Required: No

 ** externalExecutionUrl **   <a name="CodePipeline-Type-ActionExecutionResult-externalExecutionUrl"></a>
The deepest external link to the external resource (for example, a repository URL or deployment endpoint) that is used when running the action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** logStreamARN **   <a name="CodePipeline-Type-ActionExecutionResult-logStreamARN"></a>
The Amazon Resource Name (ARN) of the log stream for the action compute.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 250.  
Required: No

## See Also
<a name="API_ActionExecutionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionExecutionResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionExecutionResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionExecutionResult) 