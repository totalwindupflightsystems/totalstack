---
id: "@specs/aws/fsx/docs/API_UpdateFileSystemLustreConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFileSystemLustreConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateFileSystemLustreConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateFileSystemLustreConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFileSystemLustreConfiguration
<a name="API_UpdateFileSystemLustreConfiguration"></a>

The configuration object for Amazon FSx for Lustre file systems used in the `UpdateFileSystem` operation.

## Contents
<a name="API_UpdateFileSystemLustreConfiguration_Contents"></a>

 ** AutoImportPolicy **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-AutoImportPolicy"></a>
 (Optional) When you create your file system, your existing S3 objects appear as file and directory listings. Use this property to choose how Amazon FSx keeps your file and directory listing up to date as you add or modify objects in your linked S3 bucket. `AutoImportPolicy` can have the following values:  
+  `NONE` - (Default) AutoImport is off. Amazon FSx only updates file and directory listings from the linked S3 bucket when the file system is created. FSx does not update the file and directory listing for any new or changed objects after choosing this option.
+  `NEW` - AutoImport is on. Amazon FSx automatically imports directory listings of any new objects added to the linked S3 bucket that do not currently exist in the FSx file system. 
+  `NEW_CHANGED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket and any existing objects that are changed in the S3 bucket after you choose this option.
+  `NEW_CHANGED_DELETED` - AutoImport is on. Amazon FSx automatically imports file and directory listings of any new objects added to the S3 bucket, any existing objects that are changed in the S3 bucket, and any objects that were deleted in the S3 bucket.
This parameter is not supported for file systems with a data repository association.  
Type: String  
Valid Values: `NONE | NEW | NEW_CHANGED | NEW_CHANGED_DELETED`   
Required: No

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `0`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-DailyAutomaticBackupStartTime"></a>
A recurring daily time, in the format `HH:MM`. `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.   
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DataCompressionType **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-DataCompressionType"></a>
Sets the data compression configuration for the file system. `DataCompressionType` can have the following values:  
+  `NONE` - Data compression is turned off for the file system.
+  `LZ4` - Data compression is turned on with the LZ4 algorithm.
If you don't use `DataCompressionType`, the file system retains its current data compression configuration.  
For more information, see [Lustre data compression](https://docs.aws.amazon.com/fsx/latest/LustreGuide/data-compression.html).  
Type: String  
Valid Values: `NONE | LZ4`   
Required: No

 ** DataReadCacheConfiguration **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-DataReadCacheConfiguration"></a>
Specifies the optional provisioned SSD read cache on Amazon FSx for Lustre file systems that use the Intelligent-Tiering storage class.  
Type: [LustreReadCacheConfiguration](API_LustreReadCacheConfiguration.md) object  
Required: No

 ** LogConfiguration **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-LogConfiguration"></a>
The Lustre logging configuration used when updating an Amazon FSx for Lustre file system. When logging is enabled, Lustre logs error and warning events for data repositories associated with your file system to Amazon CloudWatch Logs.  
Type: [LustreLogCreateConfiguration](API_LustreLogCreateConfiguration.md) object  
Required: No

 ** MetadataConfiguration **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-MetadataConfiguration"></a>
The Lustre metadata performance configuration for an Amazon FSx for Lustre file system using a `PERSISTENT_2` deployment type. When this configuration is enabled, the file system supports increasing metadata performance.  
Type: [UpdateFileSystemLustreMetadataConfiguration](API_UpdateFileSystemLustreMetadataConfiguration.md) object  
Required: No

 ** PerUnitStorageThroughput **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-PerUnitStorageThroughput"></a>
The throughput of an Amazon FSx for Lustre Persistent SSD-based file system, measured in megabytes per second per tebibyte (MB/s/TiB). You can increase or decrease your file system's throughput. Valid values depend on the deployment type of the file system, as follows:  
+ For `PERSISTENT_1` SSD-based deployment types, valid values are 50, 100, and 200 MB/s/TiB.
+ For `PERSISTENT_2` SSD-based deployment types, valid values are 125, 250, 500, and 1000 MB/s/TiB.
For more information, see [ Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/LustreGuide/managing-throughput-capacity.html).  
Type: Integer  
Valid Range: Minimum value of 12. Maximum value of 1000.  
Required: No

 ** RootSquashConfiguration **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-RootSquashConfiguration"></a>
The Lustre root squash configuration used when updating an Amazon FSx for Lustre file system. When enabled, root squash restricts root-level access from clients that try to access your file system as a root user.  
Type: [LustreRootSquashConfiguration](API_LustreRootSquashConfiguration.md) object  
Required: No

 ** ThroughputCapacity **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-ThroughputCapacity"></a>
The throughput of an Amazon FSx for Lustre file system using an Intelligent-Tiering storage class, measured in megabytes per second (MBps). You can only increase your file system's throughput. Valid values are 4000 MBps or multiples of 4000 MBps.  
Type: Integer  
Valid Range: Minimum value of 4000. Maximum value of 2000000.  
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-UpdateFileSystemLustreConfiguration-WeeklyMaintenanceStartTime"></a>
(Optional) The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_UpdateFileSystemLustreConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateFileSystemLustreConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateFileSystemLustreConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateFileSystemLustreConfiguration) 