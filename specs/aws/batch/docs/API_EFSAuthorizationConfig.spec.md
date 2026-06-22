---
id: "@specs/aws/batch/docs/API_EFSAuthorizationConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EFSAuthorizationConfig"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EFSAuthorizationConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EFSAuthorizationConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EFSAuthorizationConfig
<a name="API_EFSAuthorizationConfig"></a>

The authorization configuration details for the Amazon EFS file system.

## Contents
<a name="API_EFSAuthorizationConfig_Contents"></a>

 ** accessPointId **   <a name="Batch-Type-EFSAuthorizationConfig-accessPointId"></a>
The Amazon EFS access point ID to use. If an access point is specified, the root directory value specified in the `EFSVolumeConfiguration` must either be omitted or set to `/` which enforces the path set on the EFS access point. If an access point is used, transit encryption must be enabled in the `EFSVolumeConfiguration`. For more information, see [Working with Amazon EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) in the *Amazon Elastic File System User Guide*.  
Type: String  
Required: No

 ** iam **   <a name="Batch-Type-EFSAuthorizationConfig-iam"></a>
Whether or not to use the AWS Batch job IAM role defined in a job definition when mounting the Amazon EFS file system. If enabled, transit encryption must be enabled in the `EFSVolumeConfiguration`. If this parameter is omitted, the default value of `DISABLED` is used. For more information, see [Using Amazon EFS access points](https://docs.aws.amazon.com/batch/latest/userguide/efs-volumes.html#efs-volume-accesspoints) in the * AWS Batch User Guide*. EFS IAM authorization requires that `TransitEncryption` be `ENABLED` and that a `JobRoleArn` is specified.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: No

## See Also
<a name="API_EFSAuthorizationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EFSAuthorizationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EFSAuthorizationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EFSAuthorizationConfig) 