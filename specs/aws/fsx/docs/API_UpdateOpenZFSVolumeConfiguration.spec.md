---
id: "@specs/aws/fsx/docs/API_UpdateOpenZFSVolumeConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateOpenZFSVolumeConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateOpenZFSVolumeConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateOpenZFSVolumeConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateOpenZFSVolumeConfiguration
<a name="API_UpdateOpenZFSVolumeConfiguration"></a>

Used to specify changes to the OpenZFS configuration for the volume that you are updating.

## Contents
<a name="API_UpdateOpenZFSVolumeConfiguration_Contents"></a>

 ** DataCompressionType **   <a name="FSx-Type-UpdateOpenZFSVolumeConfiguration-DataCompressionType"></a>
Specifies the method used to compress the data on the volume. The compression type is `NONE` by default.  
+  `NONE` - Doesn't compress the data on the volume. `NONE` is the default.
+  `ZSTD` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.
+  `LZ4` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.
Type: String  
Valid Values: `NONE | ZSTD | LZ4`   
Required: No

 ** NfsExports **   <a name="FSx-Type-UpdateOpenZFSVolumeConfiguration-NfsExports"></a>
The configuration object for mounting a Network File System (NFS) file system.  
Type: Array of [OpenZFSNfsExport](API_OpenZFSNfsExport.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

 ** ReadOnly **   <a name="FSx-Type-UpdateOpenZFSVolumeConfiguration-ReadOnly"></a>
A Boolean value indicating whether the volume is read-only.  
Type: Boolean  
Required: No

 ** RecordSizeKiB **   <a name="FSx-Type-UpdateOpenZFSVolumeConfiguration-RecordSizeKiB"></a>
Specifies the record size of an OpenZFS volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. Database workflows can benefit from a smaller record size, while streaming workflows can benefit from a larger record size. For additional guidance on when to set a custom record size, see [ Tips for maximizing performance](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#performance-tips-zfs) in the *Amazon FSx for OpenZFS User Guide*.  
Type: Integer  
Valid Range: Minimum value of 4. Maximum value of 4096.  
Required: No

 ** StorageCapacityQuotaGiB **   <a name="FSx-Type-UpdateOpenZFSVolumeConfiguration-StorageCapacityQuotaGiB"></a>
The maximum amount of storage in gibibytes (GiB) that the volume can use from its parent. You can specify a quota larger than the storage on the parent volume. You can specify a value of `-1` to unset a volume's storage capacity quota.  
Type: Integer  
Valid Range: Minimum value of -1. Maximum value of 2147483647.  
Required: No

 ** StorageCapacityReservationGiB **   <a name="FSx-Type-UpdateOpenZFSVolumeConfiguration-StorageCapacityReservationGiB"></a>
The amount of storage in gibibytes (GiB) to reserve from the parent volume. You can't reserve more storage than the parent volume has reserved. You can specify a value of `-1` to unset a volume's storage capacity reservation.  
Type: Integer  
Valid Range: Minimum value of -1. Maximum value of 2147483647.  
Required: No

 ** UserAndGroupQuotas **   <a name="FSx-Type-UpdateOpenZFSVolumeConfiguration-UserAndGroupQuotas"></a>
An object specifying how much storage users or groups can use on the volume.  
Type: Array of [OpenZFSUserOrGroupQuota](API_OpenZFSUserOrGroupQuota.md) objects  
Array Members: Maximum number of 500 items.  
Required: No

## See Also
<a name="API_UpdateOpenZFSVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateOpenZFSVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateOpenZFSVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateOpenZFSVolumeConfiguration) 