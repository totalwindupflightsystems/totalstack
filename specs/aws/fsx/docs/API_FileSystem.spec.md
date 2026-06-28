---
id: "@specs/aws/fsx/docs/API_FileSystem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileSystem"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# FileSystem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_FileSystem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileSystem
<a name="API_FileSystem"></a>

A description of a specific Amazon FSx file system.

## Contents
<a name="API_FileSystem_Contents"></a>

 ** AdministrativeActions **   <a name="FSx-Type-FileSystem-AdministrativeActions"></a>
A list of administrative actions for the file system that are in process or waiting to be processed. Administrative actions describe changes to the Amazon FSx system that you have initiated using the `UpdateFileSystem` operation.  
Type: Array of [AdministrativeAction](API_AdministrativeAction.md) objects  
Array Members: Maximum number of 50 items.  
Required: No

 ** CreationTime **   <a name="FSx-Type-FileSystem-CreationTime"></a>
The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.  
Type: Timestamp  
Required: No

 ** DNSName **   <a name="FSx-Type-FileSystem-DNSName"></a>
The Domain Name System (DNS) name for the file system.  
Type: String  
Length Constraints: Minimum length of 16. Maximum length of 275.  
Pattern: `^((fs|fc)i?-[0-9a-f]{8,}\..{4,253})$`   
Required: No

 ** FailureDetails **   <a name="FSx-Type-FileSystem-FailureDetails"></a>
A structure providing details of any failures that occurred.  
Type: [FileSystemFailureDetails](API_FileSystemFailureDetails.md) object  
Required: No

 ** FileSystemId **   <a name="FSx-Type-FileSystem-FileSystemId"></a>
The system-generated, unique 17-digit ID of the file system.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: No

 ** FileSystemType **   <a name="FSx-Type-FileSystem-FileSystemType"></a>
The type of Amazon FSx file system, which can be `LUSTRE`, `WINDOWS`, `ONTAP`, or `OPENZFS`.  
Type: String  
Valid Values: `WINDOWS | LUSTRE | ONTAP | OPENZFS`   
Required: No

 ** FileSystemTypeVersion **   <a name="FSx-Type-FileSystem-FileSystemTypeVersion"></a>
The Lustre version of the Amazon FSx for Lustre file system, which can be `2.10`, `2.12`, or `2.15`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `^[0-9](.[0-9]*)*$`   
Required: No

 ** KmsKeyId **   <a name="FSx-Type-FileSystem-KmsKeyId"></a>
The ID of the AWS Key Management Service (AWS KMS) key used to encrypt Amazon FSx file system data. Used as follows with Amazon FSx file system types:  
+ Amazon FSx for Lustre `PERSISTENT_1` and `PERSISTENT_2` deployment types only.

   `SCRATCH_1` and `SCRATCH_2` types are encrypted using the Amazon FSx service AWS KMS key for your account.
+ Amazon FSx for NetApp ONTAP
+ Amazon FSx for OpenZFS
+ Amazon FSx for Windows File Server
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^.{1,2048}$`   
Required: No

 ** Lifecycle **   <a name="FSx-Type-FileSystem-Lifecycle"></a>
The lifecycle status of the file system. The following are the possible values and what they mean:  
+  `AVAILABLE` - The file system is in a healthy state, and is reachable and available for use.
+  `CREATING` - Amazon FSx is creating the new file system.
+  `DELETING` - Amazon FSx is deleting an existing file system.
+  `FAILED` - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.
+  `MISCONFIGURED` - The file system is in a failed but recoverable state.
+  `MISCONFIGURED_UNAVAILABLE` - (Amazon FSx for Windows File Server only) The file system is currently unavailable due to a change in your Active Directory configuration.
+  `UPDATING` - The file system is undergoing a customer-initiated update.
Type: String  
Valid Values: `AVAILABLE | CREATING | FAILED | DELETING | MISCONFIGURED | UPDATING | MISCONFIGURED_UNAVAILABLE`   
Required: No

 ** LustreConfiguration **   <a name="FSx-Type-FileSystem-LustreConfiguration"></a>
The configuration for the Amazon FSx for Lustre file system.  
Type: [LustreFileSystemConfiguration](API_LustreFileSystemConfiguration.md) object  
Required: No

 ** NetworkInterfaceIds **   <a name="FSx-Type-FileSystem-NetworkInterfaceIds"></a>
The IDs of the elastic network interfaces from which a specific file system is accessible. The elastic network interface is automatically created in the same virtual private cloud (VPC) that the Amazon FSx file system was created in. For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide.*   
For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(eni-[0-9a-f]{8,})$`   
Required: No

 ** NetworkType **   <a name="FSx-Type-FileSystem-NetworkType"></a>
The network type of the file system.  
Type: String  
Valid Values: `IPV4 | DUAL`   
Required: No

 ** OntapConfiguration **   <a name="FSx-Type-FileSystem-OntapConfiguration"></a>
The configuration for this Amazon FSx for NetApp ONTAP file system.  
Type: [OntapFileSystemConfiguration](API_OntapFileSystemConfiguration.md) object  
Required: No

 ** OpenZFSConfiguration **   <a name="FSx-Type-FileSystem-OpenZFSConfiguration"></a>
The configuration for this Amazon FSx for OpenZFS file system.  
Type: [OpenZFSFileSystemConfiguration](API_OpenZFSFileSystemConfiguration.md) object  
Required: No

 ** OwnerId **   <a name="FSx-Type-FileSystem-OwnerId"></a>
The AWS account that created the file system. If the file system was created by a user in IAM Identity Center, the AWS account to which the IAM user belongs is the owner.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^\d{12}$`   
Required: No

 ** ResourceARN **   <a name="FSx-Type-FileSystem-ResourceARN"></a>
The Amazon Resource Name (ARN) of the file system resource.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: No

 ** StorageCapacity **   <a name="FSx-Type-FileSystem-StorageCapacity"></a>
The storage capacity of the file system in gibibytes (GiB).  
Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of `StorageCapacity` is outside of the minimum or maximum values.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: No

 ** StorageType **   <a name="FSx-Type-FileSystem-StorageType"></a>
The type of storage the file system is using.  
+ If set to `SSD`, the file system uses solid state drive storage.
+ If set to `HDD`, the file system uses hard disk drive storage.
+ If set to `INTELLIGENT_TIERING`, the file system uses fully elastic, intelligently-tiered storage.
Type: String  
Valid Values: `SSD | HDD | INTELLIGENT_TIERING`   
Required: No

 ** SubnetIds **   <a name="FSx-Type-FileSystem-SubnetIds"></a>
Specifies the IDs of the subnets that the file system is accessible from. For the Amazon FSx Windows and ONTAP `MULTI_AZ_1` file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the `PreferredSubnetID` property. All other file systems have only one subnet ID.  
For FSx for Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the file system's endpoint. For `MULTI_AZ_1` Windows and ONTAP file systems, the file system endpoint is available in the `PreferredSubnetID`.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `^(subnet-[0-9a-f]{8,})$`   
Required: No

 ** Tags **   <a name="FSx-Type-FileSystem-Tags"></a>
The tags to associate with the file system. For more information, see [Tagging your Amazon FSx resources](https://docs.aws.amazon.com/fsx/latest/LustreGuide/tag-resources.html) in the *Amazon FSx for Lustre User Guide*.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** VpcId **   <a name="FSx-Type-FileSystem-VpcId"></a>
The ID of the primary virtual private cloud (VPC) for the file system.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(vpc-[0-9a-f]{8,})$`   
Required: No

 ** WindowsConfiguration **   <a name="FSx-Type-FileSystem-WindowsConfiguration"></a>
The configuration for this Amazon FSx for Windows File Server file system.  
Type: [WindowsFileSystemConfiguration](API_WindowsFileSystemConfiguration.md) object  
Required: No

## See Also
<a name="API_FileSystem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/FileSystem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/FileSystem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/FileSystem) 