---
id: "@specs/aws/storagegateway/docs/API_AddUploadBuffer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddUploadBuffer"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# AddUploadBuffer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_AddUploadBuffer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddUploadBuffer
<a name="API_AddUploadBuffer"></a>

Configures one or more gateway local disks as upload buffer for a specified gateway. This operation is supported for the stored volume, cached volume, and tape gateway types.

In the request, you specify the gateway Amazon Resource Name (ARN) to which you want to add upload buffer, and one or more disk IDs that you want to configure as upload buffer.

## Request Syntax
<a name="API_AddUploadBuffer_RequestSyntax"></a>

```
{
   "DiskIds": [ "{{string}}" ],
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_AddUploadBuffer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DiskIds](#API_AddUploadBuffer_RequestSyntax) **   <a name="StorageGateway-AddUploadBuffer-request-DiskIds"></a>
An array of strings that identify disks that are to be configured as working storage. Each string has a minimum length of 1 and maximum length of 300. You can get the disk IDs from the [ListLocalDisks](API_ListLocalDisks.md) API.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: Yes

 ** [GatewayARN](#API_AddUploadBuffer_RequestSyntax) **   <a name="StorageGateway-AddUploadBuffer-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_AddUploadBuffer_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_AddUploadBuffer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_AddUploadBuffer_ResponseSyntax) **   <a name="StorageGateway-AddUploadBuffer-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_AddUploadBuffer_Errors"></a>

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
<a name="API_AddUploadBuffer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/AddUploadBuffer) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/AddUploadBuffer) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/AddUploadBuffer) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/AddUploadBuffer) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/AddUploadBuffer) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/AddUploadBuffer) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/AddUploadBuffer) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/AddUploadBuffer) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/AddUploadBuffer) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/AddUploadBuffer) 