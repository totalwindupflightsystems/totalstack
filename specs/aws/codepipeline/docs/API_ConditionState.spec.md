---
id: "@specs/aws/codepipeline/docs/API_ConditionState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ConditionState"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ConditionState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ConditionState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ConditionState
<a name="API_ConditionState"></a>

Information about the state of the condition.

## Contents
<a name="API_ConditionState_Contents"></a>

 ** latestExecution **   <a name="CodePipeline-Type-ConditionState-latestExecution"></a>
The state of the latest run of the rule.  
Type: [ConditionExecution](API_ConditionExecution.md) object  
Required: No

 ** ruleStates **   <a name="CodePipeline-Type-ConditionState-ruleStates"></a>
The state of the rules for the condition.  
Type: Array of [RuleState](API_RuleState.md) objects  
Required: No

## See Also
<a name="API_ConditionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ConditionState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ConditionState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ConditionState) 