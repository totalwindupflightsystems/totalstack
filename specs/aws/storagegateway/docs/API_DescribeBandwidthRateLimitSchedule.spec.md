---
id: "@specs/aws/storagegateway/docs/API_DescribeBandwidthRateLimitSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeBandwidthRateLimitSchedule"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeBandwidthRateLimitSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeBandwidthRateLimitSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeBandwidthRateLimitSchedule
<a name="API_DescribeBandwidthRateLimitSchedule"></a>

 Returns information about the bandwidth rate limit schedule of a gateway. By default, gateways do not have bandwidth rate limit schedules, which means no bandwidth rate limiting is in effect. This operation is supported only for volume, tape and S3 file gateways. FSx file gateways do not support bandwidth rate limits.

This operation returns information about a gateway's bandwidth rate limit schedule. A bandwidth rate limit schedule consists of one or more bandwidth rate limit intervals. A bandwidth rate limit interval defines a period of time on one or more days of the week, during which bandwidth rate limits are specified for uploading, downloading, or both. 

 A bandwidth rate limit interval consists of one or more days of the week, a start hour and minute, an ending hour and minute, and bandwidth rate limits for uploading and downloading 

 If no bandwidth rate limit schedule intervals are set for the gateway, this operation returns an empty response. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.

## Request Syntax
<a name="API_DescribeBandwidthRateLimitSchedule_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeBandwidthRateLimitSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeBandwidthRateLimitSchedule_RequestSyntax) **   <a name="StorageGateway-DescribeBandwidthRateLimitSchedule-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeBandwidthRateLimitSchedule_ResponseSyntax"></a>

```
{
   "BandwidthRateLimitIntervals": [ 
      { 
         "AverageDownloadRateLimitInBitsPerSec": number,
         "AverageUploadRateLimitInBitsPerSec": number,
         "DaysOfWeek": [ number ],
         "EndHourOfDay": number,
         "EndMinuteOfHour": number,
         "StartHourOfDay": number,
         "StartMinuteOfHour": number
      }
   ],
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_DescribeBandwidthRateLimitSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BandwidthRateLimitIntervals](#API_DescribeBandwidthRateLimitSchedule_ResponseSyntax) **   <a name="StorageGateway-DescribeBandwidthRateLimitSchedule-response-BandwidthRateLimitIntervals"></a>
 An array that contains the bandwidth rate limit intervals for a tape or volume gateway.   
Type: Array of [BandwidthRateLimitInterval](API_BandwidthRateLimitInterval.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [GatewayARN](#API_DescribeBandwidthRateLimitSchedule_ResponseSyntax) **   <a name="StorageGateway-DescribeBandwidthRateLimitSchedule-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_DescribeBandwidthRateLimitSchedule_Errors"></a>

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

## See Also
<a name="API_DescribeBandwidthRateLimitSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeBandwidthRateLimitSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeBandwidthRateLimitSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeBandwidthRateLimitSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeBandwidthRateLimitSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeBandwidthRateLimitSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeBandwidthRateLimitSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeBandwidthRateLimitSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeBandwidthRateLimitSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeBandwidthRateLimitSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeBandwidthRateLimitSchedule) 