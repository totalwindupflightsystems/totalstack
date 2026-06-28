---
id: "@specs/aws/storagegateway/docs/API_UpdateSMBLocalGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateSMBLocalGroups"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateSMBLocalGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateSMBLocalGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateSMBLocalGroups
<a name="API_UpdateSMBLocalGroups"></a>

Updates the list of Active Directory users and groups that have special permissions for SMB file shares on the gateway.

## Request Syntax
<a name="API_UpdateSMBLocalGroups_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "SMBLocalGroups": { 
      "GatewayAdmins": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_UpdateSMBLocalGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_UpdateSMBLocalGroups_RequestSyntax) **   <a name="StorageGateway-UpdateSMBLocalGroups-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [SMBLocalGroups](#API_UpdateSMBLocalGroups_RequestSyntax) **   <a name="StorageGateway-UpdateSMBLocalGroups-request-SMBLocalGroups"></a>
A list of Active Directory users and groups that you want to grant special permissions for SMB file shares on the gateway.  
Type: [SMBLocalGroups](API_SMBLocalGroups.md) object  
Required: Yes

## Response Syntax
<a name="API_UpdateSMBLocalGroups_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_UpdateSMBLocalGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_UpdateSMBLocalGroups_ResponseSyntax) **   <a name="StorageGateway-UpdateSMBLocalGroups-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_UpdateSMBLocalGroups_Errors"></a>

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
<a name="API_UpdateSMBLocalGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateSMBLocalGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateSMBLocalGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateSMBLocalGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateSMBLocalGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateSMBLocalGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateSMBLocalGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateSMBLocalGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateSMBLocalGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateSMBLocalGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateSMBLocalGroups) 