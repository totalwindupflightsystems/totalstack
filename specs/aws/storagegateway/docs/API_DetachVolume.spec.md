---
id: "@specs/aws/storagegateway/docs/API_DetachVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DetachVolume"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DetachVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DetachVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DetachVolume
<a name="API_DetachVolume"></a>

Disconnects a volume from an iSCSI connection and then detaches the volume from the specified gateway. Detaching and attaching a volume enables you to recover your data from one gateway to a different gateway without creating a snapshot. It also makes it easier to move your volumes from an on-premises gateway to a gateway hosted on an Amazon EC2 instance. This operation is only supported in the volume gateway type.

## Request Syntax
<a name="API_DetachVolume_RequestSyntax"></a>

```
{
   "ForceDetach": {{boolean}},
   "VolumeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DetachVolume_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ForceDetach](#API_DetachVolume_RequestSyntax) **   <a name="StorageGateway-DetachVolume-request-ForceDetach"></a>
Set to `true` to forcibly remove the iSCSI connection of the target volume and detach the volume. The default is `false`. If this value is set to `false`, you must manually disconnect the iSCSI connection from the target volume.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [VolumeARN](#API_DetachVolume_RequestSyntax) **   <a name="StorageGateway-DetachVolume-request-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume to detach from the gateway.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: Yes

## Response Syntax
<a name="API_DetachVolume_ResponseSyntax"></a>

```
{
   "VolumeARN": "string"
}
```

## Response Elements
<a name="API_DetachVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [VolumeARN](#API_DetachVolume_ResponseSyntax) **   <a name="StorageGateway-DetachVolume-response-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume that was detached.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)` 

## Errors
<a name="API_DetachVolume_Errors"></a>

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
<a name="API_DetachVolume_Examples"></a>

### Example request
<a name="API_DetachVolume_Example_1"></a>

The following example shows a request that detaches a volume from a gateway.

#### Sample Request
<a name="API_DetachVolume_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20181025T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DetachVolume

{
    "ForceDetach": "false",
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
}
```

#### Sample Response
<a name="API_DetachVolume_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Thu, 25 Oct 2018 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
}
```

## See Also
<a name="API_DetachVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DetachVolume) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DetachVolume) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DetachVolume) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DetachVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DetachVolume) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DetachVolume) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DetachVolume) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DetachVolume) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DetachVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DetachVolume) 