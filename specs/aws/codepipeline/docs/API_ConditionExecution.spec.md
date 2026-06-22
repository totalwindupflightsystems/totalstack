---
id: "@specs/aws/codepipeline/docs/API_ConditionExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ConditionExecution"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ConditionExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ConditionExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ConditionExecution
<a name="API_ConditionExecution"></a>

The run of a condition.

## Contents
<a name="API_ConditionExecution_Contents"></a>

 ** lastStatusChange **   <a name="CodePipeline-Type-ConditionExecution-lastStatusChange"></a>
The last status change of the condition.  
Type: Timestamp  
Required: No

 ** status **   <a name="CodePipeline-Type-ConditionExecution-status"></a>
The status of the run for a condition.  
Type: String  
Valid Values: `InProgress | Failed | Errored | Succeeded | Cancelled | Abandoned | Overridden`   
Required: No

 ** summary **   <a name="CodePipeline-Type-ConditionExecution-summary"></a>
The summary of information about a run for a condition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_ConditionExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ConditionExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ConditionExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ConditionExecution) 