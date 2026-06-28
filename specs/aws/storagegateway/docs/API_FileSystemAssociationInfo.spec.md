---
id: "@specs/aws/storagegateway/docs/API_FileSystemAssociationInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileSystemAssociationInfo"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# FileSystemAssociationInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_FileSystemAssociationInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileSystemAssociationInfo
<a name="API_FileSystemAssociationInfo"></a>

Describes the object returned by `DescribeFileSystemAssociations` that describes a created file system association.

## Contents
<a name="API_FileSystemAssociationInfo_Contents"></a>

 ** AuditDestinationARN **   <a name="StorageGateway-Type-FileSystemAssociationInfo-AuditDestinationARN"></a>
The Amazon Resource Name (ARN) of the storage used for the audit logs.  
Type: String  
Length Constraints: Maximum length of 1024.  
Required: No

 ** CacheAttributes **   <a name="StorageGateway-Type-FileSystemAssociationInfo-CacheAttributes"></a>
The refresh cache information for the file share or FSx file systems.  
Type: [CacheAttributes](API_CacheAttributes.md) object  
Required: No

 ** EndpointNetworkConfiguration **   <a name="StorageGateway-Type-FileSystemAssociationInfo-EndpointNetworkConfiguration"></a>
Specifies network configuration information for the gateway associated with the Amazon FSx file system.  
If multiple file systems are associated with this gateway, this parameter's `IpAddresses` field is required.
Type: [EndpointNetworkConfiguration](API_EndpointNetworkConfiguration.md) object  
Required: No

 ** FileSystemAssociationARN **   <a name="StorageGateway-Type-FileSystemAssociationInfo-FileSystemAssociationARN"></a>
The Amazon Resource Name (ARN) of the file system association.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** FileSystemAssociationStatus **   <a name="StorageGateway-Type-FileSystemAssociationInfo-FileSystemAssociationStatus"></a>
The status of the file system association. Valid Values: `AVAILABLE` \| `CREATING` \| `DELETING` \| `FORCE_DELETING` \| `UPDATING` \| `ERROR`   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 50.  
Required: No

 ** FileSystemAssociationStatusDetails **   <a name="StorageGateway-Type-FileSystemAssociationInfo-FileSystemAssociationStatusDetails"></a>
An array containing the FileSystemAssociationStatusDetail data type, which provides detailed information on file system association status.  
Type: Array of [FileSystemAssociationStatusDetail](API_FileSystemAssociationStatusDetail.md) objects  
Required: No

 ** GatewayARN **   <a name="StorageGateway-Type-FileSystemAssociationInfo-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

 ** LocationARN **   <a name="StorageGateway-Type-FileSystemAssociationInfo-LocationARN"></a>
The ARN of the backend Amazon FSx file system used for storing file data. For information, see [FileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_FileSystem.html) in the *Amazon FSx API Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Required: No

 ** Tags **   <a name="StorageGateway-Type-FileSystemAssociationInfo-Tags"></a>
A list of up to 50 tags assigned to the SMB file share, sorted alphabetically by key name. Each tag is a key-value pair.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## See Also
<a name="API_FileSystemAssociationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/FileSystemAssociationInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/FileSystemAssociationInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/FileSystemAssociationInfo) 