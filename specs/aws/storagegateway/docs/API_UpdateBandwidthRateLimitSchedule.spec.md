---
id: "@specs/aws/storagegateway/docs/API_UpdateBandwidthRateLimitSchedule"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateBandwidthRateLimitSchedule"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateBandwidthRateLimitSchedule

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateBandwidthRateLimitSchedule
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateBandwidthRateLimitSchedule
<a name="API_UpdateBandwidthRateLimitSchedule"></a>

 Updates the bandwidth rate limit schedule for a specified gateway. By default, gateways do not have bandwidth rate limit schedules, which means no bandwidth rate limiting is in effect. Use this to initiate or update a gateway's bandwidth rate limit schedule. This operation is supported for volume, tape, and S3 file gateways. S3 file gateways support bandwidth rate limits for upload only. FSx file gateways do not support bandwidth rate limits.

## Request Syntax
<a name="API_UpdateBandwidthRateLimitSchedule_RequestSyntax"></a>

```
{
   "BandwidthRateLimitIntervals": [ 
      { 
         "AverageDownloadRateLimitInBitsPerSec": {{number}},
         "AverageUploadRateLimitInBitsPerSec": {{number}},
         "DaysOfWeek": [ {{number}} ],
         "EndHourOfDay": {{number}},
         "EndMinuteOfHour": {{number}},
         "StartHourOfDay": {{number}},
         "StartMinuteOfHour": {{number}}
      }
   ],
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateBandwidthRateLimitSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BandwidthRateLimitIntervals](#API_UpdateBandwidthRateLimitSchedule_RequestSyntax) **   <a name="StorageGateway-UpdateBandwidthRateLimitSchedule-request-BandwidthRateLimitIntervals"></a>
 An array containing bandwidth rate limit schedule intervals for a gateway. When no bandwidth rate limit intervals have been scheduled, the array is empty.   
Type: Array of [BandwidthRateLimitInterval](API_BandwidthRateLimitInterval.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 20 items.  
Required: Yes

 ** [GatewayARN](#API_UpdateBandwidthRateLimitSchedule_RequestSyntax) **   <a name="StorageGateway-UpdateBandwidthRateLimitSchedule-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_UpdateBandwidthRateLimitSchedule_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_UpdateBandwidthRateLimitSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_UpdateBandwidthRateLimitSchedule_ResponseSyntax) **   <a name="StorageGateway-UpdateBandwidthRateLimitSchedule-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_UpdateBandwidthRateLimitSchedule_Errors"></a>

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
<a name="API_UpdateBandwidthRateLimitSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateBandwidthRateLimitSchedule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateBandwidthRateLimitSchedule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateBandwidthRateLimitSchedule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateBandwidthRateLimitSchedule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateBandwidthRateLimitSchedule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateBandwidthRateLimitSchedule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateBandwidthRateLimitSchedule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateBandwidthRateLimitSchedule) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateBandwidthRateLimitSchedule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateBandwidthRateLimitSchedule) 