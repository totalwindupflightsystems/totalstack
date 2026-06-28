---
id: "@specs/aws/storagegateway/docs/API_UpdateSMBSecurityStrategy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateSMBSecurityStrategy"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateSMBSecurityStrategy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateSMBSecurityStrategy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateSMBSecurityStrategy
<a name="API_UpdateSMBSecurityStrategy"></a>

Updates the SMB security strategy level for an Amazon S3 file gateway. This action is only supported for Amazon S3 file gateways.

**Note**  
For information about configuring this setting using the AWS console, see [Setting a security level for your gateway](https://docs.aws.amazon.com/filegateway/latest/files3/security-strategy.html) in the *Amazon S3 File Gateway User Guide*.  
A higher security strategy level can affect performance of the gateway.

## Request Syntax
<a name="API_UpdateSMBSecurityStrategy_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "SMBSecurityStrategy": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateSMBSecurityStrategy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_UpdateSMBSecurityStrategy_RequestSyntax) **   <a name="StorageGateway-UpdateSMBSecurityStrategy-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [SMBSecurityStrategy](#API_UpdateSMBSecurityStrategy_RequestSyntax) **   <a name="StorageGateway-UpdateSMBSecurityStrategy-request-SMBSecurityStrategy"></a>
Specifies the type of security strategy.  
 `ClientSpecified`: If you choose this option, requests are established based on what is negotiated by the client. This option is recommended when you want to maximize compatibility across different clients in your environment. Supported only for S3 File Gateway.  
 `MandatorySigning`: If you choose this option, File Gateway only allows connections from SMBv2 or SMBv3 clients that have signing enabled. This option works with SMB clients on Microsoft Windows Vista, Windows Server 2008 or newer.  
 `MandatoryEncryption`: If you choose this option, File Gateway only allows connections from SMBv3 clients that have encryption enabled. This option is recommended for environments that handle sensitive data. This option works with SMB clients on Microsoft Windows 8, Windows Server 2012 or newer.  
 `MandatoryEncryptionNoAes128`: If you choose this option, File Gateway only allows connections from SMBv3 clients that use 256-bit AES encryption algorithms. 128-bit algorithms are not allowed. This option is recommended for environments that handle sensitive data. It works with SMB clients on Microsoft Windows 8, Windows Server 2012, or later.  
Type: String  
Valid Values: `ClientSpecified | MandatorySigning | MandatoryEncryption | MandatoryEncryptionNoAes128`   
Required: Yes

## Response Syntax
<a name="API_UpdateSMBSecurityStrategy_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_UpdateSMBSecurityStrategy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_UpdateSMBSecurityStrategy_ResponseSyntax) **   <a name="StorageGateway-UpdateSMBSecurityStrategy-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_UpdateSMBSecurityStrategy_Errors"></a>

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
<a name="API_UpdateSMBSecurityStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateSMBSecurityStrategy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateSMBSecurityStrategy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateSMBSecurityStrategy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateSMBSecurityStrategy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateSMBSecurityStrategy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateSMBSecurityStrategy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateSMBSecurityStrategy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateSMBSecurityStrategy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateSMBSecurityStrategy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateSMBSecurityStrategy) 