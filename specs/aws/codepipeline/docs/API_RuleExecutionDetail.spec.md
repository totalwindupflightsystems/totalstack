---
id: "@specs/aws/codepipeline/docs/API_RuleExecutionDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RuleExecutionDetail"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# RuleExecutionDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_RuleExecutionDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RuleExecutionDetail
<a name="API_RuleExecutionDetail"></a>

The details of the runs for a rule and the results produced on an artifact as it passes through stages in the pipeline.

## Contents
<a name="API_RuleExecutionDetail_Contents"></a>

 ** input **   <a name="CodePipeline-Type-RuleExecutionDetail-input"></a>
Input details for the rule execution, such as role ARN, Region, and input artifacts.  
Type: [RuleExecutionInput](API_RuleExecutionInput.md) object  
Required: No

 ** lastUpdateTime **   <a name="CodePipeline-Type-RuleExecutionDetail-lastUpdateTime"></a>
The date and time of the last change to the rule execution, in timestamp format.  
Type: Timestamp  
Required: No

 ** output **   <a name="CodePipeline-Type-RuleExecutionDetail-output"></a>
Output details for the rule execution, such as the rule execution result.  
Type: [RuleExecutionOutput](API_RuleExecutionOutput.md) object  
Required: No

 ** pipelineExecutionId **   <a name="CodePipeline-Type-RuleExecutionDetail-pipelineExecutionId"></a>
The ID of the pipeline execution in the stage where the rule was run. Use the [GetPipelineState](API_GetPipelineState.md) action to retrieve the current pipelineExecutionId of the stage.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

 ** pipelineVersion **   <a name="CodePipeline-Type-RuleExecutionDetail-pipelineVersion"></a>
The version number of the pipeline with the stage where the rule was run.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** ruleExecutionId **   <a name="CodePipeline-Type-RuleExecutionDetail-ruleExecutionId"></a>
The ID of the run for the rule.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** ruleName **   <a name="CodePipeline-Type-RuleExecutionDetail-ruleName"></a>
The name of the rule that was run in the stage.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

 ** stageName **   <a name="CodePipeline-Type-RuleExecutionDetail-stageName"></a>
The name of the stage where the rule was run.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

 ** startTime **   <a name="CodePipeline-Type-RuleExecutionDetail-startTime"></a>
The start time of the rule execution.  
Type: Timestamp  
Required: No

 ** status **   <a name="CodePipeline-Type-RuleExecutionDetail-status"></a>
The status of the rule execution. Status categories are `InProgress`, `Succeeded`, and `Failed`.   
Type: String  
Valid Values: `InProgress | Abandoned | Succeeded | Failed`   
Required: No

 ** updatedBy **   <a name="CodePipeline-Type-RuleExecutionDetail-updatedBy"></a>
The ARN of the user who changed the rule execution details.  
Type: String  
Required: No

## See Also
<a name="API_RuleExecutionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/RuleExecutionDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/RuleExecutionDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/RuleExecutionDetail) 