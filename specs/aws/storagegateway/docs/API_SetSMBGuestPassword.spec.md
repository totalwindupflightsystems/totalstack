---
id: "@specs/aws/storagegateway/docs/API_SetSMBGuestPassword"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SetSMBGuestPassword"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# SetSMBGuestPassword

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_SetSMBGuestPassword
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SetSMBGuestPassword
<a name="API_SetSMBGuestPassword"></a>

Sets the password for the guest user `smbguest`. The `smbguest` user is the user when the authentication method for the file share is set to `GuestAccess`. This operation only supported for S3 File Gateways

## Request Syntax
<a name="API_SetSMBGuestPassword_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "Password": "{{string}}"
}
```

## Request Parameters
<a name="API_SetSMBGuestPassword_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_SetSMBGuestPassword_RequestSyntax) **   <a name="StorageGateway-SetSMBGuestPassword-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the S3 File Gateway the SMB file share is associated with.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [Password](#API_SetSMBGuestPassword_RequestSyntax) **   <a name="StorageGateway-SetSMBGuestPassword-request-Password"></a>
The password that you want to set for your SMB server.  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 512.  
Pattern: `^[ -~]+$`   
Required: Yes

## Response Syntax
<a name="API_SetSMBGuestPassword_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_SetSMBGuestPassword_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_SetSMBGuestPassword_ResponseSyntax) **   <a name="StorageGateway-SetSMBGuestPassword-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_SetSMBGuestPassword_Errors"></a>

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
<a name="API_SetSMBGuestPassword_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/SetSMBGuestPassword) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/SetSMBGuestPassword) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/SetSMBGuestPassword) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/SetSMBGuestPassword) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/SetSMBGuestPassword) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/SetSMBGuestPassword) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/SetSMBGuestPassword) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/SetSMBGuestPassword) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/SetSMBGuestPassword) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/SetSMBGuestPassword) 