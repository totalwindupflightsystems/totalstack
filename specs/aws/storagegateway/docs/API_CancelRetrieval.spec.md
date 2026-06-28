---
id: "@specs/aws/storagegateway/docs/API_CancelRetrieval"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelRetrieval"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CancelRetrieval

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CancelRetrieval
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelRetrieval
<a name="API_CancelRetrieval"></a>

Cancels retrieval of a virtual tape from the virtual tape shelf (VTS) to a gateway after the retrieval process is initiated. The virtual tape is returned to the VTS. This operation is only supported in the tape gateway type.

## Request Syntax
<a name="API_CancelRetrieval_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "TapeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_CancelRetrieval_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_CancelRetrieval_RequestSyntax) **   <a name="StorageGateway-CancelRetrieval-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [TapeARN](#API_CancelRetrieval_RequestSyntax) **   <a name="StorageGateway-CancelRetrieval-request-TapeARN"></a>
The Amazon Resource Name (ARN) of the virtual tape you want to cancel retrieval for.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$`   
Required: Yes

## Response Syntax
<a name="API_CancelRetrieval_ResponseSyntax"></a>

```
{
   "TapeARN": "string"
}
```

## Response Elements
<a name="API_CancelRetrieval_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TapeARN](#API_CancelRetrieval_ResponseSyntax) **   <a name="StorageGateway-CancelRetrieval-response-TapeARN"></a>
The Amazon Resource Name (ARN) of the virtual tape for which retrieval was canceled.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:tape\/[0-9A-Z]{5,16}$` 

## Errors
<a name="API_CancelRetrieval_Errors"></a>

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
<a name="API_CancelRetrieval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/CancelRetrieval) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/CancelRetrieval) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CancelRetrieval) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/CancelRetrieval) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CancelRetrieval) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/CancelRetrieval) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/CancelRetrieval) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/CancelRetrieval) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/CancelRetrieval) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CancelRetrieval) 