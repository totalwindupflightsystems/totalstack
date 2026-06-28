---
id: "@specs/aws/fsx/docs/API_CreateFileCache"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFileCache"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateFileCache

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateFileCache
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFileCache
<a name="API_CreateFileCache"></a>

Creates a new Amazon File Cache resource.

You can use this operation with a client request token in the request that Amazon File Cache uses to ensure idempotent creation. If a cache with the specified client request token exists and the parameters match, `CreateFileCache` returns the description of the existing cache. If a cache with the specified client request token exists and the parameters don't match, this call returns `IncompatibleParameterError`. If a file cache with the specified client request token doesn't exist, `CreateFileCache` does the following: 
+ Creates a new, empty Amazon File Cache resource with an assigned ID, and an initial lifecycle state of `CREATING`.
+ Returns the description of the cache in JSON format.

**Note**  
The `CreateFileCache` call returns while the cache's lifecycle state is still `CREATING`. You can check the cache creation status by calling the [DescribeFileCaches](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileCaches.html) operation, which returns the cache state along with other information.

## Request Syntax
<a name="API_CreateFileCache_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "CopyTagsToDataRepositoryAssociations": {{boolean}},
   "DataRepositoryAssociations": [ 
      { 
         "DataRepositoryPath": "{{string}}",
         "DataRepositorySubdirectories": [ "{{string}}" ],
         "FileCachePath": "{{string}}",
         "NFS": { 
            "DnsIps": [ "{{string}}" ],
            "Version": "{{string}}"
         }
      }
   ],
   "FileCacheType": "{{string}}",
   "FileCacheTypeVersion": "{{string}}",
   "KmsKeyId": "{{string}}",
   "LustreConfiguration": { 
      "DeploymentType": "{{string}}",
      "MetadataConfiguration": { 
         "StorageCapacity": {{number}}
      },
      "PerUnitStorageThroughput": {{number}},
      "WeeklyMaintenanceStartTime": "{{string}}"
   },
   "SecurityGroupIds": [ "{{string}}" ],
   "StorageCapacity": {{number}},
   "SubnetIds": [ "{{string}}" ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateFileCache_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-ClientRequestToken"></a>
An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
By using the idempotent operation, you can retry a `CreateFileCache` operation without the risk of creating an extra cache. This approach can be useful when an initial call fails in a way that makes it unclear whether a cache was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a cache, the client receives success as long as the parameters are the same.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [CopyTagsToDataRepositoryAssociations](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-CopyTagsToDataRepositoryAssociations"></a>
A boolean flag indicating whether tags for the cache should be copied to data repository associations. This value defaults to false.  
Type: Boolean  
Required: No

 ** [DataRepositoryAssociations](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-DataRepositoryAssociations"></a>
A list of up to 8 configurations for data repository associations (DRAs) to be created during the cache creation. The DRAs link the cache to either an Amazon S3 data repository or a Network File System (NFS) data repository that supports the NFSv3 protocol.  
The DRA configurations must meet the following requirements:  
+ All configurations on the list must be of the same data repository type, either all S3 or all NFS. A cache can't link to different data repository types at the same time.
+ An NFS DRA must link to an NFS file system that supports the NFSv3 protocol.
DRA automatic import and automatic export is not supported.  
Type: Array of [FileCacheDataRepositoryAssociation](API_FileCacheDataRepositoryAssociation.md) objects  
Array Members: Maximum number of 8 items.  
Required: No

 ** [FileCacheType](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-FileCacheType"></a>
The type of cache that you're creating, which must be `LUSTRE`.  
Type: String  
Valid Values: `LUSTRE`   
Required: Yes

 ** [FileCacheTypeVersion](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-FileCacheTypeVersion"></a>
Sets the Lustre version for the cache that you're creating, which must be `2.12`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `^[0-9](.[0-9]*)*$`   
Required: Yes

 ** [KmsKeyId](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-KmsKeyId"></a>
Specifies the ID of the AWS Key Management Service (AWS KMS) key to use for encrypting data on an Amazon File Cache. If a `KmsKeyId` isn't specified, the Amazon FSx-managed AWS KMS key for your account is used. For more information, see [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) in the * AWS Key Management Service API Reference*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^.{1,2048}$`   
Required: No

 ** [LustreConfiguration](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-LustreConfiguration"></a>
The configuration for the Amazon File Cache resource being created.  
Type: [CreateFileCacheLustreConfiguration](API_CreateFileCacheLustreConfiguration.md) object  
Required: No

 ** [SecurityGroupIds](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-SecurityGroupIds"></a>
A list of IDs specifying the security groups to apply to all network interfaces created for Amazon File Cache access. This list isn't returned in later requests to describe the cache.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 11. Maximum length of 20.  
Pattern: `^(sg-[0-9a-f]{8,})$`   
Required: No

 ** [StorageCapacity](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-StorageCapacity"></a>
The storage capacity of the cache in gibibytes (GiB). Valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: Yes

 ** [SubnetIds](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-SubnetIds"></a>
A list of subnet IDs that the cache will be accessible from. You can specify only one subnet ID in a call to the `CreateFileCache` operation.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `^(subnet-[0-9a-f]{8,})$`   
Required: Yes

 ** [Tags](#API_CreateFileCache_RequestSyntax) **   <a name="FSx-CreateFileCache-request-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## Response Syntax
<a name="API_CreateFileCache_ResponseSyntax"></a>

```
{
   "FileCache": { 
      "CopyTagsToDataRepositoryAssociations": boolean,
      "CreationTime": number,
      "DataRepositoryAssociationIds": [ "string" ],
      "DNSName": "string",
      "FailureDetails": { 
         "Message": "string"
      },
      "FileCacheId": "string",
      "FileCacheType": "string",
      "FileCacheTypeVersion": "string",
      "KmsKeyId": "string",
      "Lifecycle": "string",
      "LustreConfiguration": { 
         "DeploymentType": "string",
         "LogConfiguration": { 
            "Destination": "string",
            "Level": "string"
         },
         "MetadataConfiguration": { 
            "StorageCapacity": number
         },
         "MountName": "string",
         "PerUnitStorageThroughput": number,
         "WeeklyMaintenanceStartTime": "string"
      },
      "NetworkInterfaceIds": [ "string" ],
      "OwnerId": "string",
      "ResourceARN": "string",
      "StorageCapacity": number,
      "SubnetIds": [ "string" ],
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "VpcId": "string"
   }
}
```

## Response Elements
<a name="API_CreateFileCache_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileCache](#API_CreateFileCache_ResponseSyntax) **   <a name="FSx-CreateFileCache-response-FileCache"></a>
A description of the cache that was created.  
Type: [FileCacheCreating](API_FileCacheCreating.md) object

## Errors
<a name="API_CreateFileCache_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **   
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.    
 ** Message **   
A detailed error message.  
 ** Parameter **   
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** InvalidNetworkSettings **   
One or more network settings specified in the request are invalid.    
 ** InvalidRouteTableId **   
The route table ID is either invalid or not part of the VPC specified.  
 ** InvalidSecurityGroupId **   
The security group ID is either invalid or not part of the VPC specified.  
 ** InvalidSubnetId **   
The subnet ID that is either invalid or not part of the VPC specified.  
 ** Message **   
Error message explaining what's wrong with network settings.
HTTP Status Code: 400

 ** InvalidPerUnitStorageThroughput **   
An invalid value for `PerUnitStorageThroughput` was provided. Please create your file system again, using a valid value.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** MissingFileCacheConfiguration **   
A cache configuration is required for this operation.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** ServiceLimitExceeded **   
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.    
 ** Limit **   
Enumeration of the service limit that was exceeded.   
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateFileCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateFileCache) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateFileCache) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateFileCache) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateFileCache) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateFileCache) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateFileCache) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateFileCache) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateFileCache) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateFileCache) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateFileCache) 