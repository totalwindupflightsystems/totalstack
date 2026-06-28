---
id: "@specs/aws/fsx/docs/API_CreateFileSystemOntapConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFileSystemOntapConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateFileSystemOntapConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateFileSystemOntapConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFileSystemOntapConfiguration
<a name="API_CreateFileSystemOntapConfiguration"></a>

The ONTAP configuration properties of the FSx for ONTAP file system that you are creating.

## Contents
<a name="API_CreateFileSystemOntapConfiguration_Contents"></a>

 ** DeploymentType **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-DeploymentType"></a>
Specifies the FSx for ONTAP file system deployment type to use in creating the file system.   
+  `MULTI_AZ_1` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary Availability Zone (AZ) unavailability. This is a first-generation FSx for ONTAP file system.
+  `MULTI_AZ_2` - A high availability file system configured for Multi-AZ redundancy to tolerate temporary AZ unavailability. This is a second-generation FSx for ONTAP file system.
+  `SINGLE_AZ_1` - A file system configured for Single-AZ redundancy. This is a first-generation FSx for ONTAP file system.
+  `SINGLE_AZ_2` - A file system configured with multiple high-availability (HA) pairs for Single-AZ redundancy. This is a second-generation FSx for ONTAP file system.
For information about the use cases for Multi-AZ and Single-AZ deployments, refer to [Choosing a file system deployment type](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-AZ.html).   
Type: String  
Valid Values: `MULTI_AZ_1 | SINGLE_AZ_1 | SINGLE_AZ_2 | MULTI_AZ_2`   
Required: Yes

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups and deletes all existing automatic backups for the file system's volumes. You can retain automatic backups for a maximum of 90 days. The default is `30`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-DailyAutomaticBackupStartTime"></a>
A recurring daily time, in the format `HH:MM`. `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.   
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DiskIopsConfiguration **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-DiskIopsConfiguration"></a>
The SSD IOPS configuration for the FSx for ONTAP file system.  
Type: [DiskIopsConfiguration](API_DiskIopsConfiguration.md) object  
Required: No

 ** EndpointIpAddressRange **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-EndpointIpAddressRange"></a>
(Multi-AZ only) Specifies the IPv4 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API, Amazon FSx selects an unused IP address range for you from the 198.19.\* range. By default in the Amazon FSx console, Amazon FSx chooses the last 64 IP addresses from the VPC’s primary CIDR range to use as the endpoint IP address range for the file system. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.  
Type: String  
Length Constraints: Minimum length of 9. Maximum length of 17.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{9,17}$`   
Required: No

 ** EndpointIpv6AddressRange **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-EndpointIpv6AddressRange"></a>
(Multi-AZ only) Specifies the IPv6 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /118 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 43.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{4,43}$`   
Required: No

 ** FsxAdminPassword **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-FsxAdminPassword"></a>
The ONTAP administrative password for the `fsxadmin` user with which you administer your file system using the NetApp ONTAP CLI and REST API.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 50.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{8,50}$`   
Required: No

 ** HAPairs **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-HAPairs"></a>
Specifies how many high-availability (HA) pairs of file servers will power your file system. First-generation file systems are powered by 1 HA pair. Second-generation multi-AZ file systems are powered by 1 HA pair. Second generation single-AZ file systems are powered by up to 12 HA pairs. The default value is 1. The value of this property affects the values of `StorageCapacity`, `Iops`, and `ThroughputCapacity`. For more information, see [High-availability (HA) pairs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/administering-file-systems.html#HA-pairs) in the FSx for ONTAP user guide. Block storage protocol support (iSCSI and NVMe over TCP) is disabled on file systems with more than 6 HA pairs. For more information, see [Using block storage protocols](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/supported-fsx-clients.html#using-block-storage).   
Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:  
+ The value of `HAPairs` is less than 1 or greater than 12.
+ The value of `HAPairs` is greater than 1 and the value of `DeploymentType` is `SINGLE_AZ_1`, `MULTI_AZ_1`, or `MULTI_AZ_2`.
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 12.  
Required: No

 ** PreferredSubnetId **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-PreferredSubnetId"></a>
Required when `DeploymentType` is set to `MULTI_AZ_1` or `MULTI_AZ_2`. This specifies the subnet in which you want the preferred file server to be located.  
Type: String  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `^(subnet-[0-9a-f]{8,})$`   
Required: No

 ** RouteTableIds **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-RouteTableIds"></a>
(Multi-AZ only) Specifies the route tables in which Amazon FSx creates the rules for routing traffic to the correct file server. You should specify all virtual private cloud (VPC) route tables associated with the subnets in which your clients are located. By default, Amazon FSx selects your VPC's default route table.  
Amazon FSx manages these route tables for Multi-AZ file systems using tag-based authentication. These route tables are tagged with `Key: AmazonFSx; Value: ManagedByAmazonFSx`. When creating FSx for ONTAP Multi-AZ file systems using CloudFormation we recommend that you add the `Key: AmazonFSx; Value: ManagedByAmazonFSx` tag manually.
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(rtb-[0-9a-f]{8,})$`   
Required: No

 ** ThroughputCapacity **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-ThroughputCapacity"></a>
Sets the throughput capacity for the file system that you're creating in megabytes per second (MBps). For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-throughput-capacity.html) in the FSx for ONTAP User Guide.  
Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:  
+ The value of `ThroughputCapacity` and `ThroughputCapacityPerHAPair` are not the same value.
+ The value of `ThroughputCapacity` when divided by the value of `HAPairs` is outside of the valid range for `ThroughputCapacity`.
Type: Integer  
Valid Range: Minimum value of 8. Maximum value of 100000.  
Required: No

 ** ThroughputCapacityPerHAPair **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-ThroughputCapacityPerHAPair"></a>
Use to choose the throughput capacity per HA pair, rather than the total throughput for the file system.   
You can define either the `ThroughputCapacityPerHAPair` or the `ThroughputCapacity` when creating a file system, but not both.  
This field and `ThroughputCapacity` are the same for file systems powered by one HA pair.  
+ For `SINGLE_AZ_1` and `MULTI_AZ_1` file systems, valid values are 128, 256, 512, 1024, 2048, or 4096 MBps.
+ For `SINGLE_AZ_2`, valid values are 1536, 3072, or 6144 MBps.
+ For `MULTI_AZ_2`, valid values are 384, 768, 1536, 3072, or 6144 MBps.
Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:  
+ The value of `ThroughputCapacity` and `ThroughputCapacityPerHAPair` are not the same value for file systems with one HA pair.
+ The value of deployment type is `SINGLE_AZ_2` and `ThroughputCapacity` / `ThroughputCapacityPerHAPair` is not a valid HA pair (a value between 1 and 12).
+ The value of `ThroughputCapacityPerHAPair` is not a valid value.
Type: Integer  
Valid Range: Minimum value of 128. Maximum value of 6144.  
Required: No

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-CreateFileSystemOntapConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
For example, `1:05:00` specifies maintenance at 5 AM Monday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_CreateFileSystemOntapConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateFileSystemOntapConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateFileSystemOntapConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateFileSystemOntapConfiguration) 