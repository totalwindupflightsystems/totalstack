---
id: "@specs/aws/storagegateway/docs/API_DeleteChapCredentials"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteChapCredentials"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DeleteChapCredentials

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DeleteChapCredentials
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteChapCredentials
<a name="API_DeleteChapCredentials"></a>

Deletes Challenge-Handshake Authentication Protocol (CHAP) credentials for a specified iSCSI target and initiator pair. This operation is supported in volume and tape gateway types.

## Request Syntax
<a name="API_DeleteChapCredentials_RequestSyntax"></a>

```
{
   "InitiatorName": "{{string}}",
   "TargetARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteChapCredentials_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InitiatorName](#API_DeleteChapCredentials_RequestSyntax) **   <a name="StorageGateway-DeleteChapCredentials-request-InitiatorName"></a>
The iSCSI initiator that connects to the target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[0-9a-z:.-]+`   
Required: Yes

 ** [TargetARN](#API_DeleteChapCredentials_RequestSyntax) **   <a name="StorageGateway-DeleteChapCredentials-request-TargetARN"></a>
The Amazon Resource Name (ARN) of the iSCSI volume target. Use the [DescribeStorediSCSIVolumes](API_DescribeStorediSCSIVolumes.md) operation to return to retrieve the TargetARN for specified VolumeARN.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 800.  
Required: Yes

## Response Syntax
<a name="API_DeleteChapCredentials_ResponseSyntax"></a>

```
{
   "InitiatorName": "string",
   "TargetARN": "string"
}
```

## Response Elements
<a name="API_DeleteChapCredentials_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InitiatorName](#API_DeleteChapCredentials_ResponseSyntax) **   <a name="StorageGateway-DeleteChapCredentials-response-InitiatorName"></a>
The iSCSI initiator that connects to the target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[0-9a-z:.-]+` 

 ** [TargetARN](#API_DeleteChapCredentials_ResponseSyntax) **   <a name="StorageGateway-DeleteChapCredentials-response-TargetARN"></a>
The Amazon Resource Name (ARN) of the target.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 800.

## Errors
<a name="API_DeleteChapCredentials_Errors"></a>

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
<a name="API_DeleteChapCredentials_Examples"></a>

### Example request
<a name="API_DeleteChapCredentials_Example_1"></a>

The following example shows a request that deletes the CHAP credentials for an iSCSI target `myvolume`.

#### Sample Request
<a name="API_DeleteChapCredentials_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DeleteChapCredentials

{
    "TargetARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume",
    "InitiatorName": "iqn.1991-05.com.microsoft:computername.domain.example.com"
}
```

#### Sample Response
<a name="API_DeleteChapCredentials_Example_1_Response"></a>

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
<a name="API_DeleteChapCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DeleteChapCredentials) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DeleteChapCredentials) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DeleteChapCredentials) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DeleteChapCredentials) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DeleteChapCredentials) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DeleteChapCredentials) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DeleteChapCredentials) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DeleteChapCredentials) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DeleteChapCredentials) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DeleteChapCredentials) 