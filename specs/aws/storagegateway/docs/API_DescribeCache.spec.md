---
id: "@specs/aws/storagegateway/docs/API_DescribeCache"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCache"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeCache

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeCache
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCache
<a name="API_DescribeCache"></a>

Returns information about the cache of a gateway. This operation is only supported in the cached volume, tape, and file gateway types.

The response includes disk IDs that are configured as cache, and it includes the amount of cache allocated and used.

## Request Syntax
<a name="API_DescribeCache_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCache_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeCache_RequestSyntax) **   <a name="StorageGateway-DescribeCache-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeCache_ResponseSyntax"></a>

```
{
   "CacheAllocatedInBytes": number,
   "CacheDirtyPercentage": number,
   "CacheHitPercentage": number,
   "CacheMissPercentage": number,
   "CacheUsedPercentage": number,
   "DiskIds": [ "string" ],
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_DescribeCache_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CacheAllocatedInBytes](#API_DescribeCache_ResponseSyntax) **   <a name="StorageGateway-DescribeCache-response-CacheAllocatedInBytes"></a>
The amount of cache in bytes allocated to a gateway.  
Type: Long

 ** [CacheDirtyPercentage](#API_DescribeCache_ResponseSyntax) **   <a name="StorageGateway-DescribeCache-response-CacheDirtyPercentage"></a>
The file share's contribution to the overall percentage of the gateway's cache that has not been persisted to AWS. The sample is taken at the end of the reporting period.  
Type: Double

 ** [CacheHitPercentage](#API_DescribeCache_ResponseSyntax) **   <a name="StorageGateway-DescribeCache-response-CacheHitPercentage"></a>
Percent of application read operations from the file shares that are served from cache. The sample is taken at the end of the reporting period.  
Type: Double

 ** [CacheMissPercentage](#API_DescribeCache_ResponseSyntax) **   <a name="StorageGateway-DescribeCache-response-CacheMissPercentage"></a>
Percent of application read operations from the file shares that are not served from cache. The sample is taken at the end of the reporting period.  
Type: Double

 ** [CacheUsedPercentage](#API_DescribeCache_ResponseSyntax) **   <a name="StorageGateway-DescribeCache-response-CacheUsedPercentage"></a>
Percent use of the gateway's cache storage. This metric applies only to the gateway-cached volume setup. The sample is taken at the end of the reporting period.  
Type: Double

 ** [DiskIds](#API_DescribeCache_ResponseSyntax) **   <a name="StorageGateway-DescribeCache-response-DiskIds"></a>
An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the [ListLocalDisks](API_ListLocalDisks.md) API.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 300.

 ** [GatewayARN](#API_DescribeCache_ResponseSyntax) **   <a name="StorageGateway-DescribeCache-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_DescribeCache_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
An internal server error has occurred during the request. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more information about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

 ** InvalidGatewayRequestException **   
An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more detail about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

## Examples
<a name="API_DescribeCache_Examples"></a>

### Return information about a gateway's cache
<a name="API_DescribeCache_Example_1"></a>

The following example shows a request to obtain a description of a gateway's working storage.

#### Sample Request
<a name="API_DescribeCache_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20120425/us-east-2/storagegateway/aws4_request, SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=9cd5a3584d1d67d57e61f120f35102d6b3649066abdd4bf4bbcf05bd9f2f8fe2
x-amz-date: 20120912T120000Z
x-amz-target: StorageGateway_20130630.DescribeCache

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_DescribeCache_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: gur28r2rqlgb8vvs0mq17hlgij1q8glle1qeu3kpgg6f0kstauu0
Date: Wed, 12 Sep 2012 12:00:02 GMT
Content-Type: application/x-amz-json-1.1
Content-length: 271

{
    "CacheAllocationInBytes": "2199023255552",
    "CacheDirtyPercentage": "0.07",
    "CacheHitPercentage": "99.68",
    "CacheMissPercentage": "0.32",
    "CacheUsedPercentage": "0.07",
    "DiskIds": [
        "pci-0000:03:00.0-scsi-0:0:0:0",
        "pci-0000:04:00.0-scsi-0:1:0:0"
    ],
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

## See Also
<a name="API_DescribeCache_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeCache) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeCache) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeCache) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeCache) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeCache) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeCache) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeCache) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeCache) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeCache) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeCache) 