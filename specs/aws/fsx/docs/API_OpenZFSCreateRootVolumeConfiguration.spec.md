---
id: "@specs/aws/fsx/docs/API_OpenZFSCreateRootVolumeConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OpenZFSCreateRootVolumeConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# OpenZFSCreateRootVolumeConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_OpenZFSCreateRootVolumeConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OpenZFSCreateRootVolumeConfiguration
<a name="API_OpenZFSCreateRootVolumeConfiguration"></a>

The configuration of an Amazon FSx for OpenZFS root volume.

## Contents
<a name="API_OpenZFSCreateRootVolumeConfiguration_Contents"></a>

 ** CopyTagsToSnapshots **   <a name="FSx-Type-OpenZFSCreateRootVolumeConfiguration-CopyTagsToSnapshots"></a>
A Boolean value indicating whether tags for the volume should be copied to snapshots of the volume. This value defaults to `false`. If it's set to `true`, all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.   
Type: Boolean  
Required: No

 ** DataCompressionType **   <a name="FSx-Type-OpenZFSCreateRootVolumeConfiguration-DataCompressionType"></a>
Specifies the method used to compress the data on the volume. The compression type is `NONE` by default.  
+  `NONE` - Doesn't compress the data on the volume. `NONE` is the default.
+  `ZSTD` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.
+  `LZ4` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.
Type: String  
Valid Values: `NONE | ZSTD | LZ4`   
Required: No

 ** NfsExports **   <a name="FSx-Type-OpenZFSCreateRootVolumeConfiguration-NfsExports"></a>
The configuration object for mounting a file system.  
Type: Array of [OpenZFSNfsExport](API_OpenZFSNfsExport.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

 ** ReadOnly **   <a name="FSx-Type-OpenZFSCreateRootVolumeConfiguration-ReadOnly"></a>
A Boolean value indicating whether the volume is read-only. Setting this value to `true` can be useful after you have completed changes to a volume and no longer want changes to occur.   
Type: Boolean  
Required: No

 ** RecordSizeKiB **   <a name="FSx-Type-OpenZFSCreateRootVolumeConfiguration-RecordSizeKiB"></a>
Specifies the record size of an OpenZFS root volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. Database workflows can benefit from a smaller record size, while streaming workflows can benefit from a larger record size. For additional guidance on setting a custom record size, see [ Tips for maximizing performance](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#performance-tips-zfs) in the *Amazon FSx for OpenZFS User Guide*.  
Type: Integer  
Valid Range: Minimum value of 4. Maximum value of 4096.  
Required: No

 ** UserAndGroupQuotas **   <a name="FSx-Type-OpenZFSCreateRootVolumeConfiguration-UserAndGroupQuotas"></a>
An object specifying how much storage users or groups can use on the volume.  
Type: Array of [OpenZFSUserOrGroupQuota](API_OpenZFSUserOrGroupQuota.md) objects  
Array Members: Maximum number of 500 items.  
Required: No

## See Also
<a name="API_OpenZFSCreateRootVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OpenZFSCreateRootVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OpenZFSCreateRootVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OpenZFSCreateRootVolumeConfiguration) 