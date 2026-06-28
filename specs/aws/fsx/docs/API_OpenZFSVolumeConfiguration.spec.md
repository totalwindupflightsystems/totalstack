---
id: "@specs/aws/fsx/docs/API_OpenZFSVolumeConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OpenZFSVolumeConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# OpenZFSVolumeConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_OpenZFSVolumeConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OpenZFSVolumeConfiguration
<a name="API_OpenZFSVolumeConfiguration"></a>

The configuration of an Amazon FSx for OpenZFS volume.

## Contents
<a name="API_OpenZFSVolumeConfiguration_Contents"></a>

 ** CopyStrategy **   <a name="FSx-Type-OpenZFSVolumeConfiguration-CopyStrategy"></a>
Specifies the strategy used when copying data from the snapshot to the new volume.   
+  `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesn't consume disk throughput. However, the origin snapshot can't be deleted if there is a volume using its copied data.
+  `FULL_COPY` - Copies all data from the snapshot to the new volume.

  Specify this option to create the volume from a snapshot on another FSx for OpenZFS file system.
The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html).
Type: String  
Valid Values: `CLONE | FULL_COPY | INCREMENTAL_COPY`   
Required: No

 ** CopyTagsToSnapshots **   <a name="FSx-Type-OpenZFSVolumeConfiguration-CopyTagsToSnapshots"></a>
A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false`. If it's set to `true`, all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.  
Type: Boolean  
Required: No

 ** DataCompressionType **   <a name="FSx-Type-OpenZFSVolumeConfiguration-DataCompressionType"></a>
Specifies the method used to compress the data on the volume. The compression type is `NONE` by default.  
+  `NONE` - Doesn't compress the data on the volume. `NONE` is the default.
+  `ZSTD` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.
+  `LZ4` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.
Type: String  
Valid Values: `NONE | ZSTD | LZ4`   
Required: No

 ** DeleteClonedVolumes **   <a name="FSx-Type-OpenZFSVolumeConfiguration-DeleteClonedVolumes"></a>
A Boolean value indicating whether dependent clone volumes created from intermediate snapshots should be deleted when a volume is restored from snapshot.  
Type: Boolean  
Required: No

 ** DeleteIntermediateData **   <a name="FSx-Type-OpenZFSVolumeConfiguration-DeleteIntermediateData"></a>
A Boolean value indicating whether snapshot data that differs between the current state and the specified snapshot should be overwritten when a volume is restored from a snapshot.  
Type: Boolean  
Required: No

 ** DeleteIntermediateSnaphots **   <a name="FSx-Type-OpenZFSVolumeConfiguration-DeleteIntermediateSnaphots"></a>
A Boolean value indicating whether snapshots between the current state and the specified snapshot should be deleted when a volume is restored from snapshot.  
Type: Boolean  
Required: No

 ** DestinationSnapshot **   <a name="FSx-Type-OpenZFSVolumeConfiguration-DestinationSnapshot"></a>
The ID of the snapshot that's being copied or was most recently copied to the destination volume.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 28.  
Pattern: `^((fs)?volsnap-[0-9a-f]{8,})$`   
Required: No

 ** NfsExports **   <a name="FSx-Type-OpenZFSVolumeConfiguration-NfsExports"></a>
The configuration object for mounting a Network File System (NFS) file system.  
Type: Array of [OpenZFSNfsExport](API_OpenZFSNfsExport.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

 ** OriginSnapshot **   <a name="FSx-Type-OpenZFSVolumeConfiguration-OriginSnapshot"></a>
The configuration object that specifies the snapshot to use as the origin of the data for the volume.  
Type: [OpenZFSOriginSnapshotConfiguration](API_OpenZFSOriginSnapshotConfiguration.md) object  
Required: No

 ** ParentVolumeId **   <a name="FSx-Type-OpenZFSVolumeConfiguration-ParentVolumeId"></a>
The ID of the parent volume.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: No

 ** ReadOnly **   <a name="FSx-Type-OpenZFSVolumeConfiguration-ReadOnly"></a>
A Boolean value indicating whether the volume is read-only.  
Type: Boolean  
Required: No

 ** RecordSizeKiB **   <a name="FSx-Type-OpenZFSVolumeConfiguration-RecordSizeKiB"></a>
The record size of an OpenZFS volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. For guidance on when to set a custom record size, see the *Amazon FSx for OpenZFS User Guide*.  
Type: Integer  
Valid Range: Minimum value of 4. Maximum value of 4096.  
Required: No

 ** RestoreToSnapshot **   <a name="FSx-Type-OpenZFSVolumeConfiguration-RestoreToSnapshot"></a>
Specifies the ID of the snapshot to which the volume was restored.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 28.  
Pattern: `^((fs)?volsnap-[0-9a-f]{8,})$`   
Required: No

 ** SourceSnapshotARN **   <a name="FSx-Type-OpenZFSVolumeConfiguration-SourceSnapshotARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: No

 ** StorageCapacityQuotaGiB **   <a name="FSx-Type-OpenZFSVolumeConfiguration-StorageCapacityQuotaGiB"></a>
The maximum amount of storage in gibibytes (GiB) that the volume can use from its parent. You can specify a quota larger than the storage on the parent volume.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: No

 ** StorageCapacityReservationGiB **   <a name="FSx-Type-OpenZFSVolumeConfiguration-StorageCapacityReservationGiB"></a>
The amount of storage in gibibytes (GiB) to reserve from the parent volume. You can't reserve more storage than the parent volume has reserved.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: No

 ** UserAndGroupQuotas **   <a name="FSx-Type-OpenZFSVolumeConfiguration-UserAndGroupQuotas"></a>
An object specifying how much storage users or groups can use on the volume.  
Type: Array of [OpenZFSUserOrGroupQuota](API_OpenZFSUserOrGroupQuota.md) objects  
Array Members: Maximum number of 500 items.  
Required: No

 ** VolumePath **   <a name="FSx-Type-OpenZFSVolumeConfiguration-VolumePath"></a>
The path to the volume from the root volume. For example, `fsx/parentVolume/volume1`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^[A-za-z0-9\_\.\:\-\/]*$`   
Required: No

## See Also
<a name="API_OpenZFSVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OpenZFSVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OpenZFSVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OpenZFSVolumeConfiguration) 