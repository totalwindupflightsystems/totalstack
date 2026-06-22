---
id: "@specs/aws/codepipeline/docs/API_StageConditionsExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StageConditionsExecution"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# StageConditionsExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_StageConditionsExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StageConditionsExecution
<a name="API_StageConditionsExecution"></a>

Represents information about the run of a condition for a stage.

## Contents
<a name="API_StageConditionsExecution_Contents"></a>

 ** status **   <a name="CodePipeline-Type-StageConditionsExecution-status"></a>
The status of a run of a condition for a stage.  
Type: String  
Valid Values: `InProgress | Failed | Errored | Succeeded | Cancelled | Abandoned | Overridden`   
Required: No

 ** summary **   <a name="CodePipeline-Type-StageConditionsExecution-summary"></a>
A summary of the run of the condition for a stage.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

## See Also
<a name="API_StageConditionsExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/StageConditionsExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/StageConditionsExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/StageConditionsExecution) 