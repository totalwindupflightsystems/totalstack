---
id: "@specs/aws/fsx/docs/API_UpdateFileCache"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFileCache"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateFileCache

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateFileCache
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFileCache
<a name="API_UpdateFileCache"></a>

Updates the configuration of an existing Amazon File Cache resource. You can update multiple properties in a single request.

## Request Syntax
<a name="API_UpdateFileCache_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "FileCacheId": "{{string}}",
   "LustreConfiguration": { 
      "WeeklyMaintenanceStartTime": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateFileCache_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_UpdateFileCache_RequestSyntax) **   <a name="FSx-UpdateFileCache-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileCacheId](#API_UpdateFileCache_RequestSyntax) **   <a name="FSx-UpdateFileCache-request-FileCacheId"></a>
The ID of the cache that you are updating.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fc-[0-9a-f]{8,})$`   
Required: Yes

 ** [LustreConfiguration](#API_UpdateFileCache_RequestSyntax) **   <a name="FSx-UpdateFileCache-request-LustreConfiguration"></a>
The configuration updates for an Amazon File Cache resource.  
Type: [UpdateFileCacheLustreConfiguration](API_UpdateFileCacheLustreConfiguration.md) object  
Required: No

## Response Syntax
<a name="API_UpdateFileCache_ResponseSyntax"></a>

```
{
   "FileCache": { 
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
      "VpcId": "string"
   }
}
```

## Response Elements
<a name="API_UpdateFileCache_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FileCache](#API_UpdateFileCache_ResponseSyntax) **   <a name="FSx-UpdateFileCache-response-FileCache"></a>
A description of the cache that was updated.  
Type: [FileCache](API_FileCache.md) object

## Errors
<a name="API_UpdateFileCache_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** FileCacheNotFound **   
No caches were found based upon supplied parameters.    
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

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_UpdateFileCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/UpdateFileCache) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/UpdateFileCache) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateFileCache) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/UpdateFileCache) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateFileCache) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/UpdateFileCache) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/UpdateFileCache) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/UpdateFileCache) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/UpdateFileCache) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateFileCache) 