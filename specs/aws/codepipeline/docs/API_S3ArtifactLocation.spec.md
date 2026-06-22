---
id: "@specs/aws/codepipeline/docs/API_S3ArtifactLocation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3ArtifactLocation"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# S3ArtifactLocation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_S3ArtifactLocation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3ArtifactLocation
<a name="API_S3ArtifactLocation"></a>

The location of the S3 bucket that contains a revision.

## Contents
<a name="API_S3ArtifactLocation_Contents"></a>

 ** bucketName **   <a name="CodePipeline-Type-S3ArtifactLocation-bucketName"></a>
The name of the S3 bucket.  
Type: String  
Required: Yes

 ** objectKey **   <a name="CodePipeline-Type-S3ArtifactLocation-objectKey"></a>
The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.  
Type: String  
Required: Yes

## See Also
<a name="API_S3ArtifactLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/S3ArtifactLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/S3ArtifactLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/S3ArtifactLocation) 