---
id: "@specs/aws/codepipeline/docs/API_RuleExecutionResult"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleExecutionResult"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RuleExecutionResult

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RuleExecutionResult
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleExecutionResult
<a name="API_RuleExecutionResult"></a>

Execution result information, such as the external execution ID.

## Contents
<a name="API_RuleExecutionResult_Contents"></a>

 ** errorDetails **   <a name="CodePipeline-Type-RuleExecutionResult-errorDetails"></a>
Represents information about an error in CodePipeline.  
Type: [ErrorDetails](API_ErrorDetails.md) object  
Required: No

 ** externalExecutionId **   <a name="CodePipeline-Type-RuleExecutionResult-externalExecutionId"></a>
The external ID for the rule execution.  
Type: String  
Required: No

 ** externalExecutionSummary **   <a name="CodePipeline-Type-RuleExecutionResult-externalExecutionSummary"></a>
The external provider summary for the rule execution.  
Type: String  
Required: No

 ** externalExecutionUrl **   <a name="CodePipeline-Type-RuleExecutionResult-externalExecutionUrl"></a>
The deepest external link to the external resource (for example, a repository URL or deployment endpoint) that is used when running the rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_RuleExecutionResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleExecutionResult) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleExecutionResult) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleExecutionResult) 