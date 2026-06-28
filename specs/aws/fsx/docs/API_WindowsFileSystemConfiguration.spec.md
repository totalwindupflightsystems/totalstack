---
id: "@specs/aws/fsx/docs/API_WindowsFileSystemConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WindowsFileSystemConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# WindowsFileSystemConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_WindowsFileSystemConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WindowsFileSystemConfiguration
<a name="API_WindowsFileSystemConfiguration"></a>

The configuration for this Microsoft Windows file system.

## Contents
<a name="API_WindowsFileSystemConfiguration_Contents"></a>

 ** ActiveDirectoryId **   <a name="FSx-Type-WindowsFileSystemConfiguration-ActiveDirectoryId"></a>
The ID for an existing AWS Managed Microsoft Active Directory instance that the file system is joined to.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** Aliases **   <a name="FSx-Type-WindowsFileSystemConfiguration-Aliases"></a>
An array of one or more DNS aliases that are currently associated with the Amazon FSx file system. Aliases allow you to use existing DNS names to access the data in your Amazon FSx file system. You can associate up to 50 aliases with a file system at any time. You can associate additional DNS aliases after you create the file system using the AssociateFileSystemAliases operation. You can remove DNS aliases from the file system after it is created using the DisassociateFileSystemAliases operation. You only need to specify the alias name in the request payload. For more information, see [Managing DNS aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html).  
Type: Array of [Alias](API_Alias.md) objects  
Array Members: Maximum number of 50 items.  
Required: No

 ** AuditLogConfiguration **   <a name="FSx-Type-WindowsFileSystemConfiguration-AuditLogConfiguration"></a>
The configuration that Amazon FSx for Windows File Server uses to audit and log user accesses of files, folders, and file shares on the Amazon FSx for Windows File Server file system.  
Type: [WindowsAuditLogConfiguration](API_WindowsAuditLogConfiguration.md) object  
Required: No

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-WindowsFileSystemConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this to 0 disables automatic backups. You can retain automatic backups for a maximum of 90 days.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** CopyTagsToBackups **   <a name="FSx-Type-WindowsFileSystemConfiguration-CopyTagsToBackups"></a>
A boolean flag indicating whether tags on the file system should be copied to backups. This value defaults to false. If it's set to true, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn't specify any tags. If this value is true, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.  
Type: Boolean  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-WindowsFileSystemConfiguration-DailyAutomaticBackupStartTime"></a>
The preferred time to take daily automatic backups, in the UTC time zone.  
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DeploymentType **   <a name="FSx-Type-WindowsFileSystemConfiguration-DeploymentType"></a>
Specifies the file system deployment type, valid values are the following:  
+  `MULTI_AZ_1` - Specifies a high availability file system that is configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability, and supports SSD and HDD storage.
+  `SINGLE_AZ_1` - (Default) Specifies a file system that is configured for single AZ redundancy, only supports SSD storage.
+  `SINGLE_AZ_2` - Latest generation Single AZ file system. Specifies a file system that is configured for single AZ redundancy and supports SSD and HDD storage.
For more information, see [Single-AZ and Multi-AZ File Systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html).  
Type: String  
Valid Values: `MULTI_AZ_1 | SINGLE_AZ_1 | SINGLE_AZ_2`   
Required: No

 ** DiskIopsConfiguration **   <a name="FSx-Type-WindowsFileSystemConfiguration-DiskIopsConfiguration"></a>
The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for Windows file system. By default, Amazon FSx automatically provisions 3 IOPS per GiB of storage capacity. You can provision additional IOPS per GiB of storage, up to the maximum limit associated with your chosen throughput capacity.  
Type: [DiskIopsConfiguration](API_DiskIopsConfiguration.md) object  
Required: No

 ** FsrmConfiguration **   <a name="FSx-Type-WindowsFileSystemConfiguration-FsrmConfiguration"></a>
The File Server Resource Manager (FSRM) configuration that Amazon FSx for Windows File Server uses for the file system. FSRM is disabled by default.  
Type: [WindowsFsrmConfiguration](API_WindowsFsrmConfiguration.md) object  
Required: No

 ** MaintenanceOperationsInProgress **   <a name="FSx-Type-WindowsFileSystemConfiguration-MaintenanceOperationsInProgress"></a>
The list of maintenance operations in progress for this file system.  
Type: Array of strings  
Array Members: Maximum number of 20 items.  
Valid Values: `PATCHING | BACKING_UP`   
Required: No

 ** PreferredFileServerIp **   <a name="FSx-Type-WindowsFileSystemConfiguration-PreferredFileServerIp"></a>
For `MULTI_AZ_1` deployment types, the IPv4 address of the primary, or preferred, file server.  
Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IPv4 address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file system's DNSName instead. For more information on mapping and mounting file shares, see [Accessing data using file shares](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-file-shares.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 45.  
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`   
Required: No

 ** PreferredFileServerIpv6 **   <a name="FSx-Type-WindowsFileSystemConfiguration-PreferredFileServerIpv6"></a>
For MULTI\_AZ\_1 deployment types, the IPv6 address of the primary, or preferred, file server. Use this IP address when mounting the file system on Linux SMB clients or Windows SMB clients that are not joined to a Microsoft Active Directory. Applicable for all Windows file system deployment types. This IPv6 address is temporarily unavailable when the file system is undergoing maintenance. For Linux and Windows SMB clients that are joined to an Active Directory, use the file system's DNSName instead.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 45.  
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`   
Required: No

 ** PreferredSubnetId **   <a name="FSx-Type-WindowsFileSystemConfiguration-PreferredSubnetId"></a>
For `MULTI_AZ_1` deployment types, it specifies the ID of the subnet where the preferred file server is located. Must be one of the two subnet IDs specified in `SubnetIds` property. Amazon FSx serves traffic from this subnet except in the event of a failover to the secondary file server.  
For `SINGLE_AZ_1` and `SINGLE_AZ_2` deployment types, this value is the same as that for `SubnetIDs`. For more information, see [Availability and durability: Single-AZ and Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html#single-multi-az-resources).  
Type: String  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `^(subnet-[0-9a-f]{8,})$`   
Required: No

 ** RemoteAdministrationEndpoint **   <a name="FSx-Type-WindowsFileSystemConfiguration-RemoteAdministrationEndpoint"></a>
For `MULTI_AZ_1` deployment types, use this endpoint when performing administrative tasks on the file system using Amazon FSx Remote PowerShell.  
For `SINGLE_AZ_1` and `SINGLE_AZ_2` deployment types, this is the DNS name of the file system.  
This endpoint is temporarily unavailable when the file system is undergoing maintenance.  
Type: String  
Length Constraints: Minimum length of 16. Maximum length of 275.  
Pattern: `^((fs|fc)i?-[0-9a-f]{8,}\..{4,253})$`   
Required: No

 ** SelfManagedActiveDirectoryConfiguration **   <a name="FSx-Type-WindowsFileSystemConfiguration-SelfManagedActiveDirectoryConfiguration"></a>
The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.  
Type: [SelfManagedActiveDirectoryAttributes](API_SelfManagedActiveDirectoryAttributes.md) object  
Required: No

 ** ThroughputCapacity **   <a name="FSx-Type-WindowsFileSystemConfiguration-ThroughputCapacity"></a>
The throughput of the Amazon FSx file system, measured in megabytes per second.  
Type: Integer  
Valid Range: Minimum value of 8. Maximum value of 100000.  
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-WindowsFileSystemConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone. d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_WindowsFileSystemConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/WindowsFileSystemConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/WindowsFileSystemConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/WindowsFileSystemConfiguration) 