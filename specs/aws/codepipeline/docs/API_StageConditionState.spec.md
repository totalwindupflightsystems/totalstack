---
id: "@specs/aws/codepipeline/docs/API_StageConditionState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StageConditionState"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# StageConditionState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_StageConditionState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StageConditionState
<a name="API_StageConditionState"></a>

The state of a run of a condition for a stage.

## Contents
<a name="API_StageConditionState_Contents"></a>

 ** conditionStates **   <a name="CodePipeline-Type-StageConditionState-conditionStates"></a>
The states of the conditions for a run of a condition for a stage.  
Type: Array of [ConditionState](API_ConditionState.md) objects  
Required: No

 ** latestExecution **   <a name="CodePipeline-Type-StageConditionState-latestExecution"></a>
Represents information about the latest run of a condition for a stage.  
Type: [StageConditionsExecution](API_StageConditionsExecution.md) object  
Required: No

## See Also
<a name="API_StageConditionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/StageConditionState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/StageConditionState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/StageConditionState) 