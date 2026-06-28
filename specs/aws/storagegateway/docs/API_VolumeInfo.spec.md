---
id: "@specs/aws/storagegateway/docs/API_VolumeInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS VolumeInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# VolumeInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_VolumeInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# VolumeInfo
<a name="API_VolumeInfo"></a>

Describes a storage volume object.

## Contents
<a name="API_VolumeInfo_Contents"></a>

 ** GatewayARN **   <a name="StorageGateway-Type-VolumeInfo-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** GatewayId **   <a name="StorageGateway-Type-VolumeInfo-GatewayId"></a>
The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.  
Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 30.  
Required: No

 ** VolumeARN **   <a name="StorageGateway-Type-VolumeInfo-VolumeARN"></a>
The Amazon Resource Name (ARN) for the storage volume. For example, the following is a valid ARN:  
 `arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB`   
Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: No

 ** VolumeAttachmentStatus **   <a name="StorageGateway-Type-VolumeInfo-VolumeAttachmentStatus"></a>
One of the VolumeStatus values that indicates the state of the storage volume.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Required: No

 ** VolumeId **   <a name="StorageGateway-Type-VolumeInfo-VolumeId"></a>
The unique identifier assigned to the volume. This ID becomes part of the volume Amazon Resource Name (ARN), which you use as input for other operations.  
Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 30.  
Required: No

 ** VolumeSizeInBytes **   <a name="StorageGateway-Type-VolumeInfo-VolumeSizeInBytes"></a>
The size of the volume in bytes.  
Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).  
Type: Long  
Required: No

 ** VolumeType **   <a name="StorageGateway-Type-VolumeInfo-VolumeType"></a>
One of the VolumeType enumeration values describing the type of the volume.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 100.  
Required: No

## See Also
<a name="API_VolumeInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/VolumeInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/VolumeInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/VolumeInfo) 