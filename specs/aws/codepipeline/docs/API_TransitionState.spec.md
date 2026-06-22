---
id: "@specs/aws/codepipeline/docs/API_TransitionState"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TransitionState"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# TransitionState

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_TransitionState
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TransitionState
<a name="API_TransitionState"></a>

Represents information about the state of transitions between one stage and another stage.

## Contents
<a name="API_TransitionState_Contents"></a>

 ** disabledReason **   <a name="CodePipeline-Type-TransitionState-disabledReason"></a>
The user-specified reason why the transition between two stages of a pipeline was disabled.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Pattern: `[a-zA-Z0-9!@ \(\)\.\*\?\-]+`   
Required: No

 ** enabled **   <a name="CodePipeline-Type-TransitionState-enabled"></a>
Whether the transition between stages is enabled (true) or disabled (false).  
Type: Boolean  
Required: No

 ** lastChangedAt **   <a name="CodePipeline-Type-TransitionState-lastChangedAt"></a>
The timestamp when the transition state was last changed.  
Type: Timestamp  
Required: No

 ** lastChangedBy **   <a name="CodePipeline-Type-TransitionState-lastChangedBy"></a>
The ID of the user who last changed the transition state.  
Type: String  
Required: No

## See Also
<a name="API_TransitionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/TransitionState) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/TransitionState) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/TransitionState) 