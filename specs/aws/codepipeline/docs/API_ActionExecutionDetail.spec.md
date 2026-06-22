---
id: "@specs/aws/codepipeline/docs/API_ActionExecutionDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionExecutionDetail"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionExecutionDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionExecutionDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionExecutionDetail
<a name="API_ActionExecutionDetail"></a>

Returns information about an execution of an action, including the action execution ID, and the name, version, and timing of the action. 

## Contents
<a name="API_ActionExecutionDetail_Contents"></a>

 ** actionExecutionId **   <a name="CodePipeline-Type-ActionExecutionDetail-actionExecutionId"></a>
The action execution ID.  
Type: String  
Required: No

 ** actionName **   <a name="CodePipeline-Type-ActionExecutionDetail-actionName"></a>
The name of the action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

 ** input **   <a name="CodePipeline-Type-ActionExecutionDetail-input"></a>
Input details for the action execution, such as role ARN, Region, and input artifacts.  
Type: [ActionExecutionInput](API_ActionExecutionInput.md) object  
Required: No

 ** lastUpdateTime **   <a name="CodePipeline-Type-ActionExecutionDetail-lastUpdateTime"></a>
The last update time of the action execution.  
Type: Timestamp  
Required: No

 ** output **   <a name="CodePipeline-Type-ActionExecutionDetail-output"></a>
Output details for the action execution, such as the action execution result.  
Type: [ActionExecutionOutput](API_ActionExecutionOutput.md) object  
Required: No

 ** pipelineExecutionId **   <a name="CodePipeline-Type-ActionExecutionDetail-pipelineExecutionId"></a>
The pipeline execution ID for the action execution.  
Type: String  
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`   
Required: No

 ** pipelineVersion **   <a name="CodePipeline-Type-ActionExecutionDetail-pipelineVersion"></a>
The version of the pipeline where the action was run.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** stageName **   <a name="CodePipeline-Type-ActionExecutionDetail-stageName"></a>
The name of the stage that contains the action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

 ** startTime **   <a name="CodePipeline-Type-ActionExecutionDetail-startTime"></a>
The start time of the action execution.  
Type: Timestamp  
Required: No

 ** status **   <a name="CodePipeline-Type-ActionExecutionDetail-status"></a>
 The status of the action execution. Status categories are `InProgress`, `Succeeded`, and `Failed`.  
Type: String  
Valid Values: `InProgress | Abandoned | Succeeded | Failed`   
Required: No

 ** updatedBy **   <a name="CodePipeline-Type-ActionExecutionDetail-updatedBy"></a>
The ARN of the user who changed the pipeline execution details.  
Type: String  
Required: No

## See Also
<a name="API_ActionExecutionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionExecutionDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionExecutionDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionExecutionDetail) 