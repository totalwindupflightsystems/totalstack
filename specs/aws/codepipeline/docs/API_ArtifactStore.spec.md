---
id: "@specs/aws/codepipeline/docs/API_ArtifactStore"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ArtifactStore"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# ArtifactStore

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_ArtifactStore
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ArtifactStore
<a name="API_ArtifactStore"></a>

The S3 bucket where artifacts for the pipeline are stored.

**Note**  
You must include either `artifactStore` or `artifactStores` in your pipeline, but you cannot use both. If you create a cross-region action in your pipeline, you must use `artifactStores`.

## Contents
<a name="API_ArtifactStore_Contents"></a>

 ** location **   <a name="CodePipeline-Type-ArtifactStore-location"></a>
The S3 bucket used for storing the artifacts for a pipeline. You can specify the name of an S3 bucket but not a folder in the bucket. A folder to contain the pipeline artifacts is created for you based on the name of the pipeline. You can use any S3 bucket in the same AWS Region as the pipeline to store your pipeline artifacts.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `[a-zA-Z0-9\-\.]+`   
Required: Yes

 ** type **   <a name="CodePipeline-Type-ArtifactStore-type"></a>
The type of the artifact store, such as S3.  
Type: String  
Valid Values: `S3`   
Required: Yes

 ** encryptionKey **   <a name="CodePipeline-Type-ArtifactStore-encryptionKey"></a>
The encryption key used to encrypt the data in the artifact store, such as an AWS Key Management Service key. If this is undefined, the default key for Amazon S3 is used.  
Type: [EncryptionKey](API_EncryptionKey.md) object  
Required: No

## See Also
<a name="API_ArtifactStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ArtifactStore) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ArtifactStore) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ArtifactStore) 