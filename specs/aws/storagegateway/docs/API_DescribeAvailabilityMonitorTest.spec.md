---
id: "@specs/aws/storagegateway/docs/API_DescribeAvailabilityMonitorTest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAvailabilityMonitorTest"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeAvailabilityMonitorTest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeAvailabilityMonitorTest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAvailabilityMonitorTest
<a name="API_DescribeAvailabilityMonitorTest"></a>

Returns information about the most recent high availability monitoring test that was performed on the host in a cluster. If a test isn't performed, the status and start time in the response would be null.

## Request Syntax
<a name="API_DescribeAvailabilityMonitorTest_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAvailabilityMonitorTest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeAvailabilityMonitorTest_RequestSyntax) **   <a name="StorageGateway-DescribeAvailabilityMonitorTest-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeAvailabilityMonitorTest_ResponseSyntax"></a>

```
{
   "GatewayARN": "string",
   "StartTime": number,
   "Status": "string"
}
```

## Response Elements
<a name="API_DescribeAvailabilityMonitorTest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_DescribeAvailabilityMonitorTest_ResponseSyntax) **   <a name="StorageGateway-DescribeAvailabilityMonitorTest-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [StartTime](#API_DescribeAvailabilityMonitorTest_ResponseSyntax) **   <a name="StorageGateway-DescribeAvailabilityMonitorTest-response-StartTime"></a>
The time the high availability monitoring test was started. If a test hasn't been performed, the value of this field is null.  
Type: Timestamp

 ** [Status](#API_DescribeAvailabilityMonitorTest_ResponseSyntax) **   <a name="StorageGateway-DescribeAvailabilityMonitorTest-response-Status"></a>
The status of the high availability monitoring test. If a test hasn't been performed, the value of this field is null.  
Type: String  
Valid Values: `COMPLETE | FAILED | PENDING` 

## Errors
<a name="API_DescribeAvailabilityMonitorTest_Errors"></a>

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
<a name="API_DescribeAvailabilityMonitorTest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeAvailabilityMonitorTest) 