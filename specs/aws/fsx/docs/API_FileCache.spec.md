---
id: "@specs/aws/fsx/docs/API_FileCache"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileCache"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# FileCache

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_FileCache
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileCache
<a name="API_FileCache"></a>

A description of a specific Amazon File Cache resource, which is a response object from the `DescribeFileCaches` operation.

## Contents
<a name="API_FileCache_Contents"></a>

 ** CreationTime **   <a name="FSx-Type-FileCache-CreationTime"></a>
The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.  
Type: Timestamp  
Required: No

 ** DataRepositoryAssociationIds **   <a name="FSx-Type-FileCache-DataRepositoryAssociationIds"></a>
A list of IDs of data repository associations that are associated with this cache.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 13. Maximum length of 23.  
Pattern: `^(dra-[0-9a-f]{8,})$`   
Required: No

 ** DNSName **   <a name="FSx-Type-FileCache-DNSName"></a>
The Domain Name System (DNS) name for the cache.  
Type: String  
Length Constraints: Minimum length of 16. Maximum length of 275.  
Pattern: `^((fs|fc)i?-[0-9a-f]{8,}\..{4,253})$`   
Required: No

 ** FailureDetails **   <a name="FSx-Type-FileCache-FailureDetails"></a>
A structure providing details of any failures that occurred.  
Type: [FileCacheFailureDetails](API_FileCacheFailureDetails.md) object  
Required: No

 ** FileCacheId **   <a name="FSx-Type-FileCache-FileCacheId"></a>
The system-generated, unique ID of the cache.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fc-[0-9a-f]{8,})$`   
Required: No

 ** FileCacheType **   <a name="FSx-Type-FileCache-FileCacheType"></a>
The type of cache, which must be `LUSTRE`.  
Type: String  
Valid Values: `LUSTRE`   
Required: No

 ** FileCacheTypeVersion **   <a name="FSx-Type-FileCache-FileCacheTypeVersion"></a>
The Lustre version of the cache, which must be `2.12`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `^[0-9](.[0-9]*)*$`   
Required: No

 ** KmsKeyId **   <a name="FSx-Type-FileCache-KmsKeyId"></a>
Specifies the ID of the AWS Key Management Service (AWS KMS) key to use for encrypting data on an Amazon File Cache. If a `KmsKeyId` isn't specified, the Amazon FSx-managed AWS KMS key for your account is used. For more information, see [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) in the * AWS Key Management Service API Reference*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^.{1,2048}$`   
Required: No

 ** Lifecycle **   <a name="FSx-Type-FileCache-Lifecycle"></a>
The lifecycle status of the cache. The following are the possible values and what they mean:  
+  `AVAILABLE` - The cache is in a healthy state, and is reachable and available for use.
+  `CREATING` - The new cache is being created.
+  `DELETING` - An existing cache is being deleted.
+  `UPDATING` - The cache is undergoing a customer-initiated update.
+  `FAILED` - An existing cache has experienced an unrecoverable failure. When creating a new cache, the cache was unable to be created.
Type: String  
Valid Values: `AVAILABLE | CREATING | DELETING | UPDATING | FAILED`   
Required: No

 ** LustreConfiguration **   <a name="FSx-Type-FileCache-LustreConfiguration"></a>
The configuration for the Amazon File Cache resource.  
Type: [FileCacheLustreConfiguration](API_FileCacheLustreConfiguration.md) object  
Required: No

 ** NetworkInterfaceIds **   <a name="FSx-Type-FileCache-NetworkInterfaceIds"></a>
A list of network interface IDs.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(eni-[0-9a-f]{8,})$`   
Required: No

 ** OwnerId **   <a name="FSx-Type-FileCache-OwnerId"></a>
An AWS account ID. This ID is a 12-digit number that you use to construct Amazon Resource Names (ARNs) for resources.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^\d{12}$`   
Required: No

 ** ResourceARN **   <a name="FSx-Type-FileCache-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: No

 ** StorageCapacity **   <a name="FSx-Type-FileCache-StorageCapacity"></a>
The storage capacity of the cache in gibibytes (GiB).  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: No

 ** SubnetIds **   <a name="FSx-Type-FileCache-SubnetIds"></a>
A list of subnet IDs that the cache will be accessible from. You can specify only one subnet ID in a call to the `CreateFileCache` operation.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `^(subnet-[0-9a-f]{8,})$`   
Required: No

 ** VpcId **   <a name="FSx-Type-FileCache-VpcId"></a>
The ID of your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide*.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 21.  
Pattern: `^(vpc-[0-9a-f]{8,})$`   
Required: No

## See Also
<a name="API_FileCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/FileCache) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/FileCache) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/FileCache) 