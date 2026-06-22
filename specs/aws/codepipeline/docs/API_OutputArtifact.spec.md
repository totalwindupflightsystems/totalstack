---
id: "@specs/aws/codepipeline/docs/API_OutputArtifact"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OutputArtifact"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# OutputArtifact

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_OutputArtifact
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OutputArtifact
<a name="API_OutputArtifact"></a>

Represents information about the output of an action.

## Contents
<a name="API_OutputArtifact_Contents"></a>

 ** name **   <a name="CodePipeline-Type-OutputArtifact-name"></a>
The name of the output of an artifact, such as "My App".  
The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.  
Output artifact names must be unique within a pipeline.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: Yes

 ** files **   <a name="CodePipeline-Type-OutputArtifact-files"></a>
The files that you want to associate with the output artifact that will be exported from the compute action.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

## See Also
<a name="API_OutputArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/OutputArtifact) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/OutputArtifact) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/OutputArtifact) 