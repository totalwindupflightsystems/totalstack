---
id: "@specs/aws/codepipeline/docs/API_InputArtifact"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS InputArtifact"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# InputArtifact

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_InputArtifact
> **target_lang:** meta — documentation tier. ALL sections preserved.



# InputArtifact
<a name="API_InputArtifact"></a>

Represents information about an artifact to be worked on, such as a test or build artifact.

## Contents
<a name="API_InputArtifact_Contents"></a>

 ** name **   <a name="CodePipeline-Type-InputArtifact-name"></a>
The name of the artifact to be worked on (for example, "My App").  
Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action input artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp\_Windows.zip  
The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: Yes

## See Also
<a name="API_InputArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/InputArtifact) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/InputArtifact) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/InputArtifact) 