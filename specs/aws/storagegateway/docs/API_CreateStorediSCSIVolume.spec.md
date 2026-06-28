---
id: "@specs/aws/storagegateway/docs/API_CreateStorediSCSIVolume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateStorediSCSIVolume"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# CreateStorediSCSIVolume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_CreateStorediSCSIVolume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateStorediSCSIVolume
<a name="API_CreateStorediSCSIVolume"></a>

Creates a volume on a specified gateway. This operation is only supported in the stored volume gateway type.

The size of the volume to create is inferred from the disk size. You can choose to preserve existing data on the disk, create volume from an existing snapshot, or create an empty volume. If you choose to create an empty gateway volume, then any existing data on the disk is erased.

In the request, you must specify the gateway and the disk information on which you are creating the volume. In response, the gateway creates the volume and returns volume information such as the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.

## Request Syntax
<a name="API_CreateStorediSCSIVolume_RequestSyntax"></a>

```
{
   "DiskId": "{{string}}",
   "GatewayARN": "{{string}}",
   "KMSEncrypted": {{boolean}},
   "KMSKey": "{{string}}",
   "NetworkInterfaceId": "{{string}}",
   "PreserveExistingData": {{boolean}},
   "SnapshotId": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TargetName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateStorediSCSIVolume_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DiskId](#API_CreateStorediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-request-DiskId"></a>
The unique identifier for the gateway local disk that is configured as a stored volume. Use [ListLocalDisks](https://docs.aws.amazon.com/storagegateway/latest/userguide/API_ListLocalDisks.html) to list disk IDs for a gateway.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: Yes

 ** [GatewayARN](#API_CreateStorediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [KMSEncrypted](#API_CreateStorediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-request-KMSEncrypted"></a>
Set to `true` to use Amazon S3 server-side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Optional.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: No

 ** [KMSKey](#API_CreateStorediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-request-KMSKey"></a>
The Amazon Resource Name (ARN) of a symmetric AWS KMS key used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric KMS keys. This value can only be set when `KMSEncrypted` is `true`. Optional.  
Type: String  
Length Constraints: Minimum length of 7. Maximum length of 2048.  
Pattern: `(^arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`   
Required: No

 ** [NetworkInterfaceId](#API_CreateStorediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-request-NetworkInterfaceId"></a>
The network interface of the gateway on which to expose the iSCSI target. Accepts IPv4 and IPv6 addresses. Use [DescribeGatewayInformation](API_DescribeGatewayInformation.md) to get a list of the network interfaces available on a gateway.  
Valid Values: A valid IP address.  
Type: String  
Required: Yes

 ** [PreserveExistingData](#API_CreateStorediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-request-PreserveExistingData"></a>
Set to `true` if you want to preserve the data on the local disk. Otherwise, set to `false` to create an empty volume.  
Valid Values: `true` \| `false`   
Type: Boolean  
Required: Yes

 ** [SnapshotId](#API_CreateStorediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-request-SnapshotId"></a>
The snapshot ID (e.g., "snap-1122aabb") of the snapshot to restore as the new stored volume. Specify this field if you want to create the iSCSI storage volume from a snapshot; otherwise, do not include this field. To list snapshots for your account use [DescribeSnapshots](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html) in the *Amazon Elastic Compute Cloud API Reference*.  
Type: String  
Pattern: `\Asnap-([0-9A-Fa-f]{8}|[0-9A-Fa-f]{17})\z`   
Required: No

 ** [Tags](#API_CreateStorediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-request-Tags"></a>
A list of up to 50 tags that can be assigned to a stored volume. Each tag is a key-value pair.  
Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: \+ - = . \_ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [TargetName](#API_CreateStorediSCSIVolume_RequestSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-request-TargetName"></a>
The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying `TargetName` as *myvolume* results in the target ARN of `arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume`. The target name must be unique across all volumes on a gateway.  
If you don't specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[-\.;a-z0-9]+$`   
Required: Yes

## Response Syntax
<a name="API_CreateStorediSCSIVolume_ResponseSyntax"></a>

```
{
   "TargetARN": "string",
   "VolumeARN": "string",
   "VolumeSizeInBytes": number
}
```

## Response Elements
<a name="API_CreateStorediSCSIVolume_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TargetARN](#API_CreateStorediSCSIVolume_ResponseSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-response-TargetARN"></a>
The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name that initiators can use to connect to the target.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 800.

 ** [VolumeARN](#API_CreateStorediSCSIVolume_ResponseSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-response-VolumeARN"></a>
The Amazon Resource Name (ARN) of the configured volume.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Pattern: `arn:(aws(|-cn|-us-gov|-iso[A-Za-z0-9_-]*)):storagegateway:[a-z\-0-9]+:[0-9]+:gateway\/(.+)\/volume\/vol-(\S+)` 

 ** [VolumeSizeInBytes](#API_CreateStorediSCSIVolume_ResponseSyntax) **   <a name="StorageGateway-CreateStorediSCSIVolume-response-VolumeSizeInBytes"></a>
The size of the volume in bytes.  
Type: Long

## Errors
<a name="API_CreateStorediSCSIVolume_Errors"></a>

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
<a name="API_CreateStorediSCSIVolume_Examples"></a>

### Example request
<a name="API_CreateStorediSCSIVolume_Example_1"></a>

The following example shows a request that specifies that a local disk of a gateway be configured as a volume.

#### Sample Request
<a name="API_CreateStorediSCSIVolume_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.CreateStorediSCSIVolume

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "KMSEncrypted": "true",
    "KMSKey": "arn:aws:kms:us-east-1:11111111:key/b72aaa2a-2222-99tt-12345690qwe",
    "DiskId": "pci-0000:03:00.0-scsi-0:0:0:0",
    "PreserveExistingData": true,
    "TargetName": "myvolume",
    "NetworkInterfaceId": "10.1.1.1"
}
```

#### Sample Response
<a name="API_CreateStorediSCSIVolume_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 215

{
    "VolumeARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB",
    "VolumeSizeInBytes": 1099511627776,
    "TargetARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume"
}
```

## See Also
<a name="API_CreateStorediSCSIVolume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/CreateStorediSCSIVolume) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/CreateStorediSCSIVolume) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/CreateStorediSCSIVolume) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/CreateStorediSCSIVolume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/CreateStorediSCSIVolume) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/CreateStorediSCSIVolume) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/CreateStorediSCSIVolume) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/CreateStorediSCSIVolume) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/CreateStorediSCSIVolume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/CreateStorediSCSIVolume) 