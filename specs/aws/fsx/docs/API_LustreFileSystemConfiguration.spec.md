---
id: "@specs/aws/fsx/docs/API_LustreFileSystemConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LustreFileSystemConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# LustreFileSystemConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_LustreFileSystemConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LustreFileSystemConfiguration
<a name="API_LustreFileSystemConfiguration"></a>

The configuration for the Amazon FSx for Lustre file system.

## Contents
<a name="API_LustreFileSystemConfiguration_Contents"></a>

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-LustreFileSystemConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** CopyTagsToBackups **   <a name="FSx-Type-LustreFileSystemConfiguration-CopyTagsToBackups"></a>
A boolean flag indicating whether tags on the file system are copied to backups. If it's set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn't specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value. (Default = false)  
Type: Boolean  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-LustreFileSystemConfiguration-DailyAutomaticBackupStartTime"></a>
A recurring daily time, in the format `HH:MM`. `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.   
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DataCompressionType **   <a name="FSx-Type-LustreFileSystemConfiguration-DataCompressionType"></a>
The data compression configuration for the file system. `DataCompressionType` can have the following values:  
+  `NONE` - Data compression is turned off for the file system.
+  `LZ4` - Data compression is turned on with the LZ4 algorithm.
For more information, see [Lustre data compression](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html).  
Type: String  
Valid Values: `NONE | LZ4`   
Required: No

 ** DataReadCacheConfiguration **   <a name="FSx-Type-LustreFileSystemConfiguration-DataReadCacheConfiguration"></a>
Required when `StorageType` is set to `INTELLIGENT_TIERING`. Specifies the optional provisioned SSD read cache.  
Type: [LustreReadCacheConfiguration](API_LustreReadCacheConfiguration.md) object  
Required: No

 ** DataRepositoryConfiguration **   <a name="FSx-Type-LustreFileSystemConfiguration-DataRepositoryConfiguration"></a>
The data repository configuration object for Lustre file systems returned in the response of the `CreateFileSystem` operation.  
This data type is not supported on file systems with a data repository association. For file systems with a data repository association, see [DataRepositoryAssociation](API_DataRepositoryAssociation.md).  
Type: [DataRepositoryConfiguration](API_DataRepositoryConfiguration.md) object  
Required: No

 ** DeploymentType **   <a name="FSx-Type-LustreFileSystemConfiguration-DeploymentType"></a>
The deployment type of the FSx for Lustre file system. *Scratch deployment type* is designed for temporary storage and shorter-term processing of data.  
 `SCRATCH_1` and `SCRATCH_2` deployment types are best suited for when you need temporary storage and shorter-term processing of data. The `SCRATCH_2` deployment type provides in-transit encryption of data and higher burst throughput capacity than `SCRATCH_1`.  
The `PERSISTENT_1` and `PERSISTENT_2` deployment type is used for longer-term storage and workloads and encryption of data in transit. `PERSISTENT_2` offers higher `PerUnitStorageThroughput` (up to 1000 MB/s/TiB) along with a lower minimum storage capacity requirement (600 GiB). To learn more about FSx for Lustre deployment types, see [Deployment and storage class options for FSx for Lustre file systems](https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html).  
The default is `SCRATCH_1`.  
Type: String  
Valid Values: `SCRATCH_1 | SCRATCH_2 | PERSISTENT_1 | PERSISTENT_2`   
Required: No

 ** DriveCacheType **   <a name="FSx-Type-LustreFileSystemConfiguration-DriveCacheType"></a>
The type of drive cache used by `PERSISTENT_1` file systems that are provisioned with HDD storage devices. This parameter is required when `StorageType` is HDD. When set to `READ` the file system has an SSD storage cache that is sized to 20% of the file system's storage capacity. This improves the performance for frequently accessed files by caching up to 20% of the total storage capacity.  
This parameter is required when `StorageType` is set to HDD.  
Type: String  
Valid Values: `NONE | READ`   
Required: No

 ** EfaEnabled **   <a name="FSx-Type-LustreFileSystemConfiguration-EfaEnabled"></a>
Specifies whether Elastic Fabric Adapter (EFA) and GPUDirect Storage (GDS) support is enabled for the Amazon FSx for Lustre file system.  
Type: Boolean  
Required: No

 ** LogConfiguration **   <a name="FSx-Type-LustreFileSystemConfiguration-LogConfiguration"></a>
The Lustre logging configuration. Lustre logging writes the enabled log events for your file system to Amazon CloudWatch Logs.  
Type: [LustreLogConfiguration](API_LustreLogConfiguration.md) object  
Required: No

 ** MetadataConfiguration **   <a name="FSx-Type-LustreFileSystemConfiguration-MetadataConfiguration"></a>
The Lustre metadata performance configuration for an Amazon FSx for Lustre file system using a `PERSISTENT_2` deployment type.  
Type: [FileSystemLustreMetadataConfiguration](API_FileSystemLustreMetadataConfiguration.md) object  
Required: No

 ** MountName **   <a name="FSx-Type-LustreFileSystemConfiguration-MountName"></a>
You use the `MountName` value when mounting the file system.  
For the `SCRATCH_1` deployment type, this value is always "`fsx`". For `SCRATCH_2`, `PERSISTENT_1`, and `PERSISTENT_2` deployment types, this value is a string that is unique within an AWS Region.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 8.  
Pattern: `^([A-Za-z0-9_-]{1,8})$`   
Required: No

 ** PerUnitStorageThroughput **   <a name="FSx-Type-LustreFileSystemConfiguration-PerUnitStorageThroughput"></a>
Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. File system throughput capacity is equal to Storage capacity (TiB) \* PerUnitStorageThroughput (MB/s/TiB). This option is only valid for `PERSISTENT_1` and `PERSISTENT_2` deployment types.   
Valid values:  
+ For `PERSISTENT_1` SSD storage: 50, 100, 200.
+ For `PERSISTENT_1` HDD storage: 12, 40.
+ For `PERSISTENT_2` SSD storage: 125, 250, 500, 1000.
Type: Integer  
Valid Range: Minimum value of 12. Maximum value of 1000.  
Required: No

 ** RootSquashConfiguration **   <a name="FSx-Type-LustreFileSystemConfiguration-RootSquashConfiguration"></a>
The Lustre root squash configuration for an Amazon FSx for Lustre file system. When enabled, root squash restricts root-level access from clients that try to access your file system as a root user.  
Type: [LustreRootSquashConfiguration](API_LustreRootSquashConfiguration.md) object  
Required: No

 ** ThroughputCapacity **   <a name="FSx-Type-LustreFileSystemConfiguration-ThroughputCapacity"></a>
The throughput of an Amazon FSx for Lustre file system using the Intelligent-Tiering storage class, measured in megabytes per second (MBps).  
Type: Integer  
Valid Range: Minimum value of 4000. Maximum value of 2000000.  
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-LustreFileSystemConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. Here, `d` is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_LustreFileSystemConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/LustreFileSystemConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/LustreFileSystemConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/LustreFileSystemConfiguration) 