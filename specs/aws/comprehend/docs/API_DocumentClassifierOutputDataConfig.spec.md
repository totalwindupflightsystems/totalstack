---
id: "@specs/aws/comprehend/docs/API_DocumentClassifierOutputDataConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DocumentClassifierOutputDataConfig"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DocumentClassifierOutputDataConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DocumentClassifierOutputDataConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DocumentClassifierOutputDataConfig
<a name="API_DocumentClassifierOutputDataConfig"></a>

Provide the location for output data from a custom classifier job. This field is mandatory if you are training a native document model.

## Contents
<a name="API_DocumentClassifierOutputDataConfig_Contents"></a>

 ** FlywheelStatsS3Prefix **   <a name="comprehend-Type-DocumentClassifierOutputDataConfig-FlywheelStatsS3Prefix"></a>
The Amazon S3 prefix for the data lake location of the flywheel statistics.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

 ** KmsKeyId **   <a name="comprehend-Type-DocumentClassifierOutputDataConfig-KmsKeyId"></a>
ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt the output results from an analysis job. The KmsKeyId can be one of the following formats:  
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"` 
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"` 
+ KMS Key Alias: `"alias/ExampleAlias"` 
+ ARN of a KMS Key Alias: `"arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias"` 
Type: String  
Length Constraints: Maximum length of 2048.  
Pattern: `^\p{ASCII}+$`   
Required: No

 ** S3Uri **   <a name="comprehend-Type-DocumentClassifierOutputDataConfig-S3Uri"></a>
When you use the `OutputDataConfig` object while creating a custom classifier, you specify the Amazon S3 location where you want to write the confusion matrix and other output files. The URI must be in the same Region as the API endpoint that you are calling. The location is used as the prefix for the actual location of this output file.  
When the custom classifier job is finished, the service creates the output file in a directory specific to the job. The `S3Uri` field contains the location of the output file, called `output.tar.gz`. It is a compressed archive that contains the confusion matrix.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`   
Required: No

## See Also
<a name="API_DocumentClassifierOutputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DocumentClassifierOutputDataConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DocumentClassifierOutputDataConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DocumentClassifierOutputDataConfig) 