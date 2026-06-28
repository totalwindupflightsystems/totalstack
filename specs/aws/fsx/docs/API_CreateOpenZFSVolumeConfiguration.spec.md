---
id: "@specs/aws/fsx/docs/API_CreateOpenZFSVolumeConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateOpenZFSVolumeConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateOpenZFSVolumeConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateOpenZFSVolumeConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateOpenZFSVolumeConfiguration
<a name="API_CreateOpenZFSVolumeConfiguration"></a>

Specifies the configuration of the Amazon FSx for OpenZFS volume that you are creating.

## Contents
<a name="API_CreateOpenZFSVolumeConfiguration_Contents"></a>

 ** ParentVolumeId **   <a name="FSx-Type-CreateOpenZFSVolumeConfiguration-ParentVolumeId"></a>
The ID of the volume to use as the parent volume of the volume that you are creating.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: Yes

 ** CopyTagsToSnapshots **   <a name="FSx-Type-CreateOpenZFSVolumeConfiguration-CopyTagsToSnapshots"></a>
A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false`. If this value is set to `true`, and you do not specify any tags, all tags for the original volume are copied over to snapshots. If this value is set to `true`, and you do specify one or more tags, only the specified tags for the original volume are copied over to snapshots. If you specify one or more tags when creating a new snapshot, no tags are copied over from the original volume, regardless of this value.   
Type: Boolean  
Required: No

 ** DataCompressionType **   <a name="FSx-Type-CreateOpenZFSVolumeConfiguration-DataCompressionType"></a>
Specifies the method used to compress the data on the volume. The compression type is `NONE` by default.  
+  `NONE` - Doesn't compress the data on the volume. `NONE` is the default.
+  `ZSTD` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. ZSTD compression provides a higher level of data compression and higher read throughput performance than LZ4 compression.
+  `LZ4` - Compresses the data in the volume using the LZ4 compression algorithm. LZ4 compression provides a lower level of compression and higher write throughput performance than ZSTD compression.
For more information about volume compression types and the performance of your Amazon FSx for OpenZFS file system, see [ Tips for maximizing performance](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#performance-tips-zfs) File system and volume settings in the *Amazon FSx for OpenZFS User Guide*.  
Type: String  
Valid Values: `NONE | ZSTD | LZ4`   
Required: No

 ** NfsExports **   <a name="FSx-Type-CreateOpenZFSVolumeConfiguration-NfsExports"></a>
The configuration object for mounting a Network File System (NFS) file system.  
Type: Array of [OpenZFSNfsExport](API_OpenZFSNfsExport.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

 ** OriginSnapshot **   <a name="FSx-Type-CreateOpenZFSVolumeConfiguration-OriginSnapshot"></a>
The configuration object that specifies the snapshot to use as the origin of the data for the volume.  
Type: [CreateOpenZFSOriginSnapshotConfiguration](API_CreateOpenZFSOriginSnapshotConfiguration.md) object  
Required: No

 ** ReadOnly **   <a name="FSx-Type-CreateOpenZFSVolumeConfiguration-ReadOnly"></a>
A Boolean value indicating whether the volume is read-only.  
Type: Boolean  
Required: No

 ** RecordSizeKiB **   <a name="FSx-Type-CreateOpenZFSVolumeConfiguration-RecordSizeKiB"></a>
Specifies the suggested block size for a volume in a ZFS dataset, in kibibytes (KiB). For file systems using the Intelligent-Tiering storage class, valid values are 128, 256, 512, 1024, 2048, or 4096 KiB, with a default of 1024 KiB. For all other file systems, valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB, with a default of 128 KiB. We recommend using the default setting for the majority of use cases. Generally, workloads that write in fixed small or large record sizes may benefit from setting a custom record size, like database workloads (small record size) or media streaming workloads (large record size). For additional guidance on when to set a custom record size, see [ ZFS Record size](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#record-size-performance) in the *Amazon FSx for OpenZFS User Guide*.  
Type: Integer  
Valid Range: Minimum value of 4. Maximum value of 4096.  
Required: No

 ** StorageCapacityQuotaGiB **   <a name="FSx-Type-CreateOpenZFSVolumeConfiguration-StorageCapacityQuotaGiB"></a>
Sets the maximum storage size in gibibytes (GiB) for the volume. You can specify a quota that is larger than the storage on the parent volume. A volume quota limits the amount of storage that the volume can consume to the configured amount, but does not guarantee the space will be available on the parent volume. To guarantee quota space, you must also set `StorageCapacityReservationGiB`. To *not* specify a storage capacity quota, set this to `-1`.   
For more information, see [Volume properties](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties) in the *Amazon FSx for OpenZFS User Guide*.  
Type: Integer  
Valid Range: Minimum value of -1. Maximum value of 2147483647.  
Required: No

 ** StorageCapacityReservationGiB **   <a name="FSx-Type-CreateOpenZFSVolumeConfiguration-StorageCapacityReservationGiB"></a>
Specifies the amount of storage in gibibytes (GiB) to reserve from the parent volume. Setting `StorageCapacityReservationGiB` guarantees that the specified amount of storage space on the parent volume will always be available for the volume. You can't reserve more storage than the parent volume has. To *not* specify a storage capacity reservation, set this to `0` or `-1`. For more information, see [Volume properties](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties) in the *Amazon FSx for OpenZFS User Guide*.  
Type: Integer  
Valid Range: Minimum value of -1. Maximum value of 2147483647.  
Required: No

 ** UserAndGroupQuotas **   <a name="FSx-Type-CreateOpenZFSVolumeConfiguration-UserAndGroupQuotas"></a>
Configures how much storage users and groups can use on the volume.  
Type: Array of [OpenZFSUserOrGroupQuota](API_OpenZFSUserOrGroupQuota.md) objects  
Array Members: Maximum number of 500 items.  
Required: No

## See Also
<a name="API_CreateOpenZFSVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateOpenZFSVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateOpenZFSVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateOpenZFSVolumeConfiguration) 