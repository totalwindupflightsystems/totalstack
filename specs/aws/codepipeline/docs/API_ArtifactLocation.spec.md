---
id: "@specs/aws/codepipeline/docs/API_ArtifactLocation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ArtifactLocation"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ArtifactLocation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ArtifactLocation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ArtifactLocation
<a name="API_ArtifactLocation"></a>

Represents information about the location of an artifact.

## Contents
<a name="API_ArtifactLocation_Contents"></a>

 ** s3Location **   <a name="CodePipeline-Type-ArtifactLocation-s3Location"></a>
The S3 bucket that contains the artifact.  
Type: [S3ArtifactLocation](API_S3ArtifactLocation.md) object  
Required: No

 ** type **   <a name="CodePipeline-Type-ArtifactLocation-type"></a>
The type of artifact in the location.  
Type: String  
Valid Values: `S3`   
Required: No

## See Also
<a name="API_ArtifactLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ArtifactLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ArtifactLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ArtifactLocation) 