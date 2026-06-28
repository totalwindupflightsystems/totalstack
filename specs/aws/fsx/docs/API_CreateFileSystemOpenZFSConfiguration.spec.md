---
id: "@specs/aws/fsx/docs/API_CreateFileSystemOpenZFSConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFileSystemOpenZFSConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateFileSystemOpenZFSConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateFileSystemOpenZFSConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFileSystemOpenZFSConfiguration
<a name="API_CreateFileSystemOpenZFSConfiguration"></a>

The Amazon FSx for OpenZFS configuration properties for the file system that you are creating.

## Contents
<a name="API_CreateFileSystemOpenZFSConfiguration_Contents"></a>

 ** DeploymentType **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-DeploymentType"></a>
Specifies the file system deployment type. Valid values are the following:  
+  `MULTI_AZ_1`- Creates file systems with high availability and durability by replicating your data and supporting failover across multiple Availability Zones in the same AWS Region.
+  `SINGLE_AZ_HA_2`- Creates file systems with high availability and throughput capacities of 160 - 10,240 MB/s using an NVMe L2ARC cache by deploying a primary and standby file system within the same Availability Zone.
+  `SINGLE_AZ_HA_1`- Creates file systems with high availability and throughput capacities of 64 - 4,096 MB/s by deploying a primary and standby file system within the same Availability Zone.
+  `SINGLE_AZ_2`- Creates file systems with throughput capacities of 160 - 10,240 MB/s using an NVMe L2ARC cache that automatically recover within a single Availability Zone.
+  `SINGLE_AZ_1`- Creates file systems with throughput capacities of 64 - 4,096 MBs that automatically recover within a single Availability Zone.
For a list of which AWS Regions each deployment type is available in, see [Deployment type availability](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/availability-durability.html#available-aws-regions). For more information on the differences in performance between deployment types, see [File system performance](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#zfs-fs-performance) in the *Amazon FSx for OpenZFS User Guide*.  
Type: String  
Valid Values: `SINGLE_AZ_1 | SINGLE_AZ_2 | SINGLE_AZ_HA_1 | SINGLE_AZ_HA_2 | MULTI_AZ_1`   
Required: Yes

 ** ThroughputCapacity **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-ThroughputCapacity"></a>
Specifies the throughput of an Amazon FSx for OpenZFS file system, measured in megabytes per second (MBps). Valid values depend on the `DeploymentType` that you choose, as follows:  
+ For `MULTI_AZ_1` and `SINGLE_AZ_2`, valid values are 160, 320, 640, 1280, 2560, 3840, 5120, 7680, or 10240 MBps.
+ For `SINGLE_AZ_1`, valid values are 64, 128, 256, 512, 1024, 2048, 3072, or 4096 MBps.
You pay for additional throughput capacity that you provision.  
Type: Integer  
Valid Range: Minimum value of 8. Maximum value of 100000.  
Required: Yes

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is `30`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** CopyTagsToBackups **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-CopyTagsToBackups"></a>
A Boolean value indicating whether tags for the file system should be copied to backups. This value defaults to `false`. If it's set to `true`, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is `true`, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.  
Type: Boolean  
Required: No

 ** CopyTagsToVolumes **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-CopyTagsToVolumes"></a>
A Boolean value indicating whether tags for the file system should be copied to volumes. This value defaults to `false`. If it's set to `true`, all tags for the file system are copied to volumes where the user doesn't specify tags. If this value is `true`, and you specify one or more tags, only the specified tags are copied to volumes. If you specify one or more tags when creating the volume, no tags are copied from the file system, regardless of this value.  
Type: Boolean  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-DailyAutomaticBackupStartTime"></a>
A recurring daily time, in the format `HH:MM`. `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.   
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DiskIopsConfiguration **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-DiskIopsConfiguration"></a>
The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP, Amazon FSx for Windows File Server, or FSx for OpenZFS file system. By default, Amazon FSx automatically provisions 3 IOPS per GB of storage capacity. You can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how it is was provisioned, or the mode (by the customer or by Amazon FSx).  
Type: [DiskIopsConfiguration](API_DiskIopsConfiguration.md) object  
Required: No

 ** EndpointIpAddressRange **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-EndpointIpAddressRange"></a>
(Multi-AZ only) Specifies the IPv4 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /28 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.  
Type: String  
Length Constraints: Minimum length of 9. Maximum length of 17.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{9,17}$`   
Required: No

 ** EndpointIpv6AddressRange **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-EndpointIpv6AddressRange"></a>
(Multi-AZ only) Specifies the IPv6 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /118 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 43.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{4,43}$`   
Required: No

 ** PreferredSubnetId **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-PreferredSubnetId"></a>
Required when `DeploymentType` is set to `MULTI_AZ_1`. This specifies the subnet in which you want the preferred file server to be located.  
Type: String  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `^(subnet-[0-9a-f]{8,})$`   
Required: No

 ** ReadCacheConfiguration **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-ReadCacheConfiguration"></a>
 Specifies the optional provisioned SSD read cache on file systems that use the Intelligent-Tiering storage class.   
Type: [OpenZFSReadCacheConfiguration](API_OpenZFSReadCacheConfiguration.md) object  
Required: No

 ** RootVolumeConfiguration **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-RootVolumeConfiguration"></a>
The configuration Amazon FSx uses when creating the root value of the Amazon FSx for OpenZFS file system. All volumes are children of the root volume.   
Type: [OpenZFSCreateRootVolumeConfiguration](API_OpenZFSCreateRootVolumeConfiguration.md) object  
Required: No

 ** RouteTableIds **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-RouteTableIds"></a>
(Multi-AZ only) Specifies the route tables in which Amazon FSx creates the rules for routing traffic to the correct file server. You should specify all virtual private cloud (VPC) route tables associated with the subnets in which your clients are located. By default, Amazon FSx selects your VPC's default route table.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(rtb-[0-9a-f]{8,})$`   
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-CreateFileSystemOpenZFSConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
For example, `1:05:00` specifies maintenance at 5 AM Monday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_CreateFileSystemOpenZFSConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateFileSystemOpenZFSConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateFileSystemOpenZFSConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateFileSystemOpenZFSConfiguration) 