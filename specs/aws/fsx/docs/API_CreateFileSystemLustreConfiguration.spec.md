---
id: "@specs/aws/fsx/docs/API_CreateFileSystemLustreConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFileSystemLustreConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateFileSystemLustreConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateFileSystemLustreConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFileSystemLustreConfiguration
<a name="API_CreateFileSystemLustreConfiguration"></a>

The Lustre configuration for the file system being created.

**Note**  
The following parameters are not supported for file systems with a data repository association created with [CreateDataRepositoryAssociation](API_CreateDataRepositoryAssociation.md).  
 `AutoImportPolicy` 
 `ExportPath` 
 `ImportedFileChunkSize` 
 `ImportPath` 

## Contents
<a name="API_CreateFileSystemLustreConfiguration_Contents"></a>

 ** AutoImportPolicy **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-AutoImportPolicy"></a>
 (Optional) When you create your file system, your existing S3 objects appear as file and directory listings. Use this parameter to choose how Amazon FSx keeps your file and directory listings up to date as you add or modify objects in your linked S3 bucket. `AutoImportPolicy` can have the following values:  
+  `NONE` - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update file and directory listings for any new or changed objects after choosing this option.
+  `NEW` - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system. 
+  `NEW_CHANGED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.
+  `NEW_CHANGED_DELETED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.
For more information, see [ Automatically import updates from your S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/older-deployment-types.html#legacy-auto-import-from-s3).  
This parameter is not supported for file systems with a data repository association.
Type: String  
Valid Values: `NONE | NEW | NEW_CHANGED | NEW_CHANGED_DELETED`   
Required: No

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `0`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** CopyTagsToBackups **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-CopyTagsToBackups"></a>
(Optional) Not available for use with file systems that are linked to a data repository. A boolean flag indicating whether tags for the file system should be copied to backups. The default value is false. If `CopyTagsToBackups` is set to true, all file system tags are copied to all automatic and user-initiated backups when the user doesn't specify any backup-specific tags. If `CopyTagsToBackups` is set to true and you specify one or more backup tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.  
(Default = `false`)  
For more information, see [ Working with backups](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-backups-fsx.html) in the *Amazon FSx for Lustre User Guide*.  
Type: Boolean  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-DailyAutomaticBackupStartTime"></a>
A recurring daily time, in the format `HH:MM`. `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.   
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DataCompressionType **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-DataCompressionType"></a>
Sets the data compression configuration for the file system. `DataCompressionType` can have the following values:  
+  `NONE` - (Default) Data compression is turned off when the file system is created.
+  `LZ4` - Data compression is turned on with the LZ4 algorithm.
For more information, see [Lustre data compression](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html) in the *Amazon FSx for Lustre User Guide*.  
Type: String  
Valid Values: `NONE | LZ4`   
Required: No

 ** DataReadCacheConfiguration **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-DataReadCacheConfiguration"></a>
Specifies the optional provisioned SSD read cache on FSx for Lustre file systems that use the Intelligent-Tiering storage class. Required when `StorageType` is set to `INTELLIGENT_TIERING`.  
Type: [LustreReadCacheConfiguration](API_LustreReadCacheConfiguration.md) object  
Required: No

 ** DeploymentType **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-DeploymentType"></a>
(Optional) Choose `SCRATCH_1` and `SCRATCH_2` deployment types when you need temporary storage and shorter-term processing of data. The `SCRATCH_2` deployment type provides in-transit encryption of data and higher burst throughput capacity than `SCRATCH_1`.  
Choose `PERSISTENT_1` for longer-term storage and for throughput-focused workloads that aren’t latency-sensitive. `PERSISTENT_1` supports encryption of data in transit, and is available in all AWS Regions in which FSx for Lustre is available.  
Choose `PERSISTENT_2` for longer-term storage and for latency-sensitive workloads that require the highest levels of IOPS/throughput. `PERSISTENT_2` supports the SSD and Intelligent-Tiering storage classes. You can optionally specify a metadata configuration mode for `PERSISTENT_2` which supports increasing metadata performance. `PERSISTENT_2` is available in a limited number of AWS Regions. For more information, and an up-to-date list of AWS Regions in which `PERSISTENT_2` is available, see [Deployment and storage class options for FSx for Lustre file systems](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html) in the *Amazon FSx for Lustre User Guide*.  
If you choose `PERSISTENT_2`, and you set `FileSystemTypeVersion` to `2.10`, the `CreateFileSystem` operation fails.
Encryption of data in transit is automatically turned on when you access `SCRATCH_2`, `PERSISTENT_1`, and `PERSISTENT_2` file systems from Amazon EC2 instances that support automatic encryption in the AWS Regions where they are available. For more information about encryption in transit for FSx for Lustre file systems, see [Encrypting data in transit](https://docs.aws.amazon.com/fsx/latest/LustreGuide/encryption-in-transit-fsxl.html) in the *Amazon FSx for Lustre User Guide*.  
(Default = `SCRATCH_1`)  
Type: String  
Valid Values: `SCRATCH_1 | SCRATCH_2 | PERSISTENT_1 | PERSISTENT_2`   
Required: No

 ** DriveCacheType **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-DriveCacheType"></a>
The type of drive cache used by `PERSISTENT_1` file systems that are provisioned with HDD storage devices. This parameter is required when storage type is HDD. Set this property to `READ` to improve the performance for frequently accessed files by caching up to 20% of the total storage capacity of the file system.  
This parameter is required when `StorageType` is set to `HDD`.  
Type: String  
Valid Values: `NONE | READ`   
Required: No

 ** EfaEnabled **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-EfaEnabled"></a>
(Optional) Specifies whether Elastic Fabric Adapter (EFA) and GPUDirect Storage (GDS) support is enabled for the Amazon FSx for Lustre file system.  
(Default = `false`)  
Type: Boolean  
Required: No

 ** ExportPath **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-ExportPath"></a>
(Optional) Specifies the path in the Amazon S3 bucket where the root of your Amazon FSx file system is exported. The path must use the same Amazon S3 bucket as specified in ImportPath. You can provide an optional prefix to which new and changed data is to be exported from your Amazon FSx for Lustre file system. If an `ExportPath` value is not provided, Amazon FSx sets a default export path, `s3://import-bucket/FSxLustre[creation-timestamp]`. The timestamp is in UTC format, for example `s3://import-bucket/FSxLustre20181105T222312Z`.  
The Amazon S3 export bucket must be the same as the import bucket specified by `ImportPath`. If you specify only a bucket name, such as `s3://import-bucket`, you get a 1:1 mapping of file system objects to S3 bucket objects. This mapping means that the input data in S3 is overwritten on export. If you provide a custom prefix in the export path, such as `s3://import-bucket/[custom-optional-prefix]`, Amazon FSx exports the contents of your file system to that export prefix in the Amazon S3 bucket.  
This parameter is not supported for file systems with a data repository association.
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 4357.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`   
Required: No

 ** ImportedFileChunkSize **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-ImportedFileChunkSize"></a>
(Optional) For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.  
The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.  
This parameter is not supported for file systems with a data repository association.
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 512000.  
Required: No

 ** ImportPath **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-ImportPath"></a>
(Optional) The path to the Amazon S3 bucket (including the optional prefix) that you're using as the data repository for your Amazon FSx for Lustre file system. The root of your FSx for Lustre file system will be mapped to the root of the Amazon S3 bucket you select. An example is `s3://import-bucket/optional-prefix`. If you specify a prefix after the Amazon S3 bucket name, only object keys with that prefix are loaded into the file system.  
This parameter is not supported for file systems with a data repository association.
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 4357.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{3,4357}$`   
Required: No

 ** LogConfiguration **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-LogConfiguration"></a>
The Lustre logging configuration used when creating an Amazon FSx for Lustre file system. When logging is enabled, Lustre logs error and warning events for data repositories associated with your file system to Amazon CloudWatch Logs.  
Type: [LustreLogCreateConfiguration](API_LustreLogCreateConfiguration.md) object  
Required: No

 ** MetadataConfiguration **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-MetadataConfiguration"></a>
The Lustre metadata performance configuration for the creation of an FSx for Lustre file system using a `PERSISTENT_2` deployment type.  
Type: [CreateFileSystemLustreMetadataConfiguration](API_CreateFileSystemLustreMetadataConfiguration.md) object  
Required: No

 ** PerUnitStorageThroughput **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-PerUnitStorageThroughput"></a>
Required with `PERSISTENT_1` and `PERSISTENT_2` deployment types using an SSD or HDD storage class, provisions the amount of read and write throughput for each 1 tebibyte (TiB) of file system storage capacity, in MB/s/TiB. File system throughput capacity is calculated by multiplying ﬁle system storage capacity (TiB) by the `PerUnitStorageThroughput` (MB/s/TiB). For a 2.4-TiB ﬁle system, provisioning 50 MB/s/TiB of `PerUnitStorageThroughput` yields 120 MB/s of ﬁle system throughput. You pay for the amount of throughput that you provision.   
Valid values:  
+ For `PERSISTENT_1` SSD storage: 50, 100, 200 MB/s/TiB.
+ For `PERSISTENT_1` HDD storage: 12, 40 MB/s/TiB.
+ For `PERSISTENT_2` SSD storage: 125, 250, 500, 1000 MB/s/TiB.
Type: Integer  
Valid Range: Minimum value of 12. Maximum value of 1000.  
Required: No

 ** RootSquashConfiguration **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-RootSquashConfiguration"></a>
The Lustre root squash configuration used when creating an Amazon FSx for Lustre file system. When enabled, root squash restricts root-level access from clients that try to access your file system as a root user.  
Type: [LustreRootSquashConfiguration](API_LustreRootSquashConfiguration.md) object  
Required: No

 ** ThroughputCapacity **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-ThroughputCapacity"></a>
Specifies the throughput of an FSx for Lustre file system using the Intelligent-Tiering storage class, measured in megabytes per second (MBps). Valid values are 4000 MBps or multiples of 4000 MBps. You pay for the amount of throughput that you provision.  
Type: Integer  
Valid Range: Minimum value of 4000. Maximum value of 2000000.  
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-CreateFileSystemLustreConfiguration-WeeklyMaintenanceStartTime"></a>
(Optional) The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_CreateFileSystemLustreConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateFileSystemLustreConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateFileSystemLustreConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateFileSystemLustreConfiguration) 