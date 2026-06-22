---
id: "@specs/aws/codepipeline/docs/API_RuleExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleExecution"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RuleExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RuleExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleExecution
<a name="API_RuleExecution"></a>

Represents information about each time a rule is run as part of the pipeline execution for a pipeline configured with conditions.

## Contents
<a name="API_RuleExecution_Contents"></a>

 ** errorDetails **   <a name="CodePipeline-Type-RuleExecution-errorDetails"></a>
Represents information about an error in CodePipeline.  
Type: [ErrorDetails](API_ErrorDetails.md) object  
Required: No

 ** externalExecutionId **   <a name="CodePipeline-Type-RuleExecution-externalExecutionId"></a>
The external ID of the run of the rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1500.  
Required: No

 ** externalExecutionUrl **   <a name="CodePipeline-Type-RuleExecution-externalExecutionUrl"></a>
The URL of a resource external to AWS that is used when running the rule (for example, an external repository URL).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** lastStatusChange **   <a name="CodePipeline-Type-RuleExecution-lastStatusChange"></a>
The last status change of the rule.  
Type: Timestamp  
Required: No

 ** lastUpdatedBy **   <a name="CodePipeline-Type-RuleExecution-lastUpdatedBy"></a>
The ARN of the user who last changed the rule.  
Type: String  
Required: No

 ** ruleExecutionId **   <a name="CodePipeline-Type-RuleExecution-ruleExecutionId"></a>
The execution ID for the run of the rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** status **   <a name="CodePipeline-Type-RuleExecution-status"></a>
The status of the run of the rule, such as FAILED.  
Type: String  
Valid Values: `InProgress | Abandoned | Succeeded | Failed`   
Required: No

 ** summary **   <a name="CodePipeline-Type-RuleExecution-summary"></a>
A summary of the run of the rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** token **   <a name="CodePipeline-Type-RuleExecution-token"></a>
The system-generated token used to identify a unique request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[a-zA-Z0-9\-\.]+`   
Required: No

## See Also
<a name="API_RuleExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleExecution) 