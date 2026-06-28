---
id: "@specs/aws/fsx/docs/API_UpdateFileSystemOntapConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFileSystemOntapConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateFileSystemOntapConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateFileSystemOntapConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFileSystemOntapConfiguration
<a name="API_UpdateFileSystemOntapConfiguration"></a>

The configuration updates for an Amazon FSx for NetApp ONTAP file system.

## Contents
<a name="API_UpdateFileSystemOntapConfiguration_Contents"></a>

 ** AddRouteTableIds **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-AddRouteTableIds"></a>
(Multi-AZ only) A list of IDs of new virtual private cloud (VPC) route tables to associate (add) with your Amazon FSx for NetApp ONTAP file system.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(rtb-[0-9a-f]{8,})$`   
Required: No

 ** AutomaticBackupRetentionDays **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-AutomaticBackupRetentionDays"></a>
The number of days to retain automatic backups. Setting this property to `0` disables automatic backups and deletes all existing automatic backups for the file system's volumes. You can retain automatic backups for a maximum of 90 days. The default is `30`.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 90.  
Required: No

 ** DailyAutomaticBackupStartTime **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-DailyAutomaticBackupStartTime"></a>
A recurring daily time, in the format `HH:MM`. `HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour. For example, `05:00` specifies 5 AM daily.   
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `^([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

 ** DiskIopsConfiguration **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-DiskIopsConfiguration"></a>
The SSD IOPS (input output operations per second) configuration for an Amazon FSx for NetApp ONTAP file system. The default is 3 IOPS per GB of storage capacity, but you can provision additional IOPS per GB of storage. The configuration consists of an IOPS mode (`AUTOMATIC` or `USER_PROVISIONED`), and in the case of `USER_PROVISIONED` IOPS, the total number of SSD IOPS provisioned. For more information, see [File system storage capacity and IOPS](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.html).  
Type: [DiskIopsConfiguration](API_DiskIopsConfiguration.md) object  
Required: No

 ** EndpointIpv6AddressRange **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-EndpointIpv6AddressRange"></a>
(Multi-AZ only) Specifies the IPv6 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /118 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 43.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{4,43}$`   
Required: No

 ** FsxAdminPassword **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-FsxAdminPassword"></a>
Update the password for the `fsxadmin` user by entering a new password. You use the `fsxadmin` user to access the NetApp ONTAP CLI and REST API to manage your file system resources. For more information, see [Managing resources using NetApp Application](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-resources-ontap-apps.html).  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 50.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{8,50}$`   
Required: No

 ** HAPairs **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-HAPairs"></a>
Use to update the number of high-availability (HA) pairs for a second-generation single-AZ file system. If you increase the number of HA pairs for your file system, you must specify proportional increases for `StorageCapacity`, `Iops`, and `ThroughputCapacity`. For more information, see [High-availability (HA) pairs](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/administering-file-systems.html#HA-pairs) in the FSx for ONTAP user guide. Block storage protocol support (iSCSI and NVMe over TCP) is disabled on file systems with more than 6 HA pairs. For more information, see [Using block storage protocols](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/supported-fsx-clients.html#using-block-storage).  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 12.  
Required: No

 ** RemoveRouteTableIds **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-RemoveRouteTableIds"></a>
(Multi-AZ only) A list of IDs of existing virtual private cloud (VPC) route tables to disassociate (remove) from your Amazon FSx for NetApp ONTAP file system. You can use the [DescribeFileSystems](API_DescribeFileSystems.md) API operation to retrieve the list of VPC route table IDs for a file system.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(rtb-[0-9a-f]{8,})$`   
Required: No

 ** ThroughputCapacity **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-ThroughputCapacity"></a>
Enter a new value to change the amount of throughput capacity for the file system in megabytes per second (MBps). For more information, see [Managing throughput capacity](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-throughput-capacity.html) in the FSx for ONTAP User Guide.  
Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:  
+ The value of `ThroughputCapacity` and `ThroughputCapacityPerHAPair` are not the same value.
+ The value of `ThroughputCapacity` when divided by the value of `HAPairs` is outside of the valid range for `ThroughputCapacity`.
Type: Integer  
Valid Range: Minimum value of 8. Maximum value of 100000.  
Required: No

 ** ThroughputCapacityPerHAPair **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-ThroughputCapacityPerHAPair"></a>
Use to choose the throughput capacity per HA pair, rather than the total throughput for the file system.   
This field and `ThroughputCapacity` cannot be defined in the same API call, but one is required.  
This field and `ThroughputCapacity` are the same for file systems with one HA pair.  
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

 ** WeeklyMaintenanceStartTime **   <a name="FSx-Type-UpdateFileSystemOntapConfiguration-WeeklyMaintenanceStartTime"></a>
The preferred start time to perform weekly maintenance, formatted d:HH:MM in the UTC time zone, where d is the weekday number, from 1 through 7, beginning with Monday and ending with Sunday.  
For example, `1:05:00` specifies maintenance at 5 AM Monday.  
Type: String  
Length Constraints: Fixed length of 7.  
Pattern: `^[1-7]:([01]\d|2[0-3]):?([0-5]\d)$`   
Required: No

## See Also
<a name="API_UpdateFileSystemOntapConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateFileSystemOntapConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateFileSystemOntapConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateFileSystemOntapConfiguration) 