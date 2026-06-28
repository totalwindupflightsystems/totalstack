---
id: "@specs/aws/fsx/docs/API_OpenZFSFileSystemConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OpenZFSFileSystemConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# OpenZFSFileSystemConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_OpenZFSFileSystemConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OpenZFSFileSystemConfiguration
<a name="API_OpenZFSFileSystemConfiguration"></a>

The configuration for the Amazon FSx for OpenZFS file system. 

## Contents
<a name="API_OpenZFSFileSystemConfiguration_Contents"></a>

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** CopyTagsToBackups **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-CopyTagsToBackups"></a>
A Boolean value indicating whether tags on the file system should be copied to backups. If it's set to `true`, all tags on the file system are copied to all automatic backups and any user-initiated backups where the user doesn't specify any tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.   
Type: Boolean  
Required: No

 ** CopyTagsToVolumes **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-CopyTagsToVolumes"></a>
A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false`. If it's set to `true`, all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.   
Type: Boolean  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-DailyAutomaticBackupStartTime"></a>
A recurring daily time, in the format `HH:MM`. `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.   
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DeploymentType **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-DeploymentType"></a>
Specifies the file-system deployment type. Amazon FSx for OpenZFS supports  `MULTI_AZ_1`, `SINGLE_AZ_HA_2`, `SINGLE_AZ_HA_1`, `SINGLE_AZ_2`, and `SINGLE_AZ_1`.  
Type: String  
Valid Values: `SINGLE_AZ_1 | SINGLE_AZ_2 | SINGLE_AZ_HA_1 | SINGLE_AZ_HA_2 | MULTI_AZ_1`   
Required: No

 ** DiskIopsConfiguration **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-DiskIopsConfiguration"></a>
The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP, Amazon FSx for Windows File Server, or FSx for OpenZFS file system. By default, Amazon FSx automatically provisions 3 IOPS per GB of storage capacity. You can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how it is was provisioned, or the mode (by the customer or by Amazon FSx).  
Type: [DiskIopsConfiguration](API_DiskIopsConfiguration.md) object  
Required: No

 ** EndpointIpAddress **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-EndpointIpAddress"></a>
The IPv4 address of the endpoint that is used to access data or to manage the file system.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 45.  
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`   
Required: No

 ** EndpointIpAddressRange **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-EndpointIpAddressRange"></a>
(Multi-AZ only) Specifies the IPv4 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /28 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables.  
Type: String  
Length Constraints: Minimum length of 9. Maximum length of 17.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{9,17}$`   
Required: No

 ** EndpointIpv6Address **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-EndpointIpv6Address"></a>
The IPv6 address of the endpoint that is used to access data or to manage the file system.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 45.  
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`   
Required: No

 ** EndpointIpv6AddressRange **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-EndpointIpv6AddressRange"></a>
(Multi-AZ only) Specifies the IPv6 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /118 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 43.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{4,43}$`   
Required: No

 ** PreferredSubnetId **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-PreferredSubnetId"></a>
Required when `DeploymentType` is set to `MULTI_AZ_1`. This specifies the subnet in which you want the preferred file server to be located.  
Type: String  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `^(subnet-[0-9a-f]{8,})$`   
Required: No

 ** ReadCacheConfiguration **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-ReadCacheConfiguration"></a>
 Required when `StorageType` is set to `INTELLIGENT_TIERING`. Specifies the optional provisioned SSD read cache.   
Type: [OpenZFSReadCacheConfiguration](API_OpenZFSReadCacheConfiguration.md) object  
Required: No

 ** RootVolumeId **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-RootVolumeId"></a>
The ID of the root volume of the OpenZFS file system.   
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: No

 ** RouteTableIds **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-RouteTableIds"></a>
(Multi-AZ only) The VPC route tables in which your file system's endpoints are created.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(rtb-[0-9a-f]{8,})$`   
Required: No

 ** ThroughputCapacity **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-ThroughputCapacity"></a>
The throughput of an Amazon FSx file system, measured in megabytes per second (MBps).  
Type: Integer  
Valid Range: Minimum value of 8. Maximum value of 100000.  
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-OpenZFSFileSystemConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
For example, `1:05:00` specifies maintenance at 5 AM Monday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_OpenZFSFileSystemConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OpenZFSFileSystemConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OpenZFSFileSystemConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OpenZFSFileSystemConfiguration) 