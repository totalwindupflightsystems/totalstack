---
id: "@specs/aws/fsx/docs/API_UpdateFileSystemWindowsConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFileSystemWindowsConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateFileSystemWindowsConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateFileSystemWindowsConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFileSystemWindowsConfiguration
<a name="API_UpdateFileSystemWindowsConfiguration"></a>

Updates the configuration for an existing Amazon FSx for Windows File Server file system. Amazon FSx only overwrites existing properties with non-null values provided in the request.

## Contents
<a name="API_UpdateFileSystemWindowsConfiguration_Contents"></a>

 ** AuditLogConfiguration **   <a name="FSx-Type-UpdateFileSystemWindowsConfiguration-AuditLogConfiguration"></a>
The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system..  
Type: [WindowsAuditLogCreateConfiguration](API_WindowsAuditLogCreateConfiguration.md) object  
Required: No

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-UpdateFileSystemWindowsConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30`. For more information, see [Working with Automatic Daily Backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html#automatic-backups).  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-UpdateFileSystemWindowsConfiguration-DailyAutomaticBackupStartTime"></a>
The preferred time to start the daily automatic backup, in the UTC time zone, for example, `02:00`   
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DiskIopsConfiguration **   <a name="FSx-Type-UpdateFileSystemWindowsConfiguration-DiskIopsConfiguration"></a>
The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for Windows file system. By default, Amazon FSx automatically provisions 3 IOPS per GiB of storage capacity. You can provision additional IOPS per GiB of storage, up to the maximum limit associated with your chosen throughput capacity.  
Type: [DiskIopsConfiguration](API_DiskIopsConfiguration.md) object  
Required: No

 ** FsrmConfiguration **   <a name="FSx-Type-UpdateFileSystemWindowsConfiguration-FsrmConfiguration"></a>
The File Server Resource Manager (FSRM) configuration that Amazon FSx for Windows File Server uses for the file system. FSRM is disabled by default.  
Type: [WindowsFsrmConfiguration](API_WindowsFsrmConfiguration.md) object  
Required: No

 ** SelfManagedActiveDirectoryConfiguration **   <a name="FSx-Type-UpdateFileSystemWindowsConfiguration-SelfManagedActiveDirectoryConfiguration"></a>
The configuration Amazon FSx uses to join the Windows File Server instance to the self-managed Microsoft AD directory. You cannot make a self-managed Microsoft AD update request if there is an existing self-managed Microsoft AD update request in progress.  
Type: [SelfManagedActiveDirectoryConfigurationUpdates](API_SelfManagedActiveDirectoryConfigurationUpdates.md) object  
Required: No

 ** ThroughputCapacity **   <a name="FSx-Type-UpdateFileSystemWindowsConfiguration-ThroughputCapacity"></a>
Sets the target value for a file system's throughput capacity, in MB/s, that you are updating the file system to. Valid values are 8, 16, 32, 64, 128, 256, 512, 1024, 2048. You cannot make a throughput capacity update request if there is an existing throughput capacity update request in progress. For more information, see [Managing Throughput Capacity](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-throughput-capacity.html).  
Type: Integer  
Valid Range: Minimum value of 8. Maximum value of 100000.  
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-UpdateFileSystemWindowsConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. Where d is the weekday number, from 1 through 7, with 1 = Monday and 7 = Sunday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_UpdateFileSystemWindowsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateFileSystemWindowsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateFileSystemWindowsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateFileSystemWindowsConfiguration) 