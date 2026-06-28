---
id: "@specs/aws/storagegateway/docs/API_UpdateVTLDeviceType"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateVTLDeviceType"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateVTLDeviceType

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateVTLDeviceType
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateVTLDeviceType
<a name="API_UpdateVTLDeviceType"></a>

Updates the type of medium changer in a tape gateway. When you activate a tape gateway, you select a medium changer type for the tape gateway. This operation enables you to select a different type of medium changer after a tape gateway is activated. This operation is only supported in the tape gateway type.

## Request Syntax
<a name="API_UpdateVTLDeviceType_RequestSyntax"></a>

```
{
   "DeviceType": "{{string}}",
   "VTLDeviceARN": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateVTLDeviceType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeviceType](#API_UpdateVTLDeviceType_RequestSyntax) **   <a name="StorageGateway-UpdateVTLDeviceType-request-DeviceType"></a>
The type of medium changer you want to select.  
Valid Values: `STK-L700` \| `AWS-Gateway-VTL` \| `IBM-03584L32-0402`   
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 50.  
Required: Yes

 ** [VTLDeviceARN](#API_UpdateVTLDeviceType_RequestSyntax) **   <a name="StorageGateway-UpdateVTLDeviceType-request-VTLDeviceARN"></a>
The Amazon Resource Name (ARN) of the medium changer you want to select.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_UpdateVTLDeviceType_ResponseSyntax"></a>

```
{
   "VTLDeviceARN": "string"
}
```

## Response Elements
<a name="API_UpdateVTLDeviceType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VTLDeviceARN](#API_UpdateVTLDeviceType_ResponseSyntax) **   <a name="StorageGateway-UpdateVTLDeviceType-response-VTLDeviceARN"></a>
The Amazon Resource Name (ARN) of the medium changer you have selected.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_UpdateVTLDeviceType_Errors"></a>

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
<a name="API_UpdateVTLDeviceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateVTLDeviceType) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateVTLDeviceType) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateVTLDeviceType) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateVTLDeviceType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateVTLDeviceType) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateVTLDeviceType) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateVTLDeviceType) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateVTLDeviceType) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateVTLDeviceType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateVTLDeviceType) 