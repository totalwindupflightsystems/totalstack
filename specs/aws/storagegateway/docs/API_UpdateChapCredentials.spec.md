---
id: "@specs/aws/storagegateway/docs/API_UpdateChapCredentials"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateChapCredentials"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateChapCredentials

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateChapCredentials
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateChapCredentials
<a name="API_UpdateChapCredentials"></a>

Updates the Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target. By default, a gateway does not have CHAP enabled; however, for added security, you might use it. This operation is supported in the volume and tape gateway types.

**Important**  
When you update CHAP credentials, all existing connections on the target are closed and initiators must reconnect with the new credentials.

## Request Syntax
<a name="API_UpdateChapCredentials_RequestSyntax"></a>

```
{
   "InitiatorName": "{{string}}",
   "SecretToAuthenticateInitiator": "{{string}}",
   "SecretToAuthenticateTarget": "{{string}}",
   "TargetARN": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateChapCredentials_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InitiatorName](#API_UpdateChapCredentials_RequestSyntax) **   <a name="StorageGateway-UpdateChapCredentials-request-InitiatorName"></a>
The iSCSI initiator that connects to the target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[0-9a-z:.-]+`   
Required: Yes

 ** [SecretToAuthenticateInitiator](#API_UpdateChapCredentials_RequestSyntax) **   <a name="StorageGateway-UpdateChapCredentials-request-SecretToAuthenticateInitiator"></a>
The secret key that the initiator (for example, the Windows client) must provide to participate in mutual CHAP with the target.  
The secret key must be between 12 and 16 bytes when encoded in UTF-8.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: Yes

 ** [SecretToAuthenticateTarget](#API_UpdateChapCredentials_RequestSyntax) **   <a name="StorageGateway-UpdateChapCredentials-request-SecretToAuthenticateTarget"></a>
The secret key that the target must provide to participate in mutual CHAP with the initiator (e.g. Windows client).  
Byte constraints: Minimum bytes of 12. Maximum bytes of 16.  
The secret key must be between 12 and 16 bytes when encoded in UTF-8.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** [TargetARN](#API_UpdateChapCredentials_RequestSyntax) **   <a name="StorageGateway-UpdateChapCredentials-request-TargetARN"></a>
The Amazon Resource Name (ARN) of the iSCSI volume target. Use the [DescribeStorediSCSIVolumes](API_DescribeStorediSCSIVolumes.md) operation to return the TargetARN for specified VolumeARN.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 800.  
Required: Yes

## Response Syntax
<a name="API_UpdateChapCredentials_ResponseSyntax"></a>

```
{
   "InitiatorName": "string",
   "TargetARN": "string"
}
```

## Response Elements
<a name="API_UpdateChapCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InitiatorName](#API_UpdateChapCredentials_ResponseSyntax) **   <a name="StorageGateway-UpdateChapCredentials-response-InitiatorName"></a>
The iSCSI initiator that connects to the target. This is the same initiator name specified in the request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[0-9a-z:.-]+` 

 ** [TargetARN](#API_UpdateChapCredentials_ResponseSyntax) **   <a name="StorageGateway-UpdateChapCredentials-response-TargetARN"></a>
The Amazon Resource Name (ARN) of the target. This is the same target specified in the request.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 800.

## Errors
<a name="API_UpdateChapCredentials_Errors"></a>

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

## Examples
<a name="API_UpdateChapCredentials_Examples"></a>

### Example request
<a name="API_UpdateChapCredentials_Example_1"></a>

The following example shows a request that updates CHAP credentials for an iSCSI target.

#### Sample Request
<a name="API_UpdateChapCredentials_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.UpdateChapCredentials

{
    "TargetARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume",
    "SecretToAuthenticateInitiator": "111111111111",
    "InitiatorName": "iqn.1991-05.com.microsoft:computername.domain.example.com",
    "SecretToAuthenticateTarget": "222222222222"
}
```

#### Sample Response
<a name="API_UpdateChapCredentials_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 161

{
    "TargetARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume",
    "InitiatorName": "iqn.1991-05.com.microsoft:computername.domain.example.com"
}
```

## See Also
<a name="API_UpdateChapCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateChapCredentials) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateChapCredentials) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateChapCredentials) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateChapCredentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateChapCredentials) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateChapCredentials) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateChapCredentials) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateChapCredentials) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateChapCredentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateChapCredentials) 