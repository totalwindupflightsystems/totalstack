---
id: "@specs/aws/batch/docs/API_S3FilesVolumeConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3FilesVolumeConfiguration"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# S3FilesVolumeConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_S3FilesVolumeConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3FilesVolumeConfiguration
<a name="API_S3FilesVolumeConfiguration"></a>

This is used when you're using an S3Files file system for job storage.

## Contents
<a name="API_S3FilesVolumeConfiguration_Contents"></a>

 ** fileSystemArn **   <a name="Batch-Type-S3FilesVolumeConfiguration-fileSystemArn"></a>
The Amazon Resource Name (ARN) of the S3Files file system to use.  
Type: String  
Required: Yes

 ** accessPointArn **   <a name="Batch-Type-S3FilesVolumeConfiguration-accessPointArn"></a>
The Amazon Resource Name (ARN) of the S3Files access point to use.  
Type: String  
Required: No

 ** rootDirectory **   <a name="Batch-Type-S3FilesVolumeConfiguration-rootDirectory"></a>
The directory within the S3Files file system to mount as the root directory.  
Type: String  
Required: No

 ** transitEncryptionPort **   <a name="Batch-Type-S3FilesVolumeConfiguration-transitEncryptionPort"></a>
The port to use when sending encrypted data between the Amazon ECS host and the S3Files file system server.  
Type: Integer  
Required: No

## See Also
<a name="API_S3FilesVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/S3FilesVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/S3FilesVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/S3FilesVolumeConfiguration) 