---
id: "@specs/aws/storagegateway/docs/API_Disk"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Disk"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# Disk

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_Disk
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Disk
<a name="API_Disk"></a>

Represents a gateway's local disk.

## Contents
<a name="API_Disk_Contents"></a>

 ** DiskAllocationResource **   <a name="StorageGateway-Type-Disk-DiskAllocationResource"></a>
The iSCSI qualified name (IQN) that is defined for a disk. This field is not included in the response if the local disk is not defined as an iSCSI target. The format of this field is *targetIqn::LUNNumber::region-volumeId*.  
Type: String  
Required: No

 ** DiskAllocationType **   <a name="StorageGateway-Type-Disk-DiskAllocationType"></a>
One of the `DiskAllocationType` enumeration values that identifies how a local disk is used.  
Valid Values: `UPLOAD_BUFFER` \| `CACHE_STORAGE`   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 100.  
Required: No

 ** DiskAttributeList **   <a name="StorageGateway-Type-Disk-DiskAttributeList"></a>
A list of values that represents attributes of a local disk.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** DiskId **   <a name="StorageGateway-Type-Disk-DiskId"></a>
The unique device ID or other distinguishing data that identifies a local disk.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: No

 ** DiskNode **   <a name="StorageGateway-Type-Disk-DiskNode"></a>
The device node of a local disk as assigned by the virtualization environment.  
Type: String  
Required: No

 ** DiskPath **   <a name="StorageGateway-Type-Disk-DiskPath"></a>
The path of a local disk in the gateway virtual machine (VM).  
Type: String  
Required: No

 ** DiskSizeInBytes **   <a name="StorageGateway-Type-Disk-DiskSizeInBytes"></a>
The local disk size in bytes.  
Type: Long  
Required: No

 ** DiskStatus **   <a name="StorageGateway-Type-Disk-DiskStatus"></a>
A value that represents the status of a local disk.  
Type: String  
Required: No

## See Also
<a name="API_Disk_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/Disk) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/Disk) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/Disk) 