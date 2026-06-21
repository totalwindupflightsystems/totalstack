---
id: "@specs/aws/cloudtrail/docs/API_S3ImportSource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3ImportSource"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# S3ImportSource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_S3ImportSource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3ImportSource
<a name="API_S3ImportSource"></a>

 The settings for the source S3 bucket. 

## Contents
<a name="API_S3ImportSource_Contents"></a>

 ** S3BucketAccessRoleArn **   <a name="awscloudtrail-Type-S3ImportSource-S3BucketAccessRoleArn"></a>
 The IAM ARN role used to access the source S3 bucket.   
Type: String  
Required: Yes

 ** S3BucketRegion **   <a name="awscloudtrail-Type-S3ImportSource-S3BucketRegion"></a>
 The Region associated with the source S3 bucket.   
Type: String  
Required: Yes

 ** S3LocationUri **   <a name="awscloudtrail-Type-S3ImportSource-S3LocationUri"></a>
 The URI for the source S3 bucket.   
Type: String  
Required: Yes

## See Also
<a name="API_S3ImportSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/S3ImportSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/S3ImportSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/S3ImportSource) 