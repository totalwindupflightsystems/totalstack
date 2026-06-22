---
id: "@specs/aws/codepipeline/docs/API_DeployTargetEvent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeployTargetEvent"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# DeployTargetEvent

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_DeployTargetEvent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeployTargetEvent
<a name="API_DeployTargetEvent"></a>

A lifecycle event for the deploy action.

## Contents
<a name="API_DeployTargetEvent_Contents"></a>

 ** context **   <a name="CodePipeline-Type-DeployTargetEvent-context"></a>
The context for the event for the deploy action.  
Type: [DeployTargetEventContext](API_DeployTargetEventContext.md) object  
Required: No

 ** endTime **   <a name="CodePipeline-Type-DeployTargetEvent-endTime"></a>
The end time for the event for the deploy action.  
Type: Timestamp  
Required: No

 ** name **   <a name="CodePipeline-Type-DeployTargetEvent-name"></a>
The name of the event for the deploy action.  
Type: String  
Required: No

 ** startTime **   <a name="CodePipeline-Type-DeployTargetEvent-startTime"></a>
The start time for the event for the deploy action.  
Type: Timestamp  
Required: No

 ** status **   <a name="CodePipeline-Type-DeployTargetEvent-status"></a>
The status of the event for the deploy action.  
Type: String  
Required: No

## See Also
<a name="API_DeployTargetEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/DeployTargetEvent) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/DeployTargetEvent) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/DeployTargetEvent) 