---
id: "@specs/aws/storagegateway/docs/API_DescribeTapeRecoveryPoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTapeRecoveryPoints"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeTapeRecoveryPoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeTapeRecoveryPoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTapeRecoveryPoints
<a name="API_DescribeTapeRecoveryPoints"></a>

Returns a list of virtual tape recovery points that are available for the specified tape gateway.

A recovery point is a point-in-time view of a virtual tape at which all the data on the virtual tape is consistent. If your gateway crashes, virtual tapes that have recovery points can be recovered to a new gateway. This operation is only supported in the tape gateway type.

## Request Syntax
<a name="API_DescribeTapeRecoveryPoints_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTapeRecoveryPoints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeTapeRecoveryPoints_RequestSyntax) **   <a name="StorageGateway-DescribeTapeRecoveryPoints-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [Limit](#API_DescribeTapeRecoveryPoints_RequestSyntax) **   <a name="StorageGateway-DescribeTapeRecoveryPoints-request-Limit"></a>
Specifies that the number of virtual tape recovery points that are described be limited to the specified number.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_DescribeTapeRecoveryPoints_RequestSyntax) **   <a name="StorageGateway-DescribeTapeRecoveryPoints-request-Marker"></a>
An opaque string that indicates the position at which to begin describing the virtual tape recovery points.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

## Response Syntax
<a name="API_DescribeTapeRecoveryPoints_ResponseSyntax"></a>

```
{
   "GatewayARN": "string",
   "Marker": "string",
   "TapeRecoveryPointInfos": [ 
      { 
         "TapeARN": "string",
         "TapeRecoveryPointTime": number,
         "TapeSizeInBytes": number,
         "TapeStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTapeRecoveryPoints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_DescribeTapeRecoveryPoints_ResponseSyntax) **   <a name="StorageGateway-DescribeTapeRecoveryPoints-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [Marker](#API_DescribeTapeRecoveryPoints_ResponseSyntax) **   <a name="StorageGateway-DescribeTapeRecoveryPoints-response-Marker"></a>
An opaque string that indicates the position at which the virtual tape recovery points that were listed for description ended.  
Use this marker in your next request to list the next set of virtual tape recovery points in the list. If there are no more recovery points to describe, this field does not appear in the response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [TapeRecoveryPointInfos](#API_DescribeTapeRecoveryPoints_ResponseSyntax) **   <a name="StorageGateway-DescribeTapeRecoveryPoints-response-TapeRecoveryPointInfos"></a>
An array of TapeRecoveryPointInfos that are available for the specified gateway.  
Type: Array of [TapeRecoveryPointInfo](API_TapeRecoveryPointInfo.md) objects

## Errors
<a name="API_DescribeTapeRecoveryPoints_Errors"></a>

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
<a name="API_DescribeTapeRecoveryPoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeTapeRecoveryPoints) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeTapeRecoveryPoints) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeTapeRecoveryPoints) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeTapeRecoveryPoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeTapeRecoveryPoints) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeTapeRecoveryPoints) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeTapeRecoveryPoints) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeTapeRecoveryPoints) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeTapeRecoveryPoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeTapeRecoveryPoints) 