---
id: "@specs/aws/storagegateway/docs/API_SetLocalConsolePassword"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SetLocalConsolePassword"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# SetLocalConsolePassword

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_SetLocalConsolePassword
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SetLocalConsolePassword
<a name="API_SetLocalConsolePassword"></a>

Sets the password for your VM local console. When you log in to the local console for the first time, you log in to the VM with the default credentials. We recommend that you set a new password. You don't need to know the default password to set a new password.

## Request Syntax
<a name="API_SetLocalConsolePassword_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "LocalConsolePassword": "{{string}}"
}
```

## Request Parameters
<a name="API_SetLocalConsolePassword_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_SetLocalConsolePassword_RequestSyntax) **   <a name="StorageGateway-SetLocalConsolePassword-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [LocalConsolePassword](#API_SetLocalConsolePassword_RequestSyntax) **   <a name="StorageGateway-SetLocalConsolePassword-request-LocalConsolePassword"></a>
The password you want to set for your VM local console.  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 512.  
Pattern: `^[ -~]+$`   
Required: Yes

## Response Syntax
<a name="API_SetLocalConsolePassword_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_SetLocalConsolePassword_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_SetLocalConsolePassword_ResponseSyntax) **   <a name="StorageGateway-SetLocalConsolePassword-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_SetLocalConsolePassword_Errors"></a>

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
<a name="API_SetLocalConsolePassword_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/SetLocalConsolePassword) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/SetLocalConsolePassword) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/SetLocalConsolePassword) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/SetLocalConsolePassword) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/SetLocalConsolePassword) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/SetLocalConsolePassword) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/SetLocalConsolePassword) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/SetLocalConsolePassword) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/SetLocalConsolePassword) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/SetLocalConsolePassword) 