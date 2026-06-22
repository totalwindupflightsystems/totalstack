---
id: "@specs/aws/codepipeline/docs/API_Artifact"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Artifact"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# Artifact

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_Artifact
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Artifact
<a name="API_Artifact"></a>

Artifacts are the files that are worked on by actions in the pipeline. See the action configuration for each action for details about artifact parameters. For example, the S3 source action artifact is a file name (or file path), and the files are generally provided as a ZIP file. Example artifact name: SampleApp\_Windows.zip

## Contents
<a name="API_Artifact_Contents"></a>

 ** location **   <a name="CodePipeline-Type-Artifact-location"></a>
The location of an artifact.  
Type: [ArtifactLocation](API_ArtifactLocation.md) object  
Required: No

 ** name **   <a name="CodePipeline-Type-Artifact-name"></a>
The artifact's name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: No

 ** revision **   <a name="CodePipeline-Type-Artifact-revision"></a>
The artifact's revision ID. Depending on the type of object, this could be a commit ID (GitHub) or a revision ID (Amazon S3).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1500.  
Required: No

## See Also
<a name="API_Artifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/Artifact) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/Artifact) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/Artifact) 