---
id: "@specs/aws/codepipeline/docs/API_ActionExecutionOutput"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ActionExecutionOutput"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ActionExecutionOutput

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ActionExecutionOutput
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ActionExecutionOutput
<a name="API_ActionExecutionOutput"></a>

Output details listed for an action execution, such as the action execution result.

## Contents
<a name="API_ActionExecutionOutput_Contents"></a>

 ** executionResult **   <a name="CodePipeline-Type-ActionExecutionOutput-executionResult"></a>
Execution result information listed in the output details for an action execution.  
Type: [ActionExecutionResult](API_ActionExecutionResult.md) object  
Required: No

 ** outputArtifacts **   <a name="CodePipeline-Type-ActionExecutionOutput-outputArtifacts"></a>
Details of output artifacts of the action that correspond to the action execution.  
Type: Array of [ArtifactDetail](API_ArtifactDetail.md) objects  
Required: No

 ** outputVariables **   <a name="CodePipeline-Type-ActionExecutionOutput-outputVariables"></a>
The outputVariables field shows the key-value pairs that were output as part of that execution.  
Type: String to string map  
Key Pattern: `[A-Za-z0-9@\-_]+`   
Required: No

## See Also
<a name="API_ActionExecutionOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ActionExecutionOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ActionExecutionOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ActionExecutionOutput) 