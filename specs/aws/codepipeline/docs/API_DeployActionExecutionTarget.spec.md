---
id: "@specs/aws/codepipeline/docs/API_DeployActionExecutionTarget"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeployActionExecutionTarget"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# DeployActionExecutionTarget

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_DeployActionExecutionTarget
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeployActionExecutionTarget
<a name="API_DeployActionExecutionTarget"></a>

The target for the deploy action.

## Contents
<a name="API_DeployActionExecutionTarget_Contents"></a>

 ** endTime **   <a name="CodePipeline-Type-DeployActionExecutionTarget-endTime"></a>
The end time for the deploy action.  
Type: Timestamp  
Required: No

 ** events **   <a name="CodePipeline-Type-DeployActionExecutionTarget-events"></a>
The lifecycle events for the deploy action.  
Type: Array of [DeployTargetEvent](API_DeployTargetEvent.md) objects  
Required: No

 ** startTime **   <a name="CodePipeline-Type-DeployActionExecutionTarget-startTime"></a>
The start time for the deploy action.  
Type: Timestamp  
Required: No

 ** status **   <a name="CodePipeline-Type-DeployActionExecutionTarget-status"></a>
The status of the deploy action.  
Type: String  
Required: No

 ** targetId **   <a name="CodePipeline-Type-DeployActionExecutionTarget-targetId"></a>
The ID of the target for the deploy action.  
Type: String  
Required: No

 ** targetType **   <a name="CodePipeline-Type-DeployActionExecutionTarget-targetType"></a>
The type of target for the deploy action.  
Type: String  
Required: No

## See Also
<a name="API_DeployActionExecutionTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/DeployActionExecutionTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/DeployActionExecutionTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/DeployActionExecutionTarget) 