---
id: "@specs/aws/fsx/docs/API_UpdateFileSystemOpenZFSConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFileSystemOpenZFSConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateFileSystemOpenZFSConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateFileSystemOpenZFSConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFileSystemOpenZFSConfiguration
<a name="API_UpdateFileSystemOpenZFSConfiguration"></a>

The configuration updates for an Amazon FSx for OpenZFS file system.

## Contents
<a name="API_UpdateFileSystemOpenZFSConfiguration_Contents"></a>

 ** AddRouteTableIds **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-AddRouteTableIds"></a>
(Multi-AZ only) A list of IDs of new virtual private cloud (VPC) route tables to associate (add) with your Amazon FSx for OpenZFS file system.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(rtb-[0-9a-f]{8,})$`   
Required: No

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** CopyTagsToBackups **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-CopyTagsToBackups"></a>
A Boolean value indicating whether tags for the file system should be copied to backups. This value defaults to `false`. If it's set to `true`, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.  
Type: Boolean  
Required: No

 ** CopyTagsToVolumes **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-CopyTagsToVolumes"></a>
A Boolean value indicating whether tags for the volume should be copied to snapshots. This value defaults to `false`. If it's set to `true`, all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.  
Type: Boolean  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-DailyAutomaticBackupStartTime"></a>
A recurring daily time, in the format `HH:MM`. `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.   
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DiskIopsConfiguration **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-DiskIopsConfiguration"></a>
The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP, Amazon FSx for Windows File Server, or FSx for OpenZFS file system. By default, Amazon FSx automatically provisions 3 IOPS per GB of storage capacity. You can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how it is was provisioned, or the mode (by the customer or by Amazon FSx).  
Type: [DiskIopsConfiguration](API_DiskIopsConfiguration.md) object  
Required: No

 ** EndpointIpv6AddressRange **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-EndpointIpv6AddressRange"></a>
(Multi-AZ only) Specifies the IPv6 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /118 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 43.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{4,43}$`   
Required: No

 ** ReadCacheConfiguration **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-ReadCacheConfiguration"></a>
 The configuration for the optional provisioned SSD read cache on file systems that use the Intelligent-Tiering storage class.  
Type: [OpenZFSReadCacheConfiguration](API_OpenZFSReadCacheConfiguration.md) object  
Required: No

 ** RemoveRouteTableIds **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-RemoveRouteTableIds"></a>
(Multi-AZ only) A list of IDs of existing virtual private cloud (VPC) route tables to disassociate (remove) from your Amazon FSx for OpenZFS file system. You can use the [DescribeFileSystems](API_DescribeFileSystems.md) API operation to retrieve the list of VPC route table IDs for a file system.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(rtb-[0-9a-f]{8,})$`   
Required: No

 ** ThroughputCapacity **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-ThroughputCapacity"></a>
The throughput of an Amazon FSx for OpenZFS file system, measured in megabytes per second  (MB/s). Valid values depend on the DeploymentType you choose, as follows:  
+ For `MULTI_AZ_1` and `SINGLE_AZ_2`, valid values are 160, 320, 640, 1280, 2560, 3840, 5120, 7680, or 10240 MB/s.
+ For `SINGLE_AZ_1`, valid values are 64, 128, 256, 512, 1024, 2048, 3072, or 4096 MB/s.
Type: Integer  
Valid Range: Minimum value of 8. Maximum value of 100000.  
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-UpdateFileSystemOpenZFSConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
For example, `1:05:00` specifies maintenance at 5 AM Monday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_UpdateFileSystemOpenZFSConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateFileSystemOpenZFSConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateFileSystemOpenZFSConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateFileSystemOpenZFSConfiguration) 