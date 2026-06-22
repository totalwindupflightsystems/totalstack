---
id: "@specs/aws/codepipeline/docs/API_StageState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StageState"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# StageState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_StageState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StageState
<a name="API_StageState"></a>

Represents information about the state of the stage.

## Contents
<a name="API_StageState_Contents"></a>

 ** actionStates **   <a name="CodePipeline-Type-StageState-actionStates"></a>
The state of the stage.  
Type: Array of [ActionState](API_ActionState.md) objects  
Required: No

 ** beforeEntryConditionState **   <a name="CodePipeline-Type-StageState-beforeEntryConditionState"></a>
The state of the entry conditions for a stage.  
Type: [StageConditionState](API_StageConditionState.md) object  
Required: No

 ** inboundExecution **   <a name="CodePipeline-Type-StageState-inboundExecution"></a>
Represents information about the run of a stage.  
Type: [StageExecution](API_StageExecution.md) object  
Required: No

 ** inboundExecutions **   <a name="CodePipeline-Type-StageState-inboundExecutions"></a>
The inbound executions for a stage.  
Type: Array of [StageExecution](API_StageExecution.md) objects  
Required: No

 ** inboundTransitionState **   <a name="CodePipeline-Type-StageState-inboundTransitionState"></a>
The state of the inbound transition, which is either enabled or disabled.  
Type: [TransitionState](API_TransitionState.md) object  
Required: No

 ** latestExecution **   <a name="CodePipeline-Type-StageState-latestExecution"></a>
Information about the latest execution in the stage, including its ID and status.  
Type: [StageExecution](API_StageExecution.md) object  
Required: No

 ** onFailureConditionState **   <a name="CodePipeline-Type-StageState-onFailureConditionState"></a>
The state of the failure conditions for a stage.  
Type: [StageConditionState](API_StageConditionState.md) object  
Required: No

 ** onSuccessConditionState **   <a name="CodePipeline-Type-StageState-onSuccessConditionState"></a>
The state of the success conditions for a stage.  
Type: [StageConditionState](API_StageConditionState.md) object  
Required: No

 ** retryStageMetadata **   <a name="CodePipeline-Type-StageState-retryStageMetadata"></a>
he details of a specific automatic retry on stage failure, including the attempt number and trigger.  
Type: [RetryStageMetadata](API_RetryStageMetadata.md) object  
Required: No

 ** stageName **   <a name="CodePipeline-Type-StageState-stageName"></a>
The name of the stage.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[A-Za-z0-9.@\-_]+`   
Required: No

## See Also
<a name="API_StageState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/StageState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/StageState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/StageState) 