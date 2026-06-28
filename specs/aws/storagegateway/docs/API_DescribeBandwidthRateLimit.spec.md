---
id: "@specs/aws/storagegateway/docs/API_DescribeBandwidthRateLimit"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeBandwidthRateLimit"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeBandwidthRateLimit

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeBandwidthRateLimit
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeBandwidthRateLimit
<a name="API_DescribeBandwidthRateLimit"></a>

Returns the bandwidth rate limits of a gateway. By default, these limits are not set, which means no bandwidth rate limiting is in effect. This operation is supported only for the stored volume, cached volume, and tape gateway types. To describe bandwidth rate limits for S3 file gateways, use [DescribeBandwidthRateLimitSchedule](API_DescribeBandwidthRateLimitSchedule.md).

This operation returns a value for a bandwidth rate limit only if the limit is set. If no limits are set for the gateway, then this operation returns only the gateway ARN in the response body. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.

## Request Syntax
<a name="API_DescribeBandwidthRateLimit_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBandwidthRateLimit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeBandwidthRateLimit_RequestSyntax) **   <a name="StorageGateway-DescribeBandwidthRateLimit-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeBandwidthRateLimit_ResponseSyntax"></a>

```
{
   "AverageDownloadRateLimitInBitsPerSec": number,
   "AverageUploadRateLimitInBitsPerSec": number,
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_DescribeBandwidthRateLimit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AverageDownloadRateLimitInBitsPerSec](#API_DescribeBandwidthRateLimit_ResponseSyntax) **   <a name="StorageGateway-DescribeBandwidthRateLimit-response-AverageDownloadRateLimitInBitsPerSec"></a>
The average download bandwidth rate limit in bits per second. This field does not appear in the response if the download rate limit is not set.  
Type: Long  
Valid Range: Minimum value of 102400.

 ** [AverageUploadRateLimitInBitsPerSec](#API_DescribeBandwidthRateLimit_ResponseSyntax) **   <a name="StorageGateway-DescribeBandwidthRateLimit-response-AverageUploadRateLimitInBitsPerSec"></a>
The average upload bandwidth rate limit in bits per second. This field does not appear in the response if the upload rate limit is not set.  
Type: Long  
Valid Range: Minimum value of 51200.

 ** [GatewayARN](#API_DescribeBandwidthRateLimit_ResponseSyntax) **   <a name="StorageGateway-DescribeBandwidthRateLimit-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_DescribeBandwidthRateLimit_Errors"></a>

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
<a name="API_DescribeBandwidthRateLimit_Examples"></a>

### Example request
<a name="API_DescribeBandwidthRateLimit_Example_1"></a>

The following example shows a request that returns the bandwidth throttle properties of a gateway.

#### Sample Request
<a name="API_DescribeBandwidthRateLimit_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DescribeBandwidthRateLimit

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_DescribeBandwidthRateLimit_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 169

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "AverageUploadRateLimitInBitsPerSec": "102400",
    "AverageDownloadRateLimitInBitsPerSec": "51200"
}
```

## See Also
<a name="API_DescribeBandwidthRateLimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeBandwidthRateLimit) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeBandwidthRateLimit) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeBandwidthRateLimit) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeBandwidthRateLimit) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeBandwidthRateLimit) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeBandwidthRateLimit) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeBandwidthRateLimit) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeBandwidthRateLimit) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeBandwidthRateLimit) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeBandwidthRateLimit) 