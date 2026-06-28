---
id: "@specs/aws/storagegateway/docs/API_AttachVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AttachVolume"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# AttachVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_AttachVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AttachVolume
<a name="API_AttachVolume"></a>

Connects a volume to an iSCSI connection and then attaches the volume to the specified gateway. Detaching and attaching a volume enables you to recover your data from one gateway to a different gateway without creating a snapshot. It also makes it easier to move your volumes from an on-premises gateway to a gateway hosted on an Amazon EC2 instance.

## Request Syntax
<a name="API_AttachVolume_RequestSyntax"></a>

```
{
   "DiskId": "{{string}}",
   "GatewayARN": "{{string}}",
   "NetworkInterfaceId": "{{string}}",
   "TargetName": "{{string}}",
   "VolumeARN": "{{string}}"
}
```

## Request Parameters
<a name="API_AttachVolume_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DiskId](#API_AttachVolume_RequestSyntax) **   <a name="StorageGateway-AttachVolume-request-DiskId"></a>
The unique device ID or other distinguishing data that identifies the local disk used to create the volume. This value is only required when you are attaching a stored volume.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: No

 ** [GatewayARN](#API_AttachVolume_RequestSyntax) **   <a name="StorageGateway-AttachVolume-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway that you want to attach the volume to.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [NetworkInterfaceId](#API_AttachVolume_RequestSyntax) **   <a name="StorageGateway-AttachVolume-request-NetworkInterfaceId"></a>
The network interface of the gateway on which to expose the iSCSI target. Accepts IPv4 and IPv6 addresses. Use [DescribeGatewayInformation](API_DescribeGatewayInformation.md) to get a list of the network interfaces available on a gateway.  
Valid Values: A valid IP address.  
Type: String  
Required: Yes

 ** [TargetName](#API_AttachVolume_RequestSyntax) **   <a name="StorageGateway-AttachVolume-request-TargetName"></a>
The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying `TargetName` as *myvolume* results in the target ARN of `arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume`. The target name must be unique across all volumes on a gateway.  
If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[-\.;a-z0-9]+$`   
Required: No

 ** [VolumeARN](#API_AttachVolume_RequestSyntax) **   <a name="StorageGateway-AttachVolume-request-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume to attach to the specified gateway.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)`   
Required: Yes

## Response Syntax
<a name="API_AttachVolume_ResponseSyntax"></a>

```
{
   "TargetARN": "string",
   "VolumeARN": "string"
}
```

## Response Elements
<a name="API_AttachVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TargetARN](#API_AttachVolume_ResponseSyntax) **   <a name="StorageGateway-AttachVolume-response-TargetARN"></a>
The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name for the initiator that was used to connect to the target.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 800.

 ** [VolumeARN](#API_AttachVolume_ResponseSyntax) **   <a name="StorageGateway-AttachVolume-response-VolumeARN"></a>
The Amazon Resource Name (ARN) of the volume that was attached to the gateway.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)` 

## Errors
<a name="API_AttachVolume_Errors"></a>

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
<a name="API_AttachVolume_Examples"></a>

### Example request
<a name="API_AttachVolume_Example_1"></a>

The following example shows a request that attaches a volume to a gateway.

#### Sample Request
<a name="API_AttachVolume_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20181025T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630. AttachVolume

{
    "DiskId": "pci-0000:03:00.0-scsi-0:0:0:0",
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "NetworkInterfaceId": "10.1.1.1",
    "TargetName": "myvolume",
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
}
```

#### Sample Response
<a name="API_AttachVolume_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Thu, 25 Oct 2018 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 80

{
    "TargetARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume",
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB"
}
```

## See Also
<a name="API_AttachVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/AttachVolume) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/AttachVolume) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/AttachVolume) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/AttachVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/AttachVolume) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/AttachVolume) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/AttachVolume) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/AttachVolume) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/AttachVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/AttachVolume) 