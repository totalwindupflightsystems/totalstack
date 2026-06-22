---
id: "@specs/aws/batch/docs/API_EFSVolumeConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EFSVolumeConfiguration"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EFSVolumeConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EFSVolumeConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EFSVolumeConfiguration
<a name="API_EFSVolumeConfiguration"></a>

This is used when you're using an Amazon Elastic File System file system for job storage. For more information, see [Amazon EFS Volumes](https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html) in the * AWS Batch User Guide*.

## Contents
<a name="API_EFSVolumeConfiguration_Contents"></a>

 ** fileSystemId **   <a name="Batch-Type-EFSVolumeConfiguration-fileSystemId"></a>
The Amazon EFS file system ID to use.  
Type: String  
Required: Yes

 ** authorizationConfig **   <a name="Batch-Type-EFSVolumeConfiguration-authorizationConfig"></a>
The authorization configuration details for the Amazon EFS file system.  
Type: [EFSAuthorizationConfig](API_EFSAuthorizationConfig.md) object  
Required: No

 ** rootDirectory **   <a name="Batch-Type-EFSVolumeConfiguration-rootDirectory"></a>
The directory within the Amazon EFS file system to mount as the root directory inside the host. If this parameter is omitted, the root of the Amazon EFS volume is used instead. Specifying `/` has the same effect as omitting this parameter. The maximum length is 4,096 characters.  
If an EFS access point is specified in the `authorizationConfig`, the root directory parameter must either be omitted or set to `/`, which enforces the path set on the Amazon EFS access point.
Type: String  
Required: No

 ** transitEncryption **   <a name="Batch-Type-EFSVolumeConfiguration-transitEncryption"></a>
Determines whether to enable encryption for Amazon EFS data in transit between the Amazon ECS host and the Amazon EFS server. Transit encryption must be enabled if Amazon EFS IAM authorization is used. If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Encrypting data in transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html) in the *Amazon Elastic File System User Guide*.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

 ** transitEncryptionPort **   <a name="Batch-Type-EFSVolumeConfiguration-transitEncryptionPort"></a>
The port to use when sending encrypted data between the Amazon ECS host and the Amazon EFS server. If you don't specify a transit encryption port, it uses the port selection strategy that the Amazon EFS mount helper uses. The value must be between 0 and 65,535. For more information, see [EFS mount helper](https://docs.aws.amazon.com/efs/latest/ug/efs-mount-helper.html) in the *Amazon Elastic File System User Guide*.  
Type: Integer  
Required: No

## See Also
<a name="API_EFSVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EFSVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EFSVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EFSVolumeConfiguration) 