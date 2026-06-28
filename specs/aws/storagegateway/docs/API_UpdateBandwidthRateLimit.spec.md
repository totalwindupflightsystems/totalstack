---
id: "@specs/aws/storagegateway/docs/API_UpdateBandwidthRateLimit"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateBandwidthRateLimit"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateBandwidthRateLimit

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateBandwidthRateLimit
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateBandwidthRateLimit
<a name="API_UpdateBandwidthRateLimit"></a>

Updates the bandwidth rate limits of a gateway. You can update both the upload and download bandwidth rate limit or specify only one of the two. If you don't set a bandwidth rate limit, the existing rate limit remains. This operation is supported only for the stored volume, cached volume, and tape gateway types. To update bandwidth rate limits for S3 file gateways, use [UpdateBandwidthRateLimitSchedule](API_UpdateBandwidthRateLimitSchedule.md).

By default, a gateway's bandwidth rate limits are not set. If you don't set any limit, the gateway does not have any limitations on its bandwidth usage and could potentially use the maximum available bandwidth.

To specify which gateway to update, use the Amazon Resource Name (ARN) of the gateway in your request.

## Request Syntax
<a name="API_UpdateBandwidthRateLimit_RequestSyntax"></a>

```
{
   "AverageDownloadRateLimitInBitsPerSec": {{number}},
   "AverageUploadRateLimitInBitsPerSec": {{number}},
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateBandwidthRateLimit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AverageDownloadRateLimitInBitsPerSec](#API_UpdateBandwidthRateLimit_RequestSyntax) **   <a name="StorageGateway-UpdateBandwidthRateLimit-request-AverageDownloadRateLimitInBitsPerSec"></a>
The average download bandwidth rate limit in bits per second.  
Type: Long  
Valid Range: Minimum value of 102400.  
Required: No

 ** [AverageUploadRateLimitInBitsPerSec](#API_UpdateBandwidthRateLimit_RequestSyntax) **   <a name="StorageGateway-UpdateBandwidthRateLimit-request-AverageUploadRateLimitInBitsPerSec"></a>
The average upload bandwidth rate limit in bits per second.  
Type: Long  
Valid Range: Minimum value of 51200.  
Required: No

 ** [GatewayARN](#API_UpdateBandwidthRateLimit_RequestSyntax) **   <a name="StorageGateway-UpdateBandwidthRateLimit-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_UpdateBandwidthRateLimit_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_UpdateBandwidthRateLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_UpdateBandwidthRateLimit_ResponseSyntax) **   <a name="StorageGateway-UpdateBandwidthRateLimit-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_UpdateBandwidthRateLimit_Errors"></a>

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
<a name="API_UpdateBandwidthRateLimit_Examples"></a>

### Example request
<a name="API_UpdateBandwidthRateLimit_Example_1"></a>

The following example shows a request that returns the bandwidth throttle properties of a gateway.

#### Sample Request
<a name="API_UpdateBandwidthRateLimit_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.UpdateBandwidthRateLimit

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "AverageUploadRateLimitInBitsPerSec": "51200",
    "AverageDownloadRateLimitInBitsPerSec": "102400"
}
```

#### Sample Response
<a name="API_UpdateBandwidthRateLimit_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 80

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

## See Also
<a name="API_UpdateBandwidthRateLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateBandwidthRateLimit) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateBandwidthRateLimit) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateBandwidthRateLimit) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateBandwidthRateLimit) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateBandwidthRateLimit) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateBandwidthRateLimit) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateBandwidthRateLimit) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateBandwidthRateLimit) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateBandwidthRateLimit) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateBandwidthRateLimit) 