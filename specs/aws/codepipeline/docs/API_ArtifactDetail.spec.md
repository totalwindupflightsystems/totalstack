---
id: "@specs/aws/codepipeline/docs/API_ArtifactDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ArtifactDetail"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ArtifactDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ArtifactDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ArtifactDetail
<a name="API_ArtifactDetail"></a>

Artifact details for the action execution, such as the artifact location.

## Contents
<a name="API_ArtifactDetail_Contents"></a>

 ** name **   <a name="CodePipeline-Type-ArtifactDetail-name"></a>
The artifact object name for the action execution.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9_\-]+`   
Required: No

 ** s3location **   <a name="CodePipeline-Type-ArtifactDetail-s3location"></a>
The Amazon S3 artifact location for the action execution.  
Type: [S3Location](API_S3Location.md) object  
Required: No

## See Also
<a name="API_ArtifactDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ArtifactDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ArtifactDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ArtifactDetail) 