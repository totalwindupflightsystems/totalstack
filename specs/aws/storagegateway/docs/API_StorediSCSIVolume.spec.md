---
id: "@specs/aws/storagegateway/docs/API_StorediSCSIVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StorediSCSIVolume"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# StorediSCSIVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_StorediSCSIVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StorediSCSIVolume
<a name="API_StorediSCSIVolume"></a>

Describes an iSCSI stored volume.

## Contents
<a name="API_StorediSCSIVolume_Contents"></a>

 ** CreatedDate **   <a name="StorageGateway-Type-StorediSCSIVolume-CreatedDate"></a>
The date the volume was created. Volumes created prior to March 28, 2017 don’t have this timestamp.  
Type: Timestamp  
Required: No

 ** KMSKey **   <a name="StorageGateway-Type-StorediSCSIVolume-KMSKey"></a>
Optional. The Amazon Resource Name (ARN) of a symmetric AWS KMS key used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric KMS keys. This value must be set if `KMSEncrypted` is `true`, or if `EncryptionType` is `SseKms` or `DsseKms`.  
Type: String  
Length Constraints: Minimum length of 7. Maximum length of 2048.  
Pattern: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`   
Required: No

 ** PreservedExistingData **   <a name="StorageGateway-Type-StorediSCSIVolume-PreservedExistingData"></a>
Indicates if when the stored volume was created, existing data on the underlying local disk was preserved.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** SourceSnapshotId **   <a name="StorageGateway-Type-StorediSCSIVolume-SourceSnapshotId"></a>
If the stored volume was created from a snapshot, this field contains the snapshot ID used, e.g. snap-78e22663. Otherwise, this field is not included.  
Type: String  
Pattern: `\Asnap-([0-9A-Fa-f]{8}|[0-9A-Fa-f]{17})\z`   
Required: No

 ** TargetName **   <a name="StorageGateway-Type-StorediSCSIVolume-TargetName"></a>
The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying `TargetName` as *myvolume* results in the target ARN of `arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume`. The target name must be unique across all volumes on a gateway.  
If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[-\.;a-z0-9]+$`   
Required: No

 ** VolumeARN **   <a name="StorageGateway-Type-StorediSCSIVolume-VolumeARN"></a>
The Amazon Resource Name (ARN) of the storage volume.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: No

 ** VolumeAttachmentStatus **   <a name="StorageGateway-Type-StorediSCSIVolume-VolumeAttachmentStatus"></a>
A value that indicates whether a storage volume is attached to, detached from, or is in the process of detaching from a gateway. For more information, see [Moving your volumes to a different gateway](https://docs.aws.amazon.com/storagegateway/latest/userguide/managing-volumes.html#attach-detach-volume).  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Required: No

 ** VolumeDiskId **   <a name="StorageGateway-Type-StorediSCSIVolume-VolumeDiskId"></a>
The ID of the local disk that was specified in the [CreateStorediSCSIVolume](API_CreateStorediSCSIVolume.md) operation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: No

 ** VolumeId **   <a name="StorageGateway-Type-StorediSCSIVolume-VolumeId"></a>
The unique identifier of the volume, e.g., vol-AE4B946D.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 30.  
Required: No

 ** VolumeiSCSIAttributes **   <a name="StorageGateway-Type-StorediSCSIVolume-VolumeiSCSIAttributes"></a>
An [VolumeiSCSIAttributes](API_VolumeiSCSIAttributes.md) object that represents a collection of iSCSI attributes for one stored volume.  
Type: [VolumeiSCSIAttributes](API_VolumeiSCSIAttributes.md) object  
Required: No

 ** VolumeProgress **   <a name="StorageGateway-Type-StorediSCSIVolume-VolumeProgress"></a>
Represents the percentage complete if the volume is restoring or bootstrapping that represents the percent of data transferred. This field does not appear in the response if the stored volume is not restoring or bootstrapping.  
Type: Double  
Required: No

 ** VolumeSizeInBytes **   <a name="StorageGateway-Type-StorediSCSIVolume-VolumeSizeInBytes"></a>
The size of the volume in bytes.  
Type: Long  
Required: No

 ** VolumeStatus **   <a name="StorageGateway-Type-StorediSCSIVolume-VolumeStatus"></a>
One of the VolumeStatus values that indicates the state of the storage volume.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Required: No

 ** VolumeType **   <a name="StorageGateway-Type-StorediSCSIVolume-VolumeType"></a>
One of the VolumeType enumeration values describing the type of the volume.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 100.  
Required: No

 ** VolumeUsedInBytes **   <a name="StorageGateway-Type-StorediSCSIVolume-VolumeUsedInBytes"></a>
The size of the data stored on the volume in bytes. This value is calculated based on the number of blocks that are touched, instead of the actual amount of data written. This value can be useful for sequential write patterns but less accurate for random write patterns. `VolumeUsedInBytes` is different from the compressed size of the volume, which is the value that is used to calculate your bill.  
This value is not available for volumes created prior to May 13, 2015, until you store data on the volume.
Type: Long  
Required: No

## See Also
<a name="API_StorediSCSIVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/StorediSCSIVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/StorediSCSIVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/StorediSCSIVolume) 