---
id: "@specs/aws/storagegateway/docs/API_DescribeSMBSettings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSMBSettings"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeSMBSettings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeSMBSettings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSMBSettings
<a name="API_DescribeSMBSettings"></a>

Gets a description of a Server Message Block (SMB) file share settings from a file gateway. This operation is only supported for file gateways.

## Request Syntax
<a name="API_DescribeSMBSettings_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSMBSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeSMBSettings_RequestSyntax) **   <a name="StorageGateway-DescribeSMBSettings-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeSMBSettings_ResponseSyntax"></a>

```
{
   "ActiveDirectoryStatus": "string",
   "DomainName": "string",
   "FileSharesVisible": boolean,
   "GatewayARN": "string",
   "SMBGuestPasswordSet": boolean,
   "SMBLocalGroups": { 
      "GatewayAdmins": [ "string" ]
   },
   "SMBSecurityStrategy": "string"
}
```

## Response Elements
<a name="API_DescribeSMBSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ActiveDirectoryStatus](#API_DescribeSMBSettings_ResponseSyntax) **   <a name="StorageGateway-DescribeSMBSettings-response-ActiveDirectoryStatus"></a>
Indicates the status of a gateway that is a member of the Active Directory domain.  
This field is only used as part of a `JoinDomain` request. It is not affected by Active Directory connectivity changes that occur after the `JoinDomain` request succeeds.
+  `ACCESS_DENIED`: Indicates that the `JoinDomain` operation failed due to an authentication error.
+  `DETACHED`: Indicates that gateway is not joined to a domain.
+  `JOINED`: Indicates that the gateway has successfully joined a domain.
+  `JOINING`: Indicates that a `JoinDomain` operation is in progress.
+  `NETWORK_ERROR`: Indicates that `JoinDomain` operation failed due to a network or connectivity error.
+  `TIMEOUT`: Indicates that the `JoinDomain` operation failed because the operation didn't complete within the allotted time.
+  `UNKNOWN_ERROR`: Indicates that the `JoinDomain` operation failed due to another type of error.
Type: String  
Valid Values: `ACCESS_DENIED | DETACHED | JOINED | JOINING | NETWORK_ERROR | TIMEOUT | UNKNOWN_ERROR | INSUFFICIENT_PERMISSIONS` 

 ** [DomainName](#API_DescribeSMBSettings_ResponseSyntax) **   <a name="StorageGateway-DescribeSMBSettings-response-DomainName"></a>
The name of the domain that the gateway is joined to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$` 

 ** [FileSharesVisible](#API_DescribeSMBSettings_ResponseSyntax) **   <a name="StorageGateway-DescribeSMBSettings-response-FileSharesVisible"></a>
The shares on this gateway appear when listing shares. Only supported for S3 File Gateways.   
Type: Boolean

 ** [GatewayARN](#API_DescribeSMBSettings_ResponseSyntax) **   <a name="StorageGateway-DescribeSMBSettings-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [SMBGuestPasswordSet](#API_DescribeSMBSettings_ResponseSyntax) **   <a name="StorageGateway-DescribeSMBSettings-response-SMBGuestPasswordSet"></a>
This value is `true` if a password for the guest user `smbguest` is set, otherwise `false`. Only supported for S3 File Gateways.  
Valid Values: `true` \| `false`   
Type: Boolean

 ** [SMBLocalGroups](#API_DescribeSMBSettings_ResponseSyntax) **   <a name="StorageGateway-DescribeSMBSettings-response-SMBLocalGroups"></a>
A list of Active Directory users and groups that have special permissions for SMB file shares on the gateway.  
Type: [SMBLocalGroups](API_SMBLocalGroups.md) object

 ** [SMBSecurityStrategy](#API_DescribeSMBSettings_ResponseSyntax) **   <a name="StorageGateway-DescribeSMBSettings-response-SMBSecurityStrategy"></a>
The type of security strategy that was specified for file gateway.  
+  `ClientSpecified`: If you choose this option, requests are established based on what is negotiated by the client. This option is recommended when you want to maximize compatibility across different clients in your environment. Supported only for S3 File Gateway.
+  `MandatorySigning`: If you choose this option, File Gateway only allows connections from SMBv2 or SMBv3 clients that have signing turned on. This option works with SMB clients on Microsoft Windows Vista, Windows Server 2008, or later. 
+  `MandatoryEncryption`: If you choose this option, File Gateway only allows connections from SMBv3 clients that have encryption turned on. Both 256-bit and 128-bit algorithms are allowed. This option is recommended for environments that handle sensitive data. It works with SMB clients on Microsoft Windows 8, Windows Server 2012, or later.
+  `MandatoryEncryptionNoAes128`: If you choose this option, File Gateway only allows connections from SMBv3 clients that use 256-bit AES encryption algorithms. 128-bit algorithms are not allowed. This option is recommended for environments that handle sensitive data. It works with SMB clients on Microsoft Windows 8, Windows Server 2012, or later.
Type: String  
Valid Values: `ClientSpecified | MandatorySigning | MandatoryEncryption | MandatoryEncryptionNoAes128` 

## Errors
<a name="API_DescribeSMBSettings_Errors"></a>

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
<a name="API_DescribeSMBSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeSMBSettings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeSMBSettings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeSMBSettings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeSMBSettings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeSMBSettings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeSMBSettings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeSMBSettings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeSMBSettings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeSMBSettings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeSMBSettings) 