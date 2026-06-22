---
id: "@specs/aws/codepipeline/docs/API_ActionExecution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionExecution"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionExecution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionExecution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionExecution
<a name="API_ActionExecution"></a>

Represents information about the run of an action.

## Contents
<a name="API_ActionExecution_Contents"></a>

 ** actionExecutionId **   <a name="CodePipeline-Type-ActionExecution-actionExecutionId"></a>
ID of the workflow action execution in the current stage. Use the [GetPipelineState](API_GetPipelineState.md) action to retrieve the current action execution details of the current stage.  
For older executions, this field might be empty. The action execution ID is available for executions run on or after March 2020.
Type: String  
Required: No

 ** errorDetails **   <a name="CodePipeline-Type-ActionExecution-errorDetails"></a>
The details of an error returned by a URL external to AWS.  
Type: [ErrorDetails](API_ErrorDetails.md) object  
Required: No

 ** externalExecutionId **   <a name="CodePipeline-Type-ActionExecution-externalExecutionId"></a>
The external ID of the run of the action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1500.  
Required: No

 ** externalExecutionUrl **   <a name="CodePipeline-Type-ActionExecution-externalExecutionUrl"></a>
The URL of a resource external to AWS that is used when running the action (for example, an external repository URL).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** lastStatusChange **   <a name="CodePipeline-Type-ActionExecution-lastStatusChange"></a>
The last status change of the action.  
Type: Timestamp  
Required: No

 ** lastUpdatedBy **   <a name="CodePipeline-Type-ActionExecution-lastUpdatedBy"></a>
The ARN of the user who last changed the pipeline.  
Type: String  
Required: No

 ** logStreamARN **   <a name="CodePipeline-Type-ActionExecution-logStreamARN"></a>
The Amazon Resource Name (ARN) of the log stream for the action compute.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 250.  
Required: No

 ** percentComplete **   <a name="CodePipeline-Type-ActionExecution-percentComplete"></a>
A percentage of completeness of the action as it runs.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

 ** status **   <a name="CodePipeline-Type-ActionExecution-status"></a>
The status of the action, or for a completed action, the last status of the action.  
Type: String  
Valid Values: `InProgress | Abandoned | Succeeded | Failed`   
Required: No

 ** summary **   <a name="CodePipeline-Type-ActionExecution-summary"></a>
A summary of the run of the action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** token **   <a name="CodePipeline-Type-ActionExecution-token"></a>
The system-generated token used to identify a unique approval request. The token for each open approval request can be obtained using the `GetPipelineState` command. It is used to validate that the approval request corresponding to this token is still valid.  
Type: String  
Required: No

## See Also
<a name="API_ActionExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionExecution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionExecution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionExecution) 