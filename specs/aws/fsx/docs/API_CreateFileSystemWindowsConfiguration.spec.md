---
id: "@specs/aws/fsx/docs/API_CreateFileSystemWindowsConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFileSystemWindowsConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateFileSystemWindowsConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateFileSystemWindowsConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFileSystemWindowsConfiguration
<a name="API_CreateFileSystemWindowsConfiguration"></a>

The configuration object for the Microsoft Windows file system used in `CreateFileSystem` and `CreateFileSystemFromBackup` operations.

## Contents
<a name="API_CreateFileSystemWindowsConfiguration_Contents"></a>

 ** ThroughputCapacity **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-ThroughputCapacity"></a>
Sets the throughput capacity of an Amazon FSx file system, measured in megabytes per second (MB/s), in 2 to the *n*th increments, between 2^3 (8) and 2^11 (2048).  
Type: Integer  
Valid Range: Minimum value of 8. Maximum value of 100000.  
Required: Yes

 ** ActiveDirectoryId **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-ActiveDirectoryId"></a>
The ID for an existing AWS Managed Microsoft Active Directory (AD) instance that the file system should join when it's created.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** Aliases **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-Aliases"></a>
An array of one or more DNS alias names that you want to associate with the Amazon FSx file system. Aliases allow you to use existing DNS names to access the data in your Amazon FSx file system. You can associate up to 50 aliases with a file system at any time. You can associate additional DNS aliases after you create the file system using the AssociateFileSystemAliases operation. You can remove DNS aliases from the file system after it is created using the DisassociateFileSystemAliases operation. You only need to specify the alias name in the request payload. For more information, see [Managing DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) and [Accessing data using DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/dns-aliases.html).  
An alias name has to meet the following requirements:  
+ Formatted as a fully-qualified domain name (FQDN), `hostname.domain`, for example, `accounting.example.com`.
+ Can contain alphanumeric characters, the underscore (\_), and the hyphen (-).
+ Cannot start or end with a hyphen.
+ Can start with a numeric.
For DNS alias names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 4. Maximum length of 253.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{4,253}$`   
Required: No

 ** AuditLogConfiguration **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-AuditLogConfiguration"></a>
The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.  
Type: [WindowsAuditLogCreateConfiguration](API_WindowsAuditLogCreateConfiguration.md) object  
Required: No

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** CopyTagsToBackups **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-CopyTagsToBackups"></a>
A boolean flag indicating whether tags for the file system should be copied to backups. This value defaults to false. If it's set to true, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.  
Type: Boolean  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-DailyAutomaticBackupStartTime"></a>
The preferred time to take daily automatic backups, formatted HH:MM in the UTC time zone.  
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DeploymentType **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-DeploymentType"></a>
Specifies the file system deployment type, valid values are the following:  
+  `MULTI_AZ_1` - Deploys a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. You can only deploy a Multi-AZ file system in AWS Regions that have a minimum of three Availability Zones. Also supports HDD storage type
+  `SINGLE_AZ_1` - (Default) Choose to deploy a file system that is configured for single AZ redundancy.
+  `SINGLE_AZ_2` - The latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports HDD storage type.
For more information, see [ Availability and Durability: Single-AZ and Multi-AZ File Systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html).  
Type: String  
Valid Values: `MULTI_AZ_1 | SINGLE_AZ_1 | SINGLE_AZ_2`   
Required: No

 ** DiskIopsConfiguration **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-DiskIopsConfiguration"></a>
The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for Windows file system. By default, Amazon FSx automatically provisions 3 IOPS per GiB of storage capacity. You can provision additional IOPS per GiB of storage, up to the maximum limit associated with your chosen throughput capacity.  
Type: [DiskIopsConfiguration](API_DiskIopsConfiguration.md) object  
Required: No

 ** FsrmConfiguration **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-FsrmConfiguration"></a>
The File Server Resource Manager (FSRM) configuration that Amazon FSx for Windows File Server uses for the file system. FSRM is disabled by default.  
Type: [WindowsFsrmConfiguration](API_WindowsFsrmConfiguration.md) object  
Required: No

 ** PreferredSubnetId **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-PreferredSubnetId"></a>
Required when `DeploymentType` is set to `MULTI_AZ_1`. This specifies the subnet in which you want the preferred file server to be located. For in-AWS applications, we recommend that you launch your clients in the same Availability Zone (AZ) as your preferred file server to reduce cross-AZ data transfer costs and minimize latency.   
Type: String  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `^(subnet-[0-9a-f]{8,})$`   
Required: No

 ** SelfManagedActiveDirectoryConfiguration **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-SelfManagedActiveDirectoryConfiguration"></a>
The configuration that Amazon FSx uses to join a FSx for Windows File Server file system or an FSx for ONTAP storage virtual machine (SVM) to a self-managed (including on-premises) Microsoft Active Directory (AD) directory. For more information, see [ Using Amazon FSx for Windows with your self-managed Microsoft Active Directory](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html) or [Managing FSx for ONTAP SVMs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html).  
Type: [SelfManagedActiveDirectoryConfiguration](API_SelfManagedActiveDirectoryConfiguration.md) object  
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-CreateFileSystemWindowsConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_CreateFileSystemWindowsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateFileSystemWindowsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateFileSystemWindowsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateFileSystemWindowsConfiguration) 