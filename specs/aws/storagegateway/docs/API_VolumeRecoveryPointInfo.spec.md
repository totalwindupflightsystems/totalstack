---
id: "@specs/aws/storagegateway/docs/API_VolumeRecoveryPointInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VolumeRecoveryPointInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# VolumeRecoveryPointInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_VolumeRecoveryPointInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VolumeRecoveryPointInfo
<a name="API_VolumeRecoveryPointInfo"></a>

Describes a storage volume recovery point object.

## Contents
<a name="API_VolumeRecoveryPointInfo_Contents"></a>

 ** VolumeARN **   <a name="StorageGateway-Type-VolumeRecoveryPointInfo-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume target.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: No

 ** VolumeRecoveryPointTime **   <a name="StorageGateway-Type-VolumeRecoveryPointInfo-VolumeRecoveryPointTime"></a>
The time the recovery point was taken.  
Type: String  
Required: No

 ** VolumeSizeInBytes **   <a name="StorageGateway-Type-VolumeRecoveryPointInfo-VolumeSizeInBytes"></a>
The size of the volume in bytes.  
Type: Long  
Required: No

 ** VolumeUsageInBytes **   <a name="StorageGateway-Type-VolumeRecoveryPointInfo-VolumeUsageInBytes"></a>
The size of the data stored on the volume in bytes.  
This value is not available for volumes created prior to May 13, 2015, until you store data on the volume.
Type: Long  
Required: No

## See Also
<a name="API_VolumeRecoveryPointInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/VolumeRecoveryPointInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/VolumeRecoveryPointInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/VolumeRecoveryPointInfo) 